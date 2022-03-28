import argparse
import sys
from pydantic import BaseSettings
import requests
from http.client import HTTPConnection
import json

PUSHOVER_BASE_URL = "https://api.pushover.net/1/messages.json"


class Settings(BaseSettings):
    pushover_token: str
    pushover_user: str

    class Config:
        env_file = ".env"


def parse_args():
    parser = argparse.ArgumentParser(description="DESCRIPTION")
    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable verbose logging",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-m", "--message", help="notification", action="store", required=True
    )
    parser.add_argument("-t", "--title", help="notification title", action="store")
    parser.add_argument(
        "-p",
        "--priority",
        help="notification priority",
        action="store",
        choices=[-2, -1, 0, 1, 2],
        default=0,
    )

    return parser.parse_args()


def notify(**kwargs):
    r = requests.post(PUSHOVER_BASE_URL, **kwargs)
    r_json = r.json()

    if r.status_code == 200:
        sys.exit(0)
    if r.status_code == 400:
        print(json.dumps(r_json, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    settings = Settings()
    args = parse_args()
    if args.verbose:
        HTTPConnection.debuglevel = 1

    # Build payload
    payload = {"token": settings.pushover_token, "user": settings.pushover_user}

    payload["message"] = args.message
    payload["title"] = args.title if args.title is not None else None
    payload["priority"] = args.priority if args.priority is not None else None

    # send notification
    notify(data=payload, headers={})
