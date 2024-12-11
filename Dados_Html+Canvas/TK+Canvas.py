import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def extrair():
    n1 = float(entry1.get()) 
    n2 = float(entry2.get())
    n3 = float(entry3.get())
    n4 = float(entry4.get())

    labe_list = ['a','b','c','d']
    lista = [n1,n2,n3,n4]

    fig, grafico = plt.subplots()
    fig, grafico2 = plt.subplots()
    grafico2.plot(labe_list,lista)
    grafico.bar(labe_list,lista)

    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.LEFT ,fill = tk.BOTH, expand = True)

def extrair2():
    n1 = float(entry1.get()) 
    n2 = float(entry2.get())
    n3 = float(entry3.get())
    n4 = float(entry4.get())

    labe_list = ['a','b','c','d']
    lista = [n1,n2,n3,n4]

    fig, grafico2 = plt.subplots()
    grafico2.bar(labe_list,lista)

    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT,fill = tk.BOTH, expand = True)

janela = tk.Tk()
janela.title('Gráfico')

janela.geometry('500x500')

titulo = tk.Label(janela, text = "Gráficos")
titulo.pack()

entry1 = tk.Entry(janela)
entry1.pack()

entry2 = tk.Entry(janela)
entry2.pack()

entry3 = tk.Entry(janela)
entry3.pack()

entry4 = tk.Entry(janela)
entry4.pack()


btn = tk.Button(janela, text = "Gráfico 1", command = extrair)
btn.pack()
btn = tk.Button(janela, text = "Gráfico 2", command = extrair2)
btn.pack()


janela.mainloop()