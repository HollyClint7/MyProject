import tkinter as tk


class TemleyMXCalculatorApp(tk.Tk):

    def __init__(root):
        super().__init__()
        root.title("Temley Multi-X Calculator")
        root.geometry("400x200")
        root.configure(bg="lightblue")
        root.init_ui()
        
    def init_ui(root):
        # Input label and entry for Loan Amount
        tk.Label(root, text="Enter Loan Amount:", bg="lightblue", font=("Arial Black", 12)).pack(pady=10)
        root.celsius_entry = tk.Entry(root, width=10, font=("Times New Roman", 12))
        root.celsius_entry.pack(pady=5)

        # Submit button
        tk.Button(root, text="Submit", command="", bg="white", font=("Times New Roman", 12)).pack(pady=10)





def main():
    TemleyMXCalculatorApp().mainloop()

if __name__ == "__main__":
    main()