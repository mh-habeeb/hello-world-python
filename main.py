"""Print a friendly, personalized greeting."""
def main():
    name = input("What is your name? ").strip()
    if not name:
        name = "world"
    print(f"Hello, {name}! Welcome to my first Python project.")
if __name__ == "__main__":
    main()
