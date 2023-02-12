from customtkinter import *
from morsecode import MORSE_CODE_DICT as mcdict

set_appearance_mode("Dark")
set_default_color_theme("dark-blue")




def coder(text):
	code=""
	for char in text.upper():
		try:
			code+=mcdict[char]+" "
		except:
			return "#"
	return code

def when_click():
	mctext.delete(1.0,END)
	mc=coder(text.get(1.0,END))
	
	mctext.insert("0.0",mc[0:len(mc)-1])



def code():
	root = CTk()
	root.title("CODE")
	root.iconbitmap("morse-code.ico")
	root.geometry("600x600+400+100")
	root.resizable(False,False)


	lbl=CTkLabel(master=root,text="CODE",font=("Broadway",50))
	lbl.place(relx=0.37,rely=0.05)

	txtlbl=CTkLabel(master=root,text="TEXT",font=("Times",20,"italic"))
	txtlbl.place(relx=0.83,rely=0.28)

	global text
	text = CTkTextbox(master=root,width=450,height=150,font=("Times",20))
	text.place(relx=0.07,rely=0.2)



	mclbl=CTkLabel(master=root,text="MORSE CODE",font=("Times",15,"italic"))
	mclbl.place(relx=0.83,rely=0.7)

	global mctext
	mctext = CTkTextbox(master=root,width=450,height=150,font=("Times",20))
	mctext.place(relx=0.07,rely=0.6)

	btn=CTkButton(master=root,text="CODE",font=("Times",35),command=when_click)
	btn.place(relx=0.36,rely=0.90)

	

	root.mainloop()

