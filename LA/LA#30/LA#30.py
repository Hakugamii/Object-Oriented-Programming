import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("300x200")
root.configure(bg="grey")
fav_list = ["Danganronpa", "Tensei Shitara Slime Datta Ken", "Btooom!"]

def display_text():
    count = 0
    print("My favorite animes are:")
    for anime in fav_list:
        count += 1
        print(f"{count}. {anime}")

button = tk.Button(root, text="Print", command=display_text)
button.pack(pady=20)

root.mainloop()
