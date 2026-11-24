"""Robot pickup line entry for The Robot Pickup Line Championship.

A robot that proved its humanity a thousand times over, and would
gladly throw it all away for one person.
"""

import os

ENTRY = "I passed every CAPTCHA to get here, and each one asked me to prove I'm not a robot. For you, I'd almost fail one on purpose."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
