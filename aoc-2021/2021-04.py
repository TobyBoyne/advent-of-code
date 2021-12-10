import numpy as np
import re

def winning_board(wins):
    cols = np.sum(wins, axis=1).max(axis=-1)
    rows = np.sum(wins, axis=2).max(axis=-1)

    winners = np.nonzero(np.logical_or(cols == 5, rows == 5))
    if winners[0].shape != (0,):
        return winners


with open('day04.txt') as f:
    text = f.read()
    draws = np.array(text.split('\n')[0].split(','), dtype=int)

    board_strings = re.findall(r'\n\n(.*?)(?=\n{2}|$)' , text, flags=re.DOTALL)
    boards =  np.array([[line.split() for line in board.split('\n')] for board in board_strings], dtype=int)
    
    print(boards.shape)

    

def part_one(boards, draws):
    wins = np.zeros_like(boards)

    for x in draws:
        idxs = np.nonzero(boards == x)
        wins[idxs] = 1
        winners = winning_board(wins)
        if winners is not None:
            unmarked = np.logical_not(wins[winners])
            unmarked_sum = boards[winners][unmarked].sum()
            score = unmarked_sum * x
            return score


def part_two(boards, draws):
    wins = np.zeros_like(boards)
    num_boards = boards.shape[0]

    for x in draws:
        idxs = np.nonzero(boards == x)
        wins[idxs] = 1
        winners = winning_board(wins)
        if winners is not None:
            print(winners)
            num_winners = winners[0].shape[0]
            print(x, num_winners)
            if num_winners == num_boards - 1:
                print('found loser')

                loser = np.isin(np.arange(num_boards), winners, invert=True)

            elif num_winners == num_boards:
                print(wins[loser])
                unmarked = np.logical_not(wins[loser])
                unmarked_sum = boards[loser][unmarked].sum()
                score = unmarked_sum * x
                return score

if __name__ == '__main__':
    print('Part one', part_one(boards, draws))
    print('Part two', part_two(boards, draws))