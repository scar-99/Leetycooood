import heapq

class Solution:
    def findRelativeRanks(self, score):

        heap = []

        for i in range(len(score)):
            heapq.heappush(heap, (-score[i], i))

        result = [""] * len(score)

        rank = 0

        while heap:

            neg_score, original_index = heapq.heappop(heap)

            if rank == 0:
                result[original_index] = "Gold Medal"

            elif rank == 1:
                result[original_index] = "Silver Medal"

            elif rank == 2:
                result[original_index] = "Bronze Medal"

            else:
                result[original_index] = str(rank + 1)

            rank += 1

        return result