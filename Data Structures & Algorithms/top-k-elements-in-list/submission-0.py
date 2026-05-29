class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        chash = {}
        for j in nums:
            if j in chash.keys():
                chash[j] += 1
            else:
                chash[j] = 1
        vals = list(chash.values())
        vals.sort(reverse=True)
        topk_counts = vals[0:k]
        out = []
        keys = list(chash.keys())
        for i in range(len(vals)):
            tkey = keys[i]
            if chash[tkey] in topk_counts:
                out.append(tkey)
            else:
                None
        return out