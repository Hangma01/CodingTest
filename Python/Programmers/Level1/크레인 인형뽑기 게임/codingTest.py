def solution(board, moves):
    cart=[]
    count = 0
    for col in moves:
        for row in range(len(board)):
            if board[row][col-1] > 0:
                cart.append(board[row][col-1])
                board[row][col-1] = 0
                break

        if len(cart) > 1 and cart[-1] == cart[-2]:
            del cart[-2:]
            count += 2
    
    return count


board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
print(solution(board,moves))