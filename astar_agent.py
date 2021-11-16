import time
import random
from copy import deepcopy
from agent import Agent

import queue
import heapq
from collections import deque

class Node():

    def __init__(self, parent_node, level_matrix, player_row, player_column, depth, chosen_dir, h_value):
        self.parent_node = parent_node
        self.level_matrix = level_matrix
        self.player_row = player_row
        self.player_col = player_column
        self.depth = depth
        self.chosen_dir = chosen_dir
        self.h = h_value

    def __lt__(self, other):
        return self.depth + self.h < other.depth + other.h

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class AStarAgent(Agent):

    def __init__(self):
        super().__init__()


    def solve(self, level_matrix, goal, player_row, player_column):
        super().solve(level_matrix, goal, player_row, player_column)
        move_sequence = []
        
        infty = (len((level_matrix))+1)**2
        w = len(level_matrix)

        openSet= deque()
        openSet.append([player_row, player_column])
        cameFrom = {}

        gScore = [[infty for x in range(w)] for y in range(w)]
        gScore[player_row][player_column] = 0

        fScore = [[infty for x in range(w)] for y in range(w)]
        fScore[player_row][player_column] = abs(player_row - goal[0]) + abs(player_column - goal[1])

        nodesKeptInMemory = [] # Number of nodes kept in the deque
        numberOfVisitedNodes = 1 # Starting Node
        expandedFlag = 0 # Is node expanded

        # Finding the Path 
        while len(openSet) > 0:
            nodesKeptInMemory.append(len(openSet))
            numberOfVisitedNodes += 1
            
            # Finding the node in openSet having the lowest fScore[] value
            index = 0
            for i in range(len(openSet)):
                i_pos, curr_pos = openSet[i], openSet[index]
                i_fscore, curr_fscore = fScore[i_pos[0]][i_pos[1]], fScore[curr_pos[0]][curr_pos[1]]
                if i_fscore < curr_fscore:
                    index = i
            currentNode = openSet[i]
            
            if currentNode == goal: # Check if player found the door
                break

            openSet.remove(currentNode) 
            expandedFlag = 0 # Clear the flag
            for y, x in [[-1,0],[1,0],[0,-1],[0,1]]:
                neighborNode = [currentNode[0] + y, currentNode[1]  + x]
                if level_matrix[neighborNode[0]][neighborNode[1]] == "W": # check if current neighbor location is a Wall
                    continue
                tentative_gScore = gScore[currentNode[0]][currentNode[1]] + 1
                if tentative_gScore < gScore[neighborNode[0]][neighborNode[1]]:
                    cameFrom[tuple(neighborNode)] = currentNode
                    gScore[neighborNode[0]][neighborNode[1]] = tentative_gScore
                    fScore[neighborNode[0]][neighborNode[1]] = gScore[neighborNode[0]][neighborNode[1]] + abs(neighborNode[0] - goal[0]) + abs(neighborNode[1] - goal[1])
                    if neighborNode not in openSet:
                        openSet.append(neighborNode) # New node is generated.
                        self.generated_node_count +=1
                        if expandedFlag == 0:
                            self.expanded_node_count +=1 # Current Node is expanded
                            expandedFlag = 1    # Current Node is expanded
        self.maximum_node_in_memory_count = max(nodesKeptInMemory)

        # Obtaining Sequence
        reverse_sequence = []
        nodeTo, nodeFrom = goal, goal
        while True:
            nodeFrom = nodeTo
            if nodeTo == [player_row, player_column]:
                break
            else:
                nodeTo = cameFrom[tuple(nodeTo)]
            w = [nodeTo[a] - nodeFrom[a] for a in range(2)]
            for i in range(4):
                if w == [[1,0], [-1,0], [0,-1], [0,1]][i]:
                    reverse_sequence.append("UDRL"[i])
        move_sequence =  reverse_sequence[::-1]
        return move_sequence