import traceback
from src.read_folder import get_ful_path
from src.graph import build_graph, print_adj_inc
from src.page_rank import build_page_rank

def main():
    try:
        print('Load Folder content')
        itens = get_ful_path()

        print("Build Graph")
        adj_inc = build_graph(itens)

        print_adj_inc(adj_inc)

        alfa = float(input("Set alpha value with value between 0 and 1: "))
        if alfa < 0 and alfa > 1.0:
            raise Exception("Alfa inválido")
        epsilon = float(input("Set epsilon value: "))

        print('Build Page Rank')
        build_page_rank(adj_inc, alfa, epsilon)

    except Exception as e:
        traceback.print_exc()


main()