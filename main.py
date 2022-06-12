from tkinter import *
import pytube
from tkinter import filedialog
from tkinter import ttk
import random

root = Tk()
root.geometry('500x300') # Size of the window
root.resizable(0, 0) # makes the window adjustable with its features
root.title('Multitasking Project')

ytDownloaderScaleX = root.winfo_width()/500

tabControl = ttk.Notebook(root)

youtubeVideoDownloader = Frame(tabControl)
notebook = Frame(tabControl)
hangman = Frame(tabControl)
calculator = Frame(tabControl)

tabControl.pack(expand = 1, fill ="both")

#Adding tabs
tabControl.add(youtubeVideoDownloader,text='ytDownload')
tabControl.add(notebook,text='Notebook')
tabControl.add(hangman,text='WordGuess')
tabControl.add(calculator,text="Calculator")

#Youtube video downloader ///////////////////////////////////////////////////////////////////////
def downloadMP4():
    try:
        url = pytube.YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
        video = url.streams.get_highest_resolution() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
        video.download(output_path=file_path.get(),filename=(str(videoName.get())+".mp4"))  # This is the method with the instruction to download the video.
    except pytube.exceptions.RegexMatchError:
        downloadInfoText.set("No video is connected to this link")
    else:
        downloadInfoText.set("Downloaded") #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.


def downloadMP3():
        url = pytube.YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
        video = url.streams.get_audio_only() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
        video.download(output_path=file_path.get(),filename=(str(videoName.get())+".mp3"))  # This is the method with the instruction to download the video.
        downloadInfoText.set("No video is connected to this link")
        downloadInfoText.set("Downloaded") #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.

def select_path():
    file_path.set(filedialog.askdirectory())

Label(youtubeVideoDownloader, text="Download Youtube videos with highest resolution", font='san-serif 14 bold').pack()
link = StringVar() # Specifying the variable type

videoName = StringVar()
file_path = StringVar()
downloadInfoText = StringVar()

Label(youtubeVideoDownloader, text="Paste your link here", font='san-serif 15 bold').pack()
link_enter = Entry(youtubeVideoDownloader, width=70, textvariable=link).place(x=30, y=55)
Label(youtubeVideoDownloader, text="Rename the video", font='san-serif 15 bold').place(x=150, y=85)
rename_enter = Entry(youtubeVideoDownloader, width=70, textvariable=videoName).place(x=30, y=110)
Label(youtubeVideoDownloader, text="Choose file path", font='san-serif 15 bold').place(x=150, y=140)
directory_enter = Entry(youtubeVideoDownloader, width=70, textvariable=file_path).place(x=30, y=165)

Label(youtubeVideoDownloader, textvariable=downloadInfoText, font="arial 15").place(x=100, y=190)

Button(youtubeVideoDownloader, text='Download MP4', font='san-serif 16 bold', bg='red', padx=2,command=downloadMP4).place(x=50, y=220) #Download MP4
Button(youtubeVideoDownloader, text='Download MP3', font='san-serif 16 bold', bg='red', padx=2,command=downloadMP3).place(x=300, y=220) #Download MP3

photo = PhotoImage(file = r"C:\Users\Admin\Desktop\1 semestr\Python\untitled\Photo.png")
photoimage = photo.subsample(10, 10)
Button(youtubeVideoDownloader,image=photoimage,width=10,height=10, font='san-serif 16 bold', command=select_path).place(x=460, y=165)
#Notebook ////////////////////////////////////////////////////////////////////
textFilePath = StringVar()

def select_text_path():
    textFilePath.set(filedialog.asksaveasfilename())

def write_text():
    with open(textFilePath.get(),"w+") as f:
        inputText = textFile.get("1.0","end-1c")
        f.write(inputText)

Label(notebook, text="Create your txt file", font='san-serif 14 bold').pack()

textFile = Text(notebook, font='san-serif 10 bold', height=9,width=60)
textFile.pack()

Label(notebook,font='san-serif 12 bold',text='Choose file path').pack()
Entry(notebook,width=70,textvariable=textFilePath).pack()

Button(notebook,image=photoimage,width=10,height=10, font='san-serif 16 bold', command=select_text_path).place(x=460, y=200)

Button(notebook, text="Write", font='san-serif 16 bold', bg='yellow', command=write_text).pack(side=BOTTOM)

#Hangman //////////////////////////////////////////////////////////////////////////////////
attempts = StringVar(hangman,'attempts: 0')
attempt = 0

wordGuess = StringVar()
guess = StringVar()
message = StringVar()

num_lines = sum(1 for line in open('Hangman.txt'))

def playAgain():
    with open ('Hangman.txt','r') as words:
        wordIndex = random.randrange(0,num_lines)
        wordList = words.readlines()
    global word
    word = wordList[wordIndex]
    word = word[:-1]
    wordGuess.set('-'*len(word))

    attempts.set('attempts: 0')
    global attempt
    attempt = 0

    message.set("")

def guessWord():
    compared = str(guess.get())

    if not word.lower() == wordGuess.get():
        global attempt
        attempt = attempt + 1
        attempts.set('attempts: ' + str(attempt))

    if compared.lower() == word.lower():
        wordGuess.set(guess.get())
        message.set('You win! Congratulations!')
    elif not compared.isalpha():
        if not word.lower() == wordGuess.get():
            message.set("Only letters!")
    else:
        replacement = ""
        for i in range(len(wordGuess.get())):
            if(i < len(compared) and i < len(word)):
                if(compared[i] == word[i] and (wordGuess.get())[i] == '-'):
                    replacement = replacement + word[i]
                else:
                    replacement = replacement + (wordGuess.get())[i]
            else:
                replacement = replacement + (wordGuess.get())[i]
        wordGuess.set(replacement)
    guess.set("")

playAgain()

Label(hangman, text="Guess the word!", font='san-serif 14 bold').pack()

Label(hangman, textvariable=wordGuess, font='san-serif 14 bold').pack()

Entry(hangman,width=70,textvariable=guess).pack()
Button(hangman, text='Guess', font='san-serif 16 bold', bg='green', command=guessWord).pack()

Label(hangman, textvariable=message, font='san-serif 14 bold').pack()

Label(hangman, textvariable=attempts, font='san-serif 14 bold').pack()

Button(hangman, text='Play Again', font='san-serif 16 bold', bg='green', command=playAgain).pack(side=BOTTOM)

#Calculator //////////////////////////////////////////////////////////////////////////////////
def InputText(text):
    global calElement
    if(isinstance(text,int)):
        if(text == 0 and calElement == ""):
            return
        calElement = calElement + str(text)
    elif(calElement!=""):
        if (text == "="):
            calInput.set(eval(calInput.get()))
            return
        calElement = ""
    else:
        return
    calInput.set(calInput.get() + str(text))

def InputClear(i):
    if i == 1:
        calInput.set((calInput.get())[:-1])
        operations.pop()
    else:
        calInput.set("")
        operations.clear()

calInput = StringVar()

operations = ["+","-","*","/","=",'%']
calElement = ""

Label(calculator,text='Simple calculator', font='san-serif 14 bold').pack()

calculatorInput = Entry(calculator,width=70,textvariable=calInput,state=DISABLED).pack()

x=10
y=50
for i in range(10):
    Button(calculator,text=i,width=1,height=1, font='san-serif 16 bold', command= lambda text=i: InputText(text)).place(x = x,y = y)
    x=x+30
    if x==100:
        x=10
        y=y+40

Button(calculator, text='Del', width=3, height=1, font='san-serif 16 bold', command=lambda text=i: InputClear(1)).place(x=x, y=y)
Button(calculator, text='Clear', width=4, height=1, font='san-serif 16 bold', command=lambda text=i: InputClear(0)).place(x=10, y=210)
y = 50
x = 100

for i in operations:
    Button(calculator,text=i,width=1,height=1, font='san-serif 16 bold', command= lambda text=i: InputText(text)).place(x = x,y = y)
    y = y + 40
    if y == 250:
        y = 50
        x = x+30


root.mainloop()