class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count, h = 0, citations[0]
        while h>0:
            if count >= h:
                break
            elif count < len(citations) and h <= citations[count]:
                count += 1
            else:
                h -= 1
        return count

