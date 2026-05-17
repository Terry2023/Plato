# src/pick_soul.py — FIXED PATH + EXTENSION
import yaml
import random
import os

# FIXED: Direct path to your personalities.yml
VAULT_PATH = r"D:\Projects\collective_cognition\vault\personalities.yml"

print(f"Loading: {VAULT_PATH}")
with open(VAULT_PATH) as f:
    data = yaml.safe_load(f)
    personalities = data["personalities"]

print(f"Loaded {len(personalities)} personalities!")

# Roll the dice
soul = random.choice(personalities)

print("=" * 50)
print("🎲 SOUL ROLLED 🎲")
print("=" * 50)
print(f"Name:  {soul['name']}")
print(f"ID:    {soul['id']}")
print(f"Origin:{soul['origin']}")
print("\n📋 SYSTEM PROMPT (COPY TO OLLAMA):")
print("-" * 40)
print(soul["system_prompt"])
print("-" * 40)

# Save favorite
save = input("\n💾 Save to favorites.txt? (y/n): ")
if save.lower() == 'y':
    with open("favorites.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\n--- {soul['name']} ({soul['id']}) ---\n")
        f.write(soul["system_prompt"] + "\n")
    print("✅ Saved to favorites.txt")