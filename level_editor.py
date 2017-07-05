

# imports
from config import *


# callbacks


# create root widget
root = Tkinter.Tk()
root.title("CME-3000 Level Editor") # window label

# create main frame for other widgets
mainframe = Tkinter.Frame(root, width = 1280, height = 720, bg = "black")
mainframe.pack()

# create Option Menu for background upload

class Listbox():
    # for use in the level editor listoboxes to browse folders and choose files
    def __init__(self, master):
        self.listbox = Tkinter.Listbox(master, selectmode=Tkinter.BROWSE)
        self.listed = helpers.folder_browser()
        self.current = None
        self.entries()
        self.listbox.grid()
        self.poll()

    def entries(self):
        self.listbox.delete(0, Tkinter.END)
        for item in self.listed:
            self.listbox.insert(Tkinter.END, item)

    def poll(self):
        now = self.listbox.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.listbox.after(250, self.poll)


    def list_has_changed(self, selection):
        print "selection is ", selection
        if len(selection) != 0:
            new_path = os.getcwd() + "/Resources/" + self.listbox.get(selection[0])
            print new_path
            #TODO use os.path.isfile here to make branch the flow
            self.listed = helpers.folder_browser(new_path)
            self.entries()

def create_listbox(frame=mainframe):
    lbox = Listbox(frame)

bg_button = Tkinter.Button(mainframe, \
                           text="Push to choose a background image", \
                           command=create_listbox)
bg_button.grid()

root.mainloop()
