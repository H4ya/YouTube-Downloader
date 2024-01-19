from pytube import YouTube
from tkinter import *
from tkinter import filedialog


window=Tk()
window.title("Youtube Downloader")
window.geometry("600x320")
window.resizable(FALSE,FALSE)


def browse():
    directory = filedialog.askdirectory(title = "Save Video")
    flde.delete(0,"end")
    flde.insert(0,directory)

def downloadyt():
    link = ytli.get()
    folder = flde.get()
    YouTube(link).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(folder)


ytLogo=PhotoImage(file="YouTube_Logo.png").subsample(2) 
ytTitle=Label(window,image=ytLogo)
ytTitle.place(relx = 0.5,rely = 0.25 ,anchor="center")
#ytlb=YouTube Label
ytlb=Label(window,text="video link")

ytlb.place(x=25,y=150)
#ytli=YouTube Link
ytli=Entry(window, width=60)
ytli.place(x=140,y=150)
#flde=Downloaded File Location Entry
#fldl=Downloaded Location Label

fldl=Label(window,text="Download File")
fldl.place(x=25,y=183)

flde=Entry(window, width=50)
flde.place(x=140,y=183)
#brst= browse button
brst=Button(window,text="Browse", command=browse)
brst.place(x=455,y=180)

download=Button(window,text="Download", command=downloadyt)
download.place(x=280,y=220)

window.mainloop()