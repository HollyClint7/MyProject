import tkinter as tk


class TemleyMXCalculatorApp(tk.Tk):

    def __init__(root):
        super().__init__()
        root.title("Temley Multi-X Calculator")
        root.geometry("550x500")
        root.configure(bg="lightblue")
        
        root.label = tk.Label(root, text="Welcome to the Temley Multi-X Calculator!", bg="lightblue", font=("Arial Black", 14))
        root.label.pack(pady=20)

        root.image = tk.PhotoImage(file=r"c:/Users/User/Documents/Test/MyCalt.png")  # Ensure the image file path is correct
        root.image = root.image.subsample(6, 6)  # Resize the image to make it smaller
        root.image_label = tk.Label(root, image=root.image, bg="lightblue")
        root.image_label.pack(pady=10)

        
        root.buttons_frame = tk.Frame(root, bg="lightblue")
        root.interest_button = tk.Button(root.buttons_frame, text="Interest Checker", command=root.init_ui, bg="white")
        root.interest_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.conversion_button = tk.Button(root.buttons_frame, text="Temperature Checker", command=root.new_interface, bg="white")
        root.conversion_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.close_button = tk.Button(root.buttons_frame, text="Exit", fg="white", command=root.exit_button, bg="red")
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
        tk.Label(root, text="Welcome to the New Interface!", bg="lightblue", font=("Arial Black", 14)).pack(pady=20)
        tk.Button(root, text="Back to Main", command=root.back_to_main, bg="white", font=("Times New Roman", 12)).pack(pady=10)


def main():
    TemleyMXCalculatorApp().mainloop()

if __name__ == "__main__":
    main()