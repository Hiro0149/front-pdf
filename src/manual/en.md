# PDF_KOBO User Manual (English) v1.0.0 (2026-11-21)

## 1. Overview
- PDF_KOBO is a PDF editor that runs just by opening one HTML file (about 3.7 MB) in a browser (Edge or Chrome recommended). No installation.
- Fully offline. Files are never sent anywhere; everything is processed inside the browser on your PC.
- Features: merge, split, reorder, rotate and delete pages of PDFs and images; annotate pages (pen, shapes, text, sticky notes, stamps, emoji, images); black-out / white-out; text search; rectangle text copy (tables paste straight into Excel); watermark; A4 normalize; 2-up/4-up; PNG export; work files.
- You can also add blank pages and lay out documents freely, like a word processor.

## 2. Screen layout
- Title bar (right): Image import (layout when opening PNG/JPEG: Place on A4 / Keep image size), Skin, Language (globe), ? (help), ⓘ (version and license).
- Toolbar row 1: File (Open / Save work), View (▦ Grid / ✎ Edit), Page (Add blank, Rotate left/right, Duplicate, Delete page), Undo / Redo, and at the far right Export (Export PNG / Export PDF).
- Toolbar row 2 (Edit mode only): ◀ page number ▶, Zoom (− / menu / +), Search (box, ▲▼, hit count, Highlight all, Black out all), All pages (Watermark, Clear markups).
- Left: thumbnails (Size slider and Columns on top). Drag the divider to change its width.
- Toolbox (5 groups), page viewer in the middle, properties panel on the right (settings of the selected markup or tool), status bar at the bottom.

## 3. Modes
- Edit mode (✎ Edit): thumbnails on the left, annotate the page on the right.
- Grid mode (▦ Grid): large thumbnails only, for organizing pages. Double-click or press Enter to edit a page.
- Two-page view: click one thumbnail, then Ctrl+click another. The two pages appear side by side and both can be annotated (the active page has a frame). Click a single page to return.

## 4. Open & merge
- [Open] (Ctrl+O) or drag & drop PDF / PNG / JPEG / work files (.pdfkobo). Any number of files. The thumbnail order is the merge order.
- Images become one-page PDFs (according to "Image import").
- Password-protected PDFs cannot be opened.

## 5. Page operations
- Select: click, Ctrl+click (add), Shift+click (range), Ctrl+A in the thumbnails (all).
- Reorder: drag thumbnails.
- Rotate (↺↻), Duplicate and Delete page (Delete key) work on the selected pages. Add blank inserts an A4 page after the current page.
- Undo Ctrl+Z / Redo Ctrl+Y (one shared history for page operations and markups).

## 6. Tools
- Select: [Select] click to select a markup, drag to move, corners to resize, arrow keys to nudge (Shift = ×10), Delete to remove. Dragging from an empty spot selects text. [Select text] selects only the text inside the box you drag.
- Draw: [Pen], [Brush] (slow = thick, fast = thin; pen tablets use pressure; can switch to airbrush), [Marker pen], [Eraser] (erases pen strokes where you rub, other items entirely; never touches the original PDF). Pens: Shift = straight line in 45° steps, Ctrl = straight line at any angle.
- Shapes: [Box], [Ellipse], [Line], [Arrow], [Star], [Table] (set rows and columns in the right panel; borders only). Shift = square / circle / 45° line.
- Fill / Hide: [Highlight] (translucent yellow band), [White-out], [Black-out], [Fill] (click a markup = recolor; click inside a closed pen line = fill), [Color picker] (picks a color on the page and sets it on the previous tool or the selected markup; Alt+click while drawing).
- Insert: [Text] (click to place; content, size, font, color, background in the right panel), [Emoji] (choose in the panel, click to place; Win+. also works), [Sticky note] (paper style; click and type, double-click to edit again), [Stamp] (choose from the stamp book on the right, click to stamp), [Image] (choose a file).
- Right panel buttons: Delete / Duplicate / Bring to front / Send to back / To all pages (same spot on every other page) / Set as default / Add to stamp book.

## 7. Stamp book
- Types: check mark (✓), hanamaru (flower circle for praise), box, double box, oval, round seal (1–3 characters vertical), date stamp (top row, date, bottom row), square seal (4 characters in 2 columns, right to left), image (scanned seal).
- Edit text, color, size and date format (2026.11.20 / ’26.11.20 / R8.11.20 …). "Use the date when stamped" always inserts today's date.
- [From image] registers a scanned seal (white becomes transparent).
- Saved automatically in the browser (per PC and browser). [Export (backup)] writes StampBook_PDF_KOBO.json; [Import] reads it.

## 8. Sticky notes
- Paper-style notes like DocuWorks. Colors (yellow, pink, light blue, green, orange, purple, white), font size, text color, bold, author name (remembered).
- On PDF export they become annotations: Acrobat and Edge show them as they look, recipients can move or delete them, and they appear in the comment list. Turn on "Burn into the page" to make a note part of the content.
- Notes are not included in 2-up/4-up exports.

## 9. Text selection, copy and search
- [Select text]: only the characters whose center is inside the box you drag are selected. You can take just some columns of a table.
- Copy format: Table (tab-separated; splits into cells in Excel) / Plain text (space-separated). Ctrl+C copies, Ctrl+A selects the whole page.
- Search: Ctrl+F → type → Enter (next) / Shift+Enter (previous). Ignores full-/half-width and case. [Highlight all] / [Black out all] process every match.
- Scanned PDFs have no text data and cannot be selected or searched (no OCR).

## 10. Watermark
- [Watermark] adds a watermark to all pages and selects it. Change text, size, angle, color and strength in the right panel, or [Remove watermark]. Clicking the watermark text on the page also selects it.

## 11. Pasting and dropping images
- Ctrl+V an image copied with Snipping Tool etc.: placed at the mouse position if it is over the page, otherwise in the center of the visible area, at the size it had on screen. If the mouse is over the thumbnails, the image is added as a new page.
- Drop an image file on the page = place it there; drop it on the thumbnails = new page.
- Ctrl+V of text pastes it as a text object.

## 12. Export
- [Export PDF]: all pages merged / selected pages / one file per page / every N pages / by ranges (e.g. 1-3, 4-6, 7). Options: resize to A4, trim margins (mm), 2-up / 4-up, document title.
- If black-out or white-out is used, a confirmation appears. Masks only cover the text and the text data remains underneath, so for confidential information choose "Rasterize masked pages and export PDF (recommended)" — only those pages become images and their text data is removed.
- [Export PNG]: selected or all pages at 96 / 150 / 300 dpi.
- Markups are burned into the PDF as images (any language is preserved). Sticky notes are annotations.

## 13. Work files (.pdfkobo)
- [Save work] (Ctrl+S) saves a .pdfkobo file. Open it with [Open] or drag & drop to continue with pages, markups, stamps, notes and watermark still editable. You can pass it to a colleague who follows the instructions in the sticky notes.
- Caution: a work file contains the original PDF as is, including text under black-outs. Do not give it to people outside your organization; share the exported PDF instead.
- The stamp book and the undo history are not included. Unsaved changes show "*" in the title and trigger a warning when closing.

## 14. View & settings
- Zoom: Fit page / Fit width / 25–400%, Ctrl+wheel, Ctrl++ / Ctrl+−, Ctrl+0 to fit the page.
- Thumbnails: Size slider, Columns (Auto / 1–6), Ctrl+wheel.
- Skins: Modern / Dark / Retro PC / Aqua / Handheld. Languages: 日本語, English, 简体中文, 繁體中文, Português, Français, 한국어. Both are remembered.

## 15. Keyboard shortcuts
- Ctrl+O open / Ctrl+S save work / Ctrl+Z undo / Ctrl+Y or Ctrl+Shift+Z redo / Ctrl+F search / F3 or Enter next hit / Shift+Enter previous hit
- Delete: delete the selected markup (pages when the thumbnails are focused) / arrow keys nudge (Shift = bigger) / Esc deselect → Select tool
- PageUp / PageDown change page / Ctrl+A select all thumbnails (all text in Select text) / Ctrl+C copy selected text / Ctrl+V paste image or text
- Ctrl+wheel, Ctrl++ / −, Ctrl+0 zoom / Ctrl+Enter finish typing in a sticky note

## 16. Distribution & troubleshooting
- Company mail systems may block .html attachments → send a ZIP or use a shared folder / Teams.
- Opening the file directly from a mail or cloud preview imposes restrictions (stamp book not remembered, no save dialog, no clipboard) → save it to the PC first and double-click it.
- Stamp book, skin, language, note author etc. are stored in each PC's browser (localStorage, prefix pdfkobo98.). Clearing browser data removes them, so back up the stamp book.
- Not supported: editing existing PDF text in place, true redaction (removal from the PDF structure; use page rasterization instead), OCR, digital signatures, creating form fields.

## 17. License, copyright and official source
- Copyright © 2026 Front Softworks. License: MIT License (full text in the app via [ⓘ] → MIT License, and in the LICENSE file).
- Under the MIT License anyone — individuals and companies — may use, copy, modify, redistribute and use it commercially for free. The only condition is to keep the copyright notice and the license text.
- No warranty: the software is provided "as is" and the author accepts no warranty or liability. Always check the exported result of important documents.
- Bundled software: PDF.js (Apache License 2.0); pdf-lib, pako, @pdf-lib/standard-fonts, @pdf-lib/upng, qrcode-generator (MIT); tslib (0BSD); Adobe CMaps (BSD-3-Clause); PDFium JBIG2 (BSD-3-Clause); OpenJPEG (BSD-2-Clause). License texts: [ⓘ] → Third-party licenses, and THIRD_PARTY_NOTICES.txt.
- Official source: the GitHub releases page (the URL is shown in [ⓘ]). Files obtained elsewhere may have been modified; the author is not responsible for problems caused by modified versions.
- The author never distributes the software by email. When recommending it, share the official source URL instead of the file ([ⓘ] → "Copy intro text and URL"). The welcome screen on first launch also shows the official source.
- Exported PDFs carry "PDF_KOBO v1.0.0 (Front Softworks)" and the official URL in their properties (Producer/Creator).
- On first use a free registration is needed (once per PC and browser): (1) enter "this PC's ID" shown on screen (8 random characters made by the app; contains no PC or personal information) in "Registration" on the official page, (2) paste the issued registration text (or the 10-character code) into the app. Scanning the QR code with a phone opens the official page with the ID already filled in. The registration text works only on that PC. The official page does not send the ID anywhere; it is calculated in the browser. Clearing browser data changes the ID, so register again.
- Other software by Front Softworks: ExVAN Planner (container loading optimizer, https://exvan-planner.github.io/).
- How to verify the file is unmodified (Windows, nothing to install): run `certutil -hashfile PDF_KOBO.html SHA256` in Command Prompt and check that the value matches the SHA-256 published at the official source.
