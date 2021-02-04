import tkinter 
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
from PIL import ImageTk,Image

root = Tk()


def widget():
    image = Image.open("img/y.png")
    photo = ImageTk.PhotoImage(image)

    label = Label(image=photo,highlightthickness=0,borderwidth=0)
    label.image = photo # this line need to prevent gc
    label.pack(
    
    )


    link_label = Label(
        root,
        text="YouTube Link : ",
        fg="lime",
        bg="black"
    )

    link_label.place(
        relx=0.2,
        rely=0.5,
        anchor="w"
    )

   

    root.linkText = Entry(
        root,
        width=70,
        exportselection=0,
        textvariable=video_Link,
        fg="lime",
        bg="black",
        highlightthickness=1,
        borderwidth=0
    )

    root.linkText.place(
        relx=0.3,
        rely=0.5,
        anchor="w"
    )

    destination_label = Label(
        root,
        text="Destinantion  :",
        bg="black",
        fg="lime"
    )

    destination_label.place(
        relx=0.2,
        rely=0.6,
        anchor="w"
    )

    root.destinationText = Entry(
        root,
        width=55,
        textvariable=download_path,
        fg="lime",
        bg="black",
        highlightthickness=1,
        borderwidth=0
    )

    root.destinationText.place(
        relx=0.3,
        rely=0.6,
        anchor="w"
    )



    browse_B = Button(
        root,
        text="Browse",
        command=Browse,
        width=10,
        bg="black",
        fg="lime",
        highlightthickness=1,
        borderwidth=0,   

    )

    browse_B.place(
        relx=0.7,
        rely=0.6,
        anchor="center"
    )

    Download_B = Button(
        root,
        text="Download",
        command=Download,
        width=20,
        bg="black",
        fg="lime",
        highlightthickness=1,
        borderwidth=0
    )

    Download_B.place(
        relx=0.5,
        rely=0.7,
        anchor="s"
    )

def Browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_path.set(download_directory)

def Download():
    yotube_link = video_Link.get()
    download_folder = download_path.get()
    getVideo = YouTube(yotube_link)
    videoStream = getVideo.streams.first() 
    videoStream.download(download_folder)
    messagebox.showinfo("Succes!",  
                        "Downloaded And Saved In\n" 
                        + download_folder)
  

root.geometry("1000x500") 
root.resizable(False, False) 
root.title("YouTube Video Downloader") 
root.config(background="#000000") 
video_Link = StringVar() 
download_path = StringVar() 

widget()

root.mainloop()