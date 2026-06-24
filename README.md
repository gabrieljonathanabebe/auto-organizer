# Auto Organizer

A small Python automation project that watches local folders and organizes files automatically.

## Current feature

- Watches the macOS Desktop
- Detects new screenshots
- Creates monthly folders under `Desktop/screenshots`
- Moves screenshots into folders like `2026-06`
- Uses a dry-run mode for safer testing
- Logs detected, skipped, and moved files

## Tech stack

- Python
- watchdog
- pathlib
- logging

## Run locally

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install watchdog
```

Start the watcher:

```python
python main.py
```

Stop it with `Ctrl + C`

## Project Structure

```text
main.py              # Starts the observer
config.py            # Stores configuration
handlers.py          # Reacts to watchdog events
file_utils.py        # File-related helper functions
screenshot_utils.py  # Screenshot-specific helper functions
```
