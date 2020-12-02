import tkinter as tk
from PIL import Image, ImageTk

def main():

    images = [
        ("Mu'er",'muer_small.jpg'),
        ('Noodles','noodles_small.jpg'),
        ('FriedPotatoes','Bratkartoffeln_small.jpg'),
    ]
    app = App(left_gallery=images, right_gallery=images)
    app.mainloop()

class App(tk.Tk):
    def __init__(self, left_gallery, right_gallery):
        super().__init__()
        self.geometry("400x400")
        self.left_gallery = Gallery(master=self, images=left_gallery)
        self.left_gallery.grid(column=0, row=0, sticky='nsew')

        self.right_gallery = Gallery(master=self, images=right_gallery)
        self.right_gallery.grid(column=1, row=0, sticky='nsew')



class Gallery(tk.Frame):
    def __init__(self, master, images):
        super().__init__(master, height="300", width="200")
        self.master = master
        self.images = images
        self.cur_image = 0

        load = Image.open(self.images[self.cur_image][1])
        render = ImageTk.PhotoImage(load)
        self.img = tk.Label(self, image=render)
        self.img.image = render
        self.img.grid(column=0, row=0)

        self.control = ControlPanel(self)
        self.control.grid(column=0, row=1)

    def update_image(self):
        load = Image.open(self.images[self.cur_image][1])
        render = ImageTk.PhotoImage(load)
        self.img.destroy()
        self.img = tk.Label(self, image=render)
        self.img.image = render
        self.img.grid(row=0, column=0)



class ControlPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height="100", width="100")
        self.master = master

        self.left = tk.Button(
            self,
            text="<",
            fg='red',
            font=('', 11, 'bold'),
            command=self.left
        )
        self.left.pack(side=tk.LEFT)

        self.image_name=tk.Label(
            self,
            text=self.master.images[self.master.cur_image][0],
            font=('', 10,'bold')
            )
        self.image_name.pack(side=tk.LEFT)

        self.right = tk.Button(
            self,
            text=">",
            fg='red',
            font=('', 11, 'bold'),
            command=self.right
        )
        self.right.pack(side=tk.LEFT)

    def left(self):
        self.master.cur_image = (self.master.cur_image - 1) % len(self.master.images)
        self.image_name.config(
            text=self.master.images[self.master.cur_image][0]
        )
        self.master.update_image()

    def right(self):
        self.master.cur_image = (self.master.cur_image + 1) % len(self.master.images)
        self.image_name.config(
            text=self.master.images[self.master.cur_image][0]
        )
        self.master.update_image()


if __name__ == '__main__':
    main()
