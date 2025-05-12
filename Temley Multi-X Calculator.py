import tkinter as tk


class TemleyMXCalculatorApp(tk.Tk):

    def __init__(root):
        super().__init__()
        root.title("Temley Multi-X Calculator")
        root.geometry("600x600")
        root.configure(bg="lightblue")
        
        root.label = tk.Label(root, text="Welcome to the Temley Multi-X Calculator!", bg="lightblue", font=("Arial Black", 14))
        root.label.pack(pady=20)

        root.image = tk.PhotoImage(file=r"c:/Users/User/Documents/Test/MyCalt.png")  # Ensure the image file path is correct
        root.image = root.image.subsample(4, 4)  # Resize the image to make it smaller
        root.image_label = tk.Label(root, image=root.image, bg="lightblue")
        root.image_label.pack(pady=10)

        
        root.buttons_frame = tk.Frame(root, bg="lightblue")
        root.interest_button = tk.Button(root.buttons_frame, text="Interest Checker", font=("Times New Roman", 12), command=root.init_ui, bg="white")
        root.interest_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.conversion_button = tk.Button(root.buttons_frame, text="Temperature Checker", font=("Times New Roman", 12), command=root.new_interface, bg="white")
        root.conversion_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.close_button = tk.Button(root.buttons_frame, text="Exit", font=("Times New Roman", 12), fg="white", command=root.exit_button, bg="red")
        root.close_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.buttons_frame.pack(pady=20)

    def exit_button(root):
        """Exits the application."""
        root.quit()
        
    def back_to_main(root):
        super().destroy()  # Destroy the current window
        root.__init__()  # Reinitialize the main window
    
    def init_ui(root):
        """Creates a new interface for additional functionality."""
        # Clear existing widgets
        for widget in root.winfo_children():
            widget.destroy()

        # Add new interface elements
        tk.Label(root, text="Hey! Calculate your Loan/Interest Here", bg="lightblue", font=("Arial Black", 14)).pack(pady=20)

        root.interest_image = tk.PhotoImage(file=r"c:/Users/User/Documents/Test/MyInterest.png") 
        root.interest_image = root.interest_image.subsample(2, 2)  # Resize the image to make it smaller
        root.interest_image_label = tk.Label(root, image=root.interest_image, bg="lightblue")
        root.interest_image_label.pack(pady=10)   
        
        """Initializes the main user interface."""   
        # Input label and entry for Loan Amount
        tk.Label(root, text="Enter Loan Amount:", bg="lightblue", font=("Arial Black", 12)).pack(pady=10)
        root.amount_entry = tk.Entry(root, width=10, font=("Times New Roman", 12))
        root.amount_entry.pack(pady=5)

        # Input label and entry for Interest Rate
        tk.Label(root, text="Enter Interest Rate (%):", bg="lightblue", font=("Arial Black", 12)).pack(pady=10)
        root.interest_rate_entry = tk.Entry(root, width=10, font=("Times New Roman", 12))
        root.interest_rate_entry.pack(pady=5)

        # Input label and entry for Loan Term (in years)
        tk.Label(root, text="Enter Loan Term (years):", bg="lightblue", font=("Arial Black", 12)).pack(pady=10)
        root.loan_term_entry = tk.Entry(root, width=10, font=("Times New Roman", 12))
        root.loan_term_entry.pack(pady=5)

        # Function to calculate interest
        def calculate_interest():
            try:
                loan_amount = float(root.amount_entry.get())
                interest_rate = float(root.interest_rate_entry.get())
                loan_term = int(root.loan_term_entry.get())
                total_interest = loan_amount * (interest_rate / 100) * loan_term
                root.result_label.config(text=f"Total Interest: ${total_interest:.2f}")
                root.result_label.config(text=f"Total Interest: ${total_interest:.2f}\n"
                                              f"Monthly Payment: ${(loan_amount + total_interest) / (loan_term * 12):.2f}\n"
                                              f"Total Payment: ${loan_amount + total_interest:.2f}")
            except ValueError:
                root.result_label.config(text="Invalid input. Please enter numeric values.")

        # Submit button
        tk.Button(root, text="Submit", command=calculate_interest, bg="white", font=("Times New Roman", 12)).pack(pady=10)
             
        # Label to display the result
        root.result_label = tk.Label(root, text="", bg="lightblue", font=("Times New Roman", 12))
        root.result_label.pack(pady=10)

        # Back to main button
        tk.Button(root, text="Back to Main", command=root.back_to_main, bg="white", font=("Times New Roman", 12)).pack(pady=10)

    def new_interface(root):
        """Creates a new interface for additional functionality."""
        # Clear existing widgets
        for widget in root.winfo_children():
            widget.destroy()

        # Add new interface elements
        tk.Label(root, text="Welcome to Temperature Conversion Mode", bg="lightblue", font=("Arial Black", 14)).pack(pady=20)
        
        root.temp_image = tk.PhotoImage(file=r"c:/Users/User/Documents/Test/MyTemp.png")  # Ensure the image file path is correct
        root.temp_image = root.temp_image.subsample(2, 2)  # Resize the image to make it smaller
        root.temp_image_label = tk.Label(root, image=root.temp_image, bg="lightblue")
        root.temp_image_label.pack(pady=10)

        # Input label and entry for Celsius to Fahrenheit conversion
        tk.Label(root, text="Enter Temperature in Celsius:", bg="lightblue", font=("Arial Black", 12)).pack(pady=10)
        root.celsius_entry = tk.Entry(root, width=10, font=("Times New Roman", 12))
        root.celsius_entry.pack(pady=5)

        # Function to convert Celsius to Fahrenheit
        def celsius_to_fahrenheit():
            try:
                celsius = float(root.celsius_entry.get())
                fahrenheit = (celsius * 9/5) + 32
                root.temp_result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
            except ValueError:
                root.temp_result_label.config(text="Invalid input. Please enter a numeric value.")

        # Button for Celsius to Fahrenheit conversion
        tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit, bg="white", font=("Times New Roman", 12)).pack(pady=10)

        # Input label and entry for Fahrenheit to Celsius conversion
        tk.Label(root, text="Enter Temperature in Fahrenheit:", bg="lightblue", font=("Arial Black", 12)).pack(pady=10)
        root.fahrenheit_entry = tk.Entry(root, width=10, font=("Times New Roman", 12))
        root.fahrenheit_entry.pack(pady=5)

        # Function to convert Fahrenheit to Celsius
        def fahrenheit_to_celsius():
            try:
                fahrenheit = float(root.fahrenheit_entry.get())
                celsius = (fahrenheit - 32) * 5/9
                root.temp_result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
            except ValueError:
                root.temp_result_label.config(text="Invalid input. Please enter a numeric value.")

        # Button for Fahrenheit to Celsius conversion
        tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius, bg="white", font=("Times New Roman", 12)).pack(pady=10)

        # Label to display the conversion result
        root.temp_result_label = tk.Label(root, text="", bg="lightblue", font=("Times New Roman", 12))
        root.temp_result_label.pack(pady=10)
        
        tk.Button(root, text="Back to Main", command=root.back_to_main, bg="white", font=("Times New Roman", 12)).pack(pady=10)


def main():
    TemleyMXCalculatorApp().mainloop()

if __name__ == "__main__":
    main()