import plistlib
import sys
from pathlib import Path

LAUNCH_AGENT_LABEL = "io.github.gabrieljonathanabebe.auto-organizer"


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    python_path = Path(sys.executable).absolute()
    launch_agents_dir = Path.home() / "Library" / "LaunchAgents"
    launch_agent_path = launch_agents_dir / f"{LAUNCH_AGENT_LABEL}.plist"
    logs_dir = Path.home() / "Library" / "Logs" / "AutoOrganizer"
    logs_dir.mkdir(parents=True, exist_ok=True)

    launch_agent_config: dict[str, object] = {
        "Label": LAUNCH_AGENT_LABEL,
        "ProgramArguments": [
            str(python_path),
            str(project_dir / "main.py"),
        ],
        "RunAtLoad": True,
        "StandardOutPath": str(logs_dir / "auto-organizer.stdout.log"),
        "StandardErrorPath": str(logs_dir / "auto-organizer.stderr.log"),
        "WorkingDirectory": str(project_dir),
    }

    launch_agents_dir.mkdir(parents=True, exist_ok=True)
    with launch_agent_path.open("wb") as plist_file:
        plistlib.dump(launch_agent_config, plist_file)

    print(f"LaunchAgent installed: {launch_agent_path}")


if __name__ == "__main__":
    main()
