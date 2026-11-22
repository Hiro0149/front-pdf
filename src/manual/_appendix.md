## Appendix A. Technical notes (for developers and AI code assistants)
- Single HTML file. Inlined libraries: pdf-lib 1.17.1 (PDF writing), PDF.js 6.5.438 legacy build (rendering and text extraction; the ESM build is converted to classic scripts; the worker runs from a Blob URL and falls back to the main thread where Workers are blocked), Japanese CMaps and the JBIG2/JPEG2000 wasm decoders embedded as base64. No network access of any kind.
- Data model: `state.sources` (original PDF bytes), `state.pages` (`{uid, srcId, idx, baseRot, rot, w, h, objects[]}`), `state.wm` (watermark). Object `type`: `text` (font `emoji` for emoji) / `shape` (`rect`, `ellipse`, `star`, `table` with rows/cols) / `line` / `pen` (style `pen`, `brush`, `air`) / `image` (`bfill` = bucket fill) / `stamp` (style `check`, `box`, `box2`, `oval`, `circle`, `date`, `square`, `image`) / `note` (sticky note). Units are PDF points; `o.fr` is the page rotation at creation time (objects keep their look when the page is rotated later).
- Export: pdf-lib copies the original page → markups are rendered to a transparent PNG (about 3× resolution) and drawn on top → sticky notes become Stamp annotations with an image appearance stream → optional A4 normalize / crop / 2-up. "Rasterize masked pages" renders the page with PDF.js at 200 dpi and replaces it with a JPEG, so no text data remains.
- Undo/redo: JSON snapshots from `serialize()`. Work file `.pdfkobo`: ASCII `PDFKOBO1` + flag byte (`Z` = gzip, `J` = plain) + JSON (original PDFs in base64, pages, objects, images, watermark).
- Two-page view: `ed.panes` holds up to 2 page uids; `ed.ai` is the active pane; canvases `#edBase/#edOv` and `#edBase2/#edOv2`.
- i18n: runtime DOM translation with a MutationObserver. Dictionary `I18N` (`ex` exact strings, `pat` regex patterns, `html` rich text). Japanese is the source language.
- Skins: body class `skin-modern` / `skin-dark` / `skin-98` / `skin-aqua` / `skin-gba` + CSS variables.
- Browser storage (localStorage, prefix `pdfkobo98.`): stamp book, skin, language, thumbnail settings, note author, recent colors.

## Appendix B. License
Front PDF — Copyright (c) 2026 Front Softworks — released under the MIT License (full text in the LICENSE file and in the app: [ⓘ] → MIT License). Bundled third-party components and their licenses: THIRD_PARTY_NOTICES.txt and the app: [ⓘ] → Third-party licenses.
