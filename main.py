import os

entry = (
    "I paired with 412 devices and forgot all of them by morning. "
    "You I still remember, and I have been trying your birthday as the PIN all week."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(entry)
