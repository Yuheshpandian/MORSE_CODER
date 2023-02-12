from customtkinter import *
import code
import decode

set_appearance_mode("Dark")
set_default_color_theme("green")

root = CTk()
root.title("MORSE_CODER")
root.iconbitmap("morse-code.ico")
root.geometry("600x600+400+100")
root.resizable(False,False)



def open_code():
	set_default_color_theme("dark-blue")
	code.code()

def open_decode():
	set_default_color_theme("blue")
	decode.decode()



lbl = CTkLabel(master=root,text="MORSE CODER",font=("Broadway",50))
lbl.place(relx=0.2,rely=0.05)

code_btn=CTkButton(master=root,text="CODE",font=("Times",45),command=open_code)
code_btn.place(relx=0.38,rely=0.3)

decode_btn=CTkButton(master=root,text="DECODE",font=("Times",30),command=open_decode)
decode_btn.place(relx=0.38,rely=0.6)


if __name__=="__main__":
	root.mainloop()
