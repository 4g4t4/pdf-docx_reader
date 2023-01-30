import tkinter as tk
from tkinter import filedialog
import pdf_docx_reader


window = tk.Tk()
window.geometry("400x250")
window.title("Read this to me!")
label = tk.Label(window, text="Hello! Select a file and I'll tell you something interesting 🤗 ", font=('Arial', 10))
label.pack(padx=20, pady=20)

file_path = None


def file_docx():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Dokumenty Word", "*.docx")])

read_file = tk.Button(window, text="Read DOCX", fg="red",command=file_docx)
read_file.pack()

def file_pdf():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Dokumenty PDF", "*.pdf")])

read_file2 = tk.Button(window, text="Read PDF", fg="blue",command=file_pdf)
read_file2.pack()

def start():
    if file_path:
        pdf_docx_reader.read_pdf(file_path)
    elif file_path:
        pdf_docx_reader.read_docx(file_path)


start_read = tk.Button(window, text="START", fg="green",command=start)
start_read.pack()

window.mainloop()
