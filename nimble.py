from random import randint

def newBoard(n, p):
    """
    :param n: int, nombre d'éléments de board
    :param p: int, nombre maximal de pions par case lors de l'initialisation du plateau.
    :return: list[int], plateau de jeu
    """
    return [randint(0, p) for i in range(n)]

def display(board, n):
    """
    :param board: list[int], plateau de jeu
    :param n: int, nombre d'éléments de board
    """
    # Print the numbers of pawn in each box
    for i in range(n):
        space = "" if board[i] > 9 else " "
        print(f"{space}{board[i]} | ", end="")


    # Print the "-" to separate the two rows
    print("\n" + "-" * (5*n-1))

    # Print each box number
    for i in range(1, n + 1):
        space = "" if i >= 10 else " "
        print(f"{space}{i} | ", end="")


def possibleSquare(board, n, i):
    """
    :param board: list[int], plateau de jeu
    :param n: int, nombre d'éléments de board
    :param i: int, numéro d'une case
    :return: bool, True si la case contient un pion déplacable False sinon
    """
    if i <= 1 or i > n or board[i-1] < 1:
        return False
    return True

def selectSquare(board, n):
    """
    :param board: list[int], plateau de jeu
    :param n: int, nombre d'éléments de board
    :return: int, case contenant un pion déplacable
    """
    while True:
        player_choice = int(input("Choose a square : "))
        if possibleSquare(board, n, player_choice):
            return player_choice
        
def possibleDestination(board, n, i, j):
    """
    :param board: list[int], plateau de jeu
    :param n: int, nombre d'éléments de board
    :param i: int, numéro d'une case contenant un pion déplacable
    :param j: int, numéro d'une case sur laquelle déplacer le pion
    :return: bool, True si la case est une case sur laquelle le pion peut se déplacer False sinon
    """
    if j < 1 or j > n or j >= i:
        return False
    return True

def selectDestination(board, n, i):
    """
    :param board: list[int], plateau de jeu
    :param n: int, nombre d'éléments de board
    :param i: int, numéro d'une case contenant un pion déplacable
    :return: int, case vers laquelle un pion peut se déplacer
    """
    while True:
        player_choice = int(input("Choose a destination : "))
        if possibleDestination(board, n, i, player_choice):
            return player_choice
        
def move(board, n, i, j):
    """
    :param board: list[int], plateau de jeu
    :param n: int, nombre d'éléments de board
    :param i: int, numéro d'une case contenant un pion déplacable
    :param j: int, numéro d'une case sur laquelle déplacer le pion
    """
    board[j-1] += 1
    board[i-1] -= 1

def lose(board, n):
    """
    :param board: list[int], plateau de jeu
    :param n: int, nombre d'éléments de board
    :return: bool, True si aucun pion ne peut être déplacé False sinon
    """
    for nb in board[1:]:
        if nb != 0:
            return False
    return True

def nimble(n, p):
    """
    :param n: int, nombre d'éléments de board
    :param p: int, nombre maximal de pions par case lors de l'initialisation du plateau.
    """
    board = newBoard(n, p)
    player = 1
    display(board, n)

    while not lose(board, n):
        if player%2 == 1:
            print("\n\nPlayer 1")
        else:
            print("\n\nPlayer 2")
        
        square_selected = selectSquare(board, n)
        destination_selected = selectDestination(board, n, square_selected)
        move(board, n, square_selected, destination_selected)
        display(board, n)
        player += 1
    
    
    print("\n\nWinner :", player%2+1)

nimble(15, 24)
