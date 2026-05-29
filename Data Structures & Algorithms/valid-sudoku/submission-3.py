class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rc(rc):
            th = {}
            for i in rc:
                if i == '.':
                    continue
                elif i not in th.keys():
                    th[i] = 1
                elif i in th.keys():
                    return False
            return True

        def flatten(x):
            return [item for sublist in x for item in sublist]

        tbool = True
        for i in range(len(board)):
            print(board[i])
            tbool = tbool and check_rc(board[i])
            tbool = tbool and check_rc([row[i] for row in board])
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                tbool = tbool and check_rc(flatten([row[j:j+3] for row in board[i:i+3]]))

        return tbool