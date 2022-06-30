from email.mime import message
from itertools import count
from tkinter import *
from tkinter import messagebox
from turtle import right

color1 = "#C84B31"
color2 = "#2D4263"
color3 = "#ECDBBA"
fontF  = "Fixedsys"
title_size = 40
i = 0

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

def et_conf(x, y = 20, c =0):
    x.config(
        fg = color1,
        bg = color3,
        font = (fontF,y),
        padx = c
    )
def buttons_conf(x, y = 10, z = 10):
    x.config(
        fg = color3,
        bg = color1,
        pady=10,
        padx=z,
        font = (fontF, y),
        activebackground= color2,
        activeforeground= color3,
    )

def validar():
    if in_entry.get()=="123456":
        print("[+ Ingreso a apps]")
        apps()
    else:
        in_entry.delete("0","end")
        messagebox.showinfo(title ="Error", message = "Clave incorrecta")

def añadir():
    if len(co_entry1.get()) > 1 and len(co_entry2.get()) > 1:
        a = f"{co_entry1.get()} : {co_entry2.get()}" 
        print(a)
        if l1.cget("text") == "Vacio":
            l1.config(
                text= a
            )
        elif l2.cget("text") == "Vacio":
            l2.config(
                text= a
            )
        elif l3.cget("text") == "Vacio":
            l3.config(
                text= a
            )
        elif l4.cget("text") == "Vacio":
            l4.config(
                text= a
            )
        elif l5.cget("text") == "Vacio":
            l5.config(
                text= a
            )
        elif l6.cget("text") == "Vacio":
            l6.config(
                text= a
            )
        elif l7.cget("text") == "Vacio":
            l7.config(
                text= a
            )
        elif l8.cget("text") == "Vacio":
            l8.config(
                text= a
            )
        elif l9.cget("text") == "Vacio":
            l9.config(
                text= a
            )
        elif l10.cget("text") == "Vacio":
            l10.config(
                text= a
            )
        co_entry1.delete("0","end")
        co_entry2.delete("0","end")
    else:
        messagebox.showinfo(title="Error",message="Los datos no son validos")
        
#pantallas
def Inicio():
    try:
        ventana.iconbitmap(bitmap= "./permanente 3b/Telefono.ico")
    except :
        pass
    et_conf(in_label,title_size,60)
    et_conf(in_label2)
    et_conf(in_label3)
    et_conf(in_label4)
    in_entry.config(
        fg = color1,
        show= "*",
        bg = color3,
        font= (fontF, 24),
        justify= "center"
    )
    buttons_conf(in_button,20,30)


    in_label.grid(row=0, column=1, pady=15)
    in_label2.grid(row=1, column=1)
    in_label3.grid(row=2, column=1)
    in_label4.grid(row=3, column=1)
    in_entry.grid(row = 4, column=1,pady=40)
    in_button.grid(row=5, column=1)

    

    ca_label.grid_remove()
    co_label.grid_remove()
    ap_label.grid_remove()
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    b7.grid_remove()
    b8.grid_remove()
    b9.grid_remove()
    b10.grid_remove()
    b11.grid_remove()
    b12.grid_remove()
    b13.grid_remove()
    b14.grid_remove()
    b15.grid_remove()
    b16.grid_remove()
    b17.grid_remove()
    b18.grid_remove()
    button_return.grid_remove()
    button_return2.grid_remove()
    ca_entry.grid_remove()
    l1.grid_remove()
    l2.grid_remove()
    l3.grid_remove()
    l4.grid_remove()
    l5.grid_remove()
    l6.grid_remove()
    l7.grid_remove()
    l8.grid_remove()
    l9.grid_remove()
    l10.grid_remove()
    co_label3.grid_remove()
    co_entry2.grid_remove()
    co_label2.grid_remove()
    co_entry1.grid_remove()
    co_button.grid_remove()
def Calculadora():
    try:
        ventana.iconbitmap(bitmap= "./permanente 3b/Calculadora.ico")
    except :
        pass
    ventana.title("Calculadora")
    et_conf(ca_label,title_size + 10, 0)
    ca_entry.config(
        font=("Arial", 27), 
        fg = color3,
        bg = color2,
        justify= "right",
    )

    ca_label.grid(row=0, column=1,columnspan=4)
    ca_entry.grid(row=1, column=1,columnspan=4)
    b1.grid( column= 1 ,row=2,pady =10)
    b2.grid( column= 2 ,row=2,pady =10)
    b3.grid( column= 3 ,row=2,pady =10)
    b4.grid( column= 4 ,row=2,pady =10)
    b5.grid( column= 1 ,row=3,pady =10)
    b6.grid( column= 2 ,row=3,pady =10)
    b7.grid( column= 3 ,row=3,pady =10)
    b8.grid( column= 4 ,row=3,pady =10)
    b9.grid( column= 1 ,row=4,pady =10)
    b10.grid( column= 2 ,row=4,pady =5)
    b11.grid( column= 3 ,row=4,pady =5)
    b12.grid( column= 4 ,row=4,pady =5)
    b13.grid( column= 1 ,row=5,pady =5)
    b14.grid( column= 2 ,row=5,pady =5)
    b15.grid( column= 3 ,row=5,pady =5)
    b16.grid( column= 4 ,row=5,pady =5)
    b17.grid( column= 1 ,row=6,pady =5,columnspan=2)
    b18.grid( column= 3 ,row=6,pady =5,columnspan=2)
    button_return.grid(column= 1 ,row=7,columnspan=4)

    in_label.grid_remove()
    in_label2.grid_remove()
    in_label3.grid_remove()
    in_label4.grid_remove()
    co_label.grid_remove()
    ap_label.grid_remove()
    in_entry.grid_remove()
    in_button.grid_remove()
    ap_button1.grid_remove()
    ap_button2.grid_remove()
    button_return2.grid_remove()
    ap_button3.grid_remove()
    l1.grid_remove()
    l2.grid_remove()
    l3.grid_remove()
    l4.grid_remove()
    l5.grid_remove()
    l6.grid_remove()
    l7.grid_remove()
    l8.grid_remove()
    l9.grid_remove()
    l10.grid_remove()
    co_label3.grid_remove()
    co_entry2.grid_remove()
    co_label2.grid_remove()
    co_entry1.grid_remove()
    co_button.grid_remove()

def apps():
    try:
        ventana.iconbitmap(bitmap= "./permanente 3b/Telefono.ico")
    except:
        pass
    et_conf(ap_label,title_size,35)
    buttons_conf(ap_button1,20,20)
    buttons_conf(ap_button2,20,40)
    buttons_conf(ap_button3,20, 60)

    ap_label.grid(row=0, column=1,pady=20)
    ap_button1.grid(row=1,column=1, pady = 20)
    ap_button2.grid(row=2,column=1, pady = 20)
    ap_button3.grid(row=3,column=1, pady = 20)


    in_label.grid_remove()
    in_label2.grid_remove()
    in_label3.grid_remove()
    in_label4.grid_remove()
    in_entry.grid_remove()
    in_button.grid_remove()
    ca_label.grid_remove()

    co_label.grid_remove()

    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    b7.grid_remove()
    b8.grid_remove()
    b9.grid_remove()
    b10.grid_remove()
    b11.grid_remove()
    b12.grid_remove()
    b13.grid_remove()
    b14.grid_remove()
    b15.grid_remove()
    b16.grid_remove()
    b17.grid_remove()
    b18.grid_remove()
    ca_entry.grid_remove()
    button_return.grid_remove()
    button_return2.grid_remove()
    l1.grid_remove()
    l2.grid_remove()
    l3.grid_remove()
    l4.grid_remove()
    l5.grid_remove()
    l6.grid_remove()
    l7.grid_remove()
    l8.grid_remove()
    l9.grid_remove()
    l10.grid_remove()
    co_label3.grid_remove()
    co_entry2.grid_remove()
    co_label2.grid_remove()
    co_entry1.grid_remove()
    co_button.grid_remove()

def Contactos():
    try:
        ventana.iconbitmap(bitmap= "./permanente 3b/Contactos.ico")
    except :
        pass
    co_label.config(
        fg = color1,
        bg = color3,
        font = (fontF,title_size),
        padx=80
    )
    co_entry1.config(
        font=("Arial", 10), 
        fg = color3,
        bg = color2,
        justify= "center",
    )
    co_entry2.config(
        font=("Arial", 10), 
        fg = color3,
        bg = color2,
        justify= "center",
    )
    et_conf(co_label2,10)
    et_conf(co_label3,10)
    buttons_conf(co_button)
    et_conf(l1,10)
    et_conf(l2,10)
    et_conf(l3,10)
    et_conf(l4,10)
    et_conf(l5,10)
    et_conf(l6,10)
    et_conf(l7,10)
    et_conf(l8,10)
    et_conf(l9,10)
    et_conf(l10,10)

    co_label.grid(row=0, column=0, columnspan=2)
    co_label2.grid(row=1, column=0, pady=10)
    co_entry1.grid(row=1, column=1, pady=10)
    co_label3.grid(row=2, column=0, pady=10)
    co_entry2.grid(row=2, column=1, pady=10)
    co_button.grid(row=3,column=0, columnspan=2,pady=15)
    l1.grid(row=4, column=0)
    l2.grid(row=5, column=0)
    l3.grid(row=6, column=0)
    l4.grid(row=7, column=0)
    l5.grid(row=8, column=0)
    l6.grid(row=9, column=0)
    l7.grid(row=10, column=0)
    l8.grid(row=11, column=0)
    l9.grid(row=12, column=0)
    l10.grid(row=13, column=0)


    button_return.grid(column= 0 ,row=14, columnspan=2,pady=20)

    in_button.grid_remove()
    in_entry.grid_remove()
    in_label.grid_remove()
    in_label2.grid_remove()
    in_label3.grid_remove()
    in_label4.grid_remove()
    ca_label.grid_remove()
    ap_label.grid_remove()    
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    b7.grid_remove()
    b8.grid_remove()
    b9.grid_remove()
    b10.grid_remove()
    b11.grid_remove()
    b12.grid_remove()
    b13.grid_remove()
    b14.grid_remove()
    b15.grid_remove()
    b16.grid_remove()
    b17.grid_remove()
    b18.grid_remove()
    ca_entry.grid_remove()
    ap_button1.grid_remove()
    ap_button2.grid_remove()
    ap_button3.grid_remove()


clave = NONE

#funciones calculadora
def obtener(dato):
	global i
	i+=1
	ca_entry.insert(i, dato)
	
def operacion():
	global i

	ecuacion = ca_entry.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			ca_entry.delete(0,END)
			ca_entry.insert(0,result)
			longitud = len(result)
			i = longitud

		except:
			result = 'ERROR'
			ca_entry.delete(0,END)
			ca_entry.insert(0,result)
	else:
		pass

def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		ca_entry.delete(i,last =None)
		i-=1
		
def borrar_todo():
	ca_entry.delete(0, END)	
	i=0



ventana = Tk()

ventana.geometry("450x650")
ventana.title("Telefono")
ventana.config(
    bg  = color3
)
# ventana.resizable(width = 0, height = 0)

#inicio
in_label  = Label(ventana, text= "Bienvenido")
in_label2 = Label(ventana, text="Porfavor ingrese")
in_label3 = Label(ventana, text="su clave")
in_label4 = Label(ventana, text="|\n\/")
in_entry = Entry(ventana, textvariable= clave)
in_button = Button(ventana, text= "Validar", command=validar)

#menu-principal
ap_label = Label(ventana, text ="Aplicaciones")
ap_button1 = Button(ventana, text = "Calculadora", command=Calculadora)
ap_button2 = Button(ventana, text = "Contactos", command=Contactos)
ap_button3 = Button(ventana, text = "Apagar", command= ventana.quit)



# Calculadora
ca_label  = Label(ventana, text= "Calculadora")
ca_entry = Entry(ventana)

# Botones
b1 = HoverButton(ventana, text= "1", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(1),fg= "white")  
b2 = HoverButton(ventana, text= "2", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(2),fg= "white")  
b3 = HoverButton(ventana, text= "3", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(3),fg= "white")  
b4 = HoverButton(ventana, text= "<=", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: borrar_uno(),fg= "white") 
b5 = HoverButton(ventana, text= "4", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(4),fg= "white")  
b6 = HoverButton(ventana, text= "5", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(5),fg= "white")  
b7 = HoverButton(ventana, text= "6", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(6),fg= "white")  
b8 = HoverButton(ventana, text= "+", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener("+"),fg= "white")  
b9 = HoverButton(ventana, text= "7", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(7),fg= "white")  
b10 = HoverButton(ventana, text= "8", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(8),fg= "white")  
b11 = HoverButton(ventana, text= "9", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(9),fg= "white")  
b12 = HoverButton(ventana, text= "-", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener("-"),fg= "white")
b13 = HoverButton(ventana, text= "0", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener(0),fg= "white")  
b14 = HoverButton(ventana, text= ".", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener("."),fg= "white")  
b15 = HoverButton(ventana, text= "/", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener("/"),fg= "white")  
b16 = HoverButton(ventana, text= "x", borderwidth=2, height=2, width=5, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: obtener("*"),fg= "white")
b17 = HoverButton(ventana, text= "=", borderwidth=2, height=2, width=15, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: operacion(),fg= "white")
b18 = HoverButton(ventana, text= "C", borderwidth=2, height=2, width=15, font= ("Arial",16), activebackground=color1, bg =color2, command=lambda: borrar_todo(),fg= "white")

# Boton de Regreso
button_return = HoverButton(ventana, text = "Regresar", borderwidth=2, height=2, width=30, font= ("Arial",16), activebackground=color1, bg =color2, command=apps,fg= "white")
button_return2 = HoverButton(ventana, text = "Regresar", borderwidth=2, height=2, width=30, font= ("Arial",16), activebackground=color1, bg =color2, command=apps,fg= "white")

# Contactos
co_label  = Label(ventana, text= "Contactos")
co_button = Button(ventana, text = "Añadir", command= añadir)

co_label2 = Label(ventana, text="Datos")
co_entry1 = Entry()

co_label3 = Label(ventana, text="Numero")
co_entry2 = Entry()

# Campos para añadir
l1 = Label(ventana, text = "Vacio")
l2 = Label(ventana, text = "Vacio")
l3 = Label(ventana, text = "Vacio")
l4 = Label(ventana, text = "Vacio")
l5 = Label(ventana, text = "Vacio")
l6 = Label(ventana, text = "Vacio")
l7 = Label(ventana, text = "Vacio")
l8 = Label(ventana, text = "Vacio")
l9 = Label(ventana, text = "Vacio")
l10 = Label(ventana, text = "Vacio")


Inicio()

# Menu 
menuSup = Menu(ventana)
menuSup.add_command(label="Inicio", command=Inicio)
menuSup.add_command(label="Calculadora", command=Calculadora)
menuSup.add_command(label="Contacto", command=Contactos)
menuSup.add_command(label="Apagar", command=ventana.quit)

ventana.config(menu=menuSup)

ventana.mainloop()