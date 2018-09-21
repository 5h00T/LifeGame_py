class Cell():
    
    def __init__(self, alive):
        self.alive = alive
        

def LifeGameInit(cells_per_line, alive_probability):
    """
    Parameters
    ----------
    cells_per_line : int
        一列当たりのセルの数
    alive_probability : float
        生存セルの確率
    
    Returns
    --------
    cells : list[sells_per_line+2][sells_per_line+2]
        Cellクラスのリスト
    """
    
    import random
    
    return [[Cell(True if (random.random() < alive_probability and not (col == 0 or row == 0 or col == cells_per_line+1 or row == cells_per_line+1 )) else False) for col in range(cells_per_line+2)] for row in range(cells_per_line+2)]


def UpdateCellStatus(cells, cells_per_line):
    """
    セルの状態を更新する
    
    Parameters
    ----------
    cells : list
        更新する細胞
    cells_per_line : int
        一列当たりのセルの数
        
    Returns
    -------
    new_cells : list
        更新後の細胞
    """
    
    import copy
    
    new_sells = copy.deepcopy(cells)
    
     # ダミーのマスで囲まれているので添字は1から
    for col in range(1, cells_per_line+1):
        for row in range(1, cells_per_line+1):
            alive_cells = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if cells[col+i][row+j].alive == True and not (i == 0 and j == 0):
                        alive_cells += 1
                        
            if alive_cells == 3 and cells[col][row].alive == False:
                new_sells[col][row].alive = True
            elif alive_cells <= 1 or alive_cells >= 4:
                new_sells[col][row].alive = False

    return new_sells


def print_cells(cells, alive_cell="■", dead_cell="□"):
    """
    セルの状態を出力する
    """
    
    for i in cells[1:-1]:
        for j in i[1:-1]:
            print(alive_cell if j.alive else dead_cell, end="")
        print()  # 改行
        

if __name__=="__main__":
    import time
    import subprocess

    cells_per_line = 50
    alive_probalility = 0.5

    cells = LifeGameInit(cells_per_line, alive_probalility)

    while True:
        subprocess.call("clear")
        print_cells(cells, "o", "M")

        time.sleep(1)

        cells = UpdateCellStatus(cells, cells_per_line)
