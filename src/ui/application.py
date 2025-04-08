from tkinter import Tk, ttk, filedialog, StringVar

class Application:

    def __init__(self):
        self.window = Tk()
        self.window.title("Test")
        self.window.minsize(500, 300)

        self.entry_text = StringVar()
        self.entry = None

        self.setup()


    def start(self):
        self.window.mainloop()

    def setup(self):

        entry = ttk.Entry(master=self.window, textvariable=self.entry_text)
        label = ttk.Label(master=self.window, text="Enter path")
        select_folder = ttk.Button(master=self.window, text="Folder", command=self.handle_select_folder)
        select_file = ttk.Button(master=self.window, text="File", command=self.handle_select_file)
        button = ttk.Button(master=self.window, text="Run", command=self.handle_button)

        label.pack()
        entry.pack()
        select_folder.pack()
        select_file.pack()
        button.pack()

    def handle_select_folder(self):
        self.entry_text.set(filedialog.askdirectory())

    def handle_select_file(self):
        self.entry_text.set(filedialog.askopenfilename())

    def handle_button(self):
        print(self.entry_text.get())
        pass