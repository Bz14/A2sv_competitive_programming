class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result=[]
        new_dict={}
        d = defaultdict(list)
        for p in paths:
            path = p.split()
            root = path[0]
            for j in range(1,len(path)):
                for k in range(len(path[j])):
                    if path[j][k] == "(":
                        content = path[j][k + 1: len(path[j])-1]
                        new_dict[root+"/"+path[j][0:k]] = content
        for key, value in new_dict.items():
            d[value].append(key)
        res = []
        for k, v in d.items():
            if len(v) >= 2:
                res.append(v)
        return res