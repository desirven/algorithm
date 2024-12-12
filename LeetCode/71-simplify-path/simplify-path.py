class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        for d in path.split("/"):
            if d=="..":
                if len(answer)>0:
                    answer.pop()
            elif d not in ["", "."]:
                answer.append(d)
        return "/" + "/".join(answer)