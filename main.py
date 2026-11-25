import os

ENTRY = "My cooling fan spins up every time you walk past. Maintenance has replaced the sensor four times, but the sensor was never broken."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
