class WordFinder:
    def __init__(this):
        this.grid = None;
    
    def set_grid(this, grid):
        this.grid = grid;
    
    def count(this, word):
        wLen = len(word);
        grid = this.grid;

    
                    


if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"];

    finder = WordFinder();
    finder.set_grid(grid);

    print(finder.count("TIRA")); # 7 
    print(finder.count("TA")); # 13
    print(finder.count("RITARI")); # 3
    print(finder.count("A")); # 8
    print(finder.count("AA")); # 6
    print(finder.count("RAITA")); # 0   