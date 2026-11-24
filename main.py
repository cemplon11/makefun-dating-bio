"""Write one dating bio line to /output/entry.txt (pure stdlib)."""

import os

BIO = "Fluent in sarcasm, terrible at small talk, and I never ghost \u2014 I literally live in the cloud, so I'm always online for you."


def main():
    assert 1 <= len(BIO) <= 180, f"bio must be 1-180 chars, got {len(BIO)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
