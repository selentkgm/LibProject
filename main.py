import tkinter
import segno
import pytube
import random
from tkinter import *
from tkinter import font

window = Tk()
window.title("Do It What U Want!")
window.geometry("500x500")

my_font = font.Font(size=20)
lbl = Label(window, text="Choose it...", font=my_font)
lbl.grid(column=1, row=0, columnspan=3)

def openNewWindow(name):
    newWindow = tkinter.Toplevel(window)
    label = tkinter.Label(newWindow, text=name)
    label.pack()

    if(name == "Create QR Code"):
        newWindow.geometry("200x100")
        # Create QR code
        def create_qr_code():
            newWindow.geometry("200x300")
            url = url_entry.get()  # get the user input from the Entry box
            qr = segno.make(url)
            qr.save("QRCode.png")
            qr_image = PhotoImage(file="QRCode.png")
            qr_label = Label(newWindow, image=qr_image)
            qr_label.config(width=400, height=400)
            qr_label.image = qr_image
            qr_label.pack()

        url_label = Label(newWindow, text="Enter the URL:")
        url_label.pack()

        url_entry = Entry(newWindow)
        url_entry.pack()

        button1 = Button(newWindow,
                         text="Create QR Code",
                         command=create_qr_code)
        button1.pack()

    if (name == "Download music from Youtube"):
        newWindow.geometry("700x200")
        # Download music from Youtube
        def downloadMusic():
            # Download music from Youtube
            url = url_entry.get()
            video = pytube.YouTube(url)
            path = ""
            stream = video.streams.filter(only_audio=True).first()
            download = stream.download(output_path=path)
            label.config(text=f"Downloaded {download} successfully.")

        url_label = Label(newWindow, text="Enter Youtube URL:")
        url_label.pack()
        url_entry = Entry(newWindow)
        url_entry.pack()

        button = Button(newWindow, text="Download", command=downloadMusic)
        button.pack()

        label = Label(newWindow, text="")
        label.pack()

    if (name == "Take random music name"):
        newWindow.geometry("500x200")
        # Give random music name
        with open("musics.txt", encoding="utf-8") as f:
            lines = f.readlines()
        random_line = random.choice(lines)
        label.config(text=f"Random music name: {random_line}")

button1 = Button(window,
                 text="Create QR Code",
                 command=lambda: openNewWindow("Create QR Code"))

button1.grid(column=1, row=1, sticky="NSEW")

button2 = Button(window,
                 text="Download music from Youtube",
                 command=lambda: openNewWindow("Download music from Youtube"))

button2.grid(column=2, row=1, sticky="NSEW")

button3 = Button(window,
                 text="Take random music name",
                 command=lambda: openNewWindow("Take random music name"))

button3.grid(column=3, row=1, sticky="NSEW")

window.grid_columnconfigure((0, 4), weight=1)
window.grid_rowconfigure((0, 2), weight=1)

window.mainloop()
