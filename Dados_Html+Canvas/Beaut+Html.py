import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bs4 import BeautifulSoup
import pandas as pd

html = '''
<tabel>
    <tr>
        <td>nome</td>
        <td>idade</td>
    </tr>
    <tr>
        <td>Maria</td>
        <td>23</td>
    </tr>
    <tr>
        <td>Caio</td>
        <td>18</td>
    </tr>
    <tr>
        <td>Aline</td>
        <td>15</td>
    </tr>
</tabel>
'''

def extrair():
    soup = BeautifulSoup(html, 'html.parser')
    dados = soup.find('tabel')
    idade = []
    nome = []
    
    linhas = dados.find_all('tr')[1:]
    for linha in linhas:
        n = linha.find_all('td')
        nome.append(n[0].text)
        idade.append(int(n[1].text))
    plt.plot(nome, idade)
    plt.show()

    df = pd.DataFrame(idade)
    estatistica = df.describe()
    text.config(text=estatistica)


janela = tk.Tk()

text = tk.Label(janela, text = '')
text.pack()


btn = tk.Button(janela, text = "Gráfico 1", command = extrair)
btn.pakc()

janela.mainloop()