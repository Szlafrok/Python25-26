from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Union, cast

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:
    raise SystemExit(
        "Brakuje biblioteki Pillow. Zainstaluj ją komendą: pip install pillow"
    ) from exc

Czcionka = Union[ImageFont.FreeTypeFont, ImageFont.ImageFont]
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
OUTPUT_DIR = BASE_DIR / "output"

TEMPLATES: dict[str, Path] = {
    "1": TEMPLATES_DIR / "take-my-money.png",
    "2": TEMPLATES_DIR / "boromir-one-does-not-simply.png",
    "3": TEMPLATES_DIR / "smart-pointing-at-head.png",
}


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)


def print_templates() -> None:
    print("Dostępne szablony:")
    print("  1 - take my money")
    print("  2 - one does not simply")
    print("  3 - smart pointing")


def ask_template_key() -> str:
    while True:
        key = input("Wybierz szablon (1/2/3): ").strip()
        if key in TEMPLATES:
            return key
        print("❌ Zły wybór. Wpisz 1, 2 albo 3.")


def ask_text(prompt: str) -> str:
    return input(prompt).rstrip("\n")


def build_output_path(template_path: Path) -> Path:
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    return OUTPUT_DIR / f"meme_{template_path.stem}_{timestamp}.png"

    raise NotImplementedError("TODO: build_output_path")


def measure_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: Czcionka,
    stroke_width: int,
) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    width = int(bbox[2] - bbox[0])
    height = int(bbox[3] - bbox[1])
    return width, height


def wrap_text(
    text: str,
    draw: ImageDraw.ImageDraw,
    font: Czcionka,
    max_width: int,
    stroke_width: int,
) -> list[str]:
    words = text.split()
    if not words:
        return []

    lines: list[str] = []
    current = words[0]

    for word in words[1:]:
        test_line = current + " " + word
        test_width, _ = measure_text(draw, test_line, font, stroke_width)
        if test_width <= max_width:
            current = test_line
        else:
            lines.append(current)
            current = word

    lines.append(current)
    return lines


def fit_font_and_lines(
    text: str,
    draw: ImageDraw.ImageDraw,
    max_width: int,
    start_font_size: int,
) -> tuple[Czcionka, list[str]]:
    if not text.strip():
        return ImageFont.load_default(size=start_font_size), []

    font_size = start_font_size

    while font_size >= 12:
        font = ImageFont.load_default(size=font_size)
        stroke_width = max(2, font_size // 15)

        all_lines: list[str] = []
        for raw_line in text.splitlines():
            all_lines.extend(wrap_text(raw_line, draw, font, max_width, stroke_width))

        if all_lines and all(
            measure_text(draw, line, font, stroke_width)[0] <= max_width
            for line in all_lines
        ):
            return font, all_lines

        font_size -= 2

    font = ImageFont.load_default(size=12)
    stroke_width = max(2, 12 // 15)
    return font, wrap_text(text, draw, font, max_width, stroke_width)


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: Czcionka,
    start_y: int,
    image_width: int,
) -> None:
    font_size = int(cast(ImageFont.FreeTypeFont, font).size)
    spacing = int(font_size * 0.20)
    stroke_width = max(2, font_size // 15)

    y = start_y
    for line in lines:
        line_width, line_height = measure_text(draw, line, font, stroke_width)
        x = int((image_width - line_width) / 2)

        draw.text(
            (x, y),
            line,
            font=font,
            fill="white",
            stroke_width=stroke_width,
            stroke_fill="black",
        )
        y += line_height + spacing


def add_meme_text(image: Image.Image, top_text: str, bottom_text: str) -> Image.Image:

    image = image.copy()
    draw = ImageDraw.Draw(image)

    margin = int(image.height * 0.05)
    max_width = int(image.width * 0.92)
    start_font_size = int(image.width * 0.08)

    if top_text.strip():
        font, lines = fit_font_and_lines(top_text.strip(), draw, max_width, start_font_size)
        draw_centered_lines(draw, lines, font, margin, image.width)

    return image
    
    raise NotImplementedError("TODO: add_meme_text")


def main() -> None:
    ensure_output_dir()

    print_templates()
    template_key = ask_template_key()

    top_text = ask_text("Napis górny (może być pusty): ")
    bottom_text = ask_text("Napis dolny (może być pusty): ")

    template_path = TEMPLATES[template_key]
    output_path = build_output_path(template_path)

    image = Image.open(template_path)
    meme_image = add_meme_text(image, top_text, bottom_text)
    meme_image.save(output_path)

    print("✅ Zapisano plik:", output_path)


if __name__ == "__main__":
    main()