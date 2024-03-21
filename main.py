import tkinter as tk
from tkinter import messagebox

class ProfileRowUI:
    def __init__(self, master, byte_range="", parameter="", units="", data_type="", on_delete=lambda: None):
        self.master = master
        self.frame = tk.Frame(master, borderwidth=1, relief="solid")

        self.byte_range_var = tk.StringVar(value=byte_range)
        self.parameter_var = tk.StringVar(value=parameter)
        self.units_var = tk.StringVar(value=units)
        self.data_type_var = tk.StringVar(value=data_type)

        self.byte_range_entry = tk.Entry(self.frame, textvariable=self.byte_range_var, width=10)
        self.byte_range_entry.grid(row=0, column=0)
        self.parameter_entry = tk.Entry(self.frame, textvariable=self.parameter_var, width=15)
        self.parameter_entry.grid(row=0, column=1)
        self.units_entry = tk.Entry(self.frame, textvariable=self.units_var, width=10)
        self.units_entry.grid(row=0, column=2)
        self.data_type_entry = tk.Entry(self.frame, textvariable=self.data_type_var, width=10)
        self.data_type_entry.grid(row=0, column=3)

        self.delete_button = tk.Button(self.frame, text="-", command=lambda: self.confirm_delete(on_delete))
        self.delete_button.grid(row=0, column=4)

    def confirm_delete(self, on_delete):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this row?"):
            on_delete()

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def get_data(self):
        return {
            "byte_range": self.byte_range_var.get(),
            "parameter": self.parameter_var.get(),
            "units": self.units_var.get(),
            "data_type": self.data_type_var.get()
        }

class HexProfileApp:
    def __init__(self, master):
        self.master = master
        master.title("Hex Data Profile App")

        # Row management section
        self.profile_frame = tk.Frame(master)
        self.profile_frame.pack(fill=tk.X)

        self.row_uis = []  # List to keep track of row UI elements

        # Inputs for adding a new row
        self.new_row_frame = tk.Frame(master)
        self.new_row_frame.pack(fill=tk.X, pady=10)

        self.new_byte_range = tk.Entry(self.new_row_frame, width=10)
        self.new_byte_range.grid(row=0, column=0)
        self.new_parameter = tk.Entry(self.new_row_frame, width=15)
        self.new_parameter.grid(row=0, column=1)
        self.new_units = tk.Entry(self.new_row_frame, width=10)
        self.new_units.grid(row=0, column=2)
        self.new_data_type = tk.Entry(self.new_row_frame, width=10)
        self.new_data_type.grid(row=0, column=3)

        self.add_row_button = tk.Button(self.new_row_frame, text="+", command=self.add_new_row_ui)
        self.add_row_button.grid(row=0, column=4)

    def add_new_row_ui(self):
        # Function to add a new row to the UI
        data = {
            "byte_range": self.new_byte_range.get(),
            "parameter": self.new_parameter.get(),
            "units": self.new_units.get(),
            "data_type": self.new_data_type.get()
        }
        row_ui = ProfileRowUI(self.profile_frame, **data, on_delete=lambda ui=row_ui: self.delete_row_ui(row_ui))
        row_ui.pack(fill=tk.X, pady=2)
        self.row_uis.append(row_ui)

        # Clear input fields
        self.new_byte_range.delete(0, tk.END)
        self.new_parameter.delete(0, tk.END)
        self.new_units.delete(0, tk.END)
        self.new_data_type.delete(0, tk.END)

    def delete_row_ui(self, ui):
        self.row_uis.remove(ui)
        ui.frame.destroy()

def main():
    root = tk.Tk()
    app = HexProfileApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
