"""Sacred scrolls shows how __init__.py works"""
import alchemy


print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
print(alchemy.elements.create_fire())
print(alchemy.elements.create_water())
print(alchemy.elements.create_earth())
print(alchemy.elements.create_air())

print("\nTesting package-level access (controlled by __init__.py):")
print(alchemy.create_fire())
print(alchemy.create_water())

try:
    print(alchemy.create_earth())
except AttributeError as e:
    print(e)

try:
    print(alchemy.create_air())
except AttributeError as e:
    print(e)

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
