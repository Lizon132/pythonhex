import tkinter as tk
from tkinter import filedialog

class HexSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hex Splitter")

        # Hex Input Section
        self.hex_input_label = tk.Label(root, text="Hexstring:")
        self.hex_input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.hex_input_field = tk.Entry(root)
        self.hex_input_field.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Parameter Input Section
        self.split_position_label = tk.Label(root, text="Position:")
        self.split_position_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.split_position_field = tk.Entry(root)
        self.split_position_field.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.parameter_name_label = tk.Label(root, text="Parameter Name:")
        self.parameter_name_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.parameter_name_field = tk.Entry(root)
        self.parameter_name_field.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

        self.add_button = tk.Button(root, text="+", command=self.add_parameter)
        self.add_button.grid(row=1, column=4, padx=5, pady=5)

        self.save_button = tk.Button(root, text="Save", command=self.save_parameters)
        self.save_button.grid(row=1, column=5, padx=5, pady=5)

        self.load_button = tk.Button(root, text="Load", command=self.load_parameters)
        self.load_button.grid(row=1, column=6, padx=5, pady=5)

        # Parameter List Section
        self.parameter_listbox = tk.Listbox(root, height=5)
        self.parameter_listbox.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky="ew")

        # Results Section
        self.results_label = tk.Label(root, text="Original Results:")
        self.results_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.results_text = tk.Text(root, height=5, width=30)
        self.results_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

        self.translated_results_label = tk.Label(root, text="Translated Results:")
        self.translated_results_label.grid(row=3, column=3, padx=5, pady=5, sticky="w")
        self.translated_results_text = tk.Text(root, height=5, width=30)
        self.translated_results_text.grid(row=4, column=3, columnspan=3, padx=5, pady=5, sticky="ew")

        # Split Button
        self.split_button = tk.Button(root, text="Split", command=self.split_hex)
        self.split_button.grid(row=5, column=0, columnspan=7, padx=5, pady=5, sticky="ew")

    def add_parameter(self):
        position = self.split_position_field.get()
        name = self.parameter_name_field.get()
        if position and name:
            self.parameter_listbox.insert(tk.END, f"{position} {name}")
            self.split_position_field.delete(0, tk.END)
            self.parameter_name_field.delete(0, tk.END)

    def save_parameters(self):
        parameters = self.parameter_listbox.get(0, tk.END)
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                for parameter in parameters:
                    file.write(parameter + "\n")

    def load_parameters(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "r") as file:
                parameters = file.readlines()
                for parameter in parameters:
                    self.parameter_listbox.insert(tk.END, parameter.strip())

    def split_hex(self):
        hex_string = self.hex_input_field.get()
        parameters = self.parameter_listbox.get(0, tk.END)
        original_result_text = ""
        translated_result_text = ""
        for parameter in parameters:
            position, name = parameter.split(" ")
            position = int(position)
            start_index = (position - 1) * 2
            end_index = position * 2
            if start_index >= 0 and end_index <= len(hex_string):
                hex_value = hex_string[start_index:end_index]
                original_result_text += f"{name}: {hex_value}\n"
                byte_value = bytes.fromhex(hex_value)
                try:
                    decoded_value = byte_value.decode('utf-8')
                    translated_result_text += f"{name}: {decoded_value}\n"
                except UnicodeDecodeError:
                    translated_result_text += f"{name}: <Not a valid UTF-8 sequence>\n"
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, original_result_text.strip())
        self.translated_results_text.delete(1.0, tk.END)
        self.translated_results_text.insert(tk.END, translated_result_text.strip())





def main():
    root = tk.Tk()
    app = HexSplitterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
