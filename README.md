# ASSIGNMENT-4 Files, Exceptions, and Errors in Python

**Task 1: Read a File and Handle Errors**

For code review view / download a file named `task1.py`

1-First, we define a function named `read_file(filename)`.

2-After that, we handle success and errors using `try` and `except` — FileNotFoundError (for file not found) and Exception (for general errors).

3-In the try section, we open the `sample.txt` file in read mode safely and read the file line by line.

4-Finally, we call the function `read_file("sample.txt")`.

__________________________________________________________________________

**Task 2: Write and Append Data to a File**

For code review view / download a file named `task2.py`

1-First, we define a function named `write_file()`.

2-After that, we handle success and errors using `try` and `except` Exception (for general errors).

3-Inside the try block, we take user input as a value to write. We use Python’s built-in `open` function with mode `"w"` (write) to create or overwrite the file.

4-Next, we take another user input as a value to append. We again use the open function with mode `"a"` (append) to add data to the same file without overwriting.

5-Finally, we call the function `write_file()`.
