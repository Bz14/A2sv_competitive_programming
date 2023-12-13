class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainDict = defaultdict(int)
        for i in cpdomains:
            cost, st = i.split()
            arr = st.split('.')
            for i in range(len(arr)):
                newstr = '.'.join(arr[i:])
                domainDict[newstr] += int(cost)
        res = []
        for val in domainDict:
            res.append(str(domainDict[val]) + " " + val)
        return res
        