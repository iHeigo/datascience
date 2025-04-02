from nbformat import v4 as nbf

nb = nbf.new_notebook()

cells = [
    # Title and Overview
    nbf.new_markdown_cell("# Python & Data Science Fun Guide and Cheat Sheet"),
    nbf.new_markdown_cell(
        "Welcome, Code Warrior! This guide is designed to be both educational and fun—packed with examples inspired by sci‑fi epics (*The Matrix*, *Star Trek: TNG*, *Assassin’s Creed*, *Harry Potter*), drum & bass, 90s hip hop, and even Arsenal’s glory days from the 2000s/2010s.\n\n"
        "Whether you're debugging like Neo, looping through data like a starship captain, or handling file I/O like an undercover assassin, this cheat sheet has you covered."
    ),
    
    # ---------------- Python Fundamentals ----------------
    nbf.new_markdown_cell("## 1. Python Fundamentals"),
    
    nbf.new_markdown_cell("### Comments & Variable Assignment"),
    nbf.new_code_cell(
        "# Single-line comment: your mission log in the Matrix\n"
        "# Example: \n"
        "# This is a comment\n\n"
        "\"\"\"\nMulti-line comments: perfect for epic backstories (or documenting your functions).\n\"\"\"\n\n"
        "# Variables store your data—like secret codes:\n"
        "hero = \"Neo\"          # String\n"
        "lives = 3               # Integer (extra lives, like in a video game)\n"
        "pi = 3.14159            # Float\n"
        "is_awake = True         # Boolean"
    ),
    
    nbf.new_markdown_cell("### String Operations, Indexing & Slicing"),
    nbf.new_code_cell(
        "# Strings are sequences (imagine them as lines of code in the Matrix):\n"
        "spell = \"Expecto Patronum\"\n"
        "print('Spell:', spell)\n\n"
        "# Indexing: Get the first character\n"
        "print('First letter:', spell[0])  # 'E'\n\n"
        "# Slicing: Extract part of the spell\n"
        "print('Partial spell:', spell[0:6])  # 'Expect'\n\n"
        "# Common string methods:\n"
        "print('Lowercase:', spell.lower())\n"
        "print('Uppercase:', spell.upper())\n"
        "print('Replaced:', spell.replace(\"Patronum\", \"Lumos\"))\n"
        "words = spell.split()\n"
        "print('Words in spell:', words)"
    ),
    
    nbf.new_markdown_cell("### Operators & Comparisons"),
    nbf.new_markdown_cell(
        "Operators let you build conditions—like checking if you're ready to join the ranks of the chosen ones.\n\n"
        "For example, use `and` to ensure multiple conditions are met:\n\n"
        "```python\n"
        "marks = 90\n"
        "attendance = 87\n"
        "if marks >= 80 and attendance >= 85:\n"
        "    print(\"Qualify for honors\")\n"
        "else:\n"
        "    print(\"Not qualified for honors\")\n"
        "```\n\n"
        "Other operators include `==`, `!=`, `>=`, `>`, `<=`, `<`, and logical operators (`and`, `or`, `not`)."
    ),
    
    # ---------------- Control Flow & Looping ----------------
    nbf.new_markdown_cell("## 2. Control Flow & Looping"),
    nbf.new_markdown_cell(
        "Loops are like mission cycles: **Initialization**, **Condition Check**, **Execution**, and **Update**. They repeat until your goal is achieved.\n\n"
        "**For Loops:** Use when you know the number of iterations (like looping through your 90s hip hop playlist).\n\n"
        "**While Loops:** Use when repeating until a condition is met (like waiting for the Enterprise to finish warp travel)."
    ),
    
    nbf.new_markdown_cell("### For Loop Examples"),
    nbf.new_code_cell(
        "# Example 1: Iterating over a list of Arsenal star years\n"
        "release_years = [2001, 2003, 2005]\n"
        "for i in range(len(release_years)):\n"
        "    print(f\"Arsenal star year: {release_years[i]}\")\n\n"
        "# Example 2: Modifying a list (changing the colors of your digital avatar)\n"
        "colors = ['red', 'yellow', 'green', 'purple', 'blue']\n"
        "for i in range(len(colors)):\n"
        "    print(f\"Before: Color {i} is {colors[i]}\")\n"
        "    colors[i] = 'white'\n"
        "    print(f\"After: Color {i} is {colors[i]}\")\n\n"
        "# Example 3: Updating dictionary values (boosting starship systems, TNG style)\n"
        "systems = {'warp_drive': 5, 'shields': 3, 'phasers': 4}\n"
        "for key in systems:\n"
        "    systems[key] += 1\n"
        "print('Upgraded systems:', systems)"
    ),
    
    nbf.new_markdown_cell("### While Loop Examples"),
    nbf.new_code_cell(
        "# Example: Countdown before a hyperspace jump (Star Trek style)\n"
        "countdown = 5\n"
        "while countdown > 0:\n"
        "    print(f\"Jump in {countdown}...\")\n"
        "    countdown -= 1\n"
        "print(\"Warp drive engaged!\")"
    ),
    
    nbf.new_markdown_cell("### Using `enumerate` for Advanced Looping"),
    nbf.new_code_cell(
        "# Example: Looping over a drum & bass playlist with indices\n"
        "tracks = ['Breakbeat', 'Neurofunk', 'Liquid Funk']\n"
        "for index, track in enumerate(tracks):\n"
        "    print(f\"Track {index + 1}: {track}\")"
    ),
    
    # ---------------- Functions & Lambdas ----------------
    nbf.new_markdown_cell("## 3. Functions & Lambdas"),
    nbf.new_markdown_cell("### Defining and Calling Functions"),
    nbf.new_code_cell(
        "# Functions encapsulate code to reuse — like secret spells in Harry Potter\n"
        "def cast_spell(spell_name):\n"
        "    return f\"Casting {spell_name}!\"\n\n"
        "print(cast_spell(\"Expecto Patronum\"))"
    ),
    
    nbf.new_markdown_cell("### Lambda Functions"),
    nbf.new_code_cell(
        "# Lambda: a quick one-liner (think freestyle rap in code)\n"
        "double = lambda x: x * 2\n"
        "print(double(7))  # Output: 14"
    ),
    
    # ---------------- Data Structures ----------------
    nbf.new_markdown_cell("## 4. Data Structures"),
    nbf.new_markdown_cell("### Overview & Comparison"),
    nbf.new_markdown_cell(
        "| Feature        | List (`[]`)        | Tuple (`()`)         | Dictionary (`{}`)                           | Set (`{}`)                    |\n"
        "|----------------|--------------------|----------------------|---------------------------------------------|-------------------------------|\n"
        "| Ordered        | ✅ Yes             | ✅ Yes               | ✅ Yes (insertion order, Py3.7+)             | ❌ Unordered                  |\n"
        "| Mutable        | ✅ Yes             | ❌ No                | ✅ Yes (values mutable; keys immutable)     | ✅ Yes (elements immutable)   |\n"
        "| Duplicates     | Allowed            | Allowed              | Keys: **Unique**; Values: Allowed           | Not allowed (unique only)     |\n"
        "| Indexing       | Yes                | Yes                  | By key only                                 | Not applicable               |\n"
        "| Use Case       | Dynamic collections| Fixed data           | Fast lookup/mapping                         | Uniqueness, set operations   |"
    ),
    
    nbf.new_markdown_cell("### Lists"),
    nbf.new_code_cell(
        "# Creating and modifying a playlist (Arsenal-style mixtape)\n"
        "playlist = ['Old Skool Hip Hop', 'Drum & Bass', 'Jungle']\n"
        "print('Original playlist:', playlist)\n\n"
        "# Append a new track\n"
        "playlist.append('The Matrix Reloaded Soundtrack')\n"
        "print('Updated playlist:', playlist)"
    ),
    
    nbf.new_markdown_cell("### Tuples"),
    nbf.new_code_cell(
        "# Tuples are immutable. To update, convert to a list and back.\n"
        "coordinates = (42, 73)\n"
        "print('Original coordinates:', coordinates)\n\n"
        "temp = list(coordinates)\n"
        "temp[0] = 99\n"
        "coordinates = tuple(temp)\n"
        "print('Updated coordinates:', coordinates)"
    ),
    
    nbf.new_markdown_cell("### Dictionaries"),
    nbf.new_code_cell(
        "# Creating a dictionary of starship systems (Star Trek: TNG style)\n"
        "starship = {\"warp_drive\": 5, \"shields\": 3, \"phasers\": 4}\n"
        "print('Initial starship systems:', starship)\n\n"
        "# Boost each system\n"
        "for system in starship:\n"
        "    starship[system] += 1\n"
        "print('Upgraded starship systems:', starship)"
    ),
    
    nbf.new_markdown_cell("### Sets"),
    nbf.new_code_cell(
        "# Sets hold unique items. Think of them as your collection of legendary relics.\n"
        "relics = {\"Excalibur\", \"Mjolnir\", \"Philosopher's Stone\", \"Excalibur\"}\n"
        "print('Unique relics:', relics)\n\n"
        "# Add a relic and remove one\n"
        "relics.add(\"Infinity Gauntlet\")\n"
        "relics.discard(\"Mjolnir\")\n"
        "print('Updated relics:', relics)"
    ),
    
    # ---------------- Exception Handling & Debugging ----------------
    nbf.new_markdown_cell("## 5. Exception Handling & Debugging"),
    nbf.new_markdown_cell("### Try-Except Blocks: Handling Errors Gracefully"),
    nbf.new_code_cell(
        "# Handling division by zero and type errors\n"
        "try:\n"
        "    result = 10 / 0\n"
        "except ZeroDivisionError:\n"
        "    print(\"Error: Division by zero encountered!\")\n"
        "except TypeError:\n"
        "    print(\"Error: Invalid type provided!\")\n"
        "else:\n"
        "    print(\"Division successful, result:\", result)\n"
        "finally:\n"
        "    print(\"Cleanup actions executed.\")"
    ),
    
    nbf.new_markdown_cell("### More Exception Cases: File and Key Errors"),
    nbf.new_code_cell(
        "try:\n"
        "    data = {'matrix': 'red pill', 'reality': 'blue pill'}\n"
        "    print(data['illusion'])\n"
        "except KeyError:\n"
        "    print(\"KeyError: 'illusion' not found in data.\")\n\n"
        "try:\n"
        "    with open('non_existent_file.txt', 'r') as f:\n"
        "        content = f.read()\n"
        "except FileNotFoundError:\n"
        "    print(\"FileNotFoundError: The file does not exist.\")"
    ),
    
    nbf.new_markdown_cell("### Debugging Tips"),
    nbf.new_markdown_cell(
        "Debugging is an art—like detective work in code:\n\n"
        "- Use `print()` to inspect variable values.\n"
        "- Use a debugger (e.g., `%debug` in Jupyter) to step through your code.\n"
        "- Write tests to isolate bugs.\n"
        "- Comment your code and use logging for more complex projects.\n\n"
        "Remember: Even Morpheus had to debug the Matrix!"
    ),
    
    # ---------------- File Handling ----------------
    nbf.new_markdown_cell("## 6. File Handling"),
    nbf.new_markdown_cell("### File Modes & Cursor Control"),
    nbf.new_markdown_cell(
        "File modes determine how you interact with files:\n\n"
        "| Mode  | Description |\n"
        "|-------|-------------|\n"
        "| `'r'`   | Read (file must exist) |\n"
        "| `'w'`   | Write (overwrites file) |\n"
        "| `'a'`   | Append (adds to end of file) |\n"
        "| `'x'`   | Exclusive creation (fails if file exists) |\n"
        "| `'r+'`  | Read and write |\n\n"
        "Cursor methods:\n"
        "- `.tell()` returns the current position (in bytes).\n"
        "- `.seek(offset, from)` moves the cursor (0: start, 1: current, 2: end).\n"
        "- `.truncate()` cuts the file at the current cursor position.\n\n"
        "Think of it as rewinding or fast‑forwarding through your favorite mixtape."
    ),
    
    nbf.new_markdown_cell("### File I/O Examples"),
    nbf.new_code_cell(
        "# Example: Using 'a+' mode to read and then write\n"
        "with open('Example2.txt', 'a+') as file:\n"
        "    print(\"Initial Location:\", file.tell())\n"
        "    data = file.read()\n"
        "    if not data:\n"
        "        print('Read nothing')\n"
        "    else:\n"
        "        print('Data:', data)\n"
        "    file.seek(0, 0)  # Move to beginning\n"
        "    print(\"New Location:\", file.tell())\n"
        "    data = file.read()\n"
        "    if not data:\n"
        "        print('Read nothing')\n"
        "    else:\n"
        "        print('Data after seek:', data)\n"
        "    print(\"Location after read:\", file.tell())\n\n"
        "# Example: Using 'r+' mode with truncate\n"
        "with open('Example2.txt', 'r+') as file:\n"
        "    file.seek(0, 0)  # Write at beginning\n"
        "    file.write(\"Line 1\\nLine 2\\nLine 3\\nLine 4\\nfinished\\n\")\n"
        "    file.truncate()  # Remove extra content\n"
        "    file.seek(0, 0)\n"
        "    print(file.read())"
    ),
    
    nbf.new_markdown_cell("### Reading and Writing CSV, Excel & SQL"),
    nbf.new_markdown_cell(
        "Pandas makes it easy to work with data files. Use the following methods:\n\n"
        "- **CSV Files**:\n"
        "  - Read: `pd.read_csv('data.csv')`\n"
        "  - Write: `df.to_csv('output.csv', index=False)`\n\n"
        "- **Excel Files**:\n"
        "  - Read: `pd.read_excel('data.xlsx')`\n"
        "  - Write: `df.to_excel('output.xlsx', index=False)`\n\n"
        "- **SQL Databases**: Use `pd.read_sql()` and `df.to_sql()` (requires SQLAlchemy).\n\n"
        "These methods allow you to import/export data seamlessly."
    ),
    nbf.new_markdown_cell("#### Arsenal & Star Trek Themed Data Examples"),
    nbf.new_code_cell(
        "import pandas as pd\n\n"
        "# Arsenal-themed DataFrame\n"
        "arsenal_data = {\n"
        "    'Player': ['Thierry Henry', 'Cesc Fabregas', 'Robin van Persie', 'Samir Nasri', 'Jack Wilshere'],\n"
        "    'ShirtNumber': [14, 4, 10, 7, 8],\n"
        "    'Position': ['Forward', 'Midfielder', 'Forward', 'Midfielder', 'Midfielder'],\n"
        "    'Goals': [175, 69, 52, 30, 20],\n"
        "    'Appearances': [369, 266, 150, 200, 300]\n"
        "}\n"
        "arsenal_df = pd.DataFrame(arsenal_data)\n"
        "print('Arsenal DataFrame:')\n"
        "print(arsenal_df.head())\n\n"
        "# Star Trek: TNG-themed DataFrame\n"
        "tng_data = {\n"
        "    'Officer': ['Jean-Luc Picard', 'William Riker', 'Data', 'Geordi La Forge', 'Worf'],\n"
        "    'Position': ['Captain', 'Commander', 'Lt. Commander', 'Chief Engineer', 'Lieutenant'],\n"
        "    'Age': [59, 42, 35, 40, 38],\n"
        "    'Department': ['Command', 'Command', 'Operations', 'Engineering', 'Security']\n"
        "}\n"
        "tng_df = pd.DataFrame(tng_data)\n"
        "print('\\nStar Trek TNG DataFrame:')\n"
        "print(tng_df.head())"
    ),
    
    nbf.new_markdown_cell("### Advanced DataFrame Indexing & Slicing"),
    nbf.new_markdown_cell(
        "Pandas offers two main indexing methods:\n\n"
        "- **.loc[]**: Label-based indexing (inclusive of both start and stop).\n"
        "- **.iloc[]**: Integer position-based indexing (like standard Python slicing).\n\n"
        "Examples:\n\n"
        "```python\n"
        "# iloc: Get rows 0 to 1 and columns 0 to 2 from Arsenal DataFrame\n"
        "arsenal_df.iloc[0:2, 0:3]\n\n"
        "# loc: Select rows by label and columns by name from TNG DataFrame\n"
        "tng_df.loc[2:3, 'Officer':'Department']\n\n"
        "# Access a single element\n"
        "arsenal_df.loc[arsenal_df.index[0], 'Goals']\n\n"
        "# Slicing with loc (both bounds inclusive)\n"
        "tng_df.loc[0:2, 'Officer':'Age']\n"
        "```"
    ),
    
    nbf.new_markdown_cell("### Filtering, Grouping & Merging DataFrames"),
    nbf.new_code_cell(
        "# Filter Arsenal players with fewer than 60 goals\n"
        "filtered_arsenal = arsenal_df[arsenal_df['Goals'] < 60]\n"
        "print(filtered_arsenal)\n\n"
        "# Group TNG officers by Department and count them\n"
        "grouped_tng = tng_df.groupby('Department').size()\n"
        "print(grouped_tng)\n\n"
        "# Merging DataFrames: Example of a simple merge\n"
        "merged_df = pd.merge(arsenal_df, tng_df, how='cross')\n"
        "print(merged_df.head())"
    ),
    
    nbf.new_markdown_cell("### Working with Pandas Series"),
    nbf.new_code_cell(
        "# Creating a Pandas Series\n"
        "s = pd.Series([10, 20, 30, 40, 50])\n"
        "print('Series values:', s.values)\n"
        "print('Series index:', s.index)\n"
        "print('Series shape:', s.shape)\n\n"
        "# Series methods\n"
        "print('Mean:', s.mean())\n"
        "print('Sum:', s.sum())\n"
        "print('Unique values:', s.unique())"
    ),
    
    # ---------------- NumPy ----------------
    nbf.new_markdown_cell("## 8. Numerical Computing with NumPy"),
    nbf.new_markdown_cell("### NumPy Arrays: The Core of Scientific Computing"),
    nbf.new_markdown_cell(
        "NumPy arrays are fast and efficient—they're like the warp core of a starship, powering complex calculations."
    ),
    
    nbf.new_markdown_cell("### Creating and Manipulating Arrays"),
    nbf.new_code_cell(
        "import numpy as np\n\n"
        "# Creating arrays\n"
        "arr1 = np.array([1, 2, 3, 4, 5])\n"
        "arr2 = np.array([[1, 2], [3, 4]])\n\n"
        "# Basic attributes\n"
        "print('Dimensions:', arr1.ndim)\n"
        "print('Shape:', arr1.shape)\n"
        "print('Size:', arr1.size)\n\n"
        "# Slicing with steps\n"
        "print('Slice [1:5:2]:', arr1[1:5:2])\n\n"
        "# Element-wise operations\n"
        "print('Addition (broadcasting):', arr1 + 5)\n"
        "print('Multiplication:', arr1 * 2)\n\n"
        "# Dot product\n"
        "dot_product = np.dot(arr1, arr1)\n"
        "print('Dot product:', dot_product)"
    ),
    
    nbf.new_markdown_cell("### Universal Functions & Matrix Operations"),
    nbf.new_code_cell(
        "# Universal functions operate element-wise\n"
        "print('Mean:', np.mean(arr1))\n"
        "print('Standard Deviation:', np.std(arr1))\n\n"
        "# Matrix multiplication example\n"
        "mat1 = np.array([[1, 2], [3, 4]])\n"
        "mat2 = np.array([[5, 6], [7, 8]])\n"
        "print('Matrix multiplication (dot):', np.dot(mat1, mat2))"
    ),
    
    # ---------------- API & Web Scraping ----------------
    nbf.new_markdown_cell("## 9. API & Web Scraping"),
    nbf.new_markdown_cell("### Making API Requests with Requests"),
    nbf.new_code_cell(
        "import requests\n\n"
        "url = \"https://api.example.com/data\"\n"
        "response = requests.get(url)\n"
        "if response.status_code == 200:\n"
        "    data = response.json()\n"
        "    print(data)\n"
        "else:\n"
        "    print('Failed to retrieve data:', response.status_code)"
    ),
    
    nbf.new_markdown_cell("### Web Scraping with BeautifulSoup"),
    nbf.new_code_cell(
        "from bs4 import BeautifulSoup\n\n"
        "# Imagine scraping secret archives from a digital world like in Assassin’s Creed\n"
        "html = '<html><body><a href=\"http://example.com\">Link</a></body></html>'\n"
        "soup = BeautifulSoup(html, 'html.parser')\n"
        "link = soup.find('a')\n"
        "print('Scraped link:', link['href'])"
    ),
    
    # ---------------- End of Notebook ----------------
    nbf.new_markdown_cell("## End of Cheat Sheet"),
    nbf.new_markdown_cell(
        "Congratulations, Code Warrior! You now have a robust, fun, and friendly guide to Python and data science fundamentals. "
        "Whether you're channeling Arsenal's precision or the leadership of Captain Picard, this notebook is your secret weapon. "
        "Happy coding and may your algorithms be ever in your favor!"
    )
]

nb.cells.extend(cells)

# Save the notebook to file
notebook_path = "../SomeExamples/python_programming_fundamentals_cheatsheet_v3.ipynb"
with open(notebook_path, "w") as f:
    f.write(nbf.writes(nb))

notebook_path
