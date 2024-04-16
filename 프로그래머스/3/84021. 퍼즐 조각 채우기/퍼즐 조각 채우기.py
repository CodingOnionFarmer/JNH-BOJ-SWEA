def solution(game_board, table):
    # 90도씩 회전시킨 조각을 다 만들기 위함, dfs할거니까 처음부터 바깥탈출안되게 벽발라놓기
    n = len(table)
    table.append([0]*(n+1))
    game_board.append([1]*(n+1))
    table_90 = [[0]*(n+1) for _ in range(n+1)]
    table_180 = [[0]*(n+1) for _ in range(n+1)]
    table_270 = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        table[i].append(0)
        game_board[i].append(1)
        for j in range(n):
            table_90[j][n-1-i] = table[i][j]
            table_180[n-1-i][n-1-j] = table[i][j]
            table_270[n-j-1][i] = table[i][j]
        
            
            
    # 오른쪽1 아래2 왼쪽3 위4 돌아갈땐5 6진법으로 조각의 정보를 저장
    def dfs(x,y,p):
        table[x][y] = -p  # 회전시켰을때도 알아보기 위해 0으로 만드는게아니라 조각 번호의 음수로 바꿈
        size[p-1] += 1  # 조각의 사이즈 저장
        for i in range(4):
            dx,dy = directions[i]
            if table[x+dx][y+dy]>0:
                pieces[p-1] *= 6 
                pieces[p-1] += i+1
                dfs(x+dx,y+dy,p)
        pieces[p-1] *= 6
        pieces[p-1] += 5
        return
    
    
    def dfs_90(x,y,p):
        table_90[x][y] = 0
        for i in range(4):
            dx,dy = directions[i]
            if table_90[x+dx][y+dy]>0:
                pieces_90[p-1] *= 6 
                pieces_90[p-1] += i+1
                dfs_90(x+dx,y+dy,p)
        pieces_90[p-1] *= 6
        pieces_90[p-1] += 5
        return
    
    
    def dfs_180(x,y,p):
        table_180[x][y] = 0
        for i in range(4):
            dx,dy = directions[i]
            if table_180[x+dx][y+dy]>0:
                pieces_180[p-1] *= 6 
                pieces_180[p-1] += i+1
                dfs_180(x+dx,y+dy,p)
        pieces_180[p-1] *= 6
        pieces_180[p-1] += 5
        return
    
    
    def dfs_270(x,y,p):
        table_270[x][y] = 0
        for i in range(4):
            dx,dy = directions[i]
            if table_270[x+dx][y+dy]>0:
                pieces_270[p-1] *= 6 
                pieces_270[p-1] += i+1
                dfs_270(x+dx,y+dy,p)
        pieces_270[p-1] *= 6
        pieces_270[p-1] += 5
        return
    
    
    # 게임보드는 1이 아닌 0(구멍)을 기준으로 dfs해서 구멍 모양을 기록
    def dfs_board(x,y,p):
        game_board[x][y] = 1
        for i in range(4):
            dx,dy = directions[i]
            if not game_board[x+dx][y+dy]:
                holes[p-1] *= 6 
                holes[p-1] += i+1
                dfs_board(x+dx,y+dy,p)
        holes[p-1] *= 6
        holes[p-1] += 5
        return
    
    
    pieces = []
    size = []
    directions = ((0,1),(1,0),(0,-1),(-1,0))
    for i in range(n):
        for j in range(n):
            if table[i][j] > 0:
                pieces.append(0)
                size.append(0)
                dfs(i,j,len(pieces))
    pieces_90 = [0]*len(pieces)
    pieces_180 = [0]*len(pieces)
    pieces_270 = [0]*len(pieces)
    for i in range(n):
        for j in range(n):
            if table_90[i][j]:
                dfs_90(i,j,-table[n-1-j][i])
            if table_180[i][j]:
                dfs_180(i,j,-table[n-1-i][n-1-j])
            if table_270[i][j]:
                dfs_270(i,j,-table[j][n-1-i])
    placed = [0]*len(pieces)  # 게임보드에 이미 놓은 조각은 1로 표시
    holes = []
    for i in range(n):
        for j in range(n):
            if not game_board[i][j]:
                holes.append(0)
                dfs_board(i,j,len(holes))
    for hole in holes:
        for i in range(len(pieces)):
            if not placed[i]:
                if pieces[i] == hole or pieces_90[i] == hole or pieces_180[i] == hole or pieces_270[i] == hole:
                    placed[i] = size[i]
                    break
    answer = sum(placed)
    return answer