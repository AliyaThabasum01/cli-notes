from notes import add_note, view_notes

print("=" * 40)
print("📝 CLI Notes")
print("=" * 40)

while True:
    print("\n1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        text = input("Enter your note: ").strip()

        if text:
            add_note(text)
            print("✅ Note saved.")
        else:
            print("❌ Note cannot be empty.")

    elif choice == "2":
        notes = view_notes()

        if not notes:
            print("📭 No notes yet.")
        else:
            print("\nYour Notes:")
            for index, note in enumerate(notes, 1):
                print(f"{index}. {note}")

    elif choice == "3":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")
