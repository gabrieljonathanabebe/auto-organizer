from pathlib import Path
import time


def get_available_dest_path(dest_path: Path) -> Path:
    if not dest_path.exists():
        return dest_path
    counter = 1
    while True:
        candidate_path = dest_path.with_name(
            f"{dest_path.stem}_{counter}{dest_path.suffix}"
        )
        if not candidate_path.exists():
            return candidate_path
        counter += 1


def move_file(src_path: Path, dest_path: Path) -> None:
    src_path.rename(dest_path)


def has_stable_size(
    path: Path, checks: int = 3, delay_seconds: float = 0.2
) -> bool:
    if not path.exists():
        return False
    previous_size = path.stat().st_size
    for _ in range(checks):
        time.sleep(delay_seconds)
        if not path.exists():
            return False
        current_size = path.stat().st_size
        if current_size != previous_size:
            previous_size = current_size
            continue
    return True
