import sys
sys.stdin = open('input/5648.txt')


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for tc in range(1, int(input()) + 1):
    N = int(input())
    
    atoms = [0] * N
    atoms_index = list(range(N))
    for idx in range(N):
        atoms[idx] = list(map(int, input().split()))
        atoms[idx][0] *= 2
        atoms[idx][1] *= 2
    
    result = 0

    while atoms_index:
        L = len(atoms_index)
        trash = set()
        move = set()
        for idx in atoms_index:
            atoms[idx][0] += dx[atoms[idx][2]]
            atoms[idx][1] += dy[atoms[idx][2]]
            if -2000 <= atoms[idx][0] <= 2000 and -2000 <= atoms[idx][1] <= 2000:
                move.add((atoms[idx][0], atoms[idx][1]))
            else:
                trash.add(idx)

        if L != len(move):
            for i in range(len(atoms_index) - 1):
                if atoms_index[i] not in trash:
                    atom = atoms[atoms_index[i]]
                    E = 0
                    for j in range(i + 1, len(atoms_index)):
                        if atoms_index[j] not in trash:
                            other = atoms[atoms_index[j]]
                            if atom[:2] == other[:2]:
                                trash.add(atoms_index[j])
                                E += other[3]
                    if E:
                        trash.add(atoms_index[i])
                        E += atom[3]
                        result += E

        if trash:
            origin = set(atoms_index)
            origin -= trash
            atoms_index = list(origin)

    print(f"#{tc} {result}")
