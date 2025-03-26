from nbformat import v4 as nbf

nb = nbf.new_notebook()

cells = [
    # Title and Overview
    nbf.new_markdown_cell("# Python Programming Fundamentals Cheat Sheet"),
    nbf.new_markdown_cell(
        "Welcome to your fun and friendly Python cheat sheet! This notebook covers Python basics, "
        "control flow, data structures, file I/O, exception handling, object-oriented programming, "
        "and data libraries (Pandas, NumPy), plus API & web scraping tips. "
        "Each section includes practical examples and explanations to help you understand why things work as they do."
    ),
    
    # ---------------- Python Fundamentals ----------------
    nbf.new_markdown_cell("## 1. Python Fundamentals"),
    
    nbf.new_markdown_cell("### Comments"),
    nbf.new_code_cell(
        "# Single-line comment: used to explain code or disable execution\n"
        "# This is a comment\n\n"
        "\"\"\" \nMulti-line comments are great for longer explanations, \ndocumentation, or sectioning off your code.\n\"\"\""
    ),
    
    nbf.new_markdown_cell("### Variable Assignment & Data Types"),
    nbf.new_code_cell(
        "# Variables store values for later use\n"
        "name = \"John\"  # String\n"
        "age = 30         # Integer\n"
        "pi = 3.14        # Float\n"
        "is_valid = True  # Boolean\n\n"
        "# Data Types examples:\n"
        "x = 10           # int\n"
        "y = 3.14         # float\n"
        "text = \"Hello\"  # string\n"
        "flag = False     # bool"
    ),
    
    nbf.new_markdown_cell("### String Operations & Indexing/Slicing"),
    nbf.new_code_cell(
        "# Strings are sequences of characters\n"
        "text = \"Hello World\"\n"
        "print('Original:', text)\n\n"
        "# Indexing (0-based):\n"
        "print('First character:', text[0])  # 'H'\n"
        "print('Last character:', text[-1])  # 'd'\n\n"
        "# Slicing: extract part of the string\n"
        "print('Substring [1:5]:', text[1:5])  # 'ello'\n\n"
        "# Useful methods:\n"
        "print('Lowercase:', text.lower())\n"
        "print('Uppercase:', text.upper())\n"
        "print('Trimmed:', \"   spaced   \".strip())\n"
        "print('Replaced:', text.replace(\"World\", \"Python\"))\n"
        "print('Split:', text.split())"
    ),
    
    nbf.new_markdown_cell("### Operators & Comparisons"),
    nbf.new_markdown_cell(
        "Operators are the building blocks of expressions. Here are some common ones:\n\n"
        "| Operator | Description | Example |\n"
        "|----------|-------------|---------|\n"
        "| `+`      | Addition    | `3 + 5` |\n"
        "| `-`      | Subtraction | `10 - 2` |\n"
        "| `*`      | Multiplication | `4 * 3` |\n"
        "| `/`      | Division (float) | `10 / 2` |\n"
        "| `//`     | Floor Division | `10 // 3` |\n"
        "| `%`      | Modulus     | `10 % 3` |\n"
        "| `**`     | Exponentiation | `2 ** 3` |\n"
        "| `==`     | Equal       | `x == y` |\n"
        "| `!=`     | Not Equal   | `x != y` |\n"
        "| `>=`     | Greater Than or Equal | `x >= y` |\n"
        "| `>`      | Greater Than | `x > y` |\n"
        "| `<=`     | Less Than or Equal | `x <= y` |\n"
        "| `<`      | Less Than   | `x < y` |\n"
        "| `and`    | Logical AND | `x > 5 and y < 10` |\n"
        "| `or`     | Logical OR  | `x == 5 or y == 10` |\n"
        "| `not`    | Logical NOT | `not flag` |\n"
        "\n"
        "These operators let you compare values and build complex conditions."
    ),
    
    nbf.new_markdown_cell("### Branching & Control Flow"),
    nbf.new_markdown_cell(
        "Control flow lets your program make decisions. \n\n"
        "#### If, Elif, Else\n"
        "```python\n"
        "score = 85\n"
        "if score >= 90:\n"
        "    print(\"You got an A!\")\n"
        "elif score >= 80:\n"
        "    print(\"You got a B.\")\n"
        "else:\n"
        "    print(\"Need improvement.\")\n"
        "```\n"
        "\n"
        "This structure checks conditions in order and runs the block for the first `True` condition."
    ),
    
    # ---------------- Loop Flow ----------------
    nbf.new_markdown_cell("## 2. Loop Flow"),
    nbf.new_markdown_cell(
        "Both **for** and **while** loops follow a pattern:\n"
        "1. **Initialization:** Set up your starting point or conditions.\n"
        "2. **Condition:** Decide when the loop should keep going.\n"
        "3. **Execution:** Run the code inside the loop.\n"
        "4. **Update:** Change your starting point or condition to eventually end the loop.\n"
        "\n"
        "Use **for loops** when you know the number of iterations or are iterating over a collection. "
        "Use **while loops** when the number of iterations is uncertain and depends on a condition."
    ),
    
    nbf.new_markdown_cell("### For Loops: Iterating Over a Collection"),
    nbf.new_code_cell(
        "# Example: Iterating over a list of dates\n"
        "dates = [1982, 1980, 1973]\n"
        "N = len(dates)  # Initialization: get the number of elements\n"
        "\n"
        "for i in range(N):  # Loop from 0 to N-1\n"
        "    print(f\"Date at index {i}: {dates[i]}\")  # Execution"
    ),
    
    nbf.new_markdown_cell("### For Loops: Modifying Elements in a List"),
    nbf.new_code_cell(
        "# Example: Changing all elements in a list\n"
        "squares = ['red', 'yellow', 'green', 'purple', 'blue']\n"
        "\n"
        "for i in range(len(squares)):\n"
        "    print(f\"Before square {i}: {squares[i]}\")  # Before update\n"
        "    squares[i] = 'white'  # Update\n"
        "    print(f\"After square {i}: {squares[i]}\")  # After update"
    ),
    
    nbf.new_markdown_cell("### While Loops: Repeating Until a Condition is Met"),
    nbf.new_code_cell(
        "# Example: Print numbers until a condition is false\n"
        "count = 0  # Initialization\n"
        "while count < 5:  # Condition\n"
        "    print(f\"Count is {count}\")  # Execution\n"
        "    count += 1  # Update"
    ),
    
    nbf.new_markdown_cell("### Advanced Looping: Using `enumerate`"),
    nbf.new_code_cell(
        "# Example: Looping with enumerate to get index and value\n"
        "colors = ['red', 'green', 'blue']\n"
        "for index, color in enumerate(colors):\n"
        "    print(f\"Color at index {index}: {color}\")"
    ),
    
    # ---------------- Functions & Lambdas ----------------
    nbf.new_markdown_cell("## 3. Functions & Lambdas"),
    nbf.new_markdown_cell("### Function Definition and Call"),
    nbf.new_code_cell(
        "# Functions allow you to reuse code.\n"
        "def greet(name):\n"
        "    # Return a greeting message\n"
        "    return f\"Hello, {name}!\"\n\n"
        "print(greet(\"Alice\"))  # Output: Hello, Alice!"
    ),
    
    nbf.new_markdown_cell("### Lambda Functions: Quick, Anonymous Functions"),
    nbf.new_code_cell(
        "# Lambda example: a one-line function to square a number\n"
        "square = lambda x: x * x\n"
        "print(square(5))  # Output: 25"
    ),
    
    nbf.new_markdown_cell("### Return Statement"),
    nbf.new_code_cell(
        "def add(a, b):\n"
        "    return a + b  # Send the result back to the caller\n\n"
        "result = add(3, 5)\n"
        "print(result)  # Output: 8"
    ),
    
    # ---------------- Data Structures ----------------
    nbf.new_markdown_cell("## 4. Data Structures"),
    nbf.new_markdown_cell("### Comparison: Lists, Tuples, Dictionaries, and Sets"),
    nbf.new_markdown_cell(
        "| Feature        | List (`[]`)        | Tuple (`()`)         | Dictionary (`{}`)                           | Set (`{}`)                    |\n"
        "|----------------|--------------------|----------------------|---------------------------------------------|-------------------------------|\n"
        "| Ordered        | ✅ Yes             | ✅ Yes               | ✅ Yes (insertion order in Python 3.7+)      | ❌ Unordered                  |\n"
        "| Mutable        | ✅ Yes             | ❌ No                | ✅ Yes (values mutable; keys immutable)     | ✅ Yes (elements immutable)   |\n"
        "| Duplicates     | Allowed            | Allowed              | Keys: **Unique**; Values: Allowed            | Not allowed (unique only)     |\n"
        "| Indexing       | Yes                | Yes                  | By key only                                 | Not applicable                |\n"
        "| Use Case       | Dynamic collections| Fixed data           | Fast lookup/mapping                         | Uniqueness, set operations    |"
    ),
    
    nbf.new_markdown_cell("### Lists (Ordered, Mutable)"),
    nbf.new_code_cell(
        "# Creating and manipulating a list\n"
        "fruits = ['apple', 'banana', 'cherry']\n"
        "fruits.append('mango')       # Add element to the end\n"
        "fruits.insert(1, 'orange')     # Insert at index 1\n"
        "print(f\"Element at index 0: {fruits[0]}\")\n"
        "print(f\"Slice [1:3]: {fruits[1:3]}\")\n"
        "fruits.remove('banana')        # Remove by value\n"
        "last = fruits.pop()            # Remove and return last element\n"
        "print('Updated list:', fruits)"
    ),
    
    nbf.new_markdown_cell("### Tuples (Ordered, Immutable)"),
    nbf.new_code_cell(
        "# Creating a tuple (immutable collection)\n"
        "coordinates = (10, 20)\n"
        "x, y = coordinates           # Tuple unpacking\n"
        "print('First element of tuple:', coordinates[0])\n"
        "# Since tuples are immutable, sorting returns a new tuple\n"
        "sorted_tuple = tuple(sorted((3, 1, 4, 2)))\n"
        "print('Sorted tuple:', sorted_tuple)"
    ),
    
    nbf.new_markdown_cell("### Dictionaries (Key-Value Pairs)"),
    nbf.new_code_cell(
        "# Creating a dictionary\n"
        "person = {\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}\n"
        "print('Name:', person[\"name\"])  # Access by key\n"
        "person[\"age\"] = 31              # Update value\n"
        "person[\"country\"] = \"USA\"     # Add new key-value pair\n"
        "if \"city\" in person:\n"
        "    print(\"City exists in the dictionary.\")\n"
        "print('All keys:', list(person.keys()))\n"
        "print('All values:', list(person.values()))\n"
        "del person[\"city\"]              # Delete key\n"
        "print('Updated dictionary:', person)"
    ),
    
    nbf.new_markdown_cell("### Sets (Unordered, Unique Elements)"),
    nbf.new_code_cell(
        "# Creating a set: duplicates are automatically removed\n"
        "unique_numbers = {1, 2, 3, 4, 4}\n"
        "unique_numbers.add(5)              # Add element\n"
        "unique_numbers.discard(2)          # Remove element safely\n"
        "print('Set:', unique_numbers)\n"
        "\n"
        "# Set operations\n"
        "A = {1, 2, 3}\n"
        "B = {3, 4, 5}\n"
        "print('Union:', A.union(B))                # Union\n"
        "print('Intersection:', A.intersection(B))  # Intersection\n"
        "print('Difference:', A.difference(B))        # Difference\n"
        "print('Symmetric Difference:', A.symmetric_difference(B))  # Symmetric difference"
    ),
    
    # ---------------- Exception Handling ----------------
    nbf.new_markdown_cell("## 5. Exception Handling"),
    nbf.new_markdown_cell("### Try-Except Blocks"),
    nbf.new_code_cell(
        "try:\n"
        "    num = int(input(\"Enter a number: \"))\n"
        "except ValueError:\n"
        "    print(\"Invalid input. Please enter a valid number.\")\n"
        "else:\n"
        "    print(\"You entered:\", num)\n"
        "finally:\n"
        "    print(\"Execution complete.\")"
    ),
    
    nbf.new_markdown_cell("### Try-Except with File Handling"),
    nbf.new_code_cell(
        "try:\n"
        "    file = open(\"data.txt\", \"r\")\n"
        "    content = file.read()\n"
        "except FileNotFoundError:\n"
        "    print(\"File not found.\")\n"
        "finally:\n"
        "    file.close()"
    ),
    
    # ---------------- File Handling ----------------
    nbf.new_markdown_cell("## 6. File Handling"),
    nbf.new_markdown_cell("### Using `with` for Automatic File Closure"),
    nbf.new_code_cell(
        "with open(\"file.txt\", \"w\") as f:\n"
        "    f.write(\"Hello, World!\")\n\n"
        "with open(\"file.txt\", \"r\") as f:\n"
        "    content = f.read()\n"
        "    print(content)"
    ),
    
    nbf.new_markdown_cell("### File Reading and Writing Methods"),
    nbf.new_markdown_cell(
        "```python\n"
        "# Read entire file as a string\n"
        "content = f.read()\n\n"
        "# Read file line by line into a list\n"
        "lines = f.readlines()\n\n"
        "# Write a string to a file\n"
        "f.write(\"Some text\")\n\n"
        "# Write multiple lines from a list\n"
        "f.writelines([\"Line 1\\n\", \"Line 2\\n\"])\n"
        "```"
    ),
    
    # ---------------- Object-Oriented Programming ----------------
    nbf.new_markdown_cell("## 7. Object-Oriented Programming (OOP)"),
    nbf.new_markdown_cell("### Class Definition & Object Creation"),
    nbf.new_code_cell(
        "class Person:\n"
        "    def __init__(self, name, age):\n"
        "        self.name = name\n"
        "        self.age = age\n\n"
        "    def greet(self):\n"
        "        return f\"Hello, my name is {self.name} and I'm {self.age} years old.\"\n\n"
        "# Create an instance of Person\n"
        "person1 = Person(\"Alice\", 25)\n"
        "print(person1.greet())"
    ),
    
    # ---------------- Advanced Topics: Pandas & NumPy ----------------
    nbf.new_markdown_cell("## 8. Data Handling with Pandas and NumPy"),
    nbf.new_markdown_cell("### Pandas Cheat Sheet"),
    nbf.new_markdown_cell(
        "| Method | Description | Syntax & Example |\n"
        "|--------|-------------|------------------|\n"
        "| `.read_csv()` | Read CSV file into DataFrame | `df = pd.read_csv(\"data.csv\")` |\n"
        "| `.read_excel()` | Read Excel file | `df = pd.read_excel(\"data.xlsx\")` |\n"
        "| `.to_csv()` | Write DataFrame to CSV | `df.to_csv(\"output.csv\", index=False)` |\n"
        "| `df[\"col\"]` | Access a column | `df[\"age\"]` |\n"
        "| `.describe()` | Summary statistics | `df.describe()` |\n"
        "| `.drop()` | Drop rows/columns | `df.drop([\"col\"], axis=1, inplace=True)` |\n"
        "| `.dropna()` | Remove NaN rows | `df.dropna(inplace=True)` |\n"
        "| `.groupby()` | Group and aggregate data | `df.groupby(\"col\").agg({\"sales\": \"sum\"})` |\n"
        "| `.head()` | Show first n rows | `df.head(5)` |\n"
        "| `.tail()` | Show last n rows | `df.tail(5)` |\n"
        "| `.info()` | DataFrame info | `df.info()` |\n"
        "| `.merge()` | Merge DataFrames | `merged_df = pd.merge(df1, df2, on=[\"key\"])` |"
    ),
    nbf.new_markdown_cell("#### Importing Pandas"),
    nbf.new_code_cell("import pandas as pd"),
    
    nbf.new_markdown_cell("### NumPy Cheat Sheet"),
    nbf.new_markdown_cell(
        "| Method | Description | Syntax & Example |\n"
        "|--------|-------------|------------------|\n"
        "| `np.array()` | Create an array | `arr = np.array([1,2,3])` |\n"
        "| `np.mean()` | Mean of elements | `np.mean(arr)` |\n"
        "| `np.sum()`  | Sum of elements | `np.sum(arr)` |\n"
        "| `np.min()`  | Minimum value | `np.min(arr)` |\n"
        "| `np.max()`  | Maximum value | `np.max(arr)` |\n"
        "| `np.dot()`  | Dot product | `np.dot(arr1, arr2)` |"
    ),
    nbf.new_markdown_cell("#### Importing NumPy"),
    nbf.new_code_cell("import numpy as np\n\narray_1d = np.array([1, 2, 3])\narray_2d = np.array([[1, 2], [3, 4]])"),
    
    # ---------------- API & Data Collection ----------------
    nbf.new_markdown_cell("## 9. API & Data Collection Cheat Sheet"),
    nbf.new_markdown_cell("### Using Requests and BeautifulSoup"),
    nbf.new_markdown_cell(
        "#### Making API Requests with Requests\n"
        "```python\n"
        "import requests\n"
        "response = requests.get(\"https://api.example.com/data\")\n"
        "if response.status_code == 200:\n"
        "    data = response.json()\n"
        "    print(data)\n"
        "```\n"
        "\n"
        "#### Web Scraping with BeautifulSoup\n"
        "```python\n"
        "from bs4 import BeautifulSoup\n"
        "html = '<html><body><a href=\"http://example.com\">Link</a></body></html>'\n"
        "soup = BeautifulSoup(html, 'html.parser')\n"
        "link = soup.find('a')\n"
        "print(link['href'])\n"
        "```\n"
        "\n"
        "Other useful methods: `find_all()`, `select()`, `.text`, and DOM traversal (`.parent`, `.find_next_sibling()`)."
    ),
    
    nbf.new_markdown_cell("### API Request Methods and Headers"),
    nbf.new_markdown_cell(
        "| Method   | Description                  | Syntax & Example |\n"
        "|----------|------------------------------|------------------|\n"
        "| `GET`    | Retrieve data                | `response = requests.get(url)` |\n"
        "| `POST`   | Submit new data              | `response = requests.post(url, data={...})` |\n"
        "| `PUT`    | Update existing data         | `response = requests.put(url, data={...})` |\n"
        "| `DELETE` | Delete a resource            | `response = requests.delete(url)` |\n"
        "| Headers  | Pass custom headers          | `headers = {'Authorization': 'Bearer TOKEN'}` |"
    ),
    
    # ---------------- End of Notebook ----------------
    nbf.new_markdown_cell("## End of Cheat Sheet"),
    nbf.new_markdown_cell(
        "This notebook provides a comprehensive reference for Python programming fundamentals, "
        "data structures, control flow, file handling, OOP, and data manipulation libraries. "
        "It's designed to be both a quick reference and a learning tool. "
        "Feel free to extend and modify it to fit your projects and style. Happy coding!"
    )
]

nb.cells.extend(cells)

# Save the notebook to file
notebook_path = "../SomeExamples/python_programming_fundamentals_cheatsheet.ipynb"
with open(notebook_path, "w") as f:
    f.write(nbf.writes(nb))

notebook_path
