def solution(N, M, image):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    answer = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                answer += 1
                
                q = [[i, j]]
                visited[i][j] = True
                
                while q:
                    qs, q = q, []
                    for r, c in qs:
                        for x in range(4):
                            rr, cc = r + dr[x], c + dc[x]
                            if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc] and image[rr][cc] == image[r][c]:
                                visited[rr][cc] = True
                                q.append([rr, cc])

    return answer
