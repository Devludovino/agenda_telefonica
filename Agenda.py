# Agenda.py
# Abrir o tkinter
# Criar uma agenda 
# Conseguir escrever na agenda
# Conseguir editar a agenda

from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

# cores -----------------------------------------

co0 = "#f0f3f5" #Preto
co1 = "#f0f3f5" #cinza/grey
co2 = "#feffff" #branco
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#6f9fbd" #azul
co6 = "#ef5350" #vermelho
co7 = "#93cd95" #verde

# criando janela --------------------------------

janela = Tk ()
janela.title ("Agenda Escritorio")
janela.geometry("500x450")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# frames ----------------------------------------
frame_cima = Frame(janela, width=500, height=50, bg=co5, relief="flat") #CO5 AZUL CLARO, WIDTH = Largura
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_meio = Frame(janela, width=500, height=150, bg=co1, relief="flat")
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=248, bg=co2, relief="flat")
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NSEW)

# Configurando FRAME_cima
l_nome = Label(frame_cima, text="Agenda Telefónica", anchor=NE, font=('Verdana 20 bold'), bg=co5, fg=co1)
l_nome.place(x=8, y=5)

l_linha = Label(frame_cima, text="", width=500, anchor=NE, font=('Verdana 1'), bg=co2, fg=co1)
l_linha.place(x=0, y=46)

# Configurando FRAME_meio
l_linha = Label(frame_meio, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_linha.place(x=10, y=20)
e_nome = Entry(frame_meio, width=25, justify="left", relief=FLAT,font=('',10), highlightthickness=1)
e_nome.place(x=75, y=20)

l_genero = Label(frame_meio, text="Gênero *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_genero.place(x=10, y=50)
c_genero = Combobox(frame_meio, width = 27)
c_genero['value'] = ('', 'Masculino', 'Feminino')
c_genero.place(x=75, y=50)

l_numero = Label(frame_meio, text="Numero *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_numero.place(x=10, y=80)
e_numero = Entry(frame_meio, width=25, justify="left", relief=FLAT, font=('',10), highlightthickness=1)
e_numero.place(x=75, y=80)

l_email = Label(frame_meio, text="E-mail *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=10, y=110)
e_email = Entry(frame_meio, width=25, justify="left", relief=FLAT, font=('',10), highlightthickness=1)
e_email.place(x=75, y=110)

l_Procurar = Button(frame_meio, text="Procurar *", font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
l_Procurar.place(x=290, y=20)
e_Procurar = Entry(frame_meio, width=18, justify="left", relief=FLAT, font=('',10), highlightthickness=1)
e_Procurar.place(x=360, y=21)

l_ver = Button(frame_meio, width=10, text="Ver dados", font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
l_ver.place(x=290, y=50)

l_adicionar = Button(frame_meio, width=10, text="Adicionar", font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
l_adicionar.place(x=400, y=50)

l_atualizar = Button(frame_meio, width=10, text="Atualizar", font=('Ivy 8 bold'), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
l_atualizar.place(x=400, y=80)

l_deletar = Button(frame_meio, width=10, text="Deletar", font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
l_deletar.place(x=400, y=110)

# Configurando FRAME tabela ----------------------
dados_h = ['Nome', 'Genero', 'Numero','Email']

dados = [['joao','Masculino','1234','FJFJFJ']]

tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show="headings")
# vertical scrollbar
vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
# horizontal scrollbar
hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')


# tree cabecalho
tree.heading(0,text='Nome', anchor=NW)
tree.heading(1,text='Genero', anchor=NW)
tree.heading(2,text='Numero', anchor=NW)
tree.heading(3,text='Email', anchor=NW)

# tree  corpo
tree.column(0, width=120,anchor='nw')
tree.column(1, width=50,anchor='nw')
tree.column(2, width=100,anchor='nw')
tree.column(0, width=120,anchor='nw')


for item in dados:
    tree.insert('', 'end', values=item)



# manter janela aberta --------------------------
janela.mainloop()# Agenda.py
