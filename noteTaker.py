import tkinter


def saveFile():
    try:
        s = open("note1.txt", "w")
        data = entryBox.get("1.0", "end-1c")
        print(data)
        s.write(data)
        s.close()
    except:
        print("Unable to save data.")

def loadFile():
    try:
        s = open("note1.txt", "r")
        data = s.readline()
        entryBox.replace("1.0", "end-1c", data)
    except:
        print("unable to populate entrybox")


mainWindow = tkinter.Tk()
mainWindow.title("Note Taking Application")
mainWindow.geometry("800x450")
mainWindow.minsize(width=800, height=450)
mainWindow.maxsize(width=800, height=450)


sButtonHeight=2
sButtonWidth = 25
mainWindow.columnconfigure(0, weight=5)
mainWindow.columnconfigure(1, weight=5)
mainWindow.columnconfigure(2, weight=5)
mainWindow.rowconfigure(0, weight=5)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=5)
mainWindow.rowconfigure(4, weight=5)

labelFrame = tkinter.Frame(mainWindow)
textFrame = tkinter.Frame(mainWindow)
buttonFrame = tkinter.Frame(mainWindow)

scrollbar = tkinter.Scrollbar(textFrame)
entryBox = tkinter.Text(textFrame, yscrollcommand=scrollbar.set)
lblMain = tkinter.Label(labelFrame, text="Note Taker 2000", font=("Helvetica", 32))
btnExit = tkinter.Button(buttonFrame, text="Exit", command=mainWindow.destroy, height=sButtonHeight, width=sButtonWidth)
btnSave = tkinter.Button(buttonFrame, text="Save", height=sButtonHeight, width=sButtonWidth, command=saveFile)
btnLoad = tkinter.Button(buttonFrame, text="Load", height=sButtonHeight, width=sButtonWidth, command=loadFile)

labelFrame.pack(side='top')
textFrame.pack(side='left')
buttonFrame.pack(side='right', fill='both', expand=True)

scrollbar.pack(side='right', fill='both')
lblMain.pack()
entryBox.pack()
scrollbar.config(command=entryBox.yview)
btnLoad.pack(side='top')
btnSave.pack(side='top')
btnExit.pack(side='bottom')



mainWindow.mainloop()



    