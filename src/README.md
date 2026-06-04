# Visualizador de Vetores 2D e 3D interativo

Este projeto é uma ferramenta interativa desenvolvida em Python para criação, manipulação matemática e visualização gráfica de vetores em duas (2D) e três dimensões (3D). Utilizando o ecossistema interativo do `matplotlib`, a aplicação permite plotar, atualizar e remover pontos/vetores em tempo real através do terminal.

## 🚀 Funcionalidades

- **Representação Algébrica**: Classes dedicadas para objetos `Vetor2D` e `Vetor3D`.
- **Operações Avançadas**: Módulo de operações capaz de calcular soma, subtração, inversão de sinal, multiplicação por escalar e módulo (norma) de vetores.
- **Plotagem Dinâmica Interativa**: 
  - Criação de planos cartesianos customizados em 2D e 3D.
  - Inserção de pontos coloridos identificados com rótulos de suas respectivas coordenadas.
  - Atualização automática e remoção dinâmica de elementos sem a necessidade de fechar a janela gráfica.

## 📦 Estrutura do Projeto

- `vector.py`: Contém as estruturas de dados (`Vetor2D`, `Vetor3D`) e a classe `Operations` com a lógica matemática.
- `plotando.py`: Contém a interface gráfica baseada em Matplotlib (`Plot2D` e `Plot3D`) configurada para modo interativo.

## 🛠️ Pré-requisitos

Antes de executar o projeto, garanta que você possui o Python e a biblioteca `matplotlib` instalados:

```bash
pip install matplotlib