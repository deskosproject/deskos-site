# DeskOS website

The public site for DeskOS. Static HTML and CSS, no build step, no JavaScript.

## Run it

```bash
python3 -m http.server 8080
# http://localhost:8080/
```

## Design

A blueprint, not a brochure: graphite ground, paper text, one amber accent, thin
rules and mono labels for anything a reader might check. The wordmark and Manrope
come from `deskos-brand`; everything else here is new.

Rules the page holds itself to:

- Say only what the repository verifies. A platform that has not been booted says
  so; an ISO that does not exist yet says it is being built.
- No telemetry, no third-party scripts, no fonts from a CDN.
- One accent per screen. If a colour is not carrying meaning, it is not there.

## Status

First version, not deployed. The download section will read a published index
once the installer ISOs exist; today it points at the image and
`bootc-image-builder`.
