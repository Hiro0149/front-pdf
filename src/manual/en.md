# Front PDF User Manual (English) v1.1.0 (2026-11-23)

## 1. Overview
- Front PDF is a PDF editor that runs just by opening one HTML file (about 4 MB) in a browser (Edge or Chrome recommended). No installation.
- Fully offline. Files are never sent anywhere; everything is processed inside the browser on your PC.
- Features: merge, split, reorder, rotate and delete pages of PDFs and images; annotate pages (pen, shapes, text, sticky notes, stamps, emoji, images); black-out / white-out; text search; rectangle text copy (tables paste straight into Excel); watermark; A4 normalize; 2-up/4-up; PNG export; work files.
- You can also add blank pages and lay out documents freely, like a word processor.
- The built-in "Desk" lays out a folder's PDFs, work files and images as thumbnails you can place freely, and lets you merge, split, rename, move and print them (like DocuWorks Desk; see section 16).

## 2. Screen layout
- Title bar (right): Image import (layout when opening PNG/JPEG: Place on A4 / Keep image size), Skin, Language (globe), ? (help), ⓘ (version and license).
- Toolbar row 1: the File block at the top left (Open / Save PDF / Save work file / Save as / Print / PNG), View (▦ Grid / ✎ Edit), Page (Add blank, Rotate left/right, Duplicate, Delete page), Undo / Redo. [Desk] in the title bar switches to the desk (section 16).
- Toolbar row 2 (Edit mode only): ◀ page number ▶, Zoom (− / menu / +), Search (box, ▲▼, hit count, Highlight all, Black out all), All pages (Watermark, Clear markups).
- Left: thumbnails (Size slider and Columns on top). Drag the divider to change its width.
- Toolbox (5 groups), page viewer in the middle, properties panel on the right (settings of the selected markup or tool), status bar at the bottom.

## 3. Modes
- Edit mode (✎ Edit): thumbnails on the left, annotate the page on the right.
- Grid mode (▦ Grid): large thumbnails only, for organizing pages. Double-click or press Enter to edit a page.
- Two-page view: click one thumbnail, then Ctrl+click another. The two pages appear side by side and both can be annotated (the active page has a frame). Click a single page to return.

## 4. Open & merge
- [Open] (Ctrl+O) or drag & drop PDF / PNG / JPEG / work files (.frontpdf). Any number of files. The thumbnail order is the merge order.
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
- Saved automatically in the browser (per PC and browser). [Export (backup)] writes StampBook_Front_PDF.json; [Import] reads it.

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

## 12. Save & print
- [Save PDF] (Ctrl+S): a PDF opened from the desk is overwritten in place (the previous version is kept in the "_削除予定" folder of the same folder and can be restored with [Undo] on the desk). With a work file open, a PDF with the same name is created next to it. When the desk was not used, it works like [Save as].
- [Save as]: choose a name and format (PDF / work file). The format of the open file is selected first. For PDF you can choose: merge all pages / selected pages only / split every page / every N pages / by ranges (e.g. 1-3, 4-6, 7), fit to A4, crop margins (mm), 2-up / 4-up, document title.
- If there are black-outs or white-outs, you are asked before saving. Masks are only laid on top and the text underneath remains, so for confidential information choose "Save masked parts as images (recommended)" (only those pages are rasterized and the text data is removed).
- [Print] (Ctrl+P): prints with markups, stamps, notes and watermark. Choose the printer and copies in Edge's print screen.
- [PNG]: selected pages / all pages as PNG at 96, 150 or 300 dpi.
- Markups are burned into the PDF as images (any language prints as is). Sticky notes become annotations.

## 13. Work files (.frontpdf)
- [Save work file] saves a .frontpdf (overwrites when a work file is open). Open it with [Open], drag & drop, or a double-click on the desk to continue with pages, markups, stamps, notes and watermark still editable. You can hand it to a colleague to make corrections according to the notes.
- Caution: the work file contains the original PDF as is (including the text under black-outs). Do not give it to outsiders; give them a PDF made with [Save PDF].
- The stamp book and undo history are not included. Unsaved changes show * in the title and you are warned when closing.

## 14. View & settings
- Zoom: Fit page / Fit width / 25–400%, Ctrl+wheel, Ctrl++ / Ctrl+−, Ctrl+0 to fit the page.
- Thumbnails: Size slider, Columns (Auto / 1–6), Ctrl+wheel.
- Skins: Modern / Dark / Retro PC / Aqua / Handheld / Fluffy pets. Languages: 日本語, English, 简体中文, 繁體中文, Português, Français, 한국어. Both are remembered.

## 15. Keyboard shortcuts
- Ctrl+O open / Ctrl+S save (Save PDF for a PDF opened from the desk, otherwise Save work file) / Ctrl+P print / Ctrl+Z undo / Ctrl+Y or Ctrl+Shift+Z redo / Ctrl+F search / F3 or Enter next hit / Shift+Enter previous hit
- Delete: delete the selected markup (pages when the thumbnails are focused) / arrow keys nudge (Shift = bigger) / Esc deselect → Select tool
- PageUp / PageDown change page / Ctrl+A select all thumbnails (all text in Select text) / Ctrl+C copy selected text / Ctrl+V paste image or text
- Ctrl+wheel, Ctrl++ / −, Ctrl+0 zoom / Ctrl+Enter finish typing in a sticky note

## 16. Desk
- The app starts on the desk. Use [Choose folder] to pick the top folder with your documents (Box Drive folders work too): the folder tree appears on the left and PDFs, work files (.frontpdf), JPG and PNG appear as thumbnails on the right. The last folder opens automatically next time (the browser may require one click). Edge / Chrome only.
- Drag thumbnails anywhere. The layout is saved in a ".frontpdf-desk" file in the folder and shared with anyone who opens it. [Arrange] sorts by name; the slider sets the size. Frame colors: PDF = red, work file = blue, image = green.
- Open: double-click or Enter opens the editor in a new window; the [Editor] button opens an empty editor. Preview: Space, or press and release Ctrl+Shift (←→ pages, ↑↓ documents, Enter to open, Esc to close).
- Merge: drop a document onto another (the dragged one goes first, the target after it), or select several and right-click [Merge]. You confirm the order and name first. Images become PDF pages. If work files are included, the result is a work file and markups and notes are kept.
- Split into pages: splits a PDF into one PDF per page (same folder / new folder).
- Move: drag to the folder tree on the left. Dropping from Explorer imports (copies). Ctrl+C / Ctrl+V duplicates, F2 renames, Ctrl+F filters by file name, Ctrl+P prints (PDF and images). Right-click for the menu.
- Deleted files and previous versions of overwritten files go to a "_削除予定" folder created automatically inside that folder (it is not the Windows or Mac trash). When no longer needed, right-click the "_削除予定" folder → [Empty] to delete permanently (cannot be undone).
- Undo Ctrl+Z / Redo Ctrl+Y: moves, renames, deletions, merges, splits, overwrites and more, as many times as you like. Changes to the folder (by others or Box sync) appear automatically.
- [Log] / [Copy log]: an activity record. Paste it when reporting a problem.

## 17. Distribution & troubleshooting
- Company mail systems may block .html attachments → send a ZIP or use a shared folder / Teams.
- Opening the file directly from a mail or cloud preview imposes restrictions (stamp book not remembered, no save dialog, no clipboard) → save it to the PC first and double-click it.
- Stamp book, skin, language, note author etc. are stored in each PC's browser (localStorage, prefix pdfkobo98.). Clearing browser data removes them, so back up the stamp book.
- Not supported: editing existing PDF text in place, true redaction (removal from the PDF structure; use page rasterization instead), OCR, digital signatures, creating form fields.

## 18. License, copyright and official source
- Copyright © 2026 Front Softworks. License: MIT License (full text in the app via [ⓘ] → MIT License, and in the LICENSE file).
- Under the MIT License anyone — individuals and companies — may use, copy, modify, redistribute and use it commercially for free. The only condition is to keep the copyright notice and the license text.
- No warranty: the software is provided "as is" and the author accepts no warranty or liability. Always check the exported result of important documents.
- Bundled software: PDF.js (Apache License 2.0); pdf-lib, pako, @pdf-lib/standard-fonts, @pdf-lib/upng, qrcode-generator (MIT); tslib (0BSD); Adobe CMaps (BSD-3-Clause); PDFium JBIG2 (BSD-3-Clause); OpenJPEG (BSD-2-Clause). License texts: [ⓘ] → Third-party licenses, and THIRD_PARTY_NOTICES.txt.
- Official source: the GitHub releases page (the URL is shown in [ⓘ]). Files obtained elsewhere may have been modified; the author is not responsible for problems caused by modified versions.
- The author never distributes the software by email. When recommending it, share the official source URL instead of the file ([ⓘ] → "Copy intro text and URL"). The welcome screen on first launch also shows the official source.
- Exported PDFs carry "Front PDF v1.1.0 (Front Softworks)" and the official URL in their properties (Producer/Creator).
- On first use a free activation is needed (once per browser): (1) copy "this browser's ID" shown on screen (8 random characters made by the app; contains no PC or personal information), paste it into "Activation" on the official page and press "Issue"; (2) paste the password shown there (or the 10-character short password) into the app. Scanning the QR code on screen with a phone opens the official page with the ID filled in. The password works only in that browser, not on other PCs or browsers. The official page does not send the ID anywhere; it calculates inside the browser. Clearing browser data changes the ID, so activate again. The ID can be copied at any time while this screen is open (it cannot be closed, so you cannot miss it).
- Other software by Front Softworks: ExVAN Planner (container loading optimizer, https://exvan-planner.github.io/).
- How to verify the file is unmodified (Windows, nothing to install): run `certutil -hashfile Front_PDF.html SHA256` in Command Prompt and check that the value matches the SHA-256 published at the official source.
