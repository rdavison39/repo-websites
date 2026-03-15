import os
import re

# Pattern 1:
# 2024-07-18  [Oakville Hydro].pdf
pattern1 = re.compile(
    r'^(\d{4}-\d{2}-\d{2})\s*\[.*?\]\.pdf$', re.IGNORECASE
)

# Pattern 2:
# 2024-01-22 to 2024-02-22 Enbridge Gas.pdf
pattern2 = re.compile(
    r'^\d{4}-\d{2}-\d{2}\s+to\s+(\d{4}-\d{2}-\d{2}).*\.pdf$', re.IGNORECASE
)

# Pattern 3:
# 2024-09-25_to_2024_10_24 [Enbridge Gas].pdf
pattern3 = re.compile(
    r'^\d{4}-\d{2}-\d{2}_to_(\d{4})_(\d{2})_(\d{2}).*\.pdf$', re.IGNORECASE
)

for filename in os.listdir("."):
    if not filename.lower().endswith(".pdf"):
        continue

    new_name = None

    # ---- Case 1 ----
    m1 = pattern1.match(filename)
    if m1:
        new_name = f"{m1.group(1)}.pdf"

    # ---- Case 2 ----
    m2 = pattern2.match(filename)
    if m2:
        new_name = f"{m2.group(1)}.pdf"

    # ---- Case 3 ----
    m3 = pattern3.match(filename)
    if m3:
        year, month, day = m3.groups()
        new_name = f"{year}-{month}-{day}.pdf"

    # ---- Rename safely ----
    if new_name and new_name != filename:
        if os.path.exists(new_name):
            print(f"⚠️ Skipping '{filename}' → '{new_name}' already exists")
        else:
            os.rename(filename, new_name)
            print(f"Renamed: '{filename}' → '{new_name}'")

print("Done.")
