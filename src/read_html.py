from bs4 import BeautifulSoup

def read_html_files(path:dict)->dict:
    """
    Carrega os documentos html e os transforma em um dicionário

    args:
        path:dict -> dicionário {"caminho":"CAMINHO_ARQUIVO", "nome":"NOME_ARQUIVO"}
    
    returns:
        dicionário com o conteúdo relevante do documento {"doc":"nome", "links":[{"link": "link1", "name": "descricao1"}]}
    """
    soup = __get_html_doc(path['caminho'])
    name = path['nome']
    links = __get_links_info(soup)
    return {"doc":name, "links":links}

def __get_links_info(soup:BeautifulSoup)->list:
    """
    Obtêm os links associados dentro do documento html

    args:
        soup:BeautifulSoup -> instancia do documento html

    returns: lista de dicionários contendo {"link": "link1", "name": "descricao1"}
    """
    links = []
    for link in soup.find_all('a'):
        links.append({"link": link.get('href'),
        "name":link.string})
    return links

def __get_html_doc(path:str)-> BeautifulSoup:
    """
    Carrega o documento e converte ele em html

    args:
        path:str -> caminho do documento html

    returns: instancia do documento html
    """
    with open(path) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup