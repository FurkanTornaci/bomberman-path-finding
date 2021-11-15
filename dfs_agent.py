import abc
import time
import random
from copy import deepcopy
from typing import Final, Sequence, get_origin
from agent import Agent

import queue
import heapq
from collections import deque
from bomberman import Game

class Node():

    def __init__(self, parent_node, level_matrix, player_row, player_column, depth, chosen_dir):
        self.parent_node = parent_node
        self.level_matrix = level_matrix
        self.player_row = player_row
        self.player_col = player_column
        self.depth = depth
        self.chosen_dir = chosen_dir


class DFSAgent(Agent):

    def __init__(self):
        super().__init__()

    def solve(self, level_matrix, goal, player_row, player_column):
        super().solve(level_matrix, goal, player_row, player_column)
        move_sequence = []

        frontier = [[player_row, player_column]]
        explored = []
        parents = {}
        
        nodesKeptInMemory = [] # Number of nodes kept in the deque
        expandedFlag = 0 # Is node expanded

        # Finding the Path
        while len(frontier) > 0:
            nodesKeptInMemory.append(len(frontier))
            v = frontier.pop() # v is parent node
            if v == goal:
                break
            expandedFlag = 0 # Clear the flag
            if v not in explored:
                explored.append(v)
                for step in [[-1,0],[1,0],[0,-1],[0,1]]:
                    w = [v[i] + step[i] for i in range(2)] # w is neighbor node
                    if level_matrix[w[0]][w[1]] != "W" and w not in explored:
                        frontier.append(w)
                        self.generated_node_count +=1
                        parents[tuple(w)] = v
                        if expandedFlag == 0:
                            self.expanded_node_count +=1 # Current Node is expanded
                            expandedFlag = 1 # Current Node is expanded
        self.maximum_node_in_memory_count = max(nodesKeptInMemory)

        # Obtaining Sequence
        reverse_sequence = []
        nodeTo, nodeFrom = goal, goal
        while True:
            nodeFrom = nodeTo
            if nodeTo == [player_row, player_column]:
                break
            else:
                nodeTo = parents[tuple(nodeTo)]
            w = [nodeTo[a] - nodeFrom[a] for a in range(2)]
            for i in range(4):
                if w == [[1,0], [-1,0], [0,-1], [0,1]][i]:
                    reverse_sequence.append("UDRL"[i])
        move_sequence =  reverse_sequence[::-1]

        return move_sequence