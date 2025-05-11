import tkinter as tk


class TemleyMXCalculatorApp(tk.Tk):

    def __init__(root):
        super().__init__()
        root.title("Temley Multi-X Calculator")
        root.geometry("400x250")
        root.configure(bg="lightblue")
        
        root.label = tk.Label(root, text="Welcome to the Temley Multi-X Calculator!", bg="lightblue", font=("Arial Black", 14))
        root.label.pack(pady=20)

        root.buttons_frame = tk.Frame(root, bg="lightblue")
        root.main_button = tk.Button(root.buttons_frame, text="Main", command=root.init_ui, bg="white")
        root.main_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.conversion_button = tk.Button(root.buttons_frame, text="Conversion", command="", bg="white", state='disabled')
        root.conversion_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.calculator_button = tk.Button(root.buttons_frame, text="New Interface", command=root.new_interface, bg="white")
        root.calculator_button.pack(side=tk.LEFT, padx=10, pady=10)
        root.buttons_frame.pack(pady=20)

    
        
    def init_ui(root):
        """Initializes the main user interface."""   
        # Input label and entry for Loan Amount
        tk.Label(root, text="Enter Loan Amount:", bg="lightblue", font=("Arial Black", 12)).pack(pady=10)
        root.celsius_entry = tk.Entry(root, width=10, font=("Times New Roman", 12))
        root.celsius_entry.pack(pady=5)

        # Submit button
        tk.Button(root, text="Submit", command="", bg="white", font=("Times New Roman", 12)).pack(pady=10)

    def new_interface(root):
        """Creates a new interface for additional functionality."""
        # Clear existing widgets
        for widget in root.winfo_children():
            widget.destroy()

        # Add new interface elements
        tk.Label(root, text="Welcome to the New Interface!", bg="lightblue", font=("Arial Black", 14)).pack(pady=20)
        tk.Button(root, text="Back to Main", command=root.init_ui, bg="white", font=("Times New Roman", 12)).pack(pady=10)


def main():
    TemleyMXCalculatorApp().mainloop()

if __name__ == "__main__":
    main()