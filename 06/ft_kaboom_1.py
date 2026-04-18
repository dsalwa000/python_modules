import alchemy.grimoire.dark_spellbook as dark_spellbook


print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
result = dark_spellbook(
    "Spell recorded: Fantasy (Earth, wind and fire - VALID)",
    "fire"
)

print(result)
