

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
        self.current = os.getcwd() + "/Resources/"
        self.entries()
        self.listbox.grid()
        self.poll()

    def entries(self):
        self.listbox.delete(0, Tkinter.END)
        for item in self.listed:
            self.listbox.insert(Tkinter.END, item)

    def poll(self):
        now = self.listbox.curselection()

        if now != self.current and now != ():
            if os.path.isdir(self.current+self.listbox.get(now[0])):
                self.current = self.current + self.listbox.get(now[0]) + "/"
                self.listed = helpers.folder_browser(self.current)
                self.entries()
            else:
                filename = self.listbox.get(now[0])
                self.current = self.current + filename
                self.instantiate_canvas(self.current, filename)
                return 0
        self.listbox.after(250, self.poll)


    def instantiate_canvas(self, sel_path, file):
        print "selection is ", sel_path
        print "Instantiate ", file,  "please"
        trunc_path = sel_path[0:len(sel_path)-len(file)]
        print "Truncated path is: " + trunc_path

        #TODO make a decision button: either pick bg or continue browsing

        yes_button = Tkinter.Button(mainframe,
                                    text="Pick this file?" + str(self.current),
                                    command=fill_background)
        no_button = Tkinter.Button(mainframe,
                                   text="Continue browsing",
                                   command=self.poll)
        #TODO use the trunc_path to browse from the one-up level
        yes_button.grid()
        no_button.grid()


def fill_background():
    print "Filling background"


def create_listbox(frame=mainframe):
    lbox = Listbox(frame)

bg_button = Tkinter.Button(mainframe, \
                           text="Push to choose a background image", \
                           command=create_listbox)
bg_button.grid()

root.mainloop()
