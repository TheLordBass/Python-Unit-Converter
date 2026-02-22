# Python Unit Converter

A simple, interactive command-line tool built in Python to convert measurements between **Inches**, **Feet**, and **Yards**. This project is designed to handle multiple conversions in a single session using a continuous loop.



## 🚀 Features
- **Continuous Loop:** Perform as many conversions as you need without restarting the script.
- **Flexible Input:** Supports shorthand (in, ft, yd) and full unit names (inches, feet, yards).
- **Case Insensitivity:** Accepts inputs regardless of capitalisation (e.g., "Inches", "IN", or "inches").
- **Float Support:** Handles decimal numbers for more precise measurements.

## 🛠️ How It Works
The script uses a `while True` loop to keep the programme running until the user chooses to exit. It maps the relationship between Imperial units:
* $1 \text{ foot} = 12 \text{ inches}$
* $1 \text{ yard} = 3 \text{ feet}$
* $1 \text{ yard} = 36 \text{ inches}$



[Image of while loop flowchart in python]


## 📋 Requirements
- Python 3.x

## 🖥️ Usage
1. Clone this repository or copy the script to your local machine.
2. Open your terminal or command prompt.
3. Run the script:
   ```bash
   python converter.py
