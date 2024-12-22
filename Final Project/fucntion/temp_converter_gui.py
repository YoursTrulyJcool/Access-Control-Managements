import tkinter as tk
from tkinter import messagebox

# Function to handle temperature conversion logic
def convert_temperature_logic(temp, from_unit, to_unit):
    """Convert temperature from one unit to another."""
    if from_unit == to_unit:
        return temp  # No conversion needed if units are the same
    if from_unit == "FAHRENHEIT":
        # Convert from Fahrenheit to Celsius or Kelvin
        return (temp - 32) * 5 / 9 if to_unit == "CELSIUS" else (temp + 459.67) * 5 / 9
    if from_unit == "CELSIUS":
        # Convert from Celsius to Fahrenheit or Kelvin
        return temp * 9 / 5 + 32 if to_unit == "FAHRENHEIT" else temp + 273.15
    if from_unit == "KELVIN":
        # Convert from Kelvin to Fahrenheit or Celsius
        return temp * 9 / 5 - 459.67 if to_unit == "FAHRENHEIT" else temp - 273.15
    raise ValueError("Invalid unit selected.")  # Handle invalid unit selection

# Main application class for the temperature converter
class TempConverterApp:
    """Enhanced GUI class for a temperature converter application."""

    def __init__(self):
        """Initialize the GUI and set up the layout."""
        # Set up the main window
        self.root = tk.Tk()
        self.root.title("Temperature Converter")
        self.root.geometry("500x400")
        self.root.configure(background="#e6f7ff")

        # Title Label for the application
        tk.Label(
            self.root,
            text="Temperature Converter",
            font=("Arial", 20, "bold"),
            bg="#99ccff",
            fg="white",
            pady=10,
            relief="ridge",
        ).pack(fill="x", pady=10)

        # Frame for conversion options
        self.conversion_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.conversion_frame.pack(pady=10)

        # Section for "Convert From" radio buttons
        tk.Label(self.conversion_frame, text="Convert From:", bg="#e6f7ff", font=("Arial", 12)).grid(row=0, column=0, padx=20)
        self.from_unit = tk.StringVar(value="FAHRENHEIT")  # Default "from" unit
        self.create_radio_buttons(self.conversion_frame, self.from_unit, ["FAHRENHEIT", "CELSIUS", "KELVIN"], row=1, column=0)

        # Section for "Convert To" radio buttons
        tk.Label(self.conversion_frame, text="Convert To:", bg="#e6f7ff", font=("Arial", 12)).grid(row=0, column=1, padx=20)
        self.to_unit = tk.StringVar(value="CELSIUS")  # Default "to" unit
        self.create_radio_buttons(self.conversion_frame, self.to_unit, ["FAHRENHEIT", "CELSIUS", "KELVIN"], row=1, column=1)

        # Input field for temperature value
        input_frame = tk.Frame(self.root, bg="#e6f7ff")
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Enter Temperature:", bg="#e6f7ff", font=("Arial", 12)).grid(row=0, column=0, padx=10)
        self.temp_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)  # Text entry field
        self.temp_entry.grid(row=0, column=1)

        # Checkbox to enable/disable rounding of results
        self.round_var = tk.IntVar(value=1)  # Default to rounding enabled
        tk.Checkbutton(
            input_frame,
            text="Round Result",
            variable=self.round_var,
            bg="#e6f7ff",
            font=("Arial", 10)
        ).grid(row=0, column=2, padx=10)

        # Buttons for various actions (Convert, Swap, Reset, Quit)
        button_frame = tk.Frame(self.root, bg="#e6f7ff")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Convert", command=self.convert_temperature, bg="#99ccff", font=("Arial", 12), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Swap Units", command=self.swap_units, bg="#99ccff", font=("Arial", 12), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Reset", command=self.reset, bg="#99ccff", font=("Arial", 12), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Quit", command=self.root.quit, bg="#ff9999", font=("Arial", 12), width=10).pack(side="left", padx=10)

        # Label to display the result
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

        # Start the Tkinter main loop
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
            temp = float(self.temp_entry.get())  # Get the entered temperature
            result = convert_temperature_logic(temp, self.from_unit.get(), self.to_unit.get())  # Perform conversion
            if self.round_var.get():  # Check if rounding is enabled
                result = round(result)
            self.result_label.config(text=f"Result: {result:.2f} {self.to_unit.get().capitalize()}")  # Display result
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Handle invalid input

    def swap_units(self):
        """Swap the 'Convert From' and 'Convert To' units."""
        self.from_unit.set(self.to_unit.get())  # Set "from" unit to "to" unit
        self.to_unit.set(self.from_unit.get())  # Set "to" unit to "from" unit

    def reset(self):
        """Reset all fields and selections to default."""
        self.from_unit.set("FAHRENHEIT")  # Reset "from" unit to default
        self.to_unit.set("CELSIUS")  # Reset "to" unit to default
        self.temp_entry.delete(0, tk.END)  # Clear the temperature entry field
        self.result_label.config(text="Result: ")  # Clear the result display
        self.round_var.set(1)  # Reset rounding option to enabled


# Run the application
TempConverterApp()
