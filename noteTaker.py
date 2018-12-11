import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Note Taking Application")
mainWindow.geometry("800x450")
mainWindow.minsize(width=800, height=450)
mainWindow.maxsize(width=800, height=450)


sButtonHeight=2
sButtonWidth = 25
mainWindow.columnconfigure(0, weight=5)
mainWindow.columnconfigure(1, weight=5)
mainWindow.rowconfigure(0, weight=5)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=5)
mainWindow.rowconfigure(4, weight=5)
labelFrame = tkinter.Frame(mainWindow)
textFrame = tkinter.Frame(mainWindow)
buttonFrame = tkinter.Frame(mainWindow)
entryBox = tkinter.Text(textFrame)
lblMain = tkinter.Label(labelFrame, text="Note Taker 2000", font=("Helvetica", 32))
btnExit = tkinter.Button(buttonFrame, text="Exit", command=mainWindow.destroy, height=sButtonHeight, width=sButtonWidth)
btnSave = tkinter.Button(buttonFrame, text="Save", height=sButtonHeight, width=sButtonWidth)
btnLoad = tkinter.Button(buttonFrame, text="Load", height=sButtonHeight, width=sButtonWidth)
labelFrame.grid(row=0, column=0, columnspan=2, sticky='n')
textFrame.grid(row=1, column=0, rowspan=4, sticky='news')
buttonFrame.grid(row=1, column=1, columnspan=2, sticky='e')
lblMain.grid(sticky='news')
entryBox.grid(sticky='news')
btnLoad.grid(sticky='news')
btnSave.grid(sticky='news')
btnExit.grid(sticky='news')



mainWindow.mainloop()


