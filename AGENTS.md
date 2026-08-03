# maratyv.com — personal site

Static personal site on GitHub Pages (`master` branch). Plain HTML + one CSS file. **No build step, no JS, no external dependencies** (no CDNs, web fonts, analytics, frameworks). It must keep working untouched for years.

## Structure

- `index.html` — post list: gray `dd/mm/yyyy` date, title (the only link), media preview. Newest first.
- `posts/<slug>/index.html` — one page per post, media files live in the same folder.
- `cv/index.html` — CV.
- `style.css` — the only stylesheet. Design tokens and policies are documented at the top of the file.

## Design code (binding)

Editorial-serif direction, black/white/gray only:

- Serif system stack (Charter/Georgia). One typeface, weights 400/700.
- Single centered column, `max-width: 44rem`. Grays via CSS variables; dark mode via `prefers-color-scheme` only.
- Dates above titles, `dd/mm/yyyy`, soft gray (`--ink-soft`).
- Links: ink-colored, thin underline offset 3px. In list entries only the title links.
- No borders except 1px hairlines (`--ink-faint`) between major sections. No shadows, no rounded corners.
- Media full column width. Carousels are CSS-only: `.carousel` flex + `scroll-snap-type: x mandatory`.
- Spacing in multiples of `--space` (1.5rem).

## Adding a post

1. Source drafts live in `../posts/linkedin/<n>-<name>/` (numbered = published; `idea-*` = not ready — never import those).
2. Convert the final markdown draft to HTML by hand into `posts/<slug>/index.html`, copying an existing post page as the template. No converter scripts.
3. Copy media into the post folder; compress large images.
4. Add the entry to the top of the list in `index.html` and a `<url>` to `sitemap.xml`.

## Rules

- Never introduce tooling, package.json, generators, or JS unless explicitly asked.
- Don't push to `master` without confirmation.
