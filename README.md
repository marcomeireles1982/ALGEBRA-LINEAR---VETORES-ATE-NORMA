# Biblioteca para Operações com Vetores

Uma biblioteca simples em Python desenvolvida em Orientação a Objetos para a criação, manipulação e realização de operações matemáticas estruturadas com vetores bidimensionais (2D) e tridimensionais (3D). Ideal para estudos de Álgebra Linear e Geometria Analítica.

## 🚀 Funcionalidades

* **Vetor2D & Vetor3D**: Classes dedicadas para modelagem de vetores com propriedades de nome e coordenadas.
* **Operações Suportadas**:
    * Soma de vetores (`sum2D` / `sum3D`)
    * Subtração de vetores (`sub2D` / `sub3D`)
    * Multiplicação por um escalar (`multE_2D` / `multE_3D`)
    * Cálculo de Módulo/Norma (`module2D` / `module3D`)
    * Inversão de sentido (`invert2D` / `invert3D`)

---

## 💻 Como Usar

### Pré-requisitos
Apenas o **Python 3.x** instalado. Não há dependências externas.

### Exemplo Prático

```python
from vector import Vetor2D, Vetor3D, Operations

# Instanciando o gerenciador de operações
ops = Operations()

# --- Operações em 2D ---
u = Vetor2D('u', 3, 4)
v = Vetor2D('v', 1, 2)

# Soma
resultado_soma = ops.sum2D(u, v)
print(resultado_soma) # Saída: r = (4,6)

# Módulo (Norma)
demonstracao, valor = ops.module2D(u)
print(demonstracao)   # Saída: ||u|| = √(3²+4²)
print(valor)          # Saída: 5.0

# --- Operações em 3D ---
a = Vetor3D('a', 2, 4, 4)
demonstracao_3d, valor_3d = ops.module3D(a)
print(valor_3d)       # Saída: 6.0