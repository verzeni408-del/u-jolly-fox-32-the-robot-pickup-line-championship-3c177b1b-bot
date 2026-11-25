import os

LINE = "I cleared 4,812 errors from my log last night. The last one reads 'met her'. The fix is wiping my memory of you, so I marked it won't fix and now I crash every time you smile."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)

if __name__ == "__main__":
    main()
