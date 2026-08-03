# Plan: Modernize maratyv.com (mir.github.io)

## Problem statement

This repo (`/Users/maratyuldashev/work/mir.github.io`) is a personal site generated with Octopress around 2014–2015 and untouched since. It carries a decade of dead weight: IE conditional comments, Modernizr 2.0, jQuery 1.9 from a Google CDN over `http://`, remote Google Fonts, old Google Analytics (`_gaq`), Octopress JS, and a generated `blog/2014`, `blog/2015` tree. The owner wants to replace it with a modern, maintenance-free personal site.

**Goals:**

1. **Minimum tech, maximum longevity.** Plain static HTML + modern CSS + minimal (ideally zero) vanilla JS. No frameworks, no build step required at runtime, no CDNs, no external fonts, no analytics, no dependencies that rot. The site must "just work" for the next 10 years on GitHub Pages.
2. **Design: black / white / gray only.** Focus on excellent typography, alignment, whitespace, and simplicity. System font stack (e.g. `system-ui` / `-apple-system` or a classic serif stack). Support `prefers-color-scheme: dark` (invert: near-black bg, near-white text). Fully responsive with just fluid layout — no breakpoint acrobatics.
3. **Three page types:**
   - **Main page (`index.html`)** — per the owner's sketch: name "Yuldashev Marat" as the header; a vertical list of posts, each entry showing `dd/mm/yyyy`, post title (link), and its media (image / video / carousel) inline, since posts with visuals get more clicks; footer with contacts: `maratyv@gmail.com`, telegram `@maratyv`, `www.linkedin.com/in/marat-yuldashev/`.
   - **CV page (`cv/index.html`)** — same visual language; content can be seeded from the old `about/index.html` (photo `about/marat-yuldashev.jpg` exists) and left as a clean skeleton for the owner to fill in.
   - **One page per post (`posts/<slug>/index.html`)** — title, date, body, media. Carousel = pure CSS scroll-snap horizontal strip (`scroll-snap-type: x mandatory`), no JS needed; optional tiny vanilla-JS dots/arrows are acceptable but must degrade gracefully.

**Post source:** posts live outside this repo at `/Users/maratyuldashev/work/posts/linkedin/`. Each post is a folder (e.g. `1-research-plan-review/`, `2-jira/`, `5-mcp-cli-skills/`) containing several markdown drafts (`v1.md`, `v2.md`, `version-3-*.md`, `draft.md`, `idea.md`, etc.) and image assets (png/jpeg). Folders prefixed with a number (`1-` … `8-`) are published posts; folders prefixed `idea-` are unpublished ideas — **skip the `idea-*` folders**. For each numbered post, pick the most final-looking draft (highest version number, or the one that reads as a finished post — when ambiguous, list the candidates and ask the owner), convert it to HTML, copy its images into the site, and add it to the main page list. Dates: derive from git history or file mtimes if nothing better exists; flag any guesses to the owner.

## Constraints

- GitHub Pages hosting, `master` branch, plain static files. No Jekyll processing needed — add a `.nojekyll` file.
- No runtime dependencies: no CDN links, no web fonts, no jQuery, no analytics, no icon libraries.
- No build tooling at all — not even a local convert script. Markdown posts are converted to HTML manually (by the agent doing this work), pasted into the shared template, and committed as plain HTML. There are only ~8 posts; nothing needs to be repeatable.
- Keep it accessible: semantic HTML (`<main>`, `<article>`, `<time>`, `<nav>`), alt text on images, sufficient contrast (trivial in b/w).
- Preserve old URLs only if cheap; otherwise it's fine to drop the 2014 blog tree (decade-old content, near-zero traffic). Keep `favicon.png` or replace with a simple b/w one.

## Step 1 — Modernize what we have (cleanup)

1. Create a git branch (e.g. `modernize`).
2. Delete Octopress artifacts: `javascripts/`, `stylesheets/`, `assets/`, `atom.xml` (or regenerate later), `sitemap.xml` (regenerate at the end), `blog/` tree, `images/` (after checking nothing needed survives there), old `index.html`, `about/index.html` (salvage its text/photo first — save the CV-relevant content aside).
3. Add `.nojekyll`, keep `robots.txt` (simplify), keep/refresh `favicon.png`.
4. Create the new skeleton: `index.html`, `cv/index.html`, `posts/`, single `style.css` (one file, ~200 lines max, CSS custom properties for the gray scale).

## Step 2 — Redesign

1. **Typography-first layout:** single centered column, `max-width: 42–46rem`, generous line-height (~1.6), fluid type via `clamp()`. Grays only: e.g. `#111` text, `#666` secondary (dates), `#fff` bg; inverted for dark mode via CSS variables + `prefers-color-scheme`.
2. **Main page** exactly per the sketch: name top-left; post list where each entry is `<article>`: gray `<time>` date (dd/mm/yyyy), title as the only link styled with a subtle underline, then the post's media preview (image, `<video controls preload="metadata">`, or CSS scroll-snap carousel of images). Contacts block at the bottom in smaller gray text.
3. **Post page:** back-link ("← Marat Yuldashev"), title, date, prose, media. Shared `style.css`, no per-page CSS.
4. **CV page:** linked from main page header or footer; same column, clean sections (experience, education, contacts), photo optional.
5. **Carousel:** `<div class="carousel">` of images with `overflow-x: auto; scroll-snap-type: x mandatory;` children `scroll-snap-align: center`. No JS. Optional: thin scrollbar styling.
6. Validate: pages score clean in Lighthouse, work with JS disabled, look right at 320px and 1400px, and in dark mode.

## Step 3 — Import posts from `../posts/linkedin/`

1. Enumerate numbered folders `1-*` … `8-*` in `/Users/maratyuldashev/work/posts/linkedin/`, skipping `idea-*`.
2. For each: choose the final draft (see selection rule above), determine title (first heading or derived from folder name), date (git log / mtime — flag guesses), and collect its images.
3. Convert each chosen markdown draft to HTML by hand (no scripts, no tooling): write `posts/<slug>/index.html` following the shared post template, and copy media files into `posts/<slug>/`. Commit the plain HTML.
4. Update `index.html` post list (newest first) with date, title, and media preview per post.
5. Regenerate `sitemap.xml` (and optionally a minimal `atom.xml`) listing the new pages.
6. Final review pass: proofread each imported post's HTML rendering, check every image loads, run a link check, view on mobile width.

## Deliverables

- Clean repo: `index.html`, `style.css`, `cv/index.html`, `posts/<slug>/index.html` per post, `.nojekyll`, `robots.txt`, `sitemap.xml`, favicon.
- A short note in the PR/commit listing: which draft file was chosen per post, which dates were guessed, and anything skipped.
- Do **not** push to `master` without the owner's confirmation — leave the work on the `modernize` branch.
