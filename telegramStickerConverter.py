from tkinter import *
from tkinter import filedialog
from ttkthemes import themed_tk as tk
from PIL import Image
from tkinter import messagebox
import os

def add_images():
    images = filedialog.askopenfilenames(title='Select Images', filetypes=(('PNG files', '*.png'), ('JPG files', '*.jpg'), ('JPEG files', '*.jpeg')))
    for image in images:
        file_box.insert(END, image)

def delete():
    for item in reversed(file_box.curselection()):
        file_box.delete(item)

def convert():
    list_of_addresses = []
    file_box.select_set(0, END)
    for item in file_box.curselection():
        list_of_addresses.append(str(file_box.get(item)))
        for i in range(len(list_of_addresses)):
            img = Image.open(list_of_addresses[i])
            resized_img = img.resize((512, 512)) # WIDTH, HEIGHT
            filename = os.path.basename(list_of_addresses[i])
            if filename.endswith('.png'):
                pass
            elif filename.endswith('.jpeg'):
                filename = filename[:-4]+'png'
            else:
                filename = filename[:-3]+'png'
                
            resized_img.save(filename)
            messagebox.showinfo("Image Successfully Converted", "Your image was successfully converted to 512x512.\nCheck the folder where this program is located.")

screen = tk.ThemedTk()
screen.get_themes()
screen.set_theme("breeze")

width_of_window = 600
height_of_window = 440
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
x_coordinate = int((screen_width/2) - (width_of_window/2))
y_coordinate = int((screen_height/2) - (height_of_window/2))
screen.geometry("{}x{}+{}+{}".format(width_of_window, height_of_window, x_coordinate, y_coordinate))

screen.title('Telegram Sticker Converter')
screen.iconbitmap('telegram.ico')
screen.config(background='#0088cc')

list_frame = Frame(screen)
list_frame.config(background='#0088cc')
my_scrollbar = Scrollbar(list_frame, orient=VERTICAL)
file_box = Listbox(list_frame, width=400, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)
my_scrollbar.config(command=file_box.yview)
my_scrollbar.pack(side=RIGHT, fill=Y, pady=15)
list_frame.pack(padx=30)
file_box.pack(pady=15)

button_select = Button(screen, text='Select Files', command=add_images, background='white', fg='black', font=('Helvetica', 16), borderwidth=5)
button_select.pack(pady=15)

button_delete = Button(screen, text='Delete File', command=delete, background='white', fg='black', font=('Helvetica', 12))
button_delete.pack(pady=15)

button_convert = Button(screen, text='CONVERT', command=convert, background='black', fg='white', font=('Helvetica', 18, 'bold'), borderwidth=6)
button_convert.pack(pady=15)

screen.mainloop()
