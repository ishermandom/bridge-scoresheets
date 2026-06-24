# Bridge Scoresheets

HTML scoresheets for duplicate Bridge, with a script to generate printable PDFs.

## Overview

The repository contains a set of HTML scoresheets and a print-automation script,
`print_duplex.py`. The scoresheets are designed to be printed on 8.5" × 11"
paper and trimmed to 8" × 8.5" cards.

## Scoresheet design

The scoresheets are designed to make it easy to record a complete auction and
jot observations about each board, while fitting comfortably in a standard card
holder. That drives a core tradeoff: the **Auction + Notes** column needs to be
wide enough to write in freely, while rows still need to be tall enough to be
usable — so much of the design is optimized around that tension.

**Writable area.** The scoresheet slides into a transparent card holder that
covers the edges. Reference data — the IMP and VP conversion charts — is placed
in that covered band deliberately: still readable through the transparent
plastic, without competing with the writing area. Row heights fill the remaining
space exactly.

**Column ergonomics.** Scoresheets are often held in the air while writing,
since the information should stay private from opponents. That means the card
itself is the only support for the hand, so the layout keeps the writing surface
under the palm throughout: the notes column extends to the right edge so the
palm never hovers over empty air, and writable columns are kept clear of the
left edge where writing is physically awkward. Vertical rules divide the columns
into four functional zones — preprinted reference, scores, summarized notes, and
the detailed auction — with the within-zone separators softened to gray so the
boundaries stand out at a glance.

**Board reference.** Dealer and vulnerability are printed for every board, so
players can look them up at a glance rather than derive them mid-game.

**Game formats.** Twenty-eight rows support a pairs game of up to 28 boards, and
three common teams structures:

- **4 rounds × 7 boards:** black divider lines mark the round breaks.
- **4 rounds × 6 boards:** the same divider lines mark rounds, with one blank
  row per section available for a totals row.
- **3 rounds × 8 boards:** slightly darker rows at the round breaks serve as
  blank rows or a totals row.

The dividers are unobtrusive enough that they don't clutter a pairs game or a
teams format with a different structure.

**Printing.** The 8"×8.5" card is printed on 8.5"×11" paper and rotated 90° so
only one cut is needed. Hard-margin overlays (black) and soft-margin overlays
(translucent red) are design-time aids that show where the printer can't reach
and where the card holder covers; both are hidden at print time.

**Pen-friendly.** Fields are underlined, rows are generously tall, and the
palette is neutral grayscale — nothing that bleeds ink or distracts.

**Print-friendly.** The shading is calibrated for black-and-white laser printing
and doesn't assume a color printer. Values are tuned for a Brother HL-L2460DW
and may need minor tweaking for other printers.

## Printing

The easiest option is to print `latest.pdf` directly — it's a pre-rendered
duplex-ready PDF with front and back sides, committed to the repository
alongside the HTML files.

### Automated (`print_duplex.py`)

The script renders the scoresheet twice and combines the results into a single
duplex-ready PDF.

**Install dependencies:**

```
pip install playwright pypdf
playwright install chromium
```

**Usage:**

```
python print_duplex.py [-i SCORESHEET.html] [-o OUTPUT.pdf]
```

Both flags are optional. By default, the script picks the latest scoresheet in
the same directory and writes `latest.pdf` alongside it.

### Manual

1. Open a scoresheet HTML file in a browser and print the front side to PDF.
2. Open the browser console and run `document.body.classList.add('reverse')` to
   flip to the back side.
3. Print the back side to PDF.
4. Merge the two PDFs for duplex printing.

## License

Copyright 2026 Ilya Sherman (ishermandom@)

The scoresheets are licensed for non-commercial use; the print automation script
is MIT. See individual files for details.
