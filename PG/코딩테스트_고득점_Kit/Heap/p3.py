import heapq
from collections import deque

REQUEST_TIME = 0
def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort(key=lambda x:x[REQUEST_TIME])
    jobs = deque(jobs)
    
    wait_jobs = []
    time = jobs[0][REQUEST_TIME]
    
    while jobs or wait_jobs:
        if not wait_jobs and jobs and time < jobs[0][REQUEST_TIME]:
            time = jobs[0][REQUEST_TIME]

        while jobs and jobs[0][REQUEST_TIME] <= time:
            start, duration = jobs.popleft()
            heapq.heappush(wait_jobs, (duration, start))
        
        duration, start = heapq.heappop(wait_jobs)
        time += duration

        answer += (time - start)
    
    return answer // N
