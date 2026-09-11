#!/usr/bin/env python3
"""Generate a slide image through OpenRouter's Images API.

Example:
    python3 scripts/generate_slide_image.py \
      --provider gemini \
      --setting "Cyprus village, old Troodos monastery, cherry blossom" \
      --content "Nine Ways to Evaluate an AI Agent" \
      --resolution 2560x1440 \
      --output slide-01.png

The three named providers are convenient presets. Use --model to override a
preset when OpenRouter adds a newer image model.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://openrouter.ai/api/v1/images"
MODELS = {
    "openai": "openai/gpt-image-2",
    "gemini": "google/gemini-3.1-flash-image",
    "seedream": "bytedance-seed/seedream-5-0-lite",
}


def load_env(path: Path) -> None:
    """Load simple KEY=VALUE entries without overriding the process env."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.removeprefix("export ").strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        os.environ.setdefault(key, value)


def text_argument(value: str) -> str:
    """Accept literal text, or @path to read longer text from a UTF-8 file."""
    if value.startswith("@"):
        return Path(value[1:]).read_text(encoding="utf-8").strip()
    return value.strip()


def validate_resolution(value: str) -> str:
    if value.upper() in {"512", "1K", "2K", "4K"}:
        return value.upper()
    if re.fullmatch(r"[1-9]\d{2,4}x[1-9]\d{2,4}", value):
        return value
    raise argparse.ArgumentTypeError(
        "use a tier (512, 1K, 2K, 4K) or pixel dimensions such as 1920x1080"
    )


def build_prompt(setting: str, content: str) -> str:
    return f"""Create a polished editorial slide image.

SETTING AND VISUAL DIRECTION:
{setting}

SLIDE CONTENT:
{content}

Render the slide content faithfully and legibly as part of the scene. Preserve
its wording exactly. Do not add logos, captions, watermarks, or any other text.
Use a clear hierarchy and enough contrast for the slide to be readable at a
glance. The result must be a complete image, not a mockup surrounded by UI.
"""


def reference_part(path: Path) -> dict[str, object]:
    mime_type = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return {
        "type": "image_url",
        "image_url": {"url": f"data:{mime_type};base64,{encoded}"},
    }


def generate(
    api_key: str,
    model: str,
    prompt: str,
    resolution: str,
    references: list[Path],
) -> bytes:
    request_body: dict[str, object] = {
        "model": model,
        "prompt": prompt,
        "size": resolution,
        "n": 1,
    }
    if references:
        request_body["input_references"] = [reference_part(path) for path in references]
    payload = json.dumps(request_body).encode("utf-8")
    request = Request(
        API_URL,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://maratyv.com",
            "X-OpenRouter-Title": "maratyv.com slide generator",
        },
    )

    try:
        with urlopen(request, timeout=300) as response:
            result = json.load(response)
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenRouter returned HTTP {error.code}: {details}") from error
    except URLError as error:
        raise RuntimeError(f"Could not reach OpenRouter: {error.reason}") from error

    images = result.get("data") or []
    if not images:
        raise RuntimeError(f"OpenRouter returned no images: {json.dumps(result)}")

    image = images[0]
    encoded = image.get("b64_json") or image.get("b64Json")
    if encoded:
        if encoded.startswith("data:"):
            encoded = encoded.split(",", 1)[1]
        return base64.b64decode(encoded)

    image_url = image.get("url")
    if image_url:
        with urlopen(image_url, timeout=300) as response:
            return response.read()

    raise RuntimeError(f"Unsupported image response: {json.dumps(image)}")


def output_path_for_image(path: Path, image: bytes) -> Path:
    """Keep the filename extension consistent with the returned image bytes."""
    if image.startswith(b"\x89PNG\r\n\x1a\n"):
        suffixes = {".png"}
        preferred = ".png"
    elif image.startswith(b"\xff\xd8\xff"):
        suffixes = {".jpg", ".jpeg"}
        preferred = ".jpg"
    else:
        return path
    return path if path.suffix.lower() in suffixes else path.with_suffix(preferred)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider",
        choices=MODELS,
        default="gemini",
        help="image provider preset (default: gemini)",
    )
    parser.add_argument("--setting", required=True, help="visual direction, or @file")
    parser.add_argument("--content", required=True, help="slide copy, or @file")
    parser.add_argument(
        "--resolution",
        required=True,
        type=validate_resolution,
        help="512, 1K, 2K, 4K, or explicit pixels such as 2560x1440",
    )
    parser.add_argument("--output", type=Path, default=Path("slide.png"))
    parser.add_argument(
        "--reference",
        action="append",
        default=[],
        type=Path,
        help="reference image for visual continuity; may be repeated",
    )
    parser.add_argument("--model", help="override the selected provider preset")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env(Path(__file__).resolve().parents[1] / ".env")
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("OPENROUTER_API_KEY is missing; add it to .env", file=sys.stderr)
        return 2

    model = args.model or MODELS[args.provider]
    prompt = build_prompt(text_argument(args.setting), text_argument(args.content))
    image = generate(api_key, model, prompt, args.resolution, args.reference)
    output = output_path_for_image(args.output, image)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(image)
    print(f"Wrote {output} ({len(image):,} bytes) with {model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
