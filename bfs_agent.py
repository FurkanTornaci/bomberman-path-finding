from os import F_OK
import time
import random
from copy import deepcopy
from typing import Sequence
from agent import Agent

import queue
import heapq
from collections import deque

class Node():
    def __init__(self, parent_node, level_matrix, player_row, player_column, depth, chosen_dir):
        self.parent_node = parent_node
        self.level_matrix = level_matrix
        self.player_row = player_row
        self.player_col = player_column
        self.depth = depth
        self.chosen_dir = chosen_dir


class BFSAgent(Agent):

    def __init__(self):
        super().__init__()

    def convert_direction_to_vector(self, player_direction):
        if player_direction == 'L':
            return -1, 0
        elif player_direction == 'R':
            return 1, 0
        elif player_direction == 'U':
            return 0, -1
        elif player_direction == 'D':
            return 0, 1
    def cordsAfterSequence(self, sequence, player_row, player_column):
        playerCords = [player_row, player_column]
        for i in sequence:
            movVector = self.convert_direction_to_vector(i)
            for j in range(2): playerCords[j] += movVector[1-j]
        return playerCords

    def solve(self, level_matrix, goal, player_row, player_column):
        super().solve(level_matrix, goal, player_row, player_column)
        move_sequence = []

        frontier = queue.Queue()
        frontier.put("")

        explored = []

        nodesKeptInMemory = [] # Number of nodes kept in the deque
        expandedFlag = 0 # Is node expanded

        # Finding the Path and obtaining the sequence
        while not frontier.empty():
            nodesKeptInMemory.append(frontier.qsize())
            sequence = frontier.get()
            FinalLocation = self.cordsAfterSequence(sequence, player_row, player_column)
            if FinalLocation[0] == goal[0] and FinalLocation[1] == goal[1]:
                move_sequence = sequence
                break
            else:
                expandedFlag = 0 # Clear the flag
                for key in "LRUD":
                    validCases = {
                    "L": level_matrix[FinalLocation[0]][FinalLocation[1]-1] != "W",
                    "R": level_matrix[FinalLocation[0]][FinalLocation[1]+1] != "W",
                    "U": level_matrix[FinalLocation[0]-1][FinalLocation[1]] != "W",
                    "D": level_matrix[FinalLocation[0]+1][FinalLocation[1]] != "W"
                    }
                    if validCases[key]:
                        FinalLocation = self.cordsAfterSequence(sequence, player_row, player_column)
                        if FinalLocation not in explored:
                            frontier.put(sequence + key)
                            self.generated_node_count +=1
                            if expandedFlag == 0:
                                self.expanded_node_count +=1 # Current Node is expanded
                                expandedFlag = 1 # Current Node is expanded
                explored.append(FinalLocation)
        self.maximum_node_in_memory_count = max(nodesKeptInMemory)

        return move_sequence

