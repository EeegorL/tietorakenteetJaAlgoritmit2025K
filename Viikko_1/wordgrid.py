class WordFinder:
    def __init__(this):
        this.grid = None;
    
    def set_grid(this, grid):
        this.grid = grid;
    
    def count(this, word):        
        grid = this.grid;
        gridStr = "".join(grid);
        wLen = len(word);
        rLen = len(grid[0]);

        count = 0;

        x = 0;
        for i, cell in enumerate(gridStr):
            x+=1;
            if(x>rLen):x=1;
            y=i//rLen + 1;
            
            # left
            if(x >= wLen):
                wordMaybe = gridStr[x-wLen:x];
                print(x,wordMaybe, x-wLen,x)

        return count;


                    


if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"];

    finder = WordFinder();
    finder.set_grid(grid);

    print(finder.count("TIRA")); # 7 
    # print(finder.count("TA")); # 13
    # print(finder.count("RITARI")); # 3
    # print(finder.count("A")); # 8
    # print(finder.count("AA")); # 6
    # print(finder.count("RAITA")); # 0   