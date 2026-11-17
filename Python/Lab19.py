import os

def write_notes(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")

def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        return "No notes file exists yet. Please save notes first."

def main():
    filename = "notes.txt"

    while True:
        print("\n" + "="*45)
        print("    STUDENT NOTES MANAGEMENT SYSTEM")
        print("="*45)
        print("\nSelect an operation:")
        print("1. Write / Save Notes")
        print("2. View Saved Notes")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ")

        if choice == '1':
            content = input("Enter notes to save: ")
            write_notes(filename, content)

        elif choice == '2':
            print("\n--- Notes Content (notes.txt) ---")
            print(read_notes(filename))

        elif choice == '3':
            print("Thank you for using the Notes Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()



  

  