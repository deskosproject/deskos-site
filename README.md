# DeskOS website

The public site for DeskOS. Static HTML and CSS, no build step, no JavaScript.

## Run it

```bash
python3 -m http.server 8080
# http://localhost:8080/
```

## Design

A blueprint, not a brochure: graphite ground, paper text, one cold-blue accent, thin
rules and mono labels for anything a reader might check. The wordmark and Manrope
come from `deskos-brand`; everything else here is new.

Rules the page holds itself to:

- Say only what the repository verifies. A platform that has not been booted says
  so; an ISO that does not exist yet says it is being built.
- No telemetry, no third-party scripts, no fonts from a CDN.
- One accent per screen. If a colour is not carrying meaning, it is not there.

## Status

The page lists the three published platforms (CentOS Stream 10, Fedora 45 and
AlmaLinux 10) and RHEL 10 as private. The download section points at the Core
image and `bootc-image-builder`; only CentOS Stream 10 also has a published
installer ISO.
