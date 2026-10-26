# Website content plan (draft)

Status: draft for review. It proposes an information architecture and a
screenshot inventory; it does not change the current page.

## Goal

The site should answer three questions, in this order, for three readers:

1. **What is DeskOS?** A workstation compiled from declared intent into a
   bootable image. One screen, no jargon.
2. **Can I trust it?** What was built, booted and measured, per platform and per
   digest, with the same honesty as `deskos-core/docs/platforms.md`.
3. **How do I use it?** Install it, run it, install software, update it, and
   recover it. Then, for developers, how to build and extend it.

The reference reader changes per track: a normal user who has never run an
image-based system, a developer who knows containers, and an organization that
wants to extend Core without forking it.

## Principles

- **Two tracks, one promise.** The user track explains tasks; the developer
  track explains the model. Neither assumes the other's vocabulary.
- **Screenshots are evidence.** Every screenshot comes from a real build, with
  the digest visible where it matters. No mockups, no invented UI.
- **One screenshot per step.** A screenshot sits next to the instruction it
  belongs to, not in a gallery at the end.
- **Say only what is verified.** A feature that is not measured says so; an ISO
  that does not exist is "in progress".
- **Do not duplicate reference docs.** The site owns the beginner path and the
  tasks; Core owns the model, the platform matrix and the ADRs, and the site
  links to them.
- **No external comparisons.** Explain what we do, not who else does it.

## Information architecture

```
/                 Home: what it is, what is verified, where to start
/install/         Download, verify, write the USB, boot, first login
/manual/          User guide, task by task
  first-boot/     Welcome, language, network, account
  desktop/        Top bar, dock, application grid, windows
  software/       Bazaar, Flatpak, mise, and what belongs to the image
  updates/        Update, reboot, rollback, what survives
  files/          Home, /var, backups, external disks
  printing/       Printers and scanners
  network/        Wi-Fi, VPN, proxies
  troubleshooting/ Symptom, check, remedy
  faq/            Short answers, including "is this a distribution?"
/developers/      The model and the build
  bootc/          Image, deployment, update, rollback, from zero
  build/          Render, build, boot a local disk
  plan/           Resources, layers, the typed Plan
  extend/         Add packages, apps, settings without forking Core
/organizations/   Multiple workstations, private registry, evidence, support
/evidence/        What is verified, by digest and platform
```

The current single page becomes the home; the rest are new pages. Keep the same
design rules: paper, one accent, plates for illustration, mono for anything a
reader can check.

## Page outlines

### Home

- One sentence: a workstation compiled from declared intent.
- Three cards: **declared** (YAML), **composed** (layers, no last writer wins),
  **bootable** (an image and a disk).
- "Verified today": the latest digest, the platform matrix (published / booted /
  not measured), and a link to `/evidence/`.
- Primary action: install. Secondary: read the manual, or build it yourself.
- Screenshots: the desktop (hero), the application grid, the update
  notification.

### Install

- What you need: a USB stick, UEFI, and the target disk.
- Download: platform, file name, size, SHA-256, signature.
- Verify: the two commands, and what a good result looks like.
- Write and boot: one command per OS family.
- Try it first: the VM path.
- First login.
- Screenshots: installer language, disk selection, progress, success; GDM;
  first desktop.

### User manual

Every chapter follows the same shape:

1. what it does and when to use it;
2. the steps, each with one screenshot;
3. "if it fails": the two or three checks a person can run;
4. a link to the reference doc, not a copy of it.

**First boot.** Language, keyboard, timezone, network, account, and the first
login. Explain that the system is already installed and what the first update
does.

**Desktop.** Top bar, dock, application grid, windows, workspaces, lock screen.

**Software.** This is the page the current site lacks:

- **Bazaar** for applications, and `flatpak` for the same thing from a
  terminal: `flatpak install`, `flatpak update`, `flatpak list`,
  `flatpak uninstall`, and permissions with Flatseal.
- **mise** for command-line tools: install it, `mise use -g <tool>@<version>`,
  a project's `.mise.toml`, and why a tool installed this way survives updates.
- **What belongs to the image.** System packages are part of the image and are
  not layered at runtime; explain the boundary so a user does not look for
  `dnf install`.
- When to use each: Bazaar/Flatpak for desktop apps, mise for CLI tools, the
  image for anything that must be present before login or for every user.

**Updates.** The update notification, `deskos update`, reboot, `bootc status`,
and rollback: what it does, how to go back, and what survives (`/var`, Flatpaks,
home). One screenshot of a real update and one of a rollback.

**Files and backups.** Home versus `/var`, external disks, and Deja Dup.

**Printing, network.** Printers, scanners, Wi-Fi, VPN, proxies. Short.

**Troubleshooting.** A table with symptom → check → remedy, built from real
field reports: no network at login, a Flatpak that will not install, a full
disk, a failed update, a black screen after resume.

**FAQ.** "Is this a distribution?", "Do I use dnf?", "What happens to my files
on update?", "Can I install RPMs?", "Does it work on my laptop?" (point at the
platform matrix and the tested model, without promising more).

### Developers

**bootc from zero.** The page a developer needs before the ADRs:

- an image, not a package set: what `bootc` is and what it replaces;
- deployment, update and rollback, with `bootc status` output annotated;
- what is immutable and what is not: `/usr` from the image, `/etc` and `/var`
  writable, what a user change means;
- why an update is atomic and why a failed boot rolls back.

Include one diagram of the boot chain and one real `bootc status` capture.

**Build.** From this repository: `make validate`, `make render`, build the
image, write a disk, boot it. One command block per step and the expected
output.

**Plan.** Resources → validation → composition → typed Plan → backend. Link to
the ADRs; show a small YAML and the plan it produces.

**Extend.** Add a package set, a Flatpak, a setting, a binary artifact; keep the
organization out of Core. Point at the example organization.

### Organizations

Multiple workstations, a private registry, pull credentials, evidence, and the
support statement. Link to Core's organization docs instead of repeating them.

### Evidence

Per digest: the index, what the boot and session checks prove, what was not
measured, and the signature. This page is generated from the evidence index, not
written by hand.

## Screenshot inventory

Capture at 1440×900, same theme, real digest; no serial numbers, hostnames or
personal files. Store as WebP with a JPEG fallback, with alt text.

| # | Page | What it shows | Source | Status |
|---|---|---|---|---|
| 1 | Home | Desktop with dock and wallpaper | VM | to capture |
| 2 | Home | Application grid with the declared Flatpaks | VM | to capture |
| 3 | Home | Update-available notification | VM | to capture |
| 4 | Install | Installer: language | VM/ISO | to capture |
| 5 | Install | Installer: disk selection | VM/ISO | to capture |
| 6 | Install | Installer: progress and success | VM/ISO | to capture |
| 7 | Install | GDM login with the wordmark | VM | to capture |
| 8 | First boot | Welcome and first desktop | VM | to capture |
| 9 | Desktop | Top bar, dock and a window | VM | to capture |
| 10 | Software | Bazaar with a search result | VM | to capture |
| 11 | Software | `flatpak install` and `flatpak list` | VM | to capture |
| 12 | Software | `mise use -g` and the tool running | VM | to capture |
| 13 | Updates | `deskos update` and the reboot prompt | VM | to capture |
| 14 | Updates | `bootc status` with booted and rollback | VM | to capture |
| 15 | Files | Home, `/var` and an external disk | VM | to capture |
| 16 | Troubleshooting | `deskos check` output | VM | to capture |
| 17 | bootc | Annotated `bootc status` | VM | to capture |
| 18 | Build | `make render` output and the Containerfile | host | to capture |
| 19 | Extend | A small organization root and its plan | host | to capture |
| 20 | Evidence | The evidence index for one digest | browser | to capture |

Rules for the set: one accent, no pointing arrows added to screenshots, no
personal data, and the same wallpaper and theme throughout so the manual looks
like one product.

## Copy rules

- Define each term once, in one line: image, deployment, rollback, Flatpak,
  mise, bootc. The first use links to that definition.
- Prefer a verb and an object ("install an application") over a noun phrase
  ("application installation").
- Every page ends with "where to go next", not with a sales line.
- A failure is documented with the message the user will see, quoted exactly.

## Acceptance

- Home answers "what is this?" above the fold, with one screenshot.
- Install has the verify commands and a VM path.
- The software page covers Bazaar, `flatpak` and mise, and explains the image
  boundary.
- The developer bootc page can be read without opening an ADR.
- Every chapter has at least one real screenshot and an "if it fails" box.
- No page duplicates a Core reference doc; each links to it.

## Open questions

1. **Where does the user manual live?** This plan puts the beginner path on the
   site and links the reference to Core. The alternative is to keep everything
   in Core docs and have the site link out. Decide before writing.
2. **Versioned docs?** Pre-1.0 there is no migration between versions; a single
   current manual is simpler.
3. **Who captures the field screenshots?** The VM set can be automated in CI;
   hardware shots come from the field validation.
4. **Languages.** English first; decide whether the manual ships translated
   with the site or links to translated pages.
