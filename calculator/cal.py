import tkinter as tk
import time
from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer
import os
import fnmatch
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
from PIL import Image


light_gray='#F5F5F5'
label_colour='#25265E'
white='#FFF'
col='#90EE90'
col1='#6495ED'
off_white='#F8FAFF'
light_blue='#CCEDFF'
pink_sand='#ffa8B6'

small_font_style=('Arial',16)
large_font_style=('Arial',40,'bold')
digits_font_style=('Arial',24,'bold')
default_font_style=('Arial',20)




class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("475x667")
        self.window.title('Calculator')

        self.total_expression=''
        self.current_expression=''

        self.display_frame=self.create_display_frame()
        self.total_label,self.label=self.create_display_labels()
        self.buttons_frame=self.create_buttons_frame()

        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),'.':(4,1)
        }
        
        
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)


        self.operations={"/":'\u00F7',"*":'\u00D7','-':'-','+':'+'}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()


        #logo
        image_icon=PhotoImage(file='logo.png')
        self.window.iconphoto(False,image_icon)


    def bind_keys(self):
        self.window.bind('<Return>',lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event,digit=key:self.put_to_expression(digit))
        
        for key in self.operations:
            self.window.bind(key,lambda event,operator=key: self.append_operator(operator))
        
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_square_root_button()



    def create_display_labels(self):
        total_label=tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=pink_sand,fg=label_colour,padx=24,font=small_font_style)
        total_label.pack(expand=True,fill='both')

        label=tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,bg=pink_sand,fg=label_colour,padx=24,font=large_font_style)
        label.pack(expand=True,fill='both')

        return total_label,label

    
    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221,bg=light_gray)
        frame.pack(expand=True,fill="both")
        return frame
    

    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill='both')
        return frame
    

    def put_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()
    

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame,text=str(digit),bg=light_blue,fg=label_colour,font=digits_font_style,borderwidth=0,command=lambda x=digit:self.put_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)


    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=''
        self.update_total_label()
        self.update_label()


    def create_operator_buttons(self):
       i=0
       for operator,symbol in self.operations.items():
           button=tk.Button(self.buttons_frame,text=symbol,bg=light_blue,fg=label_colour,font=default_font_style,borderwidth=0,command=lambda x=operator: self.append_operator(x)) 
           button.grid(row=i,column=4,sticky=tk.NSEW)
           i+=1

    def clear(self):
        self.current_expression=''
        self.total_expression=''
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button=tk.Button(self.buttons_frame,text='C',bg=col1,fg=label_colour,font=default_font_style,borderwidth=0,command=self.clear) 
        button.grid(row=0,column=1,sticky=tk.NSEW)


    def square(self):
        self.current_expression=str(eval(f'{self.current_expression}**2'))
        self.update_label()


    def create_square_button(self):
        button=tk.Button(self.buttons_frame,text='x\u00b2',bg=light_blue,fg=label_colour,font=default_font_style,borderwidth=0,command=self.square) 
        button.grid(row=0,column=2,sticky=tk.NSEW)


    def square_root(self):
        self.current_expression=str(eval(f'{self.current_expression}**0.5'))
        self.update_label()


    def create_square_root_button(self):
        button=tk.Button(self.buttons_frame,text='\u221ax',bg=light_blue,fg=label_colour,font=default_font_style,borderwidth=0,command=self.square_root) 
        button.grid(row=0,column=3,sticky=tk.NSEW)


    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()

        try:
            self.current_expression=str(eval(self.total_expression))

            self.total_expression=''
        except Exception as e:
            self.current_expression='Invalid!!'

        finally:
            self.update_label()

        self.update_label()


    def create_equal_button(self):
        button=tk.Button(self.buttons_frame,text='=',bg=col,fg=label_colour,font=default_font_style,borderwidth=0,command=self.evaluate) 
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

    def update_total_label(self):
        global expression
        expression=self.total_expression
        for operator,symbol in self.operations.items():
            expression=expression.replace(operator,f'{symbol}')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])



    

    def run(self):
        self.window.mainloop()


if __name__=='__main__':
    calc=Calculator()
    calc.run()
                                 