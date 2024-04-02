import random


class Player:
    """Represents a game player.
        level: human, AI Easy, AI Hard"""
    def __init__ (self, name, player_id, level="human"):
        self.name = name
        self.player_id = player_id
        self.level = level

    """ Save a New Player to the Database
        player_id will have the unique id from the table Players"""
    def create (self):
        pass

    def update (self):
        pass

    def delete(self):
        pass

    # έκανα κάποιες αλλαγές στην σειρά 22
    def info(self):
        print(f'Id:"{self.player_id}", Name:"{self.name}" Level:"{self.level}"', end=" ")


class DashBoard:
    """" DashBoard is a square
     tile size may be given from tkinder """
    def __init__ (self, size, tilesize, tilemode):
        self.size = size

    # δεν ξέρω αν μπει σε αυτή τη μέθοδο μια εκτύπωση του πίνακα, αλλιώς να την προσθέσω στα αποτελέσματα αν χρειάζεται
    def drawCanvas(self):
        pass


class Game:
    def __init__(self, player1, player2, turns, boardSize=3, game_id=0):
        # πρόσθεσα τα ορίσματα
        self.player1 = player1
        self.player2 = player2
        self.turns = turns
        self.boardSize = boardSize
        self.game_id = game_id


        '''This is in essence the game setup'''
        pass

    def load(self):
        pass

    def create(self):
        pass

    # random επιλογή για το ποιος ξεκινάει
    """Maniputlate Game to the Database
         Game_id will have the unique id from the table Games"""
    def new(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


    def info(self):
        print(f'Id:"{self.game_id}", Player1:"{self.player1}" Player2:"{self.player2} turns:"{self.turns}" '
              f'size:"{self.boardSize}"', end=" ")


class Referee:
    def __init__(self, board, currentPlayerId):
        self.board = board
        self.currentPlayerId = currentPlayerId

    # τι εννοούμε turns; Αν κάθε γύρος είναι ένα ολοκληρωμένο παιχνίδι, τότε θα γράψω κώδικα ώστε στο τέλος κάθε γύρου
    # να προσθέτει σε αυτόν που κέρδισε έναν πόντο και αυτός που μαζέψει τρεις είναι ο νικητής.

    def check_row(self, row):
        return self.board[row][0] == self.board[row][1] == self.board[row][2] != " "

    def check_col(self, col):
        return self.board[0][col] == self.board[1][col] == self.board[2][col] != " "

    def check_diagonals(self):
        return ((self.board[0][0] == self.board[1][1] == self.board[2][2] != " ") or
                (self.board[2][0] == self.board[1][1] == self.board[0][2] != " "))


    def WaitNextPlayer(self):
        for _ in range(9):
            print(self.board)

            # choose next player
            if self.currentPlayerId == "X":
                self.currentPlayerId = "O"
            else:
                self.currentPlayerId = "X"


    def checkEmptySpaces(self):
        # Εισαγωγή στοιχείων από τον χρήστη
        while True:
            print("Player " + self.currentPlayerId + " plays! ")
            row = int(input("Give row: "))
            col = int(input("Give column: "))
            if 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] != " ":
                self.board[row][col] = self.currentPlayerId
                break
            else:
                print("Invalid choice! Try again.")


    def checkWinner(self):
        winner = None
        for i in range(3):
            if self.check_row(i) or self.check_col(i):
                winner = self.currentPlayerId
                break
        if not winner and self.check_diagonals():
            winner = self.currentPlayerId

        if winner:
            print("Player " + self.currentPlayerId + " won!")
        else:
            print("Draw!")


#//////////////////////////////
def checkIsNegativeOrZero(theNumber):
    '''Check if a number is Negative or Zero '''
    try:
        theIntEquivalent = int(theNumber)
        if theIntEquivalent <= 0:
            return True
        return False
    except ValueError:
        return False


def getNonNegativeNumberAndNoneZero(FirstPrompt, SecondPrompt, limit):
    '''Asks and returns a none negative number
        Two prompts are provided and a lower limit '''
    theIntNumber = ''
    while (theIntNumber == '') or (not theIntNumber.lstrip('-').isnumeric()):
        theIntNumber = input(FirstPrompt)
        if checkIsNegativeOrZero(theIntNumber):
            if (int(theIntNumber) <= limit) :
                print(SecondPrompt)
                theIntNumber = ''
    return int(theIntNumber)

if __name__ == '__main__':
    #Make all the decisions and ask the game to start and the Dashboard to draw,

    ##Menu to load the options, or screens etc.
    ##Create a game
    ## create a referee
    #Give the game to the referee to check

    #This are no by hand and will be handled by the db
    Player_id = 1
    Player2_id = 2


    player1 = Player('Xaris', Player_id)
    player2 = Player('Elena', Player2_id)
    #player2 = Player('Computer 1', Player2_id, "AI Easy")
    #player2 = Player('Computer 2', Player2_id, "AI Hard")
    theTurns = getNonNegativeNumberAndNoneZero("Turns: ", "Must be > 0", 1)
    theSize = getNonNegativeNumberAndNoneZero("Size: ", "Must be >= 3", 3)
    tilesize = 100 #pixels
    tilemode = 1 #some mode, graphical or other

    theGame = Game(player1, player2, theTurns, theSize)
    theBoard = DashBoard(theGame, theSize, tilesize, tilemode)
    firstPlayerId = random.randint(1, 2)

    theReferee = Referee(theGame, firstPlayerId)

    while True:
        theBoard.drawCanvas()
        theReferee.WaitNextPlayer()
        theReferee.checkWinner()
        exit()
