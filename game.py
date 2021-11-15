import time
import sys
import os

# Import constant definitions
from macros import *

# Import game class
from bomberman import Game

# Import agents
from agent import Agent
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
from astar_agent import AStarAgent

def start(player_string, PLAYED_LEVEL):
    # Initialize game
    bomberman = Game()

    # to prevent infinite loop while playing, just in case
    MAX_EPISODE_LENGTH = 1000

    player_string = player_string.upper()

    # Display player and played level
    print("Player {} will be playing level {}".format(player_string, PLAYED_LEVEL))

    if player_string == "HUMAN":
        elapsed_time_step = bomberman.start_level_human(PLAYED_LEVEL)
        printed_str = "--- Player Statistics ---\n"
        printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
        print(printed_str)
    elif player_string == "BFS":
        agent = BFSAgent()
        (elapsed_time_step, elapsed_solve_time, result) \
            = bomberman.start_level_computer(PLAYED_LEVEL,
                                        agent,
                                        render=True, play_sound=True,
                                        max_episode_length=MAX_EPISODE_LENGTH,
                                        test=True)
        printed_str = "--- BFS Agent Statistics ---\n"
        printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
        printed_str += "number of generated nodes:{}\n".format(agent.generated_node_count)
        printed_str += "number of expanded nodes:{}\n".format(agent.expanded_node_count)
        printed_str += "maximum number of nodes kept in memory:{}\n".format(agent.maximum_node_in_memory_count)
        printed_str += "elapsed solve time:{}\n".format(elapsed_solve_time)

        if result == RESULT_PLAYER_WON:
            printed_str += "WON\n"
        else:
            printed_str += "FAIL\n"
        print(printed_str)
    elif player_string == "DFS":
        agent = DFSAgent()
        (elapsed_time_step, elapsed_solve_time, result) = bomberman.start_level_computer(PLAYED_LEVEL, agent,
                                                                                    render=True, play_sound=True,
                                                                                    max_episode_length=MAX_EPISODE_LENGTH,
                                                                                    test=True)
        printed_str = "--- DFS Agent Statistics ---\n"
        printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
        printed_str += "number of generated nodes:{}\n".format(agent.generated_node_count)
        printed_str += "number of expanded nodes:{}\n".format(agent.expanded_node_count)
        printed_str += "maximum number of nodes kept in memory:{}\n".format(agent.maximum_node_in_memory_count)
        printed_str += "elapsed solve time:{}\n".format(elapsed_solve_time)
        if (result == RESULT_PLAYER_WON):
            printed_str += "WON\n"
        else:
            printed_str += "FAIL\n"
        print(printed_str)
    elif player_string == "ASTAR":
        agent = AStarAgent()
        (elapsed_time_step, elapsed_solve_time, result) = bomberman.start_level_computer(PLAYED_LEVEL, agent,
                                                                                    render=True, play_sound=True,
                                                                                    max_episode_length=MAX_EPISODE_LENGTH,
                                                                                    test=True)
        printed_str = "--- A* Agent Statistics ---\n"
        printed_str += "elapsed time step:{}\n".format(elapsed_time_step)
        printed_str += "number of generated nodes:{}\n".format(agent.generated_node_count)
        printed_str += "number of expanded nodes:{}\n".format(agent.expanded_node_count)
        printed_str += "maximum number of nodes kept in memory:{}\n".format(agent.maximum_node_in_memory_count)
        printed_str += "elapsed solve time:{}\n".format(elapsed_solve_time)
        if result == RESULT_PLAYER_WON:
            printed_str += "WON\n"
        else:
            printed_str += "FAIL\n"
        print(printed_str)