# python-100-projects-challenge

Welcome to my 100 python Projects repository! 🎉 I’ve embarked on this journey to master core python, sharpen my problem-solving skills, and boost my confidence as a programmer.

📖 About This Challenge
Over 15-16 weeks, I’ll complete 100 hands-on projects—from very simple and basic exercises to challenging problems

🎯 Motivation
Deepen my JavaScript knowledge beyond theory ✅
Gain confidence by writing code every day ✅
Build a diverse project portfolio for resumes & interviews ✅
Develop daily coding habit ✅

# Here is the roadmap that i followed

## Week 1: Python Basics – Syntax, Variables, and Data Types

**Topics:** Introduction to Python and running scripts, basic syntax (indentation, code structure), using the REPL (interactive interpreter) vs. scripts, variables and assignment, primitive data types (integers, floats, strings, booleans), basic arithmetic and string operations, using the built-in `print()` function for output and `input()` for simple user input. Ensure you can write and run a simple program that reads input and produces output.

**Resources:**

- **Text:** “The Python Tutorial” (official docs) sections on Introduction and Using the Interpreter – covers syntax and basic types.
- **Video:** _“Python for Absolute Beginners”_ by freeCodeCamp (first hour) – demonstrates setting up Python and basic syntax.
- **Book:** _Automate the Boring Stuff with Python_ (Al Sweigart) Chapters 0-1 – introduction and using Python interactively.

**Projects:** Practicing small programs early will cement the basics. Complete the following simple projects this week:

- **Project 1: Hello World Greeter** – _Description:_ A program that asks the user for their name and then greets them. _Features:_ Uses `input()` to get the user's name into a variable, and `print()` to display a greeting message. _Sample Input/Output:_

  - **Input:** `Alice`
  - **Output:** `Hello, Alice! Welcome to Python.`

- **Project 2: Simple Addition Calculator** – _Description:_ A program that reads two numbers from the user and prints their sum. _Features:_ Demonstrates reading numeric input (using `int()` or `float()` conversion on `input()` result) and performing arithmetic. It should handle basic addition of two values. _Sample Input/Output:_

  - **Input:** `5` and `17`
  - **Output:** `5 + 17 = 22`

- **Project 3: Area of a Circle** – _Description:_ Compute the area of a circle given its radius. _Features:_ Uses a formula with arithmetic expressions. You can use `radius = float(input())` to get a number and the formula `area = 3.14 * radius ** 2`. (For more accuracy, import the `math` module and use `math.pi` – an early exposure to using a module.) _Sample Input/Output:_

  - **Input:** `radius = 3`
  - **Output:** `Area = 28.274333882308138` (if using `math.pi`) or `Area = 28.26` (if using 3.14 as π)

- **Project 4: Temperature Converter** – _Description:_ Convert temperatures from Celsius to Fahrenheit. _Features:_ Uses the conversion formula `F = C * 9/5 + 32`. Reads a Celsius value from user and prints the equivalent Fahrenheit value. _Sample Input/Output:_

  - **Input:** `100` (Celsius)
  - **Output:** `100°C = 212°F`

> **Week 1 Goal:** By the end of this week, you should be comfortable writing and running simple Python scripts, using variables, and performing basic input/output. Ensure you type and run each example yourself – hands-on practice is crucial. You will have written four small programs. 🎉

## Week 2: Control Flow – Conditional Statements

**Topics:** Boolean logic and comparison operators (`==`, `!=`, `<`, `>` etc.), `if` statements, `else` and `elif` branches for decision-making. Learn how to use conditionals to execute code only when certain conditions are true. Cover common use cases like checking numeric ranges or string equality. Also introduce the concept of code _blocks_ (indented code under an `if` or else). Begin with simple one-condition checks, then multiple conditions and nested conditionals. By mid-week, you should be able to solve basic decision problems (e.g., find the maximum of two numbers using an if-else).

**Resources:**

- **Text:** W3Schools “Python If...Else” tutorial – a quick reference for syntax and examples of conditionals.
- **Video:** _“Python Programming Tutorial – If **name** == '**main**' and More”_ by Corey Schafer (YouTube) – covers Python conditionals clearly.
- **Cheat-sheet:** Truth tables for logical operators and operator precedence (for reference when combining conditions).

**Projects:** Apply conditional logic to these scenarios:

- **Project 5: Even or Odd Checker** – _Description:_ Determine if an integer is even or odd. _Features:_ Uses the modulus operator `%` to test divisibility by 2 inside an if/else. _Sample Input/Output:_

  - **Input:** `7`
  - **Output:** `7 is odd.`

- **Project 6: Grade to Letter Converter** – _Description:_ Convert a numeric exam score into a letter grade (e.g., 90+ = A, 80-89 = B, etc.). _Features:_ Uses a chain of `if...elif...else` to check ranges. _Sample Input/Output:_

  - **Input:** `85`
  - **Output:** `Score 85 => Grade B`

- **Project 7: Leap Year Checker** – _Description:_ Check if a given year is a leap year. _Features:_ A year is leap if divisible by 4 but not by 100, except if also divisible by 400. This requires multiple conditions combined with logical operators (`and`, `or`). _Sample Input/Output:_

  - **Input:** `2024`
  - **Output:** `2024 is a leap year.`

- **Project 8: Login Authentication Simulation** – _Description:_ Simulate a simple login by checking a username/password. _Features:_ Hard-code a correct username and password (e.g., `"admin"` / `"1234"`). Prompt the user for credentials and use an if/else to compare input against the correct values. Print “Login successful” if they match, or “Invalid credentials” otherwise. _Sample Input/Output:_

  - **Input:** `admin` and `1234`
  - **Output:** `Login successful.` (If input was wrong: `Invalid credentials.`)

> **Week 2 Goal:** You can now write programs that make decisions based on conditions. You understand how to compare values and combine conditions. By writing programs like the grade converter and login checker, you’ve practiced translating real-world logic into Python `if` statements. Continue to test your programs with different inputs to see if all branches work correctly (e.g., test the leap year checker with typical cases and edge cases). You’ve added another four programs to your portfolio.

## Week 3: Loops – Repeating Actions

**Topics:** Iteration with loops. Introduce the `while` loop for repeating a block of code while a condition remains true, and the `for` loop for iterating over a sequence of items. Understand the difference: use `while` for open-ended repetition (or when you need to loop until a condition changes) and `for` for looping a predetermined number of times or over a collection. Learn to use the `range()` function to generate sequences of numbers for `for` loops. Cover loop control statements: `break` (to exit a loop early) and `continue` (to skip to the next iteration). By the end of this week, you should be able to use loops to solve problems like summing numbers, generating patterns, etc..

**Resources:**

- **Text:** Real Python’s _“Python ‘for’ Loops (Definite Iteration)”_ – explains looping over ranges and collections with examples.
- **Video:** _“Python While Loops and For Loops”_ by Programming with Mosh – a clear demonstration of loop basics.
- **Practice:** Try small exercises like printing numbers 1 to 10 using both a for-loop and a while-loop to get comfortable.

**Projects:** Use loops to automate repetitive tasks and implement simple games:

- **Project 9: Rock, Paper, Scissors** – _Description:_ A two-player Rock-Paper-Scissors game against the computer. _Features:_ Uses `random.choice()` to have the computer select "rock", "paper", or "scissors". The user enters their choice, then use a series of if/elif conditions to determine the winner (rock beats scissors, scissors beats paper, paper beats rock, or tie if same). Optionally, wrap the game in a loop to allow playing multiple rounds until the user quits. _Sample Input/Output:_

  - **Input:** `rock` (user) vs **Computer:** `scissors` (random)
  - **Output:** `You chose rock, computer chose scissors – you win!`

- **Project 10: Number Guessing Game** – _Description:_ The program picks a random secret number, and the user tries to guess it. _Features:_ Use `random.randint(1, 100)` to generate a secret number. Then use a `while` loop to repeatedly prompt the user for a guess. For each guess, reply with “Too high”, “Too low”, or “Correct!” accordingly, and loop until the guess is correct. Use a counter to track number of attempts. _Sample Input/Output:_ (multiple rounds of input)

  - **Output:** `I'm thinking of a number between 1 and 100. Can you guess it?`
  - **Input:** `50` → **Output:** `Too high, try again.`
  - **Input:** `30` → **Output:** `Too low, try again.`
  - **Input:** `42` → **Output:** `Correct! You guessed it in 3 tries.`

- **Project 11: Multiplication Table Generator** – _Description:_ Ask the user for a number, and then print its multiplication table up to 10 (or up to a specified range). _Features:_ Uses a `for` loop with `range(1, 11)` to iterate through multipliers. For each iteration, calculate `number * i` and print the result in a formatted way. _Sample Input/Output:_

  - **Input:** `5`
  - **Output:**

    ```
    5 x 1 = 5
    5 x 2 = 10
    ...
    5 x 10 = 50
    ```

- **Project 12: FizzBuzz Challenge** – _Description:_ A classic programming task. Print numbers 1 to N (let N=50 for example). For multiples of 3, print "Fizz" instead of the number, for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz". _Features:_ Uses a `for` loop over range(1, N+1) with if/elif conditions inside. This exercise tests loop and condition integration. _Sample Output (for 1–15):_
  `1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...`

- **Project 13: Factorial Calculation (Iterative)** – _Description:_ Compute the factorial of a given number _n_ (n!) using a loop. _Features:_ Utilize a `for` loop from 1 to n, or a `while` loop decrementing n, to multiply the numbers. Demonstrates accumulative computation. _Sample Input/Output:_

  - **Input:** `5`
  - **Output:** `120` (because 5! = 120)

- **Project 14: Star Pattern Printer** – _Description:_ Produce a simple text-based pattern using nested loops. For example, print a right-angle triangle of `*` characters of a given size. _Features:_ Uses an outer loop for each line and an inner loop to print the required number of stars on that line. This practices nested loop logic. _Sample Input/Output:_ (for n=5)

  ```
  *
  **
  ***
  ****
  *****
  ```

> **Week 3 Goal:** You’ve learned to use loops to perform repetitive tasks. This dramatically expands what your programs can do. You built a number guessing game (combining loops with conditions) – a significant milestone in interactive programming. By creating the multiplication table and FizzBuzz programs, you practiced `for` loops, and the star pattern and factorial tasks gave you experience with nested loops and accumulators. At this point, you have \~14 small projects in your repository. You should feel more confident reading problem descriptions and translating them into code with loops and conditionals.

## Week 4: Strings, Text Processing, and File I/O

**Topics:** Dive deeper into **strings** – an essential Python data type. Learn about string indexing (accessing individual characters), slicing (extracting substrings), and useful string methods (`len()`, `lower()`, `upper()`, `find()`, `replace()`, etc.). Cover techniques for iterating over strings and building or concatenating strings. Next, introduce **file handling**: using `open()` to read from and write to text files, reading entire files vs. reading line-by-line, and the importance of closing files (or using `with` context manager for files). This is also a good point to introduce **exception handling basics** in the context of file I/O (e.g., handling file-not-found errors gracefully – though a fuller treatment of exceptions comes later). Additionally, introduce **regular expressions** (regex) for pattern matching in text – a powerful tool for searching and validating strings. Start with simple patterns (like checking if a string matches an email format). Regular expressions enable succinct solutions to complex string problems.

**Resources:**

- **Text:** Python’s Official Tutorial – section on “Strings” and “Reading and Writing Files” (covers file I/O with examples of using `with` context).
- **Video:** _“Working with Text in Python (Strings and Files)”_ by Corey Schafer – explains string methods and file reading/writing in a clear way.
- **Regex Reference:** The W3Schools regex cheat-sheet or the official [`re` module documentation](https://docs.python.org/3/library/re.html) for basic syntax (character classes, `+`, `*`, etc.).

**Projects:** These exercises will strengthen your skills in processing text and using files:

- **Project 15: Palindrome Checker** – _Description:_ Determine if a given string is a palindrome (reads the same forward and backward, e.g., "madam"). _Features:_ Ignore case and non-alphanumeric characters for the check (e.g., "Able was I ere I saw Elba" should count as palindrome). This can be done by cleaning the string (using `.lower()` and filtering out punctuation), then checking if the cleaned string equals its reverse (`[::-1]` slicing can reverse a string). _Sample Input/Output:_

  - **Input:** `Madam`
  - **Output:** `Palindrome? Yes` (since "Madam" ignoring case is the same backwards)

- **Project 16: Word Count in a Sentence** – _Description:_ Ask the user for a sentence and output the number of words in it. _Features:_ Use `str.split()` to split the input string on whitespace into words (which returns a list of words), then use `len()` on that list. This is a simple use of a string method and demonstrates basic parsing. _Sample Input/Output:_

  - **Input:** `Hello world, this is Python.`
  - **Output:** `Number of words: 5`

- **Project 17: Caesar Cipher Encryption** – _Description:_ Implement a basic Caesar cipher, which shifts each letter in a message by a fixed number of positions in the alphabet. _Features:_ Let the user input a message and a shift (e.g., 3 means `A->D, B->E, ...`). Encrypt the message by shifting letters while preserving case. This requires working with character codes (use `ord()` and `chr()` for shifting, or define strings of alphabet to index). It’s a good exercise in looping through string characters and constructing a new string. _Sample Input/Output:_

  - **Input:** message: `Attack at Dawn`, shift: `3`
  - **Output:** `Dwwdfn dw Gdzq` (each letter shifted by 3; note that spaces remain unchanged)

- **Project 18: Email Address Validator** – _Description:_ Check if an input string is a valid email format. _Features:_ Use the `re` (regex) module. A simple validation can check for the pattern `[^@]+@[^@]+\.[^@]+` (meaning “at least one character that is not @, then an @, then at least one not-@, then a dot, then at least one character”). The project should output whether the given string matches an email regex pattern. _Sample Input/Output:_

  - **Input:** `user@example.com`
  - **Output:** `Valid email format? Yes`
  - _(Test with invalid input like `"user@@example"` to ensure it says "No".)_

- **Project 19: Phone Number Extractor** – _Description:_ Search a text for phone numbers of a specific format and extract them. For example, find all occurrences of phone numbers in the format `XXX-XXX-XXXX`. _Features:_ This can be done with regular expressions using the `re.findall()` function. Use a pattern like `\d{3}-\d{3}-\d{4}` to find sequences of digits separated by hyphens. If the text is provided (you can hardcode a multiline string or read from a file), output the list of phone numbers found. _Sample Input/Output:_

  - **Input:** `"Contact us at 123-456-7890 or 987-654-3210."`
  - **Output:** `Found phone numbers: ['123-456-7890', '987-654-3210']`

- **Project 20: File Line Counter** – _Description:_ Read a text file and count how many lines, words, and characters it contains (similar to the Unix `wc` command). _Features:_ Use Python’s file I/O to open a file in read mode. Loop through each line: increment a line count, use `.split()` to count words, and use `len(line)` for character count (you may want to sum up lengths or count characters including newlines appropriately). Finally, print the counts. _Sample Input/Output:_ (Suppose `sample.txt` has 10 lines and 100 words total)

  - **Output:** `Lines: 10, Words: 100, Characters: 560`

- **Project 21: Keyword Search in File** – _Description:_ Implement a simple search utility that asks the user for a filename and a search term, then prints out all lines in the file that contain the term. _Features:_ Demonstrates reading a file line-by-line and using the `in` operator or `.find()` to check substring presence. It should handle case sensitivity (could offer an option to ignore case by comparing lowercased versions). _Sample Input/Output:_

  - **Input:** file: `notes.txt`, term: `Python`
  - **Output:** _(prints lines from notes.txt that include "Python")_
  - **Example line:** `I am learning Python programming.`

- **Project 22: File Copy Utility** – _Description:_ Copy the contents of one text file to another. _Features:_ Open the source file for reading and a target file for writing. Read the source (you can do it in one go with `.read()` or line by line) and write the content into the destination file. Ensure the new file is an exact copy of the original. This introduces writing to files and reinforces file I/O. _Sample Output:_ After running the program on a source file, verify that the destination file has identical content (you can open it or even have the program confirm by comparing sizes).

> **Week 4 Goal:** This week you tackled text – both in memory (strings) and in files. By building the palindrome and Caesar cipher programs, you practiced manipulating strings extensively (reversing, shifting characters). The email validator and phone extractor introduced you to **regular expressions**, a powerful tool for pattern matching in strings (you saw how a complex text search can be done in one line with a good pattern). You also performed file reading/writing – an essential skill for real-world scripts that deal with data. You’ve likely written short scripts to read from or write to files, which mimics basic data processing tasks. Now you have \~22 projects in total. Take a moment to organize your code files; perhaps create folders for each week’s projects. At this point, you’re starting to build the discipline of reading external data, processing it, and producing output – which is the core of many programs.

## Week 5: Data Structures Part I – Lists and Tuples

**Topics:** Now that you have a solid handle on control flow and strings, it’s time to learn about Python’s built-in **data structures** for collecting multiple items. This week focuses on **lists** and **tuples** (sequence types). Learn how to create lists, access and modify elements by index, iterate over lists with loops, and use common list methods (`append`, `remove`, `sort`, etc.). Understand list slicing (similar to string slicing) and how lists can contain heterogeneous types or even other lists (nesting). Contrast with **tuples** – which are immutable sequences. Learn when to use a tuple (for fixed collections of items that shouldn’t change, such as coordinates or database records). By the end of this week, you should be comfortable choosing list vs. tuple and performing fundamental operations on each.

**Resources:**

- **Text:** Real Python’s _“Python Lists”_ tutorial – covers list creation, indexing, slicing, and methods with examples.
- **Video:** _“Python Lists and Tuples”_ by Telusko (YouTube) – a beginner-friendly walkthrough of list operations and tuple usage.
- **Exercises:** Use an interactive shell to experiment with list operations (create a list and practice `list.append(x)`, `list.pop()`, etc., and try to modify a tuple to see the error it produces, to reinforce the immutability concept).

**Projects:** These tasks will involve manipulating lists and tuples:

- **Project 23: List Min/Max Finder** – _Description:_ Given a list of numbers (you can prompt the user to input a series of numbers separated by spaces, then split into a list), determine the minimum and maximum values. _Features:_ Demonstrate traversing a list manually with a loop to find min and max (though Python has built-in `min()` and `max()`, try implementing it with logic to appreciate how it works). _Sample Input/Output:_

  - **Input:** `Numbers: 5 3 8 2 9`
  - **Output:** `Min = 2, Max = 9`

- **Project 24: List Average Calculator** – _Description:_ Compute the average of numbers in a list. _Features:_ Sum the elements (you can use `sum(list)` or do it via loop) and divide by `len(list)`. Take care to handle empty list (maybe ask for at least one number). _Sample Input/Output:_

  - **Input:** `10 20 30 40`
  - **Output:** `Average = 25.0`

- **Project 25: List Reverser** – _Description:_ Reverse the elements of a list without using the built-in `list.reverse()` method (do it manually to practice indexing and swapping). _Features:_ You can loop over the first half of the list and swap each element with its mirror position at the end. Or build a new reversed list by iterating from the end to the start. _Sample Input/Output:_

  - **Input:** `Original list: [1, 2, 3, 4, 5]`
  - **Output:** `Reversed list: [5, 4, 3, 2, 1]`

- **Project 26: Even-Odd Separator** – _Description:_ Take a list of integers and separate it into two lists: one of even numbers and one of odd numbers. _Features:_ Iterate through the original list, use `% 2` to test even/odd, and append each number to the appropriate new list. _Sample Input/Output:_

  - **Input:** `Numbers: [10, 3, 5, 8, 2, 7]`
  - **Output:** `Evens = [10, 8, 2], Odds = [3, 5, 7]`

- **Project 27: Matrix Addition** – _Description:_ Represent two 3x3 matrices as lists of lists, and compute their sum. _Features:_ Use nested loops: an outer loop to iterate over rows (index 0 to 2) and an inner loop for columns, adding corresponding elements. Store the result in a new matrix (list of lists). _Sample Input/Output:_

  - **Input:**
    Matrix A = `[[1,2,3],[4,5,6],[7,8,9]]`
    Matrix B = `[[9,8,7],[6,5,4],[3,2,1]]`
  - **Output:** `[[10,10,10],[10,10,10],[10,10,10]]` (the elementwise sum)

> **Week 5 Goal:** You have now added **lists** and **tuples** to your toolkit. By manipulating lists in these projects (finding min/max, separating evens and odds, etc.), you practiced core operations like iteration, indexing, and appending. The matrix addition project gave you a taste of working with nested lists (2D arrays) – a precursor to doing more complex data handling. You should also recognize when a tuple might be useful – for example, as a pair of coordinates or a fixed set of options that shouldn’t change. At this stage, you’ve accumulated around 27 projects. Your programs are becoming more data-centric, operating on collections of values rather than single values, which is a key step toward writing real-world software (which often needs to manage lists of records, etc.).

## Week 6: Data Structures Part II – Sets and Dictionaries

**Topics:** Continue exploring Python collections with **sets** and **dictionaries**. A **set** is an unordered collection of unique elements. Learn how to create sets, add/remove elements, and use set operations like union, intersection, and difference – useful for tasks like filtering unique items. Then focus on **dictionaries** (dicts), one of Python’s most powerful data types, which store key–value pairs (also known as maps or hash tables in other languages). Understand how to create dictionaries, add/update values, retrieve and delete entries by key, and iterate over keys and values. Common patterns like counting occurrences (frequency counting) are introduced here, as dicts are ideal for that. By the end of the week, you should know how to decide which data structure (list, tuple, set, dict) fits a given problem, and be fluent in the basic operations of each.

**Resources:**

- **Text:** _“Python Sets and Dictionaries”_ in the official Python tutorial – explains syntax (`{}` for dict, `set()` constructor, etc.) and basic operations.
- **Video:** _“Python Dictionaries for Beginners”_ by CS Dojo – covers use cases of dictionaries (such as word count) in an easy-to-follow manner.
- **External:** Practice using the interactive interpreter: create a dict and try retrieving a key that isn’t present to see the error, use `dict.get(key, default)` method for safe lookup, and experiment with set operations using small examples (like `{1,2,3} | {3,4,5}` for union).

**Projects:** Apply sets and dicts to practical tasks:

- **Project 28: Duplicate Remover** – _Description:_ Remove duplicate elements from a list of numbers while preserving the original order. _Features:_ Use a set to track seen numbers. Iterate through the list, and build a new list containing only the first occurrence of each number. (Alternatively, convert to a `set` directly to drop duplicates, but that loses order; the goal here is to practice using a set for membership checking while maintaining order manually). _Sample Input/Output:_

  - **Input:** `[5, 1, 5, 2, 1, 3]`
  - **Output:** `[5, 1, 2, 3]` (duplicates removed)

- **Project 29: Unique Letters Finder** – _Description:_ Input a string and output the set of unique characters it contains. _Features:_ Use a set to collect characters (e.g., `set(your_string)`). Perhaps ignore spaces or consider only alphabetic characters depending on requirements. _Sample Input/Output:_

  - **Input:** `"hello world"`
  - **Output:** `{'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}` (If excluding space, then output would be `{'h','e','l','o','w','r','d'}`)

- **Project 30: Word Frequency Counter** – _Description:_ Count how often each word appears in a given sentence or paragraph. _Features:_ Use a dictionary where keys are words and values are counts. Normalize the input by lowercasing and perhaps stripping punctuation. Split the text into words and loop through them, using `dict.get(word, 0)` to increment counts. Finally, print each word with its frequency. _Sample Input/Output:_

  - **Input:** `"to be or not to be"`
  - **Output:** `{'to': 2, 'be': 2, 'or': 1, 'not': 1}`

- **Project 31: Contact Book (Dictionary)** – _Description:_ Create a simple phone book application that uses a dictionary to store names (keys) and phone numbers (values). _Features:_ The program can allow the user to **add** a new contact (name->number), **look up** an existing contact by name, and **delete** a contact. (Implementing a simple text-menu for these actions is good practice). Use a loop to repeatedly ask for an operation until the user quits. _Sample Interaction:_

  - **Input:** Add "Alice : 12345", Add "Bob : 67890", Lookup "Alice", Delete "Bob", Quit.
  - **Output:** On lookup of Alice, prints "Alice's number is 12345"; on delete of Bob, confirms removal. The internal dictionary updates accordingly.

- **Project 32: Letter Frequency (Dict)** – _Description:_ Similar to word frequency, count the frequency of each letter in a string. _Features:_ Use a dictionary with letters as keys. You can reuse logic from word frequency, but this time iterate over each character (skip spaces or non-letters). This shows how dicts can be used for counting any kind of discrete item. _Sample Input/Output:_

  - **Input:** `"BANANA"`
  - **Output:** `{'B': 1, 'A': 3, 'N': 2}`

- **Project 33: Number-to-Words Converter** – _Description:_ Convert an integer (e.g., 142) to its word form ("one hundred forty-two"). _Features:_ Use a dictionary mapping single-digit numbers to words (`0:"zero", 1:"one", ... 9:"nine"`). For multi-digit numbers, break the number into hundreds, tens, ones and use the dict for lookup. Handle tens specially (10-19 have unique words, and for others use multiples of ten like 20->"twenty"). This is a bit more complex logic, but using dict for the basic mapping simplifies the problem. _Sample Input/Output:_

  - **Input:** `142`
  - **Output:** `"one hundred forty-two"`

- **Project 34: Hangman Game (with improved logic)** – _Description:_ Implement the Hangman word-guessing game. This is a larger project combining strings, loops, and possibly sets for tracking guesses. _Features:_ Choose a secret word (perhaps from a predefined list). The user guesses letters one at a time. Use a set to store letters the user has guessed so far. After each guess, display the word with unguessed letters as underscores. Give a limited number of wrong guesses (chances). Use a loop for each guess and update the state accordingly. _Sample Interaction:_

  ```
  Secret word: PYTHON
  _ _ _ _ _ _   (6 letters)
  Guess a letter: O
  Progress: _ _ _ _ O _
  Guess a letter: P
  Progress: P _ _ _ O _
  ...
  ```

  - **Output:** Win scenario: `“Congratulations! You guessed the word PYTHON.”` or loss scenario after running out of chances: `“Game over! The word was PYTHON.”`

  _(This project uses many concepts: string manipulation, set for guessed letters, loop with break conditions, etc. By completing it, you solidify a lot of prior learning. Hangman is commonly recommended for beginners and a great test of your progress.)_

> **Week 6 Goal:** You have now mastered all of Python’s core built-in data structures: lists, tuples, sets, and dictionaries. You’ve practiced using sets to filter unique values and using dictionaries to map keys to values (and performed counting with dicts, which is a frequent pattern). The contact book project gave you a taste of designing a simple stateful application (the dictionary maintained state across user commands). By building Hangman, you combined data structures (a set of guessed letters, a string for the word, maybe a list for the display state) with control flow to create a fully interactive game – an achievement that demonstrates how far you’ve come in just 6 weeks. At roughly 34 projects, many of which are non-trivial now, you’re developing not only Python syntax familiarity but also problem-solving skills and program design thinking.

## Week 7: Functions and Modular Programming

**Topics:** This week introduces the concept of **functions** – reusable pieces of code that perform a specific task. You’ll learn how to define functions using `def` (with parameters and return values) and how to call them. Emphasize why functions are useful for structuring code (avoiding repetition, improving clarity). Cover the idea of variable **scope** (local variables inside functions vs. global variables) and how arguments are passed (by object reference in Python). Practice writing simple functions for tasks you’ve already done manually, turning those solutions into reusable functions. Additionally, touch on the concept of organizing code into **modules**: how to import functions from other Python files or standard libraries. This is a stepping stone to more modular design and eventually using third-party libraries. By end of week, you should comfortably write and use functions, and understand how to split a program into multiple functions.

**Resources:**

- **Text:** The Python Tutorial chapter on _“Defining Functions”_ – introduces function syntax, `return` statement, and scoping rules.
- **Video:** _“Functions in Python”_ by Programming with Mosh – provides a clear explanation of creating and using functions, with examples.
- **Quick reference:** A list of common built-in functions (like `len`, `range`, etc.) – though you’ve used many by now, it’s useful to recognize which are built-in vs. user-defined.

**Projects:** Refactor some previous code into functions and write new function-based solutions:

- **Project 35: Multi-Function Calculator** – _Description:_ Improve the calculator from Week 1 by structuring it with functions. _Features:_ Write separate functions for each operation: `add(x,y)`, `subtract(x,y)`, `multiply(x,y)`, `divide(x,y)`. Then have a main section of code that asks the user which operation to perform and on what numbers, calls the appropriate function, and displays the result. This demonstrates passing arguments and returning values. _Sample Interaction:_

  ```
  Select operation: 1)Add 2)Subtract 3)Multiply 4)Divide
  Enter choice: 1
  Enter two numbers: 5 7
  Result: 12
  ```

  Internally, the program uses `result = add(5,7)` for the above.

- **Project 36: Math Quiz Generator** – _Description:_ Create a simple math quiz program that generates a random addition or subtraction problem and checks the user’s answer. _Features:_ Use a function `generate_question()` that returns a tuple like (`question_text`, `correct_answer`). For example, it might randomly decide 2 + 3, and return (`"2 + 3 = ?"`, `5`). In main code, present the question, get user’s answer, and check against the returned correct*answer. You could generate a series of questions in a loop. \_Sample Interaction:*

  ```
  Question: 7 - 4 = ?
  Your answer: 3
  Correct!
  Question: 5 + 10 = ?
  Your answer: 14
  Wrong. The answer was 15.
  ```

  (At the end, maybe show score out of total questions.)

- **Project 37: Prime Number Checker (Function)** – _Description:_ Write a function `is_prime(n)` that returns True if `n` is a prime number, False otherwise. _Features:_ The function should check divisibility from 2 up to √n (for efficiency). Then use this function in a program that prints all primes up to a given number or that simply tests a single number input by the user. This practices writing a function with a clear purpose and using it as a building block. _Sample Input/Output:_

  - **Function call:** `is_prime(17)` returns `True`; `is_prime(18)` returns `False`.
  - In a script context, if user inputs 50, program might output: `Primes up to 50: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47`.

- **Project 38: Prime Numbers Upto N (Using is_prime)** – _Description:_ Now use the `is_prime(n)` function to generate a list of prime numbers up to N. _Features:_ Loop from 2 to N, and for each number call `is_prime`. If true, append to a list of primes. Print the list or the count of primes. This demonstrates reusing your own function to solve a larger problem. _Sample Input/Output:_

  - **Input:** `N = 30`
  - **Output:** `Primes <= 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`

- **Project 39: Factorial (Recursive)** – _Description:_ Implement factorial using **recursion**. _Features:_ Define a function `factorial(n)` that calls itself: `factorial(n) = n * factorial(n-1)` with a base case `factorial(0)=1`. This project illustrates a different approach to a problem you solved iteratively before. Include error handling for negative inputs (perhaps by raising a `ValueError`). _Sample Input/Output:_

  - **Function calls:** `factorial(5)` returns `120`; `factorial(0)` returns `1`.

- **Project 40: Fibonacci (Recursive)** – _Description:_ Implement a function `fib(n)` that returns the nth Fibonacci number (with `fib(0)=0, fib(1)=1`). _Features:_ Use the recursive definition: `fib(n) = fib(n-1) + fib(n-2)`. Be mindful that naive recursion is exponential – this is more of a conceptual exercise. (Optionally, discuss that this is not efficient for large n and perhaps mention the idea of memoization, but that can be left as a thought exercise or for later when learning about optimization.) _Sample Input/Output:_

  - **Function calls:** `fib(0) -> 0`, `fib(1) -> 1`, `fib(5) -> 5`, `fib(6) -> 8`.
  - If integrated into a program, you could print a sequence: e.g., for n=6, output `0, 1, 1, 2, 3, 5, 8`.

> **Week 7 Goal:** You’ve transitioned from writing everything in one block to organizing code into **functions**. This is a significant step toward writing cleaner, more maintainable code. You should now understand how to define a function, pass arguments, and use return values. The calculator and quiz projects showed how functions make it easy to handle repetitive tasks or logically separate tasks (e.g., generating questions vs. checking answers). You also explored **recursion** with factorial and Fibonacci – a different way of thinking about problem solving. While recursion isn’t always the go-to approach in Python, it’s important to understand it (and you saw how mathematical definitions can translate to code). With about 40 projects under your belt, you might start noticing that certain patterns repeat – which is exactly why functions and later modules are so useful. Next, we’ll expand on modularity by using and creating modules.

## Week 8: Modules, Packages, and the Standard Library

**Topics:** Learn how to organize code into multiple files and use Python’s **module system**. This includes writing your own modules and importing them, as well as using Python’s vast **standard library** and third-party packages. Key points:

- How to use `import` statements (importing whole module vs. specific attributes with `from module import name`).
- Explore the Python Standard Library: familiarize with a few common modules such as `math` (for mathematical functions), `random` (for random number generation, which you’ve used), `datetime` (for date and time manipulation), `os` and `sys` (for operating system interactions), `json` (for JSON serialization), etc. Not in depth for all, but know they exist and how to read documentation to use them.
- Understand the concept of installing third-party packages via `pip`. Perhaps choose one popular simple library and demonstrate its use.
- Encourage using virtual environments (just a brief mention) to manage packages (optional at this stage, but good to be aware of).
- By end of week, you should be comfortable reading library documentation and incorporating external code, which is crucial for professional Python development (knowing _“Python has a rich standard library”_ and being able to leverage it).

**Resources:**

- **Text:** Official docs chapter on _“Modules”_ – explains how to write and import modules, and discusses the Python Package Index (PyPI) for third-party packages.
- **Video:** _“Python Modules and Packages”_ by Corey Schafer – covers creating modules and using pip to install packages.
- **Website:** Python Standard Library reference (skim through the library list to see what’s available; practice looking up a module and reading about its functions).

**Projects:** This week’s projects will make use of modules and libraries:

- **Project 41: Random Password Generator** – _Description:_ Generate a random secure password of a given length. _Features:_ Use the `random` module (specifically `random.choice`) to pick characters. Define the allowed characters (could use strings from Python’s `string` module, e.g., `string.ascii_letters`, `string.digits`, `string.punctuation`). This project reinforces using an imported module. _Sample Input/Output:_

  - **Input:** desired length = 8
  - **Output:** e.g. `Generated password: G5%kQ!8z` (each run should produce a different password)

- **Project 42: Weather Info Fetcher (API call)** – _Description:_ Fetch current weather for a given city by calling a web API. _Features:_ Use the `requests` library (a popular third-party HTTP client – you’ll need to `pip install requests` which teaches package installation). Have the user input a city name, use the Requests module to call an API like OpenWeatherMap (they provide a free endpoint) or a simpler one that doesn’t require API keys for testing (there are some open APIs for weather or use a dummy one). Parse the JSON response using Python’s `json` module (which can load JSON text into dictionaries). Then display the weather info. _Sample Input/Output:_

  - **Input:** `City = London`
  - **Output:** `Weather in London: 18°C, Clear sky`
    _(The actual output depends on API’s response format. This project introduces reading JSON and using an external HTTP service.)_

- **Project 43: Custom Utilities Module** – _Description:_ Create your own module of utility functions and use it in a script. _Features:_ For instance, make a file `utilities.py` that contains functions like `capitalize_words(text)` (that capitalizes the first letter of each word), `count_vowels(text)`, etc. Then write another script that imports this module and uses those functions on user input. This teaches how to structure code across files and import your own code. _Sample:_

  - In `utilities.py`: define `def count_vowels(s): ...`
  - In main script:

    ```python
    from utilities import count_vowels
    text = input("Enter text: ")
    print("Vowel count:", count_vowels(text))
    ```

  - **Output:** If input was "Hello", outputs `Vowel count: 2`.

- **Project 44: Birthday Calculator** – _Description:_ Ask the user for their date of birth (e.g., YYYY-MM-DD) and calculate how many days until their next birthday. _Features:_ Use the `datetime` module from the standard library. Parse the input string into a `datetime.date` object. Get today’s date (`datetime.date.today()`). Construct the date for the next birthday (if the birthday this year has passed, use next year). Then subtract to get a `timedelta`. Output the days remaining. _Sample Input/Output:_

  - **Input:** `Birthday (YYYY-MM-DD): 1990-08-15`
  - **Output:** `Days until next birthday: 45` (for example, if today is June 30, 2025)

- **Project 45: File Organizer Script** – _Description:_ Organize files in a directory into subfolders based on file type/extension. _Features:_ Use the `os` module to list files in a given directory. For each file, detect its extension (e.g., `.txt`, `.jpg`). Create folders for each extension if not exist (using `os.makedirs` or `os.mkdir`), and move files into the corresponding folders (you can use `os.rename` to move, or `shutil.move` from the `shutil` module). **Caution:** This is a powerful script; test in a safe directory to avoid messing up important files. _Sample Execution:_

  - Suppose your script is pointed at a folder with `report.docx, photo.jpg, data.csv`. After running, it creates subfolders `docx, jpg, csv` and moves each file into the respective folder.
  - **Output:** Print something like "Moved report.docx to docx/" for each file moved.

- **Project 46: JSON Data Storage** – _Description:_ Persist data using JSON. For example, extend the Contact Book (Project 31) to save the contacts to a file. _Features:_ Use the `json` module to serialize the contacts dictionary to a JSON file (with `json.dump`) when the program exits, and load it (`json.load`) when it starts, so data persists between runs. Alternatively, create a standalone script that converts one data format to JSON: e.g., read a CSV file and output a JSON file (you’ll use the `csv` module to read CSV). This project gives practice in using a standard library for a common data format. _Sample (Contact Book persistence):_

  - Run program, add contacts, exit. It writes `contacts.json`.
  - On next run, it loads `contacts.json` and the previously added contacts are available.
  - **Output:** (No direct output; the result is that data is saved and loaded successfully, which you can verify by reopening the program and listing contacts.)

- **Project 47: CSV Data Analyzer** – _Description:_ Use the `csv` module to read a CSV file (for example, a file `scores.csv` containing two columns: Name and Score). Calculate something from it, such as the average score, or find the highest scorer. _Features:_ Practice with the `csv.reader` or `csv.DictReader` to parse lines. Then use your data structure skills to compute the result. _Sample Input (scores.csv):_

  ```
  Name,Score
  Alice,85
  Bob,92
  Charlie,78
  ```

  - **Output:** `Average score = 85, Highest = Bob (92)`.

> **Week 8 Goal:** You have taken a big step toward being a _Pythonic_ programmer by using modules and libraries. Now you don’t have to reinvent the wheel for every task – you can rely on the extensive Python standard library and third-party packages. This week’s projects were more tool-oriented: you created a password generator, a file organizer, and made API calls. You also organized your own code into modules. At this point, reading documentation to learn how to use a new module should feel more routine. For example, you likely referred to `datetime` or `os` docs for specific functions – this skill of **learning from documentation** will be invaluable going forward. You’ve crossed \~47 projects. From here, the focus will shift to more advanced Python concepts and larger projects that tie many pieces together.

## Week 9: Error Handling and Debugging

**Topics:** Writing robust code is an important part of being professional. This week, focus on **exception handling** in Python using `try`, `except`, `else`, and `finally` blocks. Learn how to gracefully handle errors such as invalid inputs, file not found errors, division by zero, etc., instead of letting the program crash. Understand Python’s exception hierarchy (e.g., `ValueError`, `IOError`, etc.) and how to catch specific exceptions. Also, learn how to **raise** exceptions deliberately when invalid conditions occur (for example, in your `factorial` function if a negative number is given). In addition, cover basic **debugging techniques**: using print statements to trace execution, using debugging tools or an IDE debugger (if available), and writing **logs** using the `logging` module for larger programs. By the end of the week, you should be able to anticipate and handle common error conditions in your programs, making them user-friendly and less prone to crashing unexpectedly.

**Resources:**

- **Text:** Python Tutorial section on _“Errors and Exceptions”_ – introduces catching exceptions and raising them.
- **Video:** _“Exception Handling in Python”_ by Corey Schafer – covers try/except, else, finally, and how to raise exceptions.
- **Logging Reference:** Official `logging` module documentation (for basic usage, you can refer to a shorter guide – it’s a powerful module but start with simple logging to file/console).

**Projects:** Improve previous programs with error handling and debug new ones:

- **Project 48: Robust Calculator** – _Description:_ Take the multi-function calculator from Project 35 and add error handling. _Features:_ Use try/except to handle cases like division by zero (catch `ZeroDivisionError` and print an error message instead of crashing) and invalid numeric inputs (catch `ValueError` when converting input to float/int). Ensure the program keeps running or gracefully asks for input again if an error occurs. _Sample Interaction:_

  ```
  Enter operation (1-4): 4
  Enter two numbers: 10 0
  Error: Cannot divide by zero. Try again.
  ```

  (Then it would loop back to prompt for inputs again.)

- **Project 49: Safe File Reader** – _Description:_ A program that asks for a filename and attempts to open and read it. _Features:_ Use `try` to attempt `open(filename)`. If it raises a `FileNotFoundError`, catch it and print a friendly message (“File not found, please check the name”). If successful, read and display perhaps the first line or the size of the file. Use a `finally` block to ensure the file is closed if it was opened. _Sample Interaction:_

  ```
  Enter filename: data.txt
  Error: File 'data.txt' not found.
  ```

  (If the file exists, perhaps it prints the first line.)

- **Project 50: Resilient Number Guessing Game** – _Description:_ Improve the number guessing game (Project 10) by handling non-integer inputs. _Features:_ If the user enters something that isn’t a number, catch the `ValueError` from `int()` conversion and prompt them to enter a valid number without crashing or counting it as a try. Also, perhaps implement a limit on number of attempts and raise a custom exception if exceeded. _Sample Interaction:_

  ```
  Guess the number between 1 and 100: abc
  "That's not a number, try again."
  ```

  (Game continues running.)

- **Project 51: Logging in a Game** – _Description:_ Add logging to the Hangman game (Project 34) or Guessing game to record events for debugging. _Features:_ Use the `logging` module to log each guess and whether it was correct or not. Write logs to a file (e.g., `game.log`). This is not something the user sees, but as a developer, you can open the log to troubleshoot. Practice setting `logging.basicConfig(filename='game.log', level=logging.INFO)`. _Sample log file excerpt:_

  ```
  INFO:root:Secret word: PYTHON
  INFO:root:User guessed: O (Correct)
  INFO:root:User guessed: A (Incorrect, 5 attempts left)
  ...
  ```

  (No direct user output beyond the game’s normal behavior, but the log file is created/updated.)

- **Project 52: Custom Exception Demo** – _Description:_ Write a function (or small module) that demonstrates raising and catching a custom exception. _Features:_ Define your own exception class, e.g., `class NegativeAgeError(Exception): pass`. Then write a function `compute_insurance_premium(age)` that raises `NegativeAgeError` if age < 0, or returns some dummy premium value otherwise. In the main program, call this function inside try/except and handle the custom exception with a message. _Sample Input/Output:_

  - **Input:** age = -5
  - **Output:** `Error: Age cannot be negative.` (caught from the custom exception)

> **Week 9 Goal:** Your programs are now getting **robust**. Instead of crashing on bad input, they inform the user and gracefully recover. This is a hallmark of mature programming. You’ve learned to anticipate errors (like file not found, divide by zero, invalid input) and handle them. You also learned how to use Python’s `logging` to output debug information – a technique that becomes vital in larger applications where you can’t easily print everything or step through a debugger. With around 53 projects now, you likely revisited some earlier ones to add try/except; this is a good point to reflect on how far those programs have evolved from their first versions. When you write new code now, you’ll naturally think about possible failure cases and how to handle them. This defensive programming mindset will serve you well as you proceed to bigger projects and more complex concepts.

## Week 10: Object-Oriented Programming (OOP) Basics

**Topics:** Begin exploring **object-oriented programming** in Python. Understand what classes and objects are: a class is a blueprint for objects (combining data and behavior), and an object is an instance of a class. Key ideas:

- Defining classes with the `class` keyword.
- The `__init__` constructor for initializing new objects.
- Instance attributes vs. class attributes.
- Defining methods (functions inside a class) and the use of `self`.
- Creating and using objects (calling methods, accessing attributes).
  Explain encapsulation principle (though Python doesn’t enforce access restrictions, the concept of bundling data/methods is still applicable). Illustrate with a simple real-world analogy (e.g., a class `Dog` with attributes like name and methods like bark). The goal is to be able to design simple classes and use them to model parts of a program. By the end of this week, you should be comfortable with basic class syntax and instantiation of objects.

**Resources:**

- **Text:** _“Classes”_ chapter in the official Python tutorial – introduces class syntax, `__init__`, and a simple example of a class.
- **Video:** _“Python OOP Tutorial 1: Classes and Instances”_ by Corey Schafer – a very accessible introduction to classes with examples.
- **Practice idea:** Pick objects from real life (like “Bank Account”, “Book”, “Car”) and try to sketch what attributes and methods they might have, to get into an OOP mindset.

**Projects:** Define and use classes in these projects:

- **Project 53: Rectangle Class** – _Description:_ Create a class `Rectangle` with attributes width and height, and methods to calculate area and perimeter. _Features:_ Include an `__init__` to set width and height. Add methods `area(self)` and `perimeter(self)`. Then write a small script that creates a couple of `Rectangle` objects with different sizes and prints out their area and perimeter. _Sample Output:_

  ```
  Rect1:  width=4, height=5 -> area=20, perimeter=18
  Rect2:  width=3, height=3 -> area=9, perimeter=12
  ```

- **Project 54: BankAccount Class** – _Description:_ Model a simple bank account with methods to deposit, withdraw, and check balance. _Features:_ Class `BankAccount` with an attribute `balance` (initialized to 0 or given). Implement methods `deposit(self, amount)` (adds to balance), `withdraw(self, amount)` (subtracts if sufficient funds, otherwise maybe print an error or raise exception), and `get_balance(self)` (returns the balance). Test the class by creating an account, performing some deposits and withdrawals, and printing the results. _Sample Interaction:_

  ```python
  acct = BankAccount()
  acct.deposit(100)
  acct.withdraw(30)
  print("Balance:", acct.get_balance())  # Output: Balance: 70
  acct.withdraw(100)  # Output: "Insufficient funds" (if implemented as such)
  ```

- **Project 55: Person Class** – _Description:_ Define a `Person` class with attributes for name and age, and a method to display a greeting. _Features:_ `__init__` should take name and age. Method `introduce(self)` could print `"Hello, I'm {name} and I'm {age} years old."`. Then create a few instances of Person to demonstrate. This is straightforward but reinforces the concept of methods and `self`. _Sample Output:_

  ```
  Hello, I'm Alice and I'm 30 years old.
  Hello, I'm Bob and I'm 25 years old.
  ```

- **Project 56: Student Class with Average** – _Description:_ Expand on Person: create a `Student` class that inherits from `Person` (or you can do without inheritance at first) and adds a list of grades. _Features:_ Store the grades (maybe as a list attribute). Provide a method `get_average(self)` that returns the average of the grades. Also, perhaps override the introduction to include something about being a student. _Sample Usage:_

  ```python
  student = Student("Charlie", 20, [88, 92, 79])
  print(student.introduce())  # "Hello, I'm Charlie and I'm 20 years old."
  print("My average grade is", student.get_average())  # "My average grade is 86.33"
  ```

- **Project 57: Library Catalog (Classes with composition)** – _Description:_ Simulate a simple library system with two classes: `Book` and `Library`. _Features:_ `Book` class with attributes like title, author, and maybe an ID. `Library` class with a list of books as its attribute. Implement methods in `Library` to `add_book(book)`, `remove_book(title)` (or by ID), and `find_book(title)` which returns a Book or info if found. This demonstrates objects containing other objects (a library has many books). _Sample Usage:_

  ```python
  lib = Library()
  book1 = Book("1984", "George Orwell")
  book2 = Book("To Kill a Mockingbird", "Harper Lee")
  lib.add_book(book1)
  lib.add_book(book2)
  found = lib.find_book("1984")
  if found:
      print(f"Found book: {found.title} by {found.author}")
  ```

  - **Output:** `Found book: 1984 by George Orwell` (if the find was successful).

> **Week 10 Goal:** You have now laid the groundwork in **OOP**. By implementing classes like Rectangle and BankAccount, you saw how data and functions can be bundled together in Python. You’ve used `self` to access instance attributes and learned to instantiate objects. The Library example (if you did it) shows how objects can work together (composition). At this point, you have about 58 projects; importantly, some of these are not just one-off scripts but definitions of classes that could be reused in larger programs. As you continue, you’ll build on OOP by learning about inheritance and more advanced features, which help in structuring larger applications. But even at this basic level, OOP allows you to conceptualize problems in terms of real-world entities, which is a powerful way to design software.

## Week 11: OOP Advanced – Inheritance and Polymorphism

**Topics:** Expand your OOP knowledge with **inheritance**, **polymorphism**, and other advanced class features:

- **Inheritance:** how a class can derive from another class, inheriting its attributes and methods. Understand using `class SubClass(SuperClass):` syntax. Learn how to call the superclass `__init__` in the subclass (if needed) via `super().__init__()`.
- **Method overriding:** the subclass can provide a different implementation of a method that the base class has, enabling polymorphism.
- **Polymorphism:** the concept that a subclass instance can be treated as an instance of the superclass – for example, a `Student` object might be used anywhere a `Person` is expected.
- Introduce **special methods** (dunder methods) like `__str__` to provide a human-readable string representation of objects, and `__eq__` to compare objects, etc., as needed in projects.
- Mention **class methods** and **static methods** (using `@classmethod` and `@staticmethod` decorators) for cases where methods are not about instance data – though keep it light unless needed for a project.
  By end of this week, you should be able to design class hierarchies (e.g., a base class and one or two subclasses) and understand how to extend or modify behavior in subclasses.

**Resources:**

- **Text:** _“Inheritance”_ section in Python tutorial or a beginner OOP book – explains subclassing and `super()`.
- **Video:** _“Python OOP Tutorial 2: Inheritance and Subclasses”_ by Corey Schafer – continues the earlier tutorial to cover subclassing.
- **Reference:** Python’s data model documentation for special methods (skim to know that methods like `__str__`, `__len__`, etc., exist to make objects work nicely with built-in functions).

**Projects:** Use inheritance and advanced OOP concepts:

- **Project 58: Bank Account Inheritance** – _Description:_ Extend the `BankAccount` class to simulate different types of accounts. _Features:_ Create subclasses like `SavingsAccount` (that might have an interest rate and a method to apply interest) and `CheckingAccount` (that might have a limit on withdrawals or an overdraft fee). Override the `withdraw` method in `CheckingAccount` to implement an overdraft limit, for example. This shows inheritance (both subclasses inherit deposit from base, but override withdraw differently). _Sample Usage:_

  ```python
  savings = SavingsAccount(initial_balance=1000, interest_rate=0.02)
  savings.apply_interest()
  print(savings.get_balance())  # 1020.0 after applying 2% interest

  checking = CheckingAccount(initial_balance=500, overdraft_limit=100)
  checking.withdraw(600)
  print(checking.get_balance())  # -100 if overdraft allowed
  checking.withdraw(1)  # should disallow as it'd exceed overdraft
  ```

  - **Output:** (for the above) `1020.0` for savings balance; for checking, perhaps prints an error on the second withdraw attempt like “Exceeded overdraft limit”.

- **Project 59: Animal Polymorphism** – _Description:_ Create a base class `Animal` with a method `speak()` that is meant to be overridden. Then create subclasses `Dog`, `Cat`, etc., each overriding `speak()` with an appropriate sound. _Features:_ You can also give each subclass some specific attribute if needed (not required). Then demonstrate polymorphism by writing a function that takes an `Animal` and calls `speak()` without knowing the specific subclass – each animal will speak differently. _Sample Code:_

  ```python
  class Animal:
      def speak(self):
          print("...")

  class Dog(Animal):
      def speak(self):
          print("Woof!")

  class Cat(Animal):
      def speak(self):
          print("Meow!")

  animals = [Dog(), Cat(), Dog()]
  for animal in animals:
      animal.speak()
  ```

  - **Output:**

    ```
    Woof!
    Meow!
    Woof!
    ```

  (This shows one interface `speak()` with many implementations.)

- **Project 60: Complex Number Class (Operator Overloading)** – _Description:_ Create a class `Complex` to represent complex numbers and overload the `+` and `-` operators. _Features:_ Implement `__add__` and `__sub__` special methods to allow using `+` and `-` on your Complex objects. Also implement `__str__` for nice string output. Each Complex has `real` and `imag` attributes. _Sample Usage:_

  ```python
  a = Complex(2, 3)  # 2 + 3i
  b = Complex(1, -4)  # 1 - 4i
  c = a + b
  d = a - b
  print(c)  # should print "3 - 1i" (since (2+1) + (3-4)i)
  print(d)  # should print "1 + 7i"
  ```

  - **Output:** `3 - 1i` and `1 + 7i` for the above example (depending on how you format the string).

- **Project 61: Temperature Class with Properties** – _Description:_ Create a `Temperature` class that stores temperature in Celsius internally, but provides a property to get or set the value in Fahrenheit. _Features:_ Use the `@property` decorator to make an attribute-like interface. For example, `temp.fahrenheit` property that when read, computes the Fahrenheit from the stored Celsius, and when set, converts and stores the corresponding Celsius. This demonstrates encapsulation and Pythonic properties. _Sample Usage:_

  ```python
  temp = Temperature(0)  # 0°C
  print(temp.fahrenheit)  # 32.0°F
  temp.fahrenheit = 212
  print(temp.celsius)  # 100.0°C
  ```

  - **Output:** `32.0` then `100.0` for the above.

- **Project 62: Shape Abstract Class** – _Description:_ Use the `abc` module to create an abstract base class `Shape` with an abstract method `area()`. Then implement concrete subclasses like `Circle` and `Rectangle` (again, but in the inheritance context) that provide area calculations. _Features:_ Mark `Shape` with `ABC` from `abc` module and use the `@abstractmethod` decorator for `area`. The subclasses must override `area`. This project introduces interface-like design. _Sample Usage:_

  ```python
  shapes = [Circle(radius=3), Rectangle(width=4, height=5)]
  for sh in shapes:
      print(sh.area())
  ```

  - **Output:**

    ```
    28.274333882308138  (area of circle)
    20                  (area of rectangle)
    ```

  (The exact number for circle depends on using math.pi.)

- **Project 63: Library System Enhancements** – _Description:_ If you did the Library/Book in Week 10, extend it with inheritance. E.g., `LibraryItem` as a base class and subclasses `Book`, `Magazine`, `DVD` that maybe have different attributes. Or a `User` class and subclass `Member` and `Librarian` with different permissions (just conceptual). _Features:_ Focus on how you might structure a larger system with OOP. This could remain a thought experiment with minimal code, or implement a small part like different item types. This solidifies thinking in terms of class hierarchies.

> **Week 11 Goal:** You’ve now seen how OOP scales: using **inheritance** to avoid duplication and model hierarchies of concepts. The BankAccount inheritance example showed how general and specific account behaviors can be separated, and the Animal example demonstrated polymorphism – how the same method name can do different things depending on the object’s class. You also touched on advanced topics like operator overloading and properties, which make your classes integrate well with Python’s syntax and conventions (e.g., making custom objects printable or behave like built-ins). By now, with \~63 projects, you have experience in both functional and object-oriented styles of programming. You can choose the approach best suited to a problem. Importantly, you’re preparing for designing more complex applications where OOP can help manage complexity. Next, we’ll explore some advanced Python capabilities (like iterators, generators, and decorators) that will further deepen your mastery of the language itself.

## Week 12: Advanced Python Features – Iterators, Generators, and Comprehensions

**Topics:** This week focuses on advanced constructs that make Python powerful and concise:

- **Iterators and Iterable protocol:** understand that when you loop over an object (like `for x in some_object`), Python uses the object’s iterator. Learn about the `__iter__()` and `__next__()` methods. Create a simple iterator class manually (to appreciate the concept).
- **Generators:** a simpler way to create iterators using the `yield` keyword. Explain generator functions with `yield` (which produce values on the fly and maintain state between yields). Also mention generator expressions (like list comprehensions but with parentheses).
- **List (and dict, set) Comprehensions:** a Pythonic way to construct collections in one line. You likely encountered comprehensions in earlier weeks informally, but now delve into their syntax for filtering and transforming lists succinctly.
- Possibly touch on **lambda functions**, **map/filter/reduce** here if not covered earlier (some functional programming aspects were left for now).
  By the end of the week, these constructs should not seem mysterious. You should be able to write a generator to produce an infinite sequence (like Fibonacci or prime numbers) and use comprehensions for clean data transformations.

**Resources:**

- **Text:** Real Python’s _“Iterators and Generators”_ article – a step-by-step on creating and using generators and iterators.
- **Video:** _“Python Generators Explained”_ by Computerphile (for a conceptual understanding of why generators are useful).
- **Cheat-sheet:** Syntax examples for list/dict comprehensions (e.g., `[x*x for x in range(10) if x%2==0]` etc.).

**Projects:** Practice these advanced features:

- **Project 64: Celsius to Fahrenheit with Map** – _Description:_ Use a lambda and `map()` to convert a list of temperatures in Celsius to Fahrenheit in one line. _Features:_ This is more of a one-liner exercise rather than a full program. Given `temps_c = [0, 20, 37, 100]`, do `temps_f = list(map(lambda C: C*9/5 + 32, temps_c))` and print `temps_f`. _Sample Output:_
  `Temps in F = [32.0, 68.0, 98.6, 212.0]`

- **Project 65: Prime Filter** – _Description:_ Use `filter()` with your `is_prime` function (from Project 37) to filter prime numbers from a list. _Features:_ This demonstrates higher-order functions. For example, take a list of numbers 1–30 and filter primes. _Sample Output:_
  `Primes in 1..30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`

- **Project 66: List Comprehension Practice** – _Description:_ Solve a couple of small tasks with comprehensions. _Features:_ For example, create a list of squares of even numbers 0–9 in one line. Or given a list of words, create a new list of their lengths for words that start with a vowel. This is to get comfortable with comprehension syntax. _Sample Output:_

  - Squares: `[0, 4, 16, 36, 64]` for even numbers up to 8.
  - Word lengths (if words = \["apple", "banana", "orange", "kiwi"]): output for those starting with vowel -> `[5, 6]` (for "apple" and "orange").

- **Project 67: Fibonacci Generator** – _Description:_ Write a generator function `gen_fibonacci()` that yields Fibonacci numbers indefinitely (or up to a limit). _Features:_ Use an infinite while loop or for loop and `yield`. Consumers of this generator can use `next()` to get successive values, or use it in a for-loop (with `itertools.islice` perhaps to take the first N). _Sample Usage:_

  ```python
  import itertools
  fib_gen = gen_fibonacci()
  first10 = list(itertools.islice(fib_gen, 10))
  print(first10)
  ```

  - **Output:** `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

- **Project 68: Custom Iterator Class** – _Description:_ Create a class that implements the iterator protocol. For instance, a simple iterator that generates powers of two up to a certain number. _Features:_ Define `__iter__()` returning self and `__next__()` that multiplies by 2 each time until a limit. Alternatively, make an iterator for your `Library` class to iterate over books easily (so that you can do `for book in library:` by implementing `Library.__iter__`). _Sample Implementation:_

  ```python
  class PowTwo:
      def __init__(self, max_exp):
          self.max_exp = max_exp
          self.current = 0
      def __iter__(self):
          return self
      def __next__(self):
          if self.current <= self.max_exp:
              result = 2 ** self.current
              self.current += 1
              return result
          else:
              raise StopIteration
  ```

  - **Usage:** `for value in PowTwo(3): print(value)`
  - **Output:**

    ```
    1
    2
    4
    8
    ```

  (This shows 2^0, 2^1, 2^2, 2^3.)

- **Project 69: Reduce Function Usage** – _Description:_ Demonstrate use of `functools.reduce` by computing, say, the product of a list of numbers. _Features:_ Use `from functools import reduce`. Then `reduce(lambda x,y: x*y, [1,2,3,4,5])` to get factorial of 5, for example. This is just to see another functional tool. _Sample Output:_
  `Product = 120`

> **Week 12 Goal:** You have now unlocked some of Python’s most powerful language features:

- **Comprehensions** allow writing clear, concise transformations (you’ve likely seen how a loop that would take 4-5 lines can become a one-liner list comprehension – but remember to balance conciseness with readability).
- **Generators** give you a way to handle potentially large (even infinite) sequences in a memory-efficient manner. You built a Fibonacci generator which could, in principle, generate numbers until you stop asking for more. Understanding `yield` is a step into a more advanced Pythonic thinking.
- **Iterators** and the protocol demystified how loops work under the hood. You even created a custom iterator.
- **Map/filter/reduce and lambdas** introduced a bit of the functional programming flavor in Python, which can sometimes simplify code (though list comprehensions are often more Pythonic than map/filter).
  At roughly 69 projects now, you are adept at a wide range of Python techniques. The next step is to apply this knowledge to more comprehensive projects and to learn best practices for larger codebases (including testing and project structure). The final phase of this roadmap will emphasize integrating everything you’ve learned and building portfolio-worthy projects.

## Week 13: Decorators and Context Managers

**Topics:** Two advanced constructs remain to round out core Python mastery: **decorators** and **context managers**.

- **Decorators:** functions (or classes) that modify the behavior of other functions. Learn the `@decorator` syntax sugar. A simple example is a decorator that logs function calls, or that checks types, or that caches results (memoization). Understand that a decorator is just a callable that returns a new callable. Practice writing a couple of simple decorators.
- **Context Managers:** the protocol behind the `with` statement. Explain `__enter__` and `__exit__` methods. Common use is for resource management (like opening and closing files). Try creating a context manager class or using the `contextlib` utilities (like `contextlib.contextmanager` decorator for writing context managers easily with a generator).
  These are more advanced, but by now you have the background to appreciate them. By end of week, you should be comfortable using decorators (you’ve used `@property`, which is a built-in decorator, already) and even writing basic ones. Similarly, you should understand how `with` works and be able to create a custom context manager for a specific scenario.

**Resources:**

- **Text:** Real Python’s _“Primer on Python Decorators”_ – an in-depth but clear explanation of how decorators work and common examples.
- **Video:** _“Python Decorators in 5 Minutes”_ by PyCode (YouTube) – a short introduction to the concept with examples.
- **Context Manager:** Documentation on `contextlib.contextmanager` for a simple way to make context managers with a generator.

**Projects:** Employ decorators and context managers in practice:

- **Project 70: Timing Decorator** – _Description:_ Write a decorator `@timed` that measures the execution time of the decorated function. _Features:_ Use `time.time()` before and after function call, compute the difference, and print it. Apply this decorator to a couple of functions (e.g., a function that sums up the first N numbers) to see how long they take. _Sample Output:_

  ```
  Function sum_n executed in 0.0001 seconds
  Result: 5000050000
  ```

  (for summing first 100k numbers, as an example)

- **Project 71: Logging Decorator** – _Description:_ Create a decorator `@logged` that logs the function name and arguments every time the function is called (perhaps to a file or just to console). _Features:_ This is similar to the earlier logging project, but now abstracted as a reusable decorator. Apply it to a few functions to see that it consistently logs calls. _Sample Output:_ (when calling a decorated function `add(2,3)`)
  `LOG: Called add with args=(2, 3), kwargs={}`
  `5` (result of the function)

- **Project 72: File Context Manager** – _Description:_ Implement a context manager class `FileOpener` that opens a file on enter and closes it on exit, so that you can use it with `with FileOpener(filename) as f:`. _Features:_ Define `__enter__` to open the file and return the file object, and `__exit__` to close it (handling any exceptions if needed). Test it by reading from a file inside a with-block. _Sample Usage:_

  ```python
  with FileOpener("sample.txt") as f:
      for line in f:
          print(line.strip())
  ```

  (After the block, file is automatically closed.)

- **Project 73: Exception Suppressor Context** – _Description:_ Write a context manager (using `contextlib.contextmanager` for brevity) that suppresses certain exceptions. For example, `suppress(ValueError)` context such that any ValueError inside is caught and not propagated (similar to `contextlib.suppress` function). _Features:_ Use a try/except inside the generator-based context manager to catch the specified exception type and ignore it. _Sample Usage:_

  ```python
  from contextlib import contextmanager

  @contextmanager
  def suppress(exc_type):
      try:
          yield
      except exc_type:
          pass

  with suppress(ValueError):
      print(int("abc"))  # This would normally raise ValueError, but is suppressed
  print("Continuing after suppressing error")
  ```

  - **Output:**

    ```
    Continuing after suppressing error
    ```

  (No error thrown from the invalid int conversion.)

> **Week 13 Goal:** You have now touched the deepest parts of everyday Python usage. **Decorators** may have seemed magical at first, but you see they follow the same principle of treating functions as objects (first-class citizens) – you can pass a function to another, wrap it, and return a new one. This meta-programming ability allows powerful patterns (like adding logging, access control, caching, etc., without modifying the core function code). **Context managers** provided insight into the `with` statement and you created your own, which is a professional-level skill (useful when you need to manage resources or transactions). At around 73 projects, you have a very thorough coverage of Python features and paradigms.

Now, the final leg of this roadmap will be focused on consolidating this knowledge into building larger applications and preparing you for real-world scenarios (like packaging your project, writing tests, and using your skills for specialized areas). You have the foundation – the remaining weeks will be about scaling up and integrating everything you’ve learned.

## Week 14: Concurrency – Threads and Asynchrony

**Topics:** Introduce Python’s approaches to concurrency:

- **Multithreading:** using the `threading` module to run code in parallel threads. Discuss the GIL (Global Interpreter Lock) and that CPU-bound tasks won’t speed up with threads, but I/O-bound tasks can benefit (threads will be useful if doing waiting tasks like network calls).
- **Multiprocessing:** mention the `multiprocessing` module for true parallelism on CPU-bound tasks.
- **Asyncio (Asynchronous IO):** a modern way to handle concurrency with async/await (useful for I/O-bound tasks on a single thread). Show a simple async example (like asynchronously fetching data from multiple sources).
  Focus on understanding when and why to use these. By end of week, you should be able to write a simple multi-threaded program and an async function with `asyncio`, though deep mastery of concurrency is a longer topic. The idea is to be aware of these tools and do basic concurrent tasks in Python.

**Resources:**

- **Text:** Python’s official tutorial sections or docs on `threading` and `asyncio` (introductory parts).
- **Video:** _“Python Concurrency Explained”_ (maybe by sentdex or others) – to conceptually grasp threading vs asyncio.
- **External:** Perhaps a blog post comparing threading and asyncio with simple examples.

**Projects:** Try out concurrency in practice:

- **Project 74: Multi-threaded Website Status Checker** – _Description:_ Use the `threading` module to check the status of multiple websites in parallel. _Features:_ Have a list of URLs. Write a function `check_url(url)` that fetches the URL (using `requests.get` perhaps) and prints status code. Spawn threads for each URL to call this function simultaneously. Use `threading.Thread`. _Sample Output:_

  ```
  example.com: 200
  python.org: 200
  somebroken.link: Failed to reach
  ```

  (Order may vary because of concurrency.)

- **Project 75: Multiprocessing Prime Finder** – _Description:_ Use `multiprocessing.Pool` to compute primes in a range faster by splitting the work. _Features:_ If you have a heavy prime-checking task (say finding all primes up to 100k), use multiprocessing to split range into parts and process in parallel on multiple CPU cores. Compare time with single-thread (this might show improvement due to true parallel execution). _Sample Output:_

  ```
  Found 9592 primes up to 100000 in 0.8 seconds (with 4 processes)
  (Single process took 2.3 seconds)
  ```

- **Project 76: Producer-Consumer with Queue (Threads)** – _Description:_ Implement a producer-consumer problem using threads and a `queue.Queue`. _Features:_ One thread produces numbers (e.g., 1 to 5) with a delay, another thread consumes them and prints or squares them. Use a queue to synchronize. This demonstrates coordinating threads. _Sample Output:_ (timing-dependent)

  ```
  Produced 1
  Consumed 1
  Produced 2
  Consumed 2
  ...
  ```

  (Producer and consumer actions interleaved.)

- **Project 77: Multi-file Search (Threads)** – _Description:_ Extend the earlier keyword-in-file search to work concurrently on multiple files. _Features:_ If you have many large text files and want to search all for a keyword, spawn one thread per file (or a fixed pool of threads) to search in parallel, then gather results. _Sample Output:_

  ```
  Searching in 100 files for "Python"...
  Found "Python" in 12 files.
  ```

  (This would likely be faster than doing it sequentially, if I/O is involved.)

- **Project 78: Async Web Scraper** – _Description:_ Use `asyncio` and `aiohttp` (an async HTTP library) to fetch data from multiple URLs concurrently (but single-thread, cooperative multitasking). _Features:_ Write `async def fetch(url)` that uses aiohttp to get a page. Then use `asyncio.gather` to fetch several URLs. Compare the time with doing them sequentially (should be faster if network latency is main factor). _Sample Output:_

  ```
  Fetched example.com in 0.5s
  Fetched python.org in 0.7s
  ... (all done in ~0.7s total, instead of sum of each if sequential)
  ```

- **Project 79: Unit Tests for Calculator** – _Description:_ While not concurrency, it’s a good time to introduce testing (if not already) as projects grow. Use Python’s `unittest` framework to write a few test cases for your earlier calculator or BankAccount classes. _Features:_ Ensure functions return expected results. This isn’t concurrency but is an important dev practice to integrate now that projects become larger. _Sample Output:_

  ```
  ----------------------------------------------------------------------
  Ran 3 tests in 0.002s

  OK
  ```

  (All tests passed.)

> **Week 14 Goal:** You’ve now dipped your toes into concurrency, understanding that Python can handle tasks in parallel through threads (despite the GIL limiting CPU-bound parallelism, threads are still very useful for I/O-bound tasks like waiting for web responses). You also saw how `asyncio` provides a powerful alternative for high-performance networking code by avoiding thread overhead and using an asynchronous event loop. You implemented a classic threading pattern (producer-consumer) and used multiprocessing for a compute-heavy task, which showed a real speed gain by utilizing multiple CPU cores. These are advanced topics; even many intermediate Python developers haven’t deeply used `asyncio`, so you’re ahead of the curve in awareness. With about 79 projects, you have a huge portfolio of examples and exercises.

The final part of this roadmap will focus on polishing all this knowledge: building a couple of **capstone projects** that integrate multiple concepts, and guiding you on how to keep learning beyond this roadmap (like contributing to open source, tackling domain-specific libraries for web or data science, etc.).

## Week 15-16: Capstone Projects and Final Review

**Topics:** The last two weeks are about consolidation and practice at a larger scale. Aim to build **two capstone projects (Project 82 & 83)** that are more comprehensive, incorporating many of the skills acquired:

- One could be a **To-Do List CLI Application** (or a small text-based app of choice) that uses file persistence, classes, and possibly threading or at least robust error handling.
- Another could be an **Expense Tracker** CLI (or a simple personal finance manager) which involves reading/writing to files (or a tiny database), using classes (like Transaction, Account), etc.
  These should be sizable enough to take multiple days to implement and test. Plan them first (create design, choose data structures, outline functionalities), then implement step by step.

Also, do a final review of all topics:

- Revisit any weak areas or those that felt rushed.
- Read style guidelines (PEP 8) and ensure your code in capstones is clean and well-documented.
- If time permits, explore how to package your project (so others can install it), and write unit tests for critical components.

Finally, prepare for the next steps:

- If you plan to go into web development, you might next explore Flask/Django (web frameworks).
- If data science, explore NumPy/Pandas.
- If automation/scripting, maybe more about OS and network automation.
  Your solid Python foundation will make any of those easier to learn.

**Resources:**

- **Text:** PEP 8 – Python’s Style Guide (read the highlights to write idiomatic code).
- **Video:** _“How to Write Better Code in Python”_ (which often covers meaningful naming, refactoring, etc., to improve code quality).
- **Next-step references:** Links to Flask tutorial (if web), or Pandas tutorial (if data science), etc., depending on interest.

**Projects:** Capstones and final tasks:

- **Project 80: Unit Tests for Key Components** – _Description:_ Before/during building capstones, write tests for critical functions (practicing Test-Driven Development on a small scale). _Features:_ Use `unittest` or `pytest` to ensure your classes (like BankAccount or library system) work as expected. This ensures confidence in building larger projects atop them. _Output:_ Test results, as above (OK or failures).

- **Project 81: Code Refactoring** – _Description:_ Take one of your earlier messy or lengthy programs and refactor it using the techniques learned. For example, if your Hangman game was procedural and long, maybe refactor to use a Hangman class, or break it into functions, add error handling, etc. _Features:_ Apply improvements without changing the core functionality. This is a real-world skill (improving code quality). _Output:_ Not visible, but check that the program still works after refactoring and perhaps runs more cleanly or is easier to extend.

- **Project 82: To-Do List Application (Capstone)** – _Description:_ Develop a command-line to-do list manager. Users can add tasks, mark them as done, delete tasks, and save the list to a file. _Features:_

  - Use classes (e.g., a `Task` class and a `ToDoList` class that manages tasks).
  - Use file I/O or JSON to save tasks on disk.
  - Include error handling (e.g., trying to mark a non-existing task as done).
  - Possibly use a text UI loop with options (1\:Add, 2\:List, 3\:Done, 4\:Exit).
  - This project brings together file handling, user input, data structures (list of Task objects), maybe sorting tasks, etc.
    _Sample Interaction:_

  ```
  1. Add task
  2. List tasks
  3. Mark task as done
  4. Save and Exit
  Enter choice: 1
  Enter task description: Buy groceries
  Task added.
  Enter choice: 1
  Enter task description: Call Alice
  Task added.
  Enter choice: 2
  Tasks:
  [ ] 1. Buy groceries
  [ ] 2. Call Alice
  Enter choice: 3
  Enter task number to mark done: 1
  Marked "Buy groceries" as done.
  Enter choice: 2
  Tasks:
  [x] 1. Buy groceries
  [ ] 2. Call Alice
  Enter choice: 4
  Saving tasks... Goodbye!
  ```

  - **Output:** (As above, interactive; and a file like `tasks.json` saved with the tasks.)

- **Project 83: Expense Tracker Application (Capstone)** – _Description:_ A CLI app to record expenses. Users can add an expense (amount, category, date), view a summary of expenses by category or month, and save data. _Features:_

  - Use classes (e.g., `Expense` and maybe `ExpenseTracker`).
  - Possibly use the `datetime` module to handle dates.
  - Use a CSV or JSON file for storage.
  - Support multiple operations: add expense, show total spending, show spending by category, etc.
  - Emphasize using functions to organize logic (maybe one function for each menu action).
    _Sample Interaction:_

  ```
  1. Add expense
  2. Summary by category
  3. Summary by month
  4. Exit
  Enter choice: 1
  Enter amount: 50
  Enter category: Groceries
  Enter date (YYYY-MM-DD, blank for today): (user presses Enter for today)
  Expense added: $50 to Groceries on 2025-05-03.
  Enter choice: 1
  Enter amount: 15
  Enter category: Transport
  Enter date: 2025-05-02
  Expense added: $15 to Transport on 2025-05-02.
  Enter choice: 2
  --- Spending by Category ---
  Groceries: $50
  Transport: $15
  (Total: $65)
  Enter choice: 3
  --- Spending by Month ---
  2025-05: $65
  Enter choice: 4
  Saving... Goodbye!
  ```

  - **Output:** Summaries printed as shown, and data saved to file (e.g., `expenses.csv`).

- **Project 84: Web Scraping with BeautifulSoup** – _Description:_ (Optional, if interested in web dev) Use the `requests` and `BeautifulSoup` (third-party library for HTML parsing) to scrape information from a webpage (like headlines from a news site). _Features:_ Fetch HTML, parse with BeautifulSoup, extract specific elements (like `<h2>` titles). Print them or save to a file. _Output:_ A list of headlines or similar info.

- **Project 85: GUI To-Do List (Tkinter)** – _Description:_ (Optional, if interested in GUIs) Use Tkinter (Python’s standard GUI library) to create a simple window for the to-do list (Project 82) with buttons and list display. _Features:_ This introduces event-driven programming. Out of scope for CLI-focused roadmap, but a fun extension if time permits. _Output:_ A functioning GUI application.

_(Projects 84-85 are optional extensions that can be attempted if they align with the learner’s goals. They show how to transition Python skills to specific domains like web scraping or GUI apps.)_

> **Week 15-16 Goal:** By completing the capstone projects, you’ve demonstrated the ability to integrate Python skills in a larger, real-world context. The to-do app and expense tracker required everything from user input parsing, data management, using libraries, to writing clean code with functions and classes, and handling errors. If you managed these, congratulations – you have effectively _mastered core Python_!

You also practiced testing and refactoring, which are crucial for professional development – code is read and maintained more than it is written, so clarity and correctness are paramount.

Now, with \~85 projects (including two major ones) completed, you have **extensive practical experience**. The schedule of \~15 hours/week was intense but you used it to not only learn concepts but also implement them in code (the best way to learn!).

**Next Steps:** You can confidently say you know Python deeply. From here:

- If you want to get into **Data Structures & Algorithms**, you can start solving problems on LeetCode/HackerRank using Python to improve problem-solving (your strong foundation will let you focus on the algorithms, not the syntax).
- If you aim for **Web Development**, try learning a web framework like Flask or Django next. Those will build on your understanding of Python, introducing you to web concepts.
- If you aim for **Data Science/AI**, start with libraries like NumPy, pandas, and perhaps an intro to machine learning with scikit-learn. Your knowledge of Python will let you grasp library usage quickly.
- If you like **Automation/Scripting/DevOps**, experiment with writing scripts to automate your own tasks, use libraries like `paramiko` (for SSH) or `selenium` (for browser automation).
- And consider contributing to an open source Python project on GitHub – it’s a great way to learn collaboratively and see how large Python projects are structured.

Lastly, keep coding regularly (perhaps follow the _100 Days of Code_ challenge informally to maintain consistency). Engage with the Python community (forums, Stack Overflow, etc.) to continue learning best practices and new features (like new Python 3.x releases).

**Congratulations on completing this learning journey!** You’ve transformed from a Python beginner to a highly proficient Python developer with a solid grasp of both fundamental and advanced concepts, backed by a rich portfolio of projects. Good luck on your future endeavors with Python!

**Summary Table: Weekly Pacing**

| Week        | Topics Covered                              | Key Projects (count)                                         |
| ----------- | ------------------------------------------- | ------------------------------------------------------------ |
| **Week 1**  | Python setup, Syntax, Variables, Data types | Hello World, Addition, Area of Circle, Temp Converter (4)    |
| **Week 2**  | Conditionals (if/elif/else)                 | Even/Odd, Grade Converter, Leap Year, Login Sim (4)          |
| **Week 3**  | Loops (for, while), basic algorithms        | RPS game, Guess number, Mult. table, FizzBuzz, etc. (6)      |
| **Week 4**  | Strings, File I/O, Regex                    | Palindrome, Word count, Caesar cipher, File grep, ... (8)    |
| **Week 5**  | Data structures: Lists and Tuples           | Min/Max, Average, Reverse list, Split evens/odds, Matrix (5) |
| **Week 6**  | Data structures: Sets and Dicts             | Remove dups, Unique letters, Word freq, Phonebook, etc. (6)  |
| **Week 7**  | Functions, Scope, Recursion                 | Calc (with funcs), Quiz, is_prime, factorial, fib (6)        |
| **Week 8**  | Modules, Standard Lib, Packages             | Password gen, API fetch, Custom module, CSV analyzer (7)     |
| **Week 9**  | Error Handling, Debugging, Logging          | Robust calc, Safe file read, Logging decorator (5)           |
| **Week 10** | OOP Basics (classes, methods)               | Rectangle, BankAccount, Person, Student, Library comp. (5)   |
| **Week 11** | OOP Advanced (inheritance, polymorphism)    | Account subclasses, Animal poly, Complex overload, etc. (6)  |
| **Week 12** | Iterators, Generators, Comprehensions       | Map/filter tasks, Fib generator, custom iter, reduce (6)     |
| **Week 13** | Decorators and Context Managers             | Timing/logging decorators, File context, suppress exc (4)    |
| **Week 14** | Concurrency (threads, async) + Testing      | Threaded fetch, async scraper, producer/consumer, tests (6)  |
| **Week 15** | Capstone Project 1 (To-Do CLI)              | Design, implement, test to-do list app (1 major)             |
| **Week 16** | Capstone Project 2 (Expense CLI)            | Design, implement, test expense tracker (1 major)            |

_(Weeks 15-16 primarily allocated to capstones; project count is lower but each is a comprehensive project taking many hours.)_

Each week’s plan respects prerequisite knowledge (e.g., you learned about loops before using them in later projects, learned about classes before inheritance, etc.) – ensuring a smooth progression. By following this roadmap and dedicating \~15 hours each week to study and hands-on coding, you have built proficiency in Python step-by-step, with 100 projects reinforcing every concept learned. This blend of theoretical learning and practical application is key to deep mastery.

**Congratulations on reaching the end of the roadmap!** You are now well-prepared to venture into more specialized Python fields (whether it’s web development, data science, automation, or algorithms) with confidence. Keep practicing and building – the journey of learning never truly ends, but you’ve acquired the skills to tackle whatever comes next in Python.
