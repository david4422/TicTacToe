import random
class Board:
    def __init__(self):
        self.locations = [[" " for _ in range(3)] for _ in range(3)]
        self.create_board()
    
  
    def create_board(self):
        for i, row in enumerate(self.locations):
            row_display = " | ".join(f" {cell} " for cell in row)
            print(row_display)
        
        # הדפסת קו מפריד בין השורות, חוץ מהאחרון
            if i < len(self.locations) - 1:
                print("-" * (len(row_display)))

    
    def put(self, type):
        row = int(input("Enter the location: row "))
        col = int(input("Enter the location: col "))
        if row in range(3) and col in range(3) and self.locations[row][col] == " ":
            self.locations[row][col] = type
        else:
            print("Cell is not available")
            self.change_board()
            self.put(type)
    

    def AI_put(self, type):
        print("AI is thinking...")
        self.change_board()


                # רשימה של כל הקומבינציות המנצחות: שורות, עמודות ואלכסונים
        win_patterns = [
            # שורות
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            
            # עמודות
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            
            # אלכסונים
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]        # בדיקה אם אחת הקומבינציות מכילה שלושה ערכים זהים (שאינם ריקים)
        for pattern in win_patterns:
            a, b, c = pattern  # מפרק כל שילוב לשלושה תאים
            if self.locations[a[0]][a[1]] == self.locations[b[0]][b[1]] and self.locations[a[0]][a[1]] == "O" and self.locations[c[0]][c[1]] == " ":
                    print("im winning you!!")
                    self.locations[c[0]][c[1]] = type
                    return
            if self.locations[a[0]][a[1]] == self.locations[c[0]][c[1]] and self.locations[a[0]][a[1]] == "O" and self.locations[b[0]][b[1]] == " ":
                    print("im winning you!!")
                    self.locations[b[0]][b[1]] = type
                    return
            if self.locations[b[0]][b[1]] == self.locations[c[0]][c[1]] and self.locations[b[0]][b[1]] == "O" and self.locations[a[0]][a[1]] == " ":
                    print("im winning you!!")
                    self.locations[a[0]][a[1]] = type
                    return
        for pattern in win_patterns:
            a, b, c = pattern  # מפרק כל שילוב לשלושה תאים
            if self.locations[a[0]][a[1]] == self.locations[b[0]][b[1]] and self.locations[a[0]][a[1]] != " " and self.locations[c[0]][c[1]] == " ":
                    print("im blocking you!!")
                    self.locations[c[0]][c[1]] = type
                    return
            if self.locations[a[0]][a[1]] == self.locations[c[0]][c[1]] and self.locations[a[0]][a[1]] != " " and self.locations[b[0]][b[1]] == " ":
                    print("im blocking you!!")
                    self.locations[b[0]][b[1]] = type
                    return
            if self.locations[b[0]][b[1]] == self.locations[c[0]][c[1]] and self.locations[b[0]][b[1]] != " " and self.locations[a[0]][a[1]] == " ":
                    print("im blocking you!!")
                    self.locations[a[0]][a[1]] = type
                    return
            

        if self.locations[1][1] == " ":
            print("im centering you!!")
            self.locations[1][1] = type
            return
        
        if self.locations[0][0] == " " or self.locations[0][2] == " " or self.locations[2][0] == " " or self.locations[2][2] == " ":
            print ("i will go on the corners")
            row = random.choice([0, 2])
            col = random.choice([0, 2])
            while self.locations[row][col] != " ":
                row = random.choice([0, 2])
                col = random.choice([0, 2])
            self.locations[row][col] = type
            return
            

        row = random.randint(0, 2)
        col = random.randint(0, 2)
        print(f"AI chose row {row} and col {col}")
        if self.locations[row][col] == " ":
            self.locations[row][col] = type
            return
        else:
            print("Cell is not available")
            self.change_board()
            self.AI_put(type)

    
    def change_board(self):
        self.create_board()

    def check_win(self, type):
                # רשימה של כל הקומבינציות המנצחות: שורות, עמודות ואלכסונים
        win_patterns = [
            # שורות
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            
            # עמודות
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            
            # אלכסונים
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        game_finish = False
        # בדיקה אם אחת הקומבינציות מכילה שלושה ערכים זהים (שאינם ריקים)
        for pattern in win_patterns:
            a, b, c = pattern  # מפרק כל שילוב לשלושה תאים
            if self.locations[a[0]][a[1]] == self.locations[b[0]][b[1]] == self.locations[c[0]][c[1]] != " ":
                print (f"{type} wins!")
                game_finish = True
                return game_finish
        if not any(" " in row for row in self.locations):
            print("Game over No one wins")
            game_finish = True
        return game_finish

