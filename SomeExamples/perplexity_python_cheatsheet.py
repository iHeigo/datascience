from nbformat import v4 as nbf

# Create a new notebook
nb = nbf.new_notebook()

# Define notebook cells
cells = [
    # Title and Overview
    nbf.new_markdown_cell("# Python & Data Science Fun Guide and Cheat Sheet"),
    nbf.new_markdown_cell(
        "Welcome, Code Warrior! This guide is designed to be both educational and fun—packed with examples inspired by sci‑fi epics (*The Matrix*, *Star Trek: TNG*, *Assassin’s Creed*, *Harry Potter*), drum & bass, 90s hip hop, and even Arsenal’s glory days from the 2000s/2010s.\n\n"
        "Whether you're debugging like Neo, looping through data like a starship captain, or handling file I/O like an undercover assassin, this cheat sheet has you covered."
    ),
    # Python Fundamentals
    nbf.new_markdown_cell("## 1. Python Fundamentals"),
    nbf.new_markdown_cell("### Comments & Variable Assignment"),
    nbf.new_code_cell(
        "# Single-line comment: your mission log in the Matrix\n"
        "# Example: \n"
        "# This is a comment\n\n"
        "\"\"\"\nMulti-line comments: perfect for epic backstories (or documenting your functions).\n\"\"\"\n\n"
        "# Variables store your data—like secret codes:\n"
        "hero = \"Neo\" # String\n"
        "lives = 3 # Integer (extra lives, like in a video game)\n"
        "pi = 3.14159 # Float\n"
        "is_awake = True # Boolean"
    ),
    # String Operations
    nbf.new_markdown_cell("### String Operations, Indexing & Slicing"),
    nbf.new_code_cell(
        "# Strings are sequences (imagine them as lines of code in the Matrix):\n"
        "spell = \"Expecto Patronum\"\n"
        "print('Spell:', spell)\n\n"
        "# Indexing: Get the first character\n"
        "print('First letter:', spell[0]) # 'E'\n\n"
        "# Slicing: Extract part of the spell\n"
        "print('Partial spell:', spell[0:6]) # 'Expect'\n\n"
        "# Common string methods:\n"
        "print('Lowercase:', spell.lower())\n"
        "print('Uppercase:', spell.upper())\n"
        "print('Replaced:', spell.replace(\"Patronum\", \"Lumos\"))\n"
        "words = spell.split()\n"
        "print('Words in spell:', words)"
    ),
    # Control Flow & Looping
    nbf.new_markdown_cell("## 2. Control Flow & Looping"),
    nbf.new_markdown_cell("### For Loop Examples"),
    nbf.new_code_cell(
        "# Example 1: Iterating over a list of Arsenal star years\n"
        "release_years = [2001, 2003, 2005]\n"
        "for i in range(len(release_years)):\n"
        " print(f\"Arsenal star year: {release_years[i]}\")\n\n"
        "# Example 2: Modifying a list (changing the colors of your digital avatar)\n"
        "colors = ['red', 'yellow', 'green', 'purple', 'blue']\n"
        "for i in range(len(colors)):\n"
        " print(f\"Before: Color {i} is {colors[i]}\")\n"
        " colors[i] = 'white'\n"
        " print(f\"After: Color {i} is {colors[i]}\")\n\n"
        "# Example 3: Updating dictionary values (boosting starship systems, TNG style)\n"
        "systems = {'warp_drive': 5, 'shields': 3, 'phasers': 4}\n"
        "for key in systems:\n"
        " systems[key] += 1\n"
        "print('Upgraded systems:', systems)"
    ),
]

# Add cells to notebook
nb['cells'] = cells

# Write the notebook to a file
with open("python_cheatsheet.ipynb", 'w') as f:
    nbf.write(nb, f)

print("Jupyter Notebook created successfully as 'python_cheatsheet.ipynb'")
