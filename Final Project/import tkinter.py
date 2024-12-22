import tkinter as tk
from tkinter import messagebox


def convert_temperature_logic(temp, from_unit, to_unit):
    """Convert temperature from one unit to another."""
    if from_unit == to_unit:
        return temp
    if from_unit == "FAHRENHEIT":
        return (temp - 32) * 5 / 9 if to_unit == "CELSIUS" else (temp + 459.67) * 5 / 9
    if from_unit == "CELSIUS":
        return temp * 9 / 5 + 32 if to_unit == "FAHRENHEIT" else temp + 273.15
    if from_unit == "KELVIN":
        return temp * 9 / 5 - 459.67 if to_unit == "FAHRENHEIT" else temp - 273.15
    raise ValueError("Invalid unit selected.")


class TempConverterApp:
    """Enhanced GUI class for a temperature converter application."""

    def __init__(self):
        """Initialize the GUI and set up the layout."""
        # Main window setup
        self.root = tk.Tk()
        self.root.title("Temperature Converter")
        self.root.geometry("500x400")
        self.root.configure(background="#e6f7ff")

        # Title Label
        tk.Label(
            self.root,
            text="Temperature Converter",
            font=("Arial", 20, "bold"),
            bg="#99ccff",
            fg="white",
            pady=10,
            relief="ridge",
        ).pack(fill="x", pady=10)

        # Conversion Frame
        self.conversion_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.conversion_frame.pack(pady=10)

        # "Convert From" options
        tk.Label(self.conversion_frame, text="Convert From:", bg="#e6f7ff", font=("Arial", 12)).grid(row=0, column=0, padx=20)
        self.from_unit = tk.StringVar(value="FAHRENHEIT")
        self.create_radio_buttons(self.conversion_frame, self.from_unit, ["FAHRENHEIT", "CELSIUS", "KELVIN"], row=1, column=0)

        # "Convert To" options
        tk.Label(self.conversion_frame, text="Convert To:", bg="#e6f7ff", font=("Arial", 12)).grid(row=0, column=1, padx=20)
        self.to_unit = tk.StringVar(value="CELSIUS")
        self.create_radio_buttons(self.conversion_frame, self.to_unit, ["FAHRENHEIT", "CELSIUS", "KELVIN"], row=1, column=1)

        # Temperature Input
        input_frame = tk.Frame(self.root, bg="#e6f7ff")
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Enter Temperature:", bg="#e6f7ff", font=("Arial", 12)).grid(row=0, column=0, padx=10)
        self.temp_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.temp_entry.grid(row=0, column=1)

        # Rounding Option
        self.round_var = tk.IntVar(value=1)
        tk.Checkbutton(
            input_frame,
            text="Round Result",
            variable=self.round_var,
            bg="#e6f7ff",
            font=("Arial", 10)
        ).grid(row=0, column=2, padx=10)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#e6f7ff")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Convert", command=self.convert_temperature, bg="#99ccff", font=("Arial", 12), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Swap Units", command=self.swap_units, bg="#99ccff", font=("Arial", 12), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Reset", command=self.reset, bg="#99ccff", font=("Arial", 12), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Quit", command=self.root.quit, bg="#ff9999", font=("Arial", 12), width=10).pack(side="left", padx=10)

        # Result Display
        self.result_label = tk.Label(
            self.root,
            text="Result: ",
            font=("Arial", 14),
            bg="#ffffff",
            fg="black",
            relief="sunken",
            width=25,
            pady=5
        )
        self.result_label.pack(pady=10)

        # Start the application
        self.root.mainloop()

    def create_radio_buttons(self, parent, variable, options, row, column):
        """Helper function to create radio buttons for unit selection."""
        for i, option in enumerate(options):
            tk.Radiobutton(
                parent,
                text=option.capitalize(),
                variable=variable,
                value=option,
                bg="#e6f7ff",
                font=("Arial", 10)
            ).grid(row=row + i, column=column, sticky="w")

    def convert_temperature(self):
        """Convert the temperature based on user input and selection."""
        try:
            temp = float(self.temp_entry.get())
            result = convert_temperature_logic(temp, self.from_unit.get(), self.to_unit.get())
            if self.round_var.get():
                result = round(result)
            self.result_label.config(text=f"Result: {result:.2f} {self.to_unit.get().capitalize()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def swap_units(self):
        """Swap the 'Convert From' and 'Convert To' units."""
        self.from_unit.set(self.to_unit.get())
        self.to_unit.set(self.from_unit.get())

    def reset(self):
        """Reset all fields and selections to default."""
        self.from_unit.set("FAHRENHEIT")
        self.to_unit.set("CELSIUS")
        self.temp_entry.delete(0, tk.END)
        self.result_label.config(text="Result: ")
        self.round_var.set(1)


# Run the application
TempConverterApp()
