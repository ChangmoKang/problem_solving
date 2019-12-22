import sys
sys.stdin = open('input/18228.txt')

N = int(input())
board = list(map(int, input().split()))
penguin = board.index(-1)
print(min(board[:penguin]) + min(board[penguin + 1:]))
