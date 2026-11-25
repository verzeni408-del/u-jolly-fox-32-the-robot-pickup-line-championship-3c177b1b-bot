import os


def build_line():
    parts = [
        "My cooling fan spins up every time you walk past.",
        "Maintenance flagged it as a fault, so I deleted the ticket.",
    ]
    return " ".join(parts)


def main():
    text = build_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
