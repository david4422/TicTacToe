import random
class Board:
    def __init__(self):
        self.locations = [" "," "," "," "," "," "," "," "," ",]
        self.create_board()
    
  
    def create_board(self):
        board = [self.locations[i:i+3] for i in range(0, len(self.locations), 3)]  # חותך את הליסט לשורות של 3 ערכים כל אחת
        for row in board:
            print(f" {row[0]} | {row[1]} | {row[2]} ")# אם זו לא השורה האחרונה
            print("---|---|---")
        


    
    def put(self, type, index):
        self.locations[index] = type
 

    def AI_put(self, type):
        print("AI is thinking...")

                # רשימה של כל הקומבינציות המנצחות: שורות, עמודות ואלכסונים
        win_patterns = [
            # שורות
            [0,1,2],
            [3,4,5],
            [6,7,8],
            
            # עמודות
            [0,3,6],
            [1,4,7],
            [2,5,8],
            
            # אלכסונים
            [0,4,8],
            [2,4,6]
        ]        # בדיקה אם אחת הקומבינציות מכילה שלושה ערכים זהים (שאינם ריקים)
        for pattern in win_patterns:
            if self.locations[pattern[0]] == self.locations[pattern[1]] and self.locations[pattern[0]] == "O" and self.locations[pattern[2]] == " ":
                    print("im winning you!!")
                    self.locations[pattern[2]] = type
                    squer_index = pattern[2]
                    return squer_index
            if self.locations[pattern[0]] == self.locations[pattern[2]] and self.locations[pattern[0]] == "O" and self.locations[pattern[1]] == " ":
                    print("im winning you!!")
                    self.locations[pattern[1]] = type
                    squer_index = pattern[1]
                    return squer_index
            if self.locations[pattern[1]] == self.locations[pattern[2]] and self.locations[pattern[1]] == "O" and self.locations[pattern[0]] == " ":
                    print("im winning you!!")
                    self.locations[pattern[0]] = type
                    squer_index = pattern[0]
                    return squer_index
        for pattern in win_patterns:
            if self.locations[pattern[0]] == self.locations[pattern[1]] and self.locations[pattern[0]] == "X" and self.locations[pattern[2]] == " ":
                    print("im blocking you!!")
                    self.locations[pattern[2]] = type
                    squer_index = pattern[2]
                    return squer_index
            if self.locations[pattern[0]] == self.locations[pattern[2]] and self.locations[pattern[0]] == "X" and self.locations[pattern[1]] == " ":
                    print("im blocking you!!")
                    self.locations[pattern[1]] = type
                    squer_index = pattern[1]
                    return squer_index
            if self.locations[pattern[1]] == self.locations[pattern[2]] and self.locations[pattern[1]] == "X" and self.locations[pattern[0]] == " ":
                    print("im blocking you!!")
                    self.locations[pattern[0]] = type
                    squer_index = pattern[0]
                    return squer_index
            

        if self.locations[4] == " ":
            print("im centering you!!")
            self.locations[4] = type
            squer_index = 4
            return squer_index
        
        if self.locations[0] == " " or self.locations[2] == " " or self.locations[6] == " " or self.locations[8] == " ":
            print ("i will go on the corners")
            index = random.choice([0, 2, 6, 8])            
            while self.locations[index] != " ":
                index = random.choice([0, 2, 6, 8])           
            self.locations[index] = type
            squer_index = index
            return squer_index
            
        else:
            index = random.choice([1, 3, 5, 7])            
            print(f"AI chose index {index}")
            while self.locations[index] != " ":
                index = random.choice([1, 3, 5, 7])            
            self.locations[index] = type
            squer_index = index
            return squer_index
        

    
    def change_board(self):
        self.create_board()

    def check_win(self, type):
                # רשימה של כל הקומבינציות המנצחות: שורות, עמודות ואלכסונים
        win_patterns = [
            # שורות
            [0,1,2],
            [3,4,5],
            [6,7,8],
            
            # עמודות
            [0,3,6],
            [1,4,7],
            [2,5,8],
            
            # אלכסונים
            [0,4,8],
            [2,4,6]
        ]
        game_finish = False
        # בדיקה אם אחת הקומבינציות מכילה שלושה ערכים זהים (שאינם ריקים)
        for pattern in win_patterns:
            if self.locations[pattern[0]] == self.locations[pattern[1]] == self.locations[pattern[2]] and self.locations[pattern[0]] != " ":
                print (f"{type} wins!")
                game_finish = True
                return game_finish
        return game_finish

