import os.path
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.colorchooser import *
import time
from tkinter import font



def change_color():
    user=askcolor(title='pick a color')
    print(user)
    textarea.config(fg=user[1])

def change_font(*args):
    textarea.config(font=(font_name.get(),size_box.get()))
def new_file():
    textarea.delete(1.0,END)
    window.title('untitled.txt')
def open_file():
    file=askopenfilename(defaultextension='.txt',

                    title='my new file',
                    initialfile='untitled.txt',
                    filetypes=[('all files','.*'),
                               ('python files','.py'),
                               ('corel files','.cdr'),
                               ('html files','.html'),
                               ('css files','.css')])

    try:
        window.title(os.path.basename(file))
        textarea.delete(1.0,END)

        file=open(file,'r')
        textarea.insert(1.0,file.read())
    except Exception:
        print('the file was not found')
    finally:
        file.close()

def save_file():
    file=asksaveasfilename(defaultextension='.txt',
                           initialdir='C:\\Users\\DELL 5470\\PycharmProjects\\pythonProject5',
                    title='my new file',
                    initialfile='untitled.txt',
                    filetypes=[('all files','.*'),
                               ('python files','.py'),
                               ('corel files','.cdr'),
                               ('html files','.html'),
                               ('css files','.css')])

    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file=open(file,'w')
            file.write(str(textarea.get(1.0,END)))
        except Exception:
            print('could not find this file')
        finally:
            file.close()
def cut():
    textarea.event_generate('<<Cut>>')
def copy():
    textarea.event_generate('<<Copy>>')
def paste():
    textarea.event_generate('<<Paste>>')
def about():
    showinfo(title='about this project',message='do you want to continue',icon=WARNING)
def quit():
    window.destroy()

window=Tk()
window.title('text editor program')
window_width=500
window_height=500

font_name=StringVar(window)
font_name.set('Arial')

font_size=StringVar(window)
font_size.set('25')

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))

window.geometry('{}x{}+{}+{}'.format(window_width,window_height,x,y))

textarea=Text(window,font=(font_name.get(),font_size.get()),fg='red',bg='black')
scroll_bar=Scrollbar(textarea)
scroll_bar.pack(side=RIGHT,fill=Y)
textarea.config(yscrollcommand=scroll_bar.set)

window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)

textarea.grid(sticky=N+E+W+S)

frame=Frame(window)
frame.grid()

color_button=Button(frame,text='color picker',command=change_color)
color_button.grid(row=0,column=0)

font_box=OptionMenu(frame,font_name,*font.families(),command=change_font)
font_box.grid(row=0, column=1)

size_box=Spinbox(frame,textvariable=font_size,command=change_font,from_=1,to=100)
size_box.grid(row=0,column=2)

menu_bar=Menu(window)
window.config(menu=menu_bar)

filemenu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='new',command=new_file)
filemenu.add_command(label='open',command=open_file)
filemenu.add_command(label='save',command=save_file)

editmenu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=cut)
editmenu.add_command(label='Copy',command=copy)
editmenu.add_command(label='Paste',command=paste)
editmenu.add_command(label='Quit',command=quit)

aboutmenu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help',menu=aboutmenu)
aboutmenu.add_command(label='About',command=about)
window.mainloop()