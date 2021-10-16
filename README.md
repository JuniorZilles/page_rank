# Trabalho de Introdução a Recuperação de Informação PAGE RANK

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

O objetivo geral deste trabalho é aplicar os conhecimentos adquiridos em aula para a implementação do algoritmo Page Rank. A aplicação possui 2 objetivos específicos que serão avaliados separadamente:

1. Montar uma representação do grafo Web baseada em qualquer estratégia (lista ou matriz de adjacências ou incidências) a partir do parsing de um conjunto de páginas armazenadas localmente. Estas páginas devem ser documentos HTML conectados entre si por meio de múltiplos links. (50% da nota);
2. Executar o algoritmo Page Rank para o grafo Web construído anteriormente. Deve ser possível alterar os parâmetros alfa (probabilidade do teleporte) e epsilon (erro aceitável para convergência). Para cada iteração do algoritmo, mostre os valores de Page Rank de todos os vértices. (50% da nota).
## Getting Started <a name = "getting_started"></a>

Para executar é necessario ter instalado na máquina:

### Prerequisites

[python](https://www.python.org/)
[pip](https://pip.pypa.io/en/stable/installation/)

### Installing

Instalado os requisitos é necessário rodar o comando abaixo:

```
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

Colocar os arquivos HTML dentro da pasta `arquivos`

```
- arquivos
    - arquivos .html para gerar o gráfico
- src
- LICENSE
- README.md
- Requirements.txt
- run.py
```

Caso for utilizar linha de comando usar o seguinte comando:
```
python run.py
```

Pela IDE executar o arquivo run.py utilizando o F5

