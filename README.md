# Python Morse Code Converter (CustomTkinter)

A Morse code translator built with Python and the CustomTkinter library. This application allows users to easily convert text to Morse code and vice-versa through a clean graphical interface.

## Features

* **Modern GUI:** Uses the CustomTkinter library for an updated look.
* **Dark Theme:** Features a pre-configured dark appearance mode.
* **Bidirectional Conversion:**
    * Convert plain text (alphanumeric characters supported by the dictionary) into Morse code.
    * Convert Morse code back into plain text.
* **Clear Input/Output:** Separate text boxes for input and displaying results.
* **Easy Controls:** Dedicated buttons for "Text -> Morse", "Morse -> Text", and "Clear".
* **Standard Morse Format:**
    * Uses spaces to separate Morse letters.
    * Uses ' / ' (space, slash, space) to represent spaces between words in Morse code.
* **Dependency Management:** Uses a `requirements.txt` file for easy installation of necessary libraries.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CreaTKeW/Morse-Code-Converter.git
    cd Morse-Code-Converter
    ```

2.  **Install the required dependencies:**
    Open your terminal or command prompt in the project directory and run:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1.  **Navigate** to the project directory in your terminal.
2.  **Run the application:**
    ```bash
    python main.py
    ```
3.  The "Mouse Code Converter" window will appear.

    * **Text to Morse:**
        1.  Enter your text in the top text box ("Enter your text:").
        2.  Click the **"Text -> Morse"** button.
        3.  The resulting Morse code will appear in the bottom text box ("Result:"). Letters are separated by spaces, words by ` / `.

    * **Morse to Text:**
        1.  Enter the Morse code in the top text box.
        2.  **Important:** Use single spaces between Morse letters and ` / ` (space, slash, space) between words. Example: `.... . .-.. .-.. --- / .-- --- .-. .-.. -..` for "HELLO WORLD".
        3.  Click the **"Morse -> Text"** button.
        4.  The decoded text will appear in the bottom text box.

    * **Clear Fields:**
        1.  Click the **"Clear"** button to empty both the input and output text boxes.

## Code Structure

* **`app.py`**:
    * Contains the main `App` class, inheriting from `customtkinter.CTk`.
    * Defines the GUI layout, widgets (labels, text boxes, buttons).
    * Includes the `morse_dict` (imported from `morse_code.py`) and its reversed version for lookups.
    * Implements the core conversion logic (`convert_to_morse`, `convert_to_text`).
    * Handles button commands (`clear_fields`).
* **`main.py`**:
    * The entry point for the application.
    * Imports the `App` class from `app.py`.
    * Instantiates the `App` and runs the CustomTkinter main loop (`app.mainloop()`).
* **`morse_code.py`** (Assumed):
    * This file (imported by `app.py`) should contain the `morse_dict` dictionary, mapping characters (like 'A', 'B', '1', '2', '.') to their corresponding Morse code strings (like '.-', '-...', '.----', '..---', '.-.-.-').
* **`requirements.txt`**:
    * Lists the necessary Python package dependencies (e.g., `customtkinter`) for installation via `pip`.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/CreaTKeW/Morse-Code-Converter/issues).
