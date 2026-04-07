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
        buffer = []
        seq = []
        rnd = 0
        while len(heap) + len(buffer) > 0:
            rnd += 1
            if len(heap) == 0:
                seq.append("idle")
            else:
                t_now = heapq.heappop(heap)
                seq.append(t_now[1])
                if t_now[0] + 1 < 0:
                    buffer.append((t_now[0] + 1, t_now[1], rnd + n + 1))

            if len(buffer) > 0:
                t_new = buffer[0]
                if t_new[2] == rnd + 1:
                    buffer = buffer[1:]
                    heapq.heappush(heap, t_new)

            # print(rnd, seq, buffer)
            
        return rnd
            



