class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def test_ana(s1, s2):
            l1 = list(s1)
            l2 = list(s2)
            l1.sort()
            l2.sort()
            if len(l1) != len(l2):
                return False
            elif l1 == l2:
                return True
            else:
                return False

        def flatten(a):
            return [item for sublist in a for item in sublist]

        all_list = []
        for i in range(len(strs)):
            if strs[i] in flatten(all_list):
                continue
            else:
                None
            t_list = [strs[i]]

            for j in range(i+1,len(strs)):
                if test_ana(strs[i],strs[j]):
                    t_list.append(strs[j])
                else:
                    None
            all_list.append(t_list)

        return all_list