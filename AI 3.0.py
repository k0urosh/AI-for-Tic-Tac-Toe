import numpy as np
import copy
import math

class Player():
    def __init__(self):
        pass
        
    def play(self, game_board_state, player_n):
        convert_board = np.arange(game_board_state).reshape((4,4))
        return alphaBeta(convert_board, -math.inf, math.inf, 5, True, player_n)

    
def alphaBeta(node, alpha, beta, depth, maximiser, player_n):
    children = []
    
    children = expandBoardState(node, children)
    
    if(depth == 0):
        return findHeuristicValue(node, player_n)
            
    if(maximiser is True):
        for child in children:
            alpha = max(alpha, alphaBeta(child, alpha, beta, depth-1, False))
            if alpha >= beta:
                break 
        return alpha
    elif(maximiser is False):
        for child in children:
            beta = max(beta, alphaBeta(child, alpha, beta, depth-1, True))
            if alpha >= beta:
                break;
        return beta

def checkTurn(board):
    x = 0
    for row in range (0,4):
        for col in range (0,4):
            if(board[row][col] == 0):
                x = x+1
            elif(board[row][col] == 1):
                x = x-1
    return x

def expandBoardState(node, children):
    for row in 4:
        for col in 4:
            node_copy = copy(node)
            if(node_copy[row][col] == -1):
                node_copy[row][col] = checkTurn(node)
                if(checkDuplicate(node, children) == False):
                    children.append(node_copy)
                    return children
    return children             
          
def checkDuplicate(node, children):
    for child in (children):
        for rotate in range (0,4):
            if(np.array_equal(child), np.rot90(node, 1) == True):
                return True
        for rotate in range (0,2):
            if(np.array_equal(child), np.fliplr(node) == True):
                return True
        for rotate in range(0,2):
            if(np.array_equal(child), np.flipud(node) == True):
                return True            
    return False
       
def findHeuristicValue(node, player_n):
    # x at index 0, o at index 1
    value = []
    value.append(0)
    value.append(0)
    value = calculateHorizontal(node, value)
    if(player_n == 0):
        value.append(value[0] - value[1])
    elif(player_n == 1):
        value.append(value[1] - value[0])
    return value[-1]
    
def calculateHorizontal(node, value):
    for row in range(0,4):
        if (np.any(node[row][:] != 1) == True):
            value[0] = value[0] + 1
        if (np.any(node[row][:] != 0) == True):
            value[1] = value[1] + 1
    return value
            
def calculateVertical(node, value):
    for col in range(0,4):
        if (np.any(node[:][col] != 1) == True):
            value[0] = value[0] + 1
        if (np.any(node[:][col] != 0) == True):
            value[1] = value[1] + 1
    return value

def calculateDiagonal(node, value):
    # do i need to reflip??
    if (np.any(np.diagonal(node) != 1) == True):
        value[0] = value[0] + 1
    if (np.any(np.diagonal(np.fliplr(node)) != 1) == True):
        value[0] = value[0] + 1
    if (np.any(np.diagonal(node) != 0) == True):
        value[1] = value[1] + 1
    if (np.any(np.diagonal(np.fliplr(node)) != 0) == True):
        value[1] = value[1] + 1        
    return value
                
                
                
                
                
                