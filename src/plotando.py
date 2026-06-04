import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.ticker as ticker  
from vector import *

class Plot3D:
    """_summary_
    Classe responsável por criar o plano cartesiano em 3D (x, y, z)
    
    Parametros Obrigatórios
        x => Limite do plano em x
        y => Limite do plano em y
        z => Limite do plano em z
    
    Exemplo:
        pl = Plot3D(10,10,10)  =>  Abrirá o plano cartesiano com os limites 10, 10 e 10
    """
    
    def __init__(self, x, y, z):
        plt.ion()
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.ax.set_xlim(0, x)
        self.ax.set_ylim(0, y)
        self.ax.set_zlim(0, z)
        
        # Intervalos de 1 em 1 nos 3 eixos
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.zaxis.set_major_locator(ticker.MultipleLocator(1))
        
        self.ax.set_xlabel("Eixo X")
        self.ax.set_ylabel("Eixo Y")
        self.ax.set_zlabel("Eixo Z")
        self.ax.set_title("Plano Cartesiano 3D Ativo", fontsize=13, fontweight='bold')
        
        self.elementos_plotados = {}
        
        plt.pause(0.1)
        print("Janela 3D aberta!")
        print("Comandos: .add(v1, color) e .rem('nome_do_vetor')\n")

    def add(self, v1, color):
        """_summary_
        Método responsável por incluir os vetores no plano cartesiano em 3D (x, y, z)
        
        Parametros Obrigatórios
            v1 => Vetor3D coordenadas x,y,z
            color => Cor do ponto ou pelo nome em ingles ou pelo #RGB
            
        Exemplo:
             pl = Plot3D(10,10,10)
             
             u = Vetor3D('u', 2, 5)
             
             pl.add(u, 'red') ou  pl.add(u, '#093323') 
        """
        nome = v1.getName()    
        if nome in self.elementos_plotados:
            self.rem(nome)
        ponto_grafico = self.ax.plot([v1.getX()], [v1.getY()], [v1.getZ()], marker='o', markersize=10, color=color)[0]
        
        texto_grafico = self.ax.text(v1.getX(), v1.getY(), v1.getZ() + 0.5, 
                                     f"{nome}=({v1.getX()}, {v1.getY()}, {v1.getZ()})", 
                                     ha='center', fontsize=9, fontweight='bold')
        
        self.elementos_plotados[nome] = {
            'ponto': ponto_grafico,
            'texto': texto_grafico
        }
        plt.pause(0.1)

    def rem(self, nvetor):
        """_summary_
        Método responsável por excluir os vetores no plano cartesiano 3D (x, y, z)
        
        Parametros Obrigatórios
            nvetor => nome do vetor em str
            
        Exemplo:
            pl.rem('u')  => remove o vetor u do plano cartesiano
             
        """
        if nvetor in self.elementos_plotados:
            grafico = self.elementos_plotados[nvetor]
            grafico['ponto'].remove()
            grafico['texto'].remove()
            
            del self.elementos_plotados[nvetor]
            
            plt.draw()
            plt.pause(0.1)
            print(f"Ponto '{nvetor}' removido com sucesso.")
        else:
            print(f"Erro: O ponto '{nvetor}' não foi encontrado no gráfico.")
        
class Plot2D:
    """_summary_
    Classe responsável por criar o plano cartesiano em 2D (x, y)
    
    Parametros Obrigatórios
        x => Limite do plano em x
        y => Limite do plano em y
    
    Exemplo:
        pl = Plot2D(10,10)  =>  Abrirá o plano cartesiano com os limites 10 e 10
    """

    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        self.ax.set_xlim(0, self.x_max)
        self.ax.set_ylim(0, self.y_max)
        
        # --- OTIMIZADO: Padronizado com MultipleLocator para evitar quebras de escala ---
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        
        self.ax.axhline(0, color='black', linewidth=1.2)
        self.ax.axvline(0, color='black', linewidth=1.2)
        self.ax.grid(True, linestyle='--', alpha=0.6)
        self.ax.set_title("Plano Cartesiano 2D Ativo")
        self.elementos_plotados = {}
        plt.pause(0.1)
        print(f"Janela 2D ({x_max}x{y_max}) aberta!")
        print("Comandos: .add(v1, cor) ou .rem('nome_do_vetor')\n")

    def add(self, v1, color):
        """_summary_
        Método responsável por incluir os vetores no plano cartesiano em 2D (x, y)
        
        Parametros Obrigatórios
            v1 => Vetor2D coordenadas x,y
            color => Cor do ponto ou pelo nome em ingles ou pelo #RGB
            
        Exemplo:
             pl = Plot2D(10,10)
             
             u = Vetor2D('u', 2, 5)
             
             pl.add(u, 'red') ou  pl.add(u, '#093323') 
        """
        nome = v1.getName()
        if nome in self.elementos_plotados:
            self.rem(nome)
            
        ponto_ref = self.ax.plot(v1.getX(), v1.getY(), marker='o', markersize=8, color=color)[0]
        texto_ref = self.ax.text(v1.getX(), v1.getY() + 0.3, 
                                 f"{nome}=({v1.getX()}, {v1.getY()})", 
                                 ha='center', va='bottom', fontsize=9, color='black')
        self.elementos_plotados[nome] = {
            'ponto': ponto_ref,
            'texto': texto_ref
        }
        plt.pause(0.1)

    def rem(self, nvetor):
        """_summary_
        Método responsável por excluir os vetores no plano cartesiano 3D (x, y)
        
        Parametros Obrigatórios
            nvetor => nome do vetor em str
            
        Exemplo:
            pl.rem('u')  => remove o vetor u do plano cartesiano
             
        """
        if nvetor in self.elementos_plotados:
            elementos = self.elementos_plotados[nvetor]
            elementos['ponto'].remove()
            elementos['texto'].remove()
            del self.elementos_plotados[nvetor]
            plt.draw()
            plt.pause(0.1)
            print(f"Ponto '{nvetor}' removido.")
        else:
            print(f"Vetor '{nvetor}' não encontrado.")

        """
        usar no modo
        
        python -i plotando.py
        
        """