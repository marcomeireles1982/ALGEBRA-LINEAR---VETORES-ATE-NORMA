import math
#--------Classe vetor2D
class Vetor2D:
    """_summary_        
    Classe responsável por criar um vetor de 2 dimensões\n
    Parametros exigidos:
        name :  Nome do vetor em formato string
        x    :  Coordenada eixo x em formato inteiro
        y    :  Coordenada eixo y em formato inteiro\n
    
    Exemplo de uso:\n
    
        u = Vetor2D('u',2, 1)  ->  Você acabou de criar um vetor u = (x, y)
    
    """    
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.str = f'{name} = ({x},{y})'
    
    def getName(self)->str:
        """_summary_\n
        Método responsável por retornar o nome do vetor 
        
        Parametro de retorno:\n
            name  :  Nome do vetor em formato string
        
        Exemplo:
        
            u = Vetor2D('u',2, 1)
            print(u.getName())  -> Retorna o nome da matriz 
        """    
        return self.name
    
    def getX(self)->int:
        """_summary_\n
        Método responsável por retornar o parametro do eixo x do vetor 
        
        Parametro de retorno:\n
            x : Valor do eixo x em formato int
    
        Exemplo:
            
            u = Vetor2D('u',2, 1)
            
            print(u.getX())  -> Retorna o valor de x do vetor 
        """   
        return self.x
    
    def getY(self)->int:
        """_summary_\n
        Método responsável por retornar o parametro do eixo y do vetor 
        
        Parametro de retorno:\n
            y : Valor do eixo y em formato int
    
        Exemplo:
        
            u = Vetor2D('u',2, 1)
            
            print(u.getY())  -> Valor do eixo y do vetor
        """   
        return self.y

    def __str__(self)->str:
        """_summary_\n
        Método responsável por retornar dados sobre o vetor criado 
        
        Parametro de retorno:\n
            u   :   Nome do vetor
            x   :   valor da coordenada x do vetor
    
        Exemplo:
        
            u = Vetor2D('u',2, 1)
            print(u.__str__())
        """   
        return self.str

#--------Classe vetor3D
class Vetor3D:
    """_summary_
    Classe responsável por criar um vetor de 3 dimensões\n
    Parametros exigidos:
    
        name :  Nome do vetor em formato string
        x    :  Coordenada eixo x em formato inteiro
        y    :  Coordenada eixo y em formato inteiro        
        z    :  Coordenada eixo z em formato inteiro

    Exemplo de uso:\n
    
        u = Vetor3D('u',2, 1, 1)  ->  Você acabou de criar um vetor u = (x, y, z)
    """
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.str = f'{name} = ({x},{y},{z})'
    
    def getName(self)->str:
        """_summary_\n
        Método responsável por retornar o nome do vetor 
        
        Parametro de retorno:
        
            name  :  Nome do vetor em formato string
        
        Exemplo:
        
            u = Vetor3D('u',2, 1, 3)
            print(u.getName())  -> Retorna o nome da matriz 
        """  
        return self.name
    
    def getX(self):
        """_summary_\n
        Método responsável por retornar o parametro do eixo x do vetor 
        
        Parametro de retorno:\n
            x : Valor do eixo x em formato int
    
        Exemplo:
            
            u = Vetor3D('u',2, 1, 1)
            
            print(u.getX())  -> Retorna o valor de x do vetor 
        """   
        return self.x
    
    def getY(self):
        """_summary_\n
        Método responsável por retornar o parametro do eixo y do vetor 
        
        Parametro de retorno:\n
            y : Valor do eixo y em formato int
    
        Exemplo:
            
            u = Vetor3D('u',2, 1, 1)
            
            print(u.getY())  -> Retorna o valor de y do vetor 
        """   
        return self.y

    def getZ(self):
        """_summary_\n
        Método responsável por retornar o parametro do eixo z do vetor 
        
        Parametro de retorno:\n
            z : Valor do eixo x em formato int
    
        Exemplo:
            
            u = Vetor3D('u',2, 1, 1)
            
            print(u.getZ())  -> Retorna o valor de z do vetor 
        """   
        return self.z

    def __str__(self):
        """_summary_
        
        Método responsável por retornar dados sobre o vetor criado 
        
        Parametro de retorno:
        
            u   :   Nome do vetor
            x   :   valor da coordenada x do vetor
            y   :   valor da coordenada y do vetor
    
        Exemplo:
        
            u = Vetor3D('u',2, 1, 1)
            print(u.__str__())
        """   
        return self.str
    
class Operations:
    """_summary_
    Metodo responsável pelas operações usando os vetores criados
    
    """
    def __init__(self):
        self.str = None
#---Operações vetores em 2 dimensões

    def invert2D(self, v1):
        
        """_summary_
        Método responsável por inverter o sinal dos elementos do vetor

        Returns:
            _Vetor2D_: _description_
            
            Retorna os um Vetor2D com os valores de x e y invertidos
        """
        self.str = f"{v1.getName()} <=> {v1.getName()} = ({v1.getX()* -1}, {v1.getY()* -1})"
        return Vetor2D('i', (v1.getX() * -1), (v1.getY() * -1))
    
    def module2D(self, v1):
        """_summary_
        
        Método responsável por calcular o modulo do Vetor

        Returns:
            _tupla_: _description_
            
            Retornará uma tupla com demonstração do calculo e com o resultado do calculo
            
                obj[0]  -  Demostração do calculo no formato String
                
                obj[1]  - o resultado do cálculo em float caso for continuar usando
            """
        self.str = f"||{v1.getName()}|| = √({v1.getX()**2}+{v1.getY()})"
        return f"||{v1.getName()}|| = √({v1.getX()**2}+{v1.getY()**2})" , (math.sqrt((v1.getX()**2) + (v1.getY()**2)))
    
    def sum2D(self, v1, v2):
        """_summary_
        
        Método responsável por realizar a soma de 2 vetores

        Args:
            v1 (Vetor2D):_description_
            
                Vetor2D  :  Vetor coordenadas x e y

            v2 (_type_): _description_
            
                Vetor2D  :  Vetor coordenadas x e y
                
        Returns:
            _Vetor2D_: _description_
            
                Retorna um Vetor2D com o resultado da soma de 2 vetores de coordenadas x e y
        """
        self.str = f'{v1.getName()} + {v2.getName()} = ({v1.getName()}x + {v2.getName()}x, {v1.getName()}y + {v2.getName()}y) = \n{v1.getName()} + {v2.getName()} = ({v1.getX()} + {v2.getX()}, {v1.getY()} + {v2.getY()})'    
        return Vetor2D('r',v1.getX() + v2.getX(), v1.getY() + v2.getY())

    def sub2D(self, v1, v2):
        """_summary_
        
        Método responsável por realizar a subtração de 2 vetores

        Args:
            v1 (Vetor2D):_description_
            
                Vetor2D  :  Vetor coordenadas x e y

            v2 (_type_): _description_
            
                Vetor2D  :  Vetor coordenadas x e y
                
        Returns:
            _Vetor2D_: _description_
            
                Retorna um Vetor2D com o resultado da subtração de 2 vetores de coordenadas x e y
        """
        self.str = f'{v1.getName()} - {v2.getName()} = ({v1.getName()}x - {v2.getName()}x, {v1.getName()}y - {v2.getName()}y) = \n{v1.getName()} - {v2.getName()} = ({v1.getX()} - {v2.getX()}, {v1.getY()} - {v2.getY()})'    
        return Vetor2D('r',v1.getX() - v2.getX(), v1.getY() - v2.getY())
    
    def multE_2D(self, escalar, v1):
        """_summary_
        
        Método responsável por realizar a multiplicação de um Escalar por um vetor 2D

        Args:
            escalar (int):_description_
            
                int  :  Valor inteiro 

            v1 (Vetor2D): _description_
            
                Vetor2D  :  Vetor coordenadas x e y
                
        Returns:
            _Vetor2D_: _description_
                         
                Retorna um Vetor2D com o resultado da soma de 2 vetores de coordenadas x e y
        """
        self.str = f'{escalar}{v1.getName()} = ({escalar} x {v1.getName()}x, {escalar} x {v1.getName()}y) = \n{escalar}{v1.getName()} = ({escalar} x {v1.getX()}, {escalar} x {v1.getY()})'    
        return Vetor2D('r', escalar * v1.getX(), escalar * v1.getY())

#--Operações vetores em 3 dimensões

    def invert3D(self, v1):
        
        """_summary_
        Método responsável por inverter o sinal dos elementos do vetor

        Returns:
            _Vetor3D_: _description_
            
            Retorna os um Vetor3D com os valores de x e y e z invertidos
        """
        self.str = f"{v1.getName()} <=> {v1.getName()} = ({v1.getX()* -1}, {v1.getY()* -1}, {v1.getZ()* -1})"
        return Vetor3D('i', (v1.getX() * -1), (v1.getY() * -1), (v1.getZ() * -1))
    
    def sum3D(self, v1, v2):
        """_summary_
        
        Método responsável por realizar a soma de 2 vetores

        Args:
            v1 (Vetor3D):_description_
            
                Vetor3D  :  Vetor coordenadas x e y e z

            v2 (Vetor3D): _description_
            
                Vetor3D  :  Vetor coordenadas x e y e z
                
        Returns:
            _Vetor3D_: _description_
            
                Retorna um Vetor3D com o resultado da soma de 2 vetores de coordenadas x e y e z
        """

        self.str = f'{v1.getName()} + {v2.getName()} = ({v1.getName()}x + {v2.getName()}x, {v1.getName()}y + {v2.getName()}y, {v1.getName()}z + {v2.getName()}z) = \n{v1.getName()} + {v2.getName()} = ({v1.getX()} + {v2.getX()}, {v1.getY()} + {v2.getY()}, {v1.getZ()} + {v2.getZ()})'    
        return Vetor3D('r',v1.getX() + v2.getX(), v1.getY() + v2.getY(), v1.getZ() + v2.getZ()) 

    def sub3D(self, v1, v2):
        """_summary_
        
        Método responsável por realizar a subtração de 2 vetores

        Args:
            v1 (Vetor3D):_description_
            
                Vetor3D  :  Vetor coordenadas x e y e z

            v2 (Vetor3D): _description_
            
                Vetor3D  :  Vetor coordenadas x e y e z
                
        Returns:
            _Vetor3D_: _description_
            
                Retorna um Vetor3D com o resultado da subtração de 2 vetores de coordenadas x e y e z
        """
        self.str = f'{v1.getName()} - {v2.getName()} = ({v1.getName()}x - {v2.getName()}x, {v1.getName()}y - {v2.getName()}y, {v1.getName()}z - {v2.getName()}z) = \n{v1.getName()} - {v2.getName()} = ({v1.getX()} - {v2.getX()}, {v1.getY()} - {v2.getY()}, {v1.getZ()} - {v2.getZ()})'    
        return Vetor3D('r',v1.getX() - v2.getX(), v1.getY() - v2.getY(), v1.getZ() - v2.getZ()) 
    

    def multE_3D(self, escalar, v1):
        """_summary_
        
        Método responsável por realizar a multiplicação de um Escalar por um vetor 3D

        Args:
            escalar (int):_description_
            
                int  :  Valor inteiro 

            v1 (Vetor3D): _description_
            
                Vetor3D  :  Vetor coordenadas x e y e z
                
        Returns:
            _Vetor3D_: _description_
                         
                Retorna um Vetor2D com o resultado da soma de 2 vetores de coordenadas x e y e z
        """
        self.str = f'{escalar}{v1.getName()} = ({escalar} x {v1.getName()}x, {escalar} x {v1.getName()}y, x {v1.getName()}z) = \n{2}{v1.getName()} = ({escalar} x {v1.getX()}, {escalar} x {v1.getY()}, {escalar} x {v1.getZ()})'    
        return Vetor3D('r', escalar * v1.getX(), escalar * v1.getY(), escalar * v1.getZ())

    def module3D(self, v1):
        """_summary_
        
        Método responsável por calcular o modulo do Vetor

        Returns:
            _tupla_: _description_
            
            Retornará uma tupla com demonstração do calculo e com o resultado do calculo
            
                obj[0]  -  Demostração do calculo no formato String
                
                obj[1]  - o resultado do cálculo em float caso for continuar usando
            """
        self.str = f"||{v1.getName()}|| = √({v1.getX()**2}+{v1.getY()}+{v1.getZ()})"
        return f"|{v1.getName()}| = √({v1.getX()**2}+{v1.getY()**2}+{v1.getZ()**2})" , (math.sqrt((v1.getX()**2) + (v1.getY()**2)+ (v1.getZ()**2)))


    def __str__(self):
        """_summary_
        
        Método responsável por retornar dados sobre o vetor criado 
        
        Parametro de retorno:
        
            u   :   Nome do vetor
            x   :   valor da coordenada x do vetor
            y   :   valor da coordenada y do vetor
    
        Exemplo:
        
            u = Vetor3D('u',2, 1, 1)
            print(u.__str__())
        """
        return self.str