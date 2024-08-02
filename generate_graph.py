# -*- coding: utf-8 -*-
"""Flower_Tesi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fH3s9zi3X8vf4NZcYVqUmwqfgaBRiauK
"""

def genera_grafo_connesso(tipo_grafo, num_nodi, prob=None, m=None):
    """
    Genera un grafo connesso utilizzando networkx.

    Parametri:
    tipo_grafo (str): Tipo di grafo ('erdos_renyi' o 'scale_free')
    num_nodi (int): Numero di nodi nel grafo
    prob (float, optional): Probabilità per il grafo di Erdos-Renyi
    m (int, optional): Numero di archi da aggiungere in ogni nuovo nodo per il grafo scale-free

    Ritorna:
    np.ndarray: Matrice di adiacenza
    np.ndarray: Matrice del Laplaciano
    """

    while True:
        if tipo_grafo == 'erdos':
            if prob is None:
                raise ValueError("Per un grafo di Erdos-Renyi, specificare la probabilità 'prob'")
            G = nx.erdos_renyi_graph(num_nodi, prob)
        elif tipo_grafo == 'scale_free':
            if m is None:
                raise ValueError("Per un grafo scale-free, specificare il numero di archi 'm'")
            G = nx.barabasi_albert_graph(num_nodi, m)
        else:
            raise ValueError("Tipo di grafo non supportato. Scegliere tra 'erdos_renyi' o 'scale_free'")

        # Controlla se il grafo è connesso
        if nx.is_connected(G):
            break

    # Matrice di adiacenza
    adj_matrix = nx.adjacency_matrix(G).todense()

    # Matrice del Laplaciano
    laplacian_matrix = nx.laplacian_matrix(G).todense()

    # Plot del grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=50, edge_color='gray')
    plt.title(f"Graph {tipo_grafo.replace('_', ' ').title()}")
    plt.show()

    return adj_matrix, laplacian_matrix

# # Esempio di utilizzo:
# tipo_grafo = 'erdos'
# num_nodi = 20
# prob = 0.3

# adj_matrix, laplacian_matrix = genera_grafo_connesso(tipo_grafo, num_nodi, prob=prob)

# print("Matrice di adiacenza:\n", adj_matrix)
# print("Matrice del Laplaciano:\n", laplacian_matrix)





