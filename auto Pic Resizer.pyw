import PIL.Image
import glob, os
from tkinter import *
from tkinter import filedialog
import textwrap
import webbrowser


def callback(url):
    webbrowser.open_new(url)


def selectFolder():
    root.geometry("300x410")
    startButton.place(x=100, y=320)
    errorText.config(text="", justify=LEFT)
    errorButton.place(x=1000, y=4150)
    selectFolderLabel.config(foreground="black")
    filetypes = (
        ('PDF Files', '*.pdf')
    )
    folderSelected = filedialog.askdirectory()
    if len(folderSelected) > 1:
        withoutWrapFolderLocation.config(text=folderSelected)
        dir = os.listdir(folderSelected)
        if len(folderSelected) > 0:
            if len(dir) == 0:
                getFolderLocation.config(text="Empty directory", fg="red")
                selectFolderLabel.config(foreground="red")
            else:
                wrapper = textwrap.TextWrapper(width=38)
                word_list = wrapper.wrap(text=folderSelected)
                caption_new = ''
                for ii in word_list[:-1]:
                    caption_new = caption_new + ii + '\n'
                caption_new += word_list[-1]
                getFolderLocation.config(text=caption_new, justify=LEFT)
                selectFolderLabel.config(foreground="black")
                getFolderLocation.config(foreground="green")


def outputFolder():
    root.geometry("300x410")
    startButton.place(x=100, y=320)
    errorText.config(text="", justify=LEFT)
    errorButton.place(x=1000, y=4150)
    outputFolderLabel.config(foreground="black")
    filetypes = (
        ('PDF Files', '*.pdf')
    )
    outputSelected = filedialog.askdirectory()
    if len(outputSelected) > 1:
        withoutWrapOutputLocation.config(text=outputSelected)
        if len(outputSelected) > 0:
            wrapper = textwrap.TextWrapper(width=38)
            word_list = wrapper.wrap(text=outputSelected)
            caption_new = ''
            for ii in word_list[:-1]:
                caption_new = caption_new + ii + '\n'
            caption_new += word_list[-1]
            getOutputLocation.config(text=caption_new, justify=LEFT)


def resizer():
    getFolderLocationLength = withoutWrapFolderLocation.cget("text")
    getOutputLocationLength = withoutWrapOutputLocation.cget("text")
    width = widthText.get()
    height = heightText.get()
    intLock = 1
    error = "Width or Height Value Error: Only Enter Numeric Value Without Decimal"
    try:
        int(width)
        widthLabel.config(foreground="black")
    except ValueError:
        widthLabel.config(foreground="red")
        root.geometry("300x440")
        startButton.place(x=100, y=365)
        errorText.place(x=5, y=310)
        wrapper = textwrap.TextWrapper(width=38)
        word_list = wrapper.wrap(text=error)
        caption_new = ''
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]
        errorText.config(text=caption_new, justify=LEFT)
        intLock = 0
    try:
        int(height)
        heightLabel.config(foreground="black")
    except ValueError:
        heightLabel.config(foreground="red")
        root.geometry("300x440")
        startButton.place(x=100, y=365)
        errorText.place(x=5, y=310)
        wrapper = textwrap.TextWrapper(width=38)
        word_list = wrapper.wrap(text=error)
        caption_new = ''
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]
        errorText.config(text=caption_new, justify=LEFT)
        intLock = 0

    if len(getFolderLocationLength) > 0 and len(getOutputLocationLength) > 0 and len(width) > 0 and len(height) > 0 and getFolderLocationLength != "Empty directory" and intLock > 0:
        errorText.place(x=5000, y=3100)
        root.geometry("300x410")
        startButton.place(x=100, y=320)
        if withoutWrapFolderLocation.cget("text") == withoutWrapOutputLocation.cget("text"):
            root.geometry("300x510")
            startButton.place(x=1000, y=3200)
            errorTextIs = "WARNING: Both Directories are same. Will Replace the Original Pictures With New Sized Ones.\nAction Cannot Be Reversed"
            wrapper = textwrap.TextWrapper(width=38)
            word_list = wrapper.wrap(text=errorTextIs)
            caption_new = ''
            for ii in word_list[:-1]:
                caption_new = caption_new + ii + '\n'
            caption_new += word_list[-1]
            errorText.config(text=caption_new, justify=LEFT)
            errorButton.place(x=100, y=415)

        else:
            outputFolderLabel.config(foreground="black")
            selectFolderLabel.config(foreground="black")
            widthLabel.config(foreground="black")
            heightLabel.config(foreground="black")
            folder = os.path.expanduser(withoutWrapFolderLocation.cget("text"))
            os.chdir(folder)
            file_dict = {}
            for file in glob.glob("*.jpg"):
                filepath = folder + "/" + file
                image = PIL.Image.open(file)
                # new_image = image.resize((285, 176))
                new_image = image.resize((int(widthText.get()), int(heightText.get())))
                output = os.path.expanduser(withoutWrapOutputLocation.cget("text"))

                os.chdir(output)
                new_image.save(output + "\\" + file)

                folder = os.path.expanduser(withoutWrapFolderLocation.cget("text"))
                os.chdir(folder)

            os.startfile(withoutWrapOutputLocation.cget("text"))
            root.destroy()

    else:
        if len(getFolderLocationLength) < 1 and len(getOutputLocationLength) < 1 and len(width) < 1 and len(height) < 1:
            outputFolderLabel.config(foreground="red")
            selectFolderLabel.config(foreground="red")
            widthLabel.config(foreground="red")
            heightLabel.config(foreground="red")

        if len(getFolderLocationLength) < 1 and len(getOutputLocationLength) < 1:
            outputFolderLabel.config(foreground="red")
            selectFolderLabel.config(foreground="red")

        elif len(getFolderLocationLength) < 1:
            selectFolderLabel.config(foreground="red")

        elif len(getOutputLocationLength) < 1:
            outputFolderLabel.config(foreground="red")

        elif len(width) < 1:
            widthLabel.config(foreground="red")

        elif len(width) > 0:
            widthLabel.config(foreground="black")

        elif len(height) < 1:
            heightLabel.config(foreground="red")

        elif len(height) > 0:
            heightLabel.config(foreground="black")


def warningResizer():
    folder = os.path.expanduser(withoutWrapFolderLocation.cget("text"))
    os.chdir(folder)
    file_dict = {}
    for file in glob.glob("*.jpg"):
        filepath = folder + "/" + file
        image = PIL.Image.open(file)
        # new_image = image.resize((285, 176))
        new_image = image.resize((int(widthText.get()), int(heightText.get())))
        output = os.path.expanduser(withoutWrapOutputLocation.cget("text"))

        os.chdir(output)
        new_image.save(output + "\\" + file)

        folder = os.path.expanduser(withoutWrapFolderLocation.cget("text"))
        os.chdir(folder)

    os.startfile(withoutWrapOutputLocation.cget("text"))
    root.destroy()


root = Tk()
root.resizable(0,0)
root.iconbitmap('icon.ico')
root.title('Multi-Pic Resizer')
# root.geometry("300x285")
root.geometry("300x410")
root.configure(bg="white")

# myFont = font.Font(family='Helvetica', size=20, weight='bold')


img=PhotoImage(file='Multi-Pic Resizer.png')
label = Label(root, image=img)
label.configure(foreground="black")
label.configure(bg="white")
label.place(x=47, y=1)

selectFolderLabel = Label(root, text="Select Pic Folder", font=("Comic Sans MS", 17, 'bold'))
selectFolderLabel.configure(bg="white")
selectFolderLabel.place(x=5, y=119)

selectFolder = Button(root, text='Browse', command=selectFolder)
selectFolder.place(x=230, y=127)

getFolderLocation = Label(root, text="", font=("calibri", 12))
getFolderLocation.configure(bg="white")
getFolderLocation.configure(fg="green")
getFolderLocation.place(x=5, y=154)

outputFolderLabel = Label(root, text="Output Folder", font=("Comic Sans MS", 16, 'bold'))
outputFolderLabel.configure(bg="white")
outputFolderLabel.place(x=5, y=199)

outputFolder = Button(root, text='Browse', command=outputFolder)
outputFolder.place(x=230, y=205)

getOutputLocation = Label(root, text="", font=("calibri", 12))
getOutputLocation.configure(bg="white")
getOutputLocation.configure(fg="green")
getOutputLocation.place(x=5, y=232)

widthLabel = Label(root, text="Width: ", font=("Inter", 12, 'bold'), justify='center')
widthLabel.configure(bg="white")
widthLabel.place(x=10, y=283)

widthText = Entry(root, width=5, textvariable=(StringVar(root, value='320')), foreground='green', font=("Arial", 12, 'bold'))
widthText.place(x=70, y=284)

xLabel = Label(root, text="X ", font=("Inter", 7, 'bold'), justify='center')
xLabel.configure(bg="white")
xLabel.place(x=142, y=285)

heightLabel = Label(root, text="Height: ", font=("Inter", 12, 'bold'), justify='center')
heightLabel.configure(bg="white")
heightLabel.place(x=170, y=283)

heightText = Entry(root, width=5, textvariable=(StringVar(root, value='240')), foreground='green', font=("Arial", 12, 'bold'))
heightText.place(x=235, y=284)

errorText = Label(root, text="", font=("Comic Sans MS", 10, 'bold'), foreground='red')
errorText.configure(bg="white")
errorText.place(x=5, y=320)

errorButton = Button(root, text="Proceed", font=("Arial", 15, 'bold'), justify='center', command=warningResizer, cursor="hand1")
errorButton.configure(foreground="light green")
errorButton.configure(bg="black")
# startButton.place(x=100, y=208)
errorButton.place(x=1000, y=3200)

startButton = Button(root, text="S T A R T", font=("Arial", 15, 'bold'), justify='center', command=resizer, cursor="hand1")
startButton.configure(foreground="light green")
startButton.configure(bg="black")
# startButton.place(x=100, y=208)
startButton.place(x=100, y=320)

withoutWrapFolderLocation = Label(root, text="", font=("Comic Sans MS", 10, 'bold'), foreground='red')
withoutWrapOutputLocation = Label(root, text="", font=("Comic Sans MS", 10, 'bold'), foreground='red')

footer = Label(root, text="softwares.rubick.org", font=(14), cursor="hand2")
footer.bind("<Button-1>", lambda e: callback("http://softwares.rubick.org"))
footer.configure(foreground="white")
footer.configure(bg="black")
footer.pack(side=BOTTOM)
root.mainloop()