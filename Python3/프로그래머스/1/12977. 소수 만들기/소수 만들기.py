def solution(nums):
    prime = [2]
    MAX = max(nums) + (max(nums) - 1) + (max(nums) - 2)
    for i in range(1, MAX):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i - 1:
                prime.append(i)

    answer = 0
    for a in range(len(nums)):
        for b in range(a, len(nums)):
            for c in range(b, len(nums)):
                if nums[a] != nums[b] and nums[b] != nums[c] and nums[a] != nums[c]:
                    if nums[a] + nums[b] + nums[c] in prime:
                        answer += 1

    return answer