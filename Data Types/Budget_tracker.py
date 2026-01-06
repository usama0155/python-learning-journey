from fpdf import FPDF

# Create PDF with basic ASCII only (replace all special characters)
def clean_ascii(text):
    replacements = {
        "–": "-",
        "’": "'",
        "↔": "<->",
        "✅": "",
        "⚡": "",
        "💎": ""
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Helvetica", 'B', 16)

pdf.cell(0, 10, clean_ascii("Python Basics - Projects & Exercises Roadmap"), ln=True, align='C')
pdf.ln(5)

pdf.set_font("Helvetica", '', 12)
intro_text = ("This PDF contains a structured roadmap of Python basics projects and exercises, "
              "designed to strengthen problem-solving, logic, and programming skills. "
              "It also includes tips for organizing a GitHub repo and README files for professional presentation.\n")
pdf.multi_cell(0, 6, clean_ascii(intro_text))
pdf.ln(3)

topics = {
    "1. Data Types (Numbers, Strings, Booleans)": [
        "Budget Tracker - Track expenses by category, calculate totals and averages",
        "Temperature Converter - Celsius <-> Fahrenheit <-> Kelvin, batch conversion",
        "Tip Calculator - Bill split between people with tip %, handle invalid input",
        "Password Strength Checker - Check strength, suggest improvements",
        "Text Analyzer - Count words, sentences, average word length, vowels/consonants",
        "Mini Number Game - Guessing game with hints and scoring"
    ],
    "2. Lists & Tuples": [
        "Grocery List Manager - Add/remove/search/sort items, handle duplicates",
        "Student Grades Analyzer - Find highest, lowest, average, and ranking",
        "Movie Watchlist - Track movies with tuples, sort/filter by rating/genre",
        "Top 5 Frequent Words - Count word frequency in text, ignore case/punctuation",
        "Task Tracker / To-Do App - Store tasks with priority/status, add/update/delete",
        "Number Stats from User Input - Sum, mean, median, max/min, range",
        "Simple Inventory System - Track stock, low stock alerts, restock"
    ],
    "3. Dictionaries & Sets": [
        "Phonebook - Store contacts {name: number}, search/update/delete",
        "Word Counter - Count frequency of words in text using dictionary",
        "Voting System - Record votes and calculate results",
        "Unique Items Finder - Remove duplicates from lists",
        "Student Attendance Tracker - Mark present/absent, calculate attendance %"
    ],
    "4. Conditional Logic & Loops": [
        "FizzBuzz - Classic, customizable numbers",
        "Multiplication Table Generator - Print tables for user input",
        "Number Classifier - Even/odd, prime, perfect numbers",
        "Password Attempts Simulator - Limited login tries",
        "Pattern Printer - Stars, pyramids, numbers"
    ],
    "5. Functions": [
        "Calculator - Add, subtract, multiply, divide",
        "Unit Converter - Convert lengths, weights, currencies",
        "Factorial Recursion - Compute factorial recursively",
        "Fibonacci Generator - Return nth Fibonacci or list of Fibonacci numbers",
        "Prime Checker - Function to check if number is prime"
    ],
    "6. File I/O": [
        "Log Parser - Read log file, count errors/warnings",
        "Word Counter from File - Count frequency of words in text file",
        "To-Do App with File Storage - Save/load tasks to/from file",
        "CSV Student Grades - Read/write CSV, calculate averages",
        "File Backup Utility - Copy/rename files, handle missing files"
    ],
    "7. Exception Handling": [
        "Safe Division - Handle divide by zero & invalid input",
        "File Reader - Handle missing/non-text files",
        "Input Validator - Force correct type from user",
        "Calculator with Error Handling - Extend calculator with try/except"
    ],
    "8. Modules & Packages": [
        "Math Tools Module - Factorial, prime check, Fibonacci functions",
        "String Tools Module - Text analysis, reverse, palindrome check",
        "Main App - Import modules, menu-driven program",
        "Weather Fetcher (Optional) - Fetch weather data with requests"
    ],
    "9. Object-Oriented Programming (OOP)": [
        "Bank Account - Deposit, withdraw, check balance",
        "Student Class - Store info, calculate grades",
        "Library System - Borrow/return books using objects",
        "Employee Manager - Store employee data, promotions, salary updates"
    ],
    "10. Advanced Lists & Dict Manipulation": [
        "Matrix Operations - Add, multiply, transpose matrices",
        "Nested Dict Parser - Extract info from nested dictionaries",
        "Shopping Cart - Products with price, quantity, total calculation",
        "Data Filtering - Filter list of dicts by conditions"
    ],
    "11. Small CLI Projects / Extras": [
        "Quiz Game - Multiple-choice quiz with score tracking",
        "Hangman - Classic word guessing game",
        "Simple Bank CLI - Menu-driven bank app",
        "Contact Manager - CRUD contacts via CLI"
    ]
}

pdf.add_page()
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, clean_ascii("GitHub Repo & README Tips"), ln=True)
pdf.set_font("Helvetica", '', 12)
tips_text = ("- Organize repo folder by topic (1_data_types_numbers_strings, 2_lists_tuples, etc.)\n"
             "- Include README.md in main repo and each folder\n"
             "- Use modular code (functions/classes) for cleaner scripts\n"
             "- Include sample input/output as comments\n"
             "- Commit in small, meaningful chunks\n"
             "- Optional: Add GIFs/screenshots for LinkedIn\n"
             "- Use type hints and docstrings for professional look")
pdf.multi_cell(0, 6, clean_ascii(tips_text))
pdf.ln(5)

# Add topics and projects
for topic, projects in topics.items():
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.multi_cell(0, 6, clean_ascii(topic))
    pdf.ln(2)
    pdf.set_font("Helvetica", '', 12)
    for idx, project in enumerate(projects, 1):
        pdf.multi_cell(0, 6, clean_ascii(f"{idx}. {project}"))
    pdf.ln(3)

# Save PDF
output_path = "/mnt/data/Python_Basics_Projects_Roadmap_ASCII.pdf"
pdf.output(output_path)
output_path
