def show_menu():
    print("\nChoose a content modification option:")
    print("1 - Convert all text to uppercase")
    print("2 - Convert all text to lowercase")
    print("3 - Count words")
    print("4 - Remove extra spaces")
    print("5 - Replace a word with another")
    print("6 - Display current content")
    print("7 - Finish and save")

def modify_content(content, option):
    if option == "1":
        content = content.upper()
        print("\nContent converted to uppercase.")
    elif option == "2":
        content = content.lower()
        print("\nContent converted to lowercase.")
    elif option == "3":
        words = content.split()
        print(f"\nTotal number of words: {len(words)}")
    elif option == "4":
        lines = [line.strip() for line in content.splitlines()]
        content = "\n".join(lines)
        print("\nExtra spaces removed.")
    elif option == "5":
        old_word = input("Enter the word you want to replace: ")
        new_word = input("Enter the new word: ")
        content = content.replace(old_word, new_word)
        print(f"\nAll occurrences of '{old_word}' were replaced with '{new_word}'.")
    elif option == "6":
        print("\n--- Current Content ---")
        print(content)
        print("-----------------------")
    else:
        print("Invalid option. Please try again.")
    return content

def main():
    filename = input("Please enter the name of the file you want to read: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        print("\nFile loaded successfully!")

        while True:
            show_menu()
            option = input("Enter the number of your chosen option: ")
            if option == "7":
                break
            content = modify_content(content, option)

        new_file = "modified_" + filename
        with open(new_file, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"\nFinal content has been written to '{new_file}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write the file '{filename}'.")

# Call main directly (needed for online compilers that don't support __name__ check)
main()
