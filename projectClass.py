#!/usr/bin/env python3
import sys
import random
from colorama import Fore, Back

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game"""


# the main Class
class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


# A player that always plays 'rock'
class RockPlayer(Player):
    def move(self):
        return "rock"


# A player that chooses its moves randomly.
class Randomplayer(Player):
    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input(
                'rock, paper, or scissors?\t"type quit to end the game"\n'
            ).lower()
            if move in moves:
                return move
            elif move == "quit":

                sys.exit("thanks for playing :)")
            else:
                print("Please type in Rock, Paper, Or Scissors")


# A player that remembers and imitates what human player did in previous round.
class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = 0

    def move(self):
        if self.last_move == 0:
            return random.choice(moves)
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move


# A player that cycles through the three moves
class CyclePlayer(Player):
    moves = ["rock", "paper", "scissors"]

    def __init__(self):
        # Start with -1 to indicate no move has been made yet
        self.last_move_index = -1

    def move(self):

        if self.last_move_index == -1:
            # Choose a random move
            self.last_move_index = random.randint(0, len(self.moves) - 1)
        else:
            # Move to the next move
            self.last_move_index = (self.last_move_index + 1) % len(self.moves)
        return self.moves[self.last_move_index]

    def learn(self, my_move, their_move):
        self.last_move_index = self.moves.index(my_move)


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_1 = 0
        self.score_2 = 0

    def play_round(self):
        move1 = self.p1.move()

        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins this round")
            self.score_1 += 1
        elif beats(move2, move1):
            print("player 2 wins this round ")
            self.score_2 += 1
        else:
            print("this round is a tie ")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\033[34mGame start!\033[0m")

        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
            print(
                Fore.BLUE + f"Score: Player 1 has {self.score_1} points",
                Fore.YELLOW + f"Player 2 has {self.score_2} points",
            )

        print("\033[42mGame over!\033[0m")

        print(
            f"Final Score: Player 1 has {self.score_1} points,",
            f" Player 2 has {self.score_2} points",
        )
        if self.score_1 > self.score_2:
            print(Fore.LIGHTBLUE_EX + "Player 1 wins the game!")
        elif self.score_2 > self.score_1:
            print(Fore.YELLOW + "Player 2 wins the game!")
        else:
            print("The game is a tie!")
        print("thanks for playing :) ", end=" ")


if __name__ == "__main__":
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
