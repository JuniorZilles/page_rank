from src.read_html import read_html_files


def build_graph(paths: list) -> dict:
    """
    Monta um dicionario contendo a lista de adjacencias e de incidencias

    """
    adj_inci = {"adj": {}, "inc": {}, "docs":[]}
    for path in paths:
        item = read_html_files(path)
        document = item['doc']
        adj_inci['docs'].append(document)
        for link in item['links']:
            ref_doc = link['link']
            __insert_on_list_adj_inc(adj_inci, 'adj', document, ref_doc)
            __insert_on_list_adj_inc(adj_inci, 'inc', ref_doc, document)

    return adj_inci

def __insert_on_list_adj_inc(adj_inci:dict, index:str, ref_doc:str, document:str)->None:
    """
    Adiciona ou cria uma entrada nas listas de incidencia ou adjacencia

    args:
        adj_inci:dict ->  {"adj": {}, "inc": {}, "docs":[]}
        index:str ->  adj ou inc
        ref_doc:str -> documento base
        document:str -> documento a ser agragado ao documento base
    """
    if ref_doc in adj_inci[index]:
        if document not in adj_inci[index][ref_doc]:
            adj_inci[index][ref_doc].append(document)
    else:
        adj_inci[index][ref_doc] = [document]

def print_adj_inc(adj_inci:dict)->None:
    """
    Apresenta a representação do grafo em lista de adjacencia e incidencia
    """
    print("Adjacências:")
    for key, value in adj_inci['adj'].items():
        print(f"{key}: {value}")

    print("Incidências:")
    for key, value in adj_inci['inc'].items():
        print(f"{key}: {value}")
