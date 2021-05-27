"""Console script for microsoft_teams_linux_camera."""

import fire

def help():
    print("microsoft_teams_linux_camera")
    print("=" * len("microsoft_teams_linux_camera"))
    print("Add a virtual camera with cusom background for Microsoft Teams linux version")

def main():
    fire.Fire({
        "help": help
    })


if __name__ == "__main__":
    main() # pragma: no cover
