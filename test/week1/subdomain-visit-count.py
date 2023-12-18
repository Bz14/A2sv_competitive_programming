class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainDict = defaultdict(int)
        for i in cpdomains:
            cost, st = i.split()
            arr = st.split('.')
            for i in range(len(arr)):
                newstr = '.'.join(arr[i:])
                domainDict[newstr] += int(cost)
        result = []
        for val in domainDict:
            result.append(str(domainDict[val]) + " " + val)
        return result
        