import sys
sys.stdin = open('input/16236.txt')


class Shark:
    def __init__(self):
        self.dr = [-1, 1, 0, 0]
        self.dc = [0, 0, -1, 1]

        self.N = int(input())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

        self.loc = self.find_shark_location()
        self.size = 2
        self.eat_count = 0
        self.move_count = 0

        self.go()


    def find_shark_location(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 9:
                    self.board[i][j] = 0
                    return [i, j]


    def find_and_eat_fish(self):
        r, c = self.loc

        visited = [[0]*self.N for _ in range(self.N)]
        visited[r][c] = 1

        q = [[r, c]]
        move = 0
        while q:
            move += 1
            qs, q = q, []
            fish = []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + self.dr[x], c + self.dc[x]
                    if 0 <= rr < self.N and 0 <= cc < self.N and not visited[rr][cc] and self.board[rr][cc] <= self.size:
                        visited[rr][cc] = 1
                        q.append([rr, cc])
                        if 0 < self.board[rr][cc] < self.size:
                            fish.append([rr, cc])
            if fish:
                fish.sort(key=lambda x: (x[0], x[1]))
                self.board[fish[0][0]][fish[0][1]] = 0
                self.loc = fish[0]
                self.eat_count += 1
                if self.eat_count == self.size:
                    self.size += 1
                    self.eat_count = 0
                self.move_count += move
                return True
        
        return False


    def go(self):
        while self.find_and_eat_fish():
            pass
        print(self.move_count)


shark = Shark()
