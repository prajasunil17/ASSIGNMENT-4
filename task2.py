def write_file():
    filename = "output.txt"

    try:
        string = input("Enter text to write to the file: ")
        with open(filename, "w") as file:
            file.write(string + "\n")

        print(f"\nData successfully written to  {filename}")

        addData = input("Enter additional text to append: ")
        with open(filename, "a") as file:
            file.write(addData + "\n")

        print(f"\nData successfully appended")


        print(f"\nFinal content of {filename}:")
        with open(filename, "r") as file:
            for i, line in enumerate(file, start=1):
                print(f"Line {i}: {line.strip()}")

    except Exception as e:
        print(f"Error occurred: {e}")


# Run the program
write_file()
