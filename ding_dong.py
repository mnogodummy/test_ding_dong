#!/usr/bin/env python3
"""Simple Ding Dong generator."""

from datetime import datetime


def ding_dong(times: int = 4) -> None:
    for i in range(1, times + 1):
        print(f"{i}. ding 🔔")
        print(f"{i}. dong 🛎️")


if __name__ == "__main__":
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"Ding Dong started at {now}")
    ding_dong(5)
    print("Done. Have a nice chime!")
