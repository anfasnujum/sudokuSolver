class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        remaining = [[[str(x) for x in range(1,10)] for x in range(9)] for x in range(9)]
        self.updateRemaining(board,remaining)

        next = self.findNext(board,0,0)
        count=0
        
        
        print(count,remaining[next[0]][next[1]])
        for k in remaining[next[0]][next[1]]:
            self.sudokuSolver(board.copy(),remaining.copy(),next[0],next[1],k,count)
        



    def sudokuSolver(self,board,remaining,i,j,number,count):
        count+=1
        new = self.putAndUpdate(board,remaining,number,i,j)
        newboard = new[0]
        newremaining = new[1]

        if self.checkVictory(newboard):
            print("Solved")
            print(newboard)
            return True
        
        next = self.findNext(newboard,i,j)
        if not next:
            return False

        if len(newremaining[next[0]][next[1]]) == 0:
            print("bye")
            return False

        for k in newremaining[next[0]][next[1]]:
            print(count,k,newremaining[next[0]][next[1]])
            if self.sudokuSolver(newboard,newremaining,next[0],next[1],k,count):
                print("Yay")
                return True
            print(count,"sad",k,newremaining[next[0]][next[1]])
            
        return False
            
    def updateRemaining(self,board,remaining):
        for i in range(9):
            for j in range(9):
                
                if board[i][j] != ".":
                    remaining[i][j] = []
                    continue
                
                #checkcolumn
                for m in range(9):
                    if board[m][j] != "." and board[m][j] in remaining[i][j]:   
                        remaining[i][j].remove(board[m][j])
                    
                
                #checkRow
                
                for k in range(9):
                    if board[i][k] != "." and board[i][k] in remaining[i][j]:
                        remaining[i][j].remove(board[i][k])
                        
                #check box
                for m in range(3*int(i/3),3*int(i/3) +3):
                    for k in range(3*int(j/3),3*int(j/3) + 3):
                        if board[m][k] != "." and board[m][k] in remaining[i][j]:
                            remaining[i][j].remove(board[m][k])

                if len(remaining[i][j]) == 1:
                    board[i][j] = remaining[i][j][0]
                    remaining[i][j].pop()
                            
    def findNext(self,board,i,j):
        for i in range(i,9):
            for j in range(9):
                if board[i][j] == ".":
                    return (i,j)
        for i in range(0,i):
            for j in range(0,9):
                if board[i][j] == ".":
                    return (i,j)
        return False
        
    def putAndUpdate(self,board,remaining,number,i,j):
        newboard = board.copy()
        newremaining = remaining.copy()
        newboard[i][j] = number

        #Update row elements
        
        for k in range(9):
            if number in newremaining[i][k]:
                newremaining[i][k].remove(number)

        
        #Update column elements
        for m in range(9):
            if number in newremaining[m][j]:
                newremaining[m][j].remove(number)

        
        #update box
        for m in range(3*int(i/3),3*int(i/3) + 3):
            for k in range(3*int(j/3), 3*int(j/3)+3):
                if number in newremaining[m][k]:
                    newremaining[m][k].remove(number)

        
        return [newboard,newremaining]  
  
    
    def checkVictory(self,board):
        
        #Check Rows
        for i in range(9):
            sum=0
            for j in range(9):
                if board[i][j] == ".":
                    continue
                sum+=int(board[i][j])
            if sum != 45:
                return False
        
        #check Columns
        for j in range(9):
            sum = 0
            for i in range(0,9):
                if board[i][j] == ".":
                    continue
                sum += int(board[i][j])
            if sum != 45:
                return False
        #Check Box
        for i in range(3):
            for j in range(3):
                sum = 0
                for m in range(3*i,3*i+3):
                    for k in range(3*j,3*j+3):
                        if board[m][k] == ".":
                            continue
                        sum+= int(board[m][k])
                
                if sum != 45:
                    return False
        return True
                        
                
        
Anfas = Solution()

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(board)

Anfas.solveSudoku(board)

board = [["5","3","1","2","7","4","8","9","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
