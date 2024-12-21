import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("300x200")
root.configure(bg="grey")

count = 1
def display_text():
    global count
    print(f"{count}. {text_input.get()}")
    count += 1

label = tk.Label(root, text="Input Text:")
label.pack(pady=20)

text_input = tk.Entry(root)
text_input.pack()

button = tk.Button(root, text="Submit", command=display_text)
button.pack(pady=10)

root.mainloop()
