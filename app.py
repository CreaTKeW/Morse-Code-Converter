import customtkinter as ctk
from morse_code import morse_dict

# Reversed morse code used for decoding morse code
REVERSED_MORSE_CODE_DICT = {v: k for k, v in morse_dict.items()}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x550")
        self.title("Mouse Code Converter")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme('dark-blue')

        # Top label adn textbox
        self.input_label = ctk.CTkLabel(self, text="Enter your text:")
        self.input_textbox = ctk.CTkTextbox(self, height=150, width=550)

        # Bottom label and textbox
        self.output_label = ctk.CTkLabel(self, text="Result:")
        self.output_textbox = ctk.CTkTextbox(self, height=150, width=550, state="disabled")

        self.button_frame = ctk.CTkFrame(self)
        self.button_to_morse = ctk.CTkButton(self.button_frame, text="Text -> Morse", command=self.convert_to_morse)
        self.button_to_text = ctk.CTkButton(self.button_frame, text="Morse -> Text", command=self.convert_to_text)
        self.button_clear = ctk.CTkButton(self.button_frame, text="Clear", command=self.clear_fields, fg_color="grey", hover_color="#555555")

        self.input_label.pack(pady=(10, 0))
        self.input_textbox.pack(pady=5, padx=20, fill="x")

        self.output_label.pack(pady=(10, 0))
        self.output_textbox.pack(pady=5, padx=20, fill="x")

        self.button_frame.pack(pady=20)

        self.button_to_morse.grid(row=0, column=0, padx=10, pady=10)
        self.button_to_text.grid(row=0, column=1, padx=10, pady=10)
        self.button_clear.grid(row=0, column=2, padx=10, pady=10)

        self.original_input_color = self.input_textbox.cget("fg_color")

    # def flash_warning(self, widget, duration_ms=500, flash_color="#FF5050"):
    #     original_color = widget.cget("fg_color")
    #     warning_bg = flash_color
    #
    #     widget.configure(fg_color=warning_bg)
    #     widget.after(duration_ms, widget.configure(fg_color=original_color))

    def convert_to_morse(self):
        input_text = self.input_textbox.get("1.0", "end-1c").upper()
        morse_result = ""
        try:
            for char in input_text:
                if char in morse_dict:
                    morse_result += morse_dict[char] + " "
                elif char == ' ':
                    morse_result += "/ "
                else:
                    # TODO: Add a flash warning about word not being recognized
                    #self.flash_warning(self.input_textbox)
                    pass

            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", morse_result.strip())
            self.output_textbox.configure(state="disabled")

        except Exception as e:
            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", f"Error has occurred: {e}")
            self.output_textbox.configure(state="disabled")


    def convert_to_text(self):
        morse_code = self.input_textbox.get("1.0", "end-1c").strip()
        text_result = ""

        morse_code = morse_code.replace('/', ' / ')
        words = morse_code.split(' / ')

        try:
            for word in words:
                letters = word.split()
                for letter_code in letters:
                    if letter_code in REVERSED_MORSE_CODE_DICT:
                        text_result += REVERSED_MORSE_CODE_DICT[letter_code]
                    else:
                        # TODO: Add a flash warning about word not being recognized
                        pass
                text_result += " "

            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", text_result.strip())
            self.output_textbox.configure(state="disabled")

        except Exception as e:
            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", f"Error has occurred:  {e}")
            self.output_textbox.configure(state="disabled")

    def clear_fields(self):
        self.input_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="disabled")