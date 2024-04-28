import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, edit):
    filepath = askopenfilename(filetypes=[("Text files", "*.txt")])

    if not filepath:
        return
    
    edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        edit.insert(tk.END, content)
    window.title(f"Open file: {filepath}")


def save_file(edit):
    filepath = asksaveasfilename(filetypes=[("Text files", "*.txt")])

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = edit.get(1.0, tk.END)
        f.write(content)


def resize(event, edit):
    edit.config(width=event.width // 10)


def main():
    window = tk.Tk()
    window.title("Redemption office of struggle")

    window.minsize(800, 800)

    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    
    toolbox = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_bttn = tk.Button(toolbox, text="Save", command=lambda: save_file(edit))
    open_bttn = tk.Button(toolbox, text="Open", command=lambda: open_file(window, edit))

    save_bttn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_bttn.grid(row=1, column=0, padx=5, sticky="ew")
    toolbox.grid(row=0, column=0, sticky="ns")

    edit = tk.Text(window, font="Helvetica 11")
    edit.grid(row=0, column=1, sticky="nsew")
    edit.config(width=80)  

    window.bind("<Control-s>", lambda event: save_file(edit))
    window.bind("<Control-o>", lambda event: open_file(window, edit))

    window.bind("<Configure>", resize)

    window.mainloop()

main()
