def build_page_rank(adj_inc_doc:dict, alfa:float, epsilon:float):
    """
    Realiza o cálculo de page rank para cada documento realizando mais de uma iteração
    """
    page_ranks = {}
    qtd_docs = len(adj_inc_doc['docs'])
    finished = []
    iteration = 0
    while len(finished) < qtd_docs:
        for doc in adj_inc_doc['docs']:
            __calculate_new_page_rank(alfa, qtd_docs, doc, adj_inc_doc, page_ranks)
            if(__calculate_error(page_ranks[doc], epsilon) and doc not in finished):
                finished.append(doc)
        
        __print_page_rank_for_iteration(iteration, page_ranks)
        iteration += 1

def __calculate_error(page_rank:list, epsilon:float)->bool:
    """
    Calcula o erro aceitável que determina se deve continuar ou não

    args:
        page_rank:list -> lista dos page ranks calculado para o documento
        epsilon:float -> valor do erro aceitável
    
    returns: 
        bool -> True caso a diferença do valor dos ultimos dois seja menor que o epsilon, False caso contrário
    """
    if len(page_rank) < 2:
        return False
    elif abs(page_rank[-1] - page_rank[-2]) < epsilon:
        return True
    return False

def __calculate_new_page_rank(alfa:float, n_docs:int, doc:str, adj_inc_doc:dict, page_ranks:dict)->None:
    """
    Atualiza o valor de page rank para o documento em questão

    args:
        alfa:float -> valor do alfa
        n_docs:int -> numero total de documentos
        doc:str -> documento avaliado
        adj_inc_doc:dict -> dicionário com a lista de adjacentes e incidentes
        page_ranks:dict -> dicionário contendo para cada documento a lista dos valores de page rank calculados
    """
    soma = 0
    if doc in adj_inc_doc['inc']:
        for a in adj_inc_doc['inc'][doc]:
            qtd_adj = len(adj_inc_doc['adj'][a])
            valor = 1/n_docs
            if a in page_ranks:
                valor = page_ranks[a][-1]
            soma += (valor/qtd_adj)
    pr = (alfa/n_docs) + (1-alfa)*soma
    if doc in page_ranks:
        page_ranks[doc].append(pr)
    else:
        page_ranks[doc] = [pr]

def __print_page_rank_for_iteration(iteration:int, page_ranks:dict)->None:
    """
    Mostra as pontuações do page rank para cada iteração

    args:
        iteration:int -> corrente iteracao
        page_ranks:dict -> {"doc":[0,0.1,0.2]}
    """
    print(f'Iteration {iteration}')
    for pr_key, pr_value in page_ranks.items():
        print(f'document {pr_key}, page rank: {pr_value[-1]}')
