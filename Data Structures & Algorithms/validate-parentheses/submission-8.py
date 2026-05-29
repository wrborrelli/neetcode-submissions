class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        opens = []
        s_split = [c for c in s]
        for i in s_split:
            if i == "(" or i == "[" or i == "{":
                opens.append(i)
            elif i == ')':
                if len(opens) == 0:
                    return False
                if opens[-1] == '(':
                    opens.pop()
                else:
                    return False
            elif i == ']':
                if len(opens) == 0:
                    return False
                if opens[-1] == '[':
                    opens.pop()
                else:
                    return False
            elif i == '}':
                if len(opens) == 0:
                    return False
                if opens[-1] == '{':
                    opens.pop()
                else:
                    return False
            else:
                return False
        if len(opens) == 0:
            return True
        else:
            return False
            