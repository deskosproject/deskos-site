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
AlmaLinux 10) and RHEL 10 as private. CentOS Stream 10 and Fedora 45 have a
published installer ISO; AlmaLinux 10 points at the Core image and
`bootc-image-builder`.

The hero offers the two adoption paths: compile from `deskosctl render`, or boot
the reference ISO. `01 Compile` shows the reference workstation as YAML and an
excerpt of the Containerfile it renders, then the three alternatives it
replaces.
