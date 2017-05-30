from CFR_API import *
from tkinter import *
import threading

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
scene = "MainMenu"
photo = 0
imageLabel = 0

class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.g_Tk.quit()

    def change_scene(self, path):
        global imageLabel
        img = PhotoImage(file=path)
        imageLabel.configure(image=img)
        imageLabel.image = img

    def mouse(self, event):
        global scene
        if event.x < 300:
            scene = "waiting"
            self.change_scene(scene+".gif")

    def run(self):
        global scene, photo, imageLabel, b1

        self.g_Tk = Tk()
        self.g_Tk.wm_title("Project_CFR")
        SetCenter = (self.g_Tk.winfo_screenwidth() // 2) - 450
        self.g_Tk.geometry("{0}x{1}+{2}+0".format(WINDOW_WIDTH, WINDOW_HEIGHT, SetCenter))
        self.g_Tk.protocol("WM_DELETE_WINDOW", self.callback)
        self.g_Tk.bind("<Button-1>", self.mouse)

        # scene
        photo = PhotoImage(file="MainMenu.gif")
        imageLabel = Label(self.g_Tk, image=photo)
        imageLabel.pack()

        self.g_Tk.mainloop()


if __name__ == "__main__":
    app = App()
    CFR_Process()





