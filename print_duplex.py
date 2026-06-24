# Copyright 2026 Ilya Sherman (ishermandom@)
# SPDX-License-Identifier: MIT

"""Renders scoresheet_v4.html to a duplex-ready two-page PDF.

Page 1 is the front side (+90° rotation); page 2 is the back side
(-90° rotation). Print both sides of a single sheet to get the duplex
scoresheet.

Usage:
  python print_duplex.py
"""

import argparse
import asyncio
import tempfile
from pathlib import Path

from playwright.async_api import Page, async_playwright
from pypdf import PdfWriter

_DIR = Path(__file__).parent


def _latest_scoresheet() -> Path:
  """Returns the highest-versioned scoresheet_v*.html in the script directory."""
  candidates = sorted(
    _DIR.glob('scoresheet_v*.html'),
    key=lambda p: int(p.stem.removeprefix('scoresheet_v')),
  )
  if not candidates:
    raise FileNotFoundError('No scoresheet_v*.html found in script directory')
  return candidates[-1]


async def _render_pdf(page: Page, dest: Path) -> None:
  """Prints the current page state to a PDF at dest."""
  await page.pdf(
    path=str(dest),
    format='Letter',
    print_background=True,
  )


async def main() -> None:
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    '-i',
    '--input',
    type=Path,
    default=None,
    metavar='FILE',
    help='HTML scoresheet to render (default: latest scoresheet_v*.html)',
  )
  parser.add_argument(
    '-o',
    '--output',
    type=Path,
    default=None,
    metavar='FILE',
    help='PDF output path (default: latest.pdf alongside input)',
  )
  args = parser.parse_args()

  html_path = args.input.resolve() if args.input else _latest_scoresheet()
  output_path = (
    args.output.resolve() if args.output else html_path.parent / 'latest.pdf'
  )

  with tempfile.TemporaryDirectory() as tmp:
    side_a = Path(tmp) / 'side_a.pdf'
    side_b = Path(tmp) / 'side_b.pdf'

    async with async_playwright() as p:
      browser = await p.chromium.launch()
      page = await browser.new_page()
      await page.goto(html_path.as_uri())

      await _render_pdf(page, side_a)  # front: rotate(90deg)

      await page.evaluate("document.body.classList.add('reverse')")
      await _render_pdf(page, side_b)  # back: rotate(-90deg)

      await browser.close()

    writer = PdfWriter()
    writer.append(str(side_a))
    writer.append(str(side_b))
    writer.write(str(output_path))

  print(f'Written: {output_path}')


asyncio.run(main())
