class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        data = {}
        for t in tasks:
            if t not in data:
                data[t] = 1
            else:
                data[t] += 1

        if len(data) == 0:
            return 0
        
        heap = [(-value, key) for key, value in data.items()]
        heapq.heapify(heap)
        buffer = collections.deque()
        rnd = 0
        while heap or buffer:
            # cooldown ok
            while buffer and buffer[0][2] <= rnd:
                heapq.heappush(heap, buffer[0][:2])
                buffer.popleft()

            if heap:
                task_now = heapq.heappop(heap)
                if task_now[0] + 1 < 0:
                    ready_time = rnd + n + 1
                    buffer.append((task_now[0] + 1, task_now[1], ready_time))

            rnd += 1
            
        return rnd
