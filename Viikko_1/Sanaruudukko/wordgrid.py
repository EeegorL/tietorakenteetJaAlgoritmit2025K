class WordFinder:
    def __init__(this):
        this.grid = None;
    
    def set_grid(this, grid):
        this.grid = grid;
    
    def count(this, word):
        # 1: Käydää läpi listana sellasenaan

        wLen = len(word);
        grid = this.grid;
        count = 0;

        for iy, row in enumerate(grid):
            for ix, cell in enumerate(row):
                distN = iy + 1;
                distS = len(grid) - iy;
                distE = ix + 1;
                distW = len(row) - ix;

                if(ix <= distE):
                    print(row, row[ix:wLen])
                    

        # 2: Käydää läpi stringinä!! Tää on varmaa nopeempi mut toki vaikeempaa ajatella mut katotaa
        # gridStr = "".join(grid);
        # rLen = len(grid[0]);

        # print(gridStr[:rLen])


                    


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