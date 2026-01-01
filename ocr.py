from paddleocr import PaddleOCR

# Инициализируем один раз
ocr = PaddleOCR(
    lang="ru",
    use_angle_cls=True,
    show_log=False
)

def extract_text(image_path: str) -> list[str]:
    result = ocr.ocr(image_path, cls=True)

    lines = []
    for block in result:
        for line in block:
            text = line[1][0]
            lines.append(text)

    return lines
