# maratyv.com — personal site

- Static personal site on GitHub Pages (`master` branch).
- Plain HTML + one CSS file. 
- No build step, no JS, no external dependencies

## Structure

- `index.html` — post list: gray `dd/mm/yyyy` date, title (the only link), media preview. Newest first.
- `posts/<slug>/index.html` — one page per post, media files live in the same folder.
- `cv/index.html` — CV.
- `style.css` — the only stylesheet. Design tokens and policies are documented at the top of the file.

## Publishing posts (binding)

- Whenever adding a new post, add its canonical `https://maratyv.com/posts/<slug>/` URL to `sitemap.xml` in the same change.
- Before finishing, verify that every `posts/<slug>/index.html` page is represented in `sitemap.xml`.

## Local development

- When previewing the site locally, run BrowserSync in a dedicated detached `tmux` session so its output can be watched independently:

```sh
tmux new-session -d -s maratyv-server -c "$PWD" \
  'npx browser-sync start --server . --files "**/*.{html,css,js,png,jpg,jpeg,gif,svg,mp4}" --listen 127.0.0.1 --no-open --no-ui --no-ghost-mode --no-notify'
```

- Open the preview at `http://127.0.0.1:3000`.
- Watch the server with `tmux attach -t maratyv-server` and detach with `Ctrl-b d`.
- Stop it with `tmux kill-session -t maratyv-server`.

## Design code (binding)

- Keep the design intentionally minimalistic. 
- Any element, color, or accent should be intentional and serve a purpose.
- Prefer to use fonts and spacing to separate elements from each other instead of blocks, lines, or other elements
- If some post introduces a new element or style, propose to consistently apply that changes to other pages where it make sense
- Never squash images and videos vertically or horizontally, including the carusels
- Prefer shades of gray to colors

Editorial-serif direction, black/white/gray only:

- Serif system stack (Charter/Georgia). One typeface, weights 400/700.
- Single centered column, `max-width: 44rem`. Grays via CSS variables; dark mode via `prefers-color-scheme` only.
- Dates above titles, `dd/mm/yyyy`, soft gray (`--ink-soft`).
- Links: ink-colored, thin underline offset 3px. In list entries only the title links.
- No borders except 1px hairlines (`--ink-faint`) between major sections. No shadows, no rounded corners.
- Media full column width. Carousels are CSS-only: `.carousel` flex + `scroll-snap-type: x mandatory`.
- Spacing in multiples of `--space` (1.5rem).
