from pathlib import Path

from screenshot_utils import is_screenshot


def test_detects_macos_screenshot() -> None:
    path = Path("Bildschirmfoto 2026-06-24 um 10.00.00.png")
    assert is_screenshot(path) is True


def test_rejects_screenshit_name_without_image_extension() -> None:
    path = Path("Bildschirmfoto 2026-06-24.txt")
    assert is_screenshot(path) is False


def test_rejects_regular_image() -> None:
    path = Path("vacation.png")
    assert is_screenshot(path) is False


def test_accepts_uppercase_image_extension() -> None:
    path = Path("Bildschirmfoto 2026-06-24.PNG")
    assert is_screenshot(path) is True
