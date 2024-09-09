def main():
    try:
        # File Creation and Writing
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("2nd line with a number: 123\n")
            file.write("Third line - hello world!\n")

        # File Reading and Display
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:\n", content)

        # File Appending
        with open("my_file.txt", "a") as file:
            file.write("Appended line 1\n")
            file.write("Appended line 2: 456\n")
            file.write("Appended line 3 - goodbye!\n")

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except PermissionError:
        print("Permission error. You may not have permission to write to the file.")
    finally:
        print("File operations completed.")

if __name__ == "__main__":
    main()