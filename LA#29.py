import tkinter as tk

root = tk.Tk()
name = "Sean_Rodg_Belmonte"
section = "BSIT-2A"
root.title("OOP")
root.geometry("300x200")
root.configure(bg="white")


frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text=f"OOP LA29 {name} {section}")
label.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
