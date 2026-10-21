# AGENTS.md

Working rules for this repository. `README.md` explains what the site is; this
file is how to change it without breaking it.

## What this is

A static site: one `index.html`, one stylesheet, a few SVG assets and the
hand-drawn plates. **No build step, no JavaScript, no framework.** Open
`index.html` or run `python3 -m http.server 8080` and you are looking at
production.

## Content rules

1. **Say only what the repository verifies.** The source of truth is
   `deskosproject/deskos-core`: `docs/platforms.md` for the platform matrix,
   `docs/architecture.md` for validation status. If a platform has not been
   booted, the page says so. If an ISO does not exist, it is "in progress".
2. **No invented features.** No lockfiles, no fleets, no compliance, no AI. If a
   sentence implies a capability, the capability must exist in Core first.
3. **One promise per screen.** The hero says one thing. If a new section needs
   two paragraphs to justify itself, it belongs in the docs, not here.
4. **No telemetry.** No analytics, no trackers, no third-party scripts, no fonts
   from a CDN. The site never phones home.
5. **Links go to the repository** for anything that changes: platform status,
   install steps, architecture. Do not duplicate the docs, point at them.

## Design rules

- **Palette.** Paper `#F1F5F8`; ink `#1E2A33`; the brand blue `#4E7892` (taken
  from the lockup's symbol); one muted warning `#A5564A`. Do not introduce a
  second accent.
- **Type.** Serif display (`Iowan Old Style`/Palatino/Georgia stack) and Manrope
  for body, both defined in `assets/site.css`. Mono is for anything a reader can
  check: digests, versions, commands.
- **Logo.** `assets/lockup.svg` is the horizontal lockup from
  `deskos-core/docs/images/deskos-lockup-light.svg`; `assets/favicon.svg` follows
  the same geometry. Do not redraw either.
- **Illustrations are plates, not CSS diagrams.** `assets/intent-to-image.*`,
  `four-layers.*` and `install-update-reboot.*` come from generated artwork in a
  notebook style, each as WebP + JPEG. They sit on the paper with
  `mix-blend-mode: darken` and a feathered edge. Do not replace them with CSS
  boxes, and do not add text inside an image: AI lettering is unreliable, so
  labels live in HTML/SVG.
- **Alternating layout.** Sections pair text and a plate, alternating sides
  (`.split` / `.split.flip`). Below 980 px everything stacks with the text
  first.
- **No dark mode** by decision: the site is paper. Do not add a theme toggle.

## Deployment

- GitHub Pages, from `main`, branch root; `.nojekyll` keeps files as they are.
- Custom domain: `deskos.org` (and `www.deskos.org`). The `CNAME` file at the
  root must keep saying `deskos.org`.
- **DNS is not managed here.** `deskos.org` lives in
  `~/Documents/Projects/DeskOS/deskos-infrastructure` (Terraform, Cloudflare):
  apex `A` records to GitHub Pages and a `www` `CNAME` to
  `deskosproject.github.io`, both **DNS-only** so GitHub can issue the
  certificate. Secondary domains redirect to `deskos.org`. Change DNS there, not
  in the dashboard.
- After a DNS change, GitHub's certificate can take a while; `Enforce HTTPS` in
  the Pages settings is the last step, once the domain resolves.

## Before committing

- Preview at 360, 768 and 1440 px; the table scrolls, the hero stacks, the
  plates stay legible.
- Every relative link and `#anchor` resolves.
- No file is added that the page does not use; keep the pair WebP + JPEG for each
  plate.
- Small copy fixes may go straight to `main`; anything structural opens a pull
  request and waits for a human.

## Not in scope

- Downloads. `download.deskos.org` will be an R2 bucket, not this repository; do
  not add download links until the bucket and its index exist.
- Blog, changelog, docs site. Those live in the repositories that own the
  content.
- Personal data, forms, cookies, comments.
