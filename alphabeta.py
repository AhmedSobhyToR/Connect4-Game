import random
import math
from copy import deepcopy

#Number Of Rows And Columns
NumberOfRows = 6
NumberOfColumns = 7

class PlayerType:
    Idle = 0
    AgentAI = 1
    ComputerAI = 2



def alplhaBeta(maximizingPlayer,depth,Board, alpha, beta):
    HasStopped = IsStopped(Board)
    AvailablePlaces = AvailableColumnsForCurrentTime(Board)
    if HasStopped:
        if HasStopped:
            if hasWon(Board, PlayerType.AgentAI):
                return (None, 9999999)
            elif hasWon(Board, PlayerType.ComputerAI):
                return (None, -9999999)
            else: 
                return (None, 0)

    elif depth == 0:
         return (None, OutComeSum_position(Board, PlayerType.AgentAI))   
            
    if maximizingPlayer:  
        CurrentAmount = -math.inf
        column = random.choice(AvailablePlaces)
        for ThisCol in AvailablePlaces:
            row = FirstMove(Board, ThisCol)
            simulatedBoard = deepcopy(Board)
            simulatedBoard[row][ThisCol] = PlayerType.AgentAI
            NewOutComeSum = alplhaBeta(False, depth-1,simulatedBoard, alpha, beta)[1]
            if NewOutComeSum > CurrentAmount:
                CurrentAmount = NewOutComeSum
                column = ThisCol
            alpha = max(alpha, CurrentAmount)
            if alpha >= beta:
                break
        return column, CurrentAmount
    else: 
        CurrentAmount = math.inf
        column = random.choice(AvailablePlaces)
        for ThisCol in AvailablePlaces:
            row = FirstMove(Board, ThisCol)
            simulatedBoard = deepcopy(Board)
            simulatedBoard[row][ThisCol] = PlayerType.ComputerAI

            NewOutComeSum = alplhaBeta(  True, depth-1,simulatedBoard,alpha, beta)[1]
            if NewOutComeSum < CurrentAmount:
                CurrentAmount = NewOutComeSum
                column = ThisCol
            beta = min(beta, CurrentAmount)
            if alpha >= beta:
                break
        return column, CurrentAmount


def IsStopped(Board):
    if(hasWon(Board, PlayerType.ComputerAI)):
        return True
    elif (hasWon(Board, PlayerType.AgentAI)):
        return True
    elif(len(AvailableColumnsForCurrentTime(Board)) == 0):
        return True

def CorrectColumn(Board, ThisCol):
    return Board[0][ThisCol] == 0

def FirstMove(Board, ThisCol):
    ThisRow = int()
    for Roww in range(NumberOfRows):
        if Board[Roww][ThisCol] == 0:
            ThisRow = Roww
    return ThisRow

def AvailableColumnsForCurrentTime(Board):
    availableNumberOfColumns = []
    for ThisCol in range(NumberOfColumns):
        if CorrectColumn(Board, ThisCol):
            availableNumberOfColumns.append(ThisCol)
    return availableNumberOfColumns


def verticalOutComeSum(Board,Chunk, OutComeSum):
    for Columnn in range(NumberOfColumns):
        col_array = [int(row[Columnn]) for row in Board]
        for Roww in range(NumberOfRows-3):
            Screen = col_array[Roww:Roww+4]
            OutComeSum += UpdateScreen(Screen, Chunk)
    return OutComeSum

def horizontalOutComeSum(Board,Chunk,OutComeSum):
    for Roww in range(NumberOfRows):
        row_array = [int(i) for i in Board[Roww]]
        for Columnn in range(NumberOfColumns-3):
            Screen = row_array[Columnn:Columnn+4]
            OutComeSum += UpdateScreen(Screen, Chunk)
    return OutComeSum



def SlashedOutComeSum(Board,Chunk,OutComeSum):
    for Roww in range(NumberOfRows-3):
        for Columnn in range(NumberOfColumns-3):
            Screen = [Board[Roww +i][Columnn+i] for i in range(4)]
            OutComeSum += UpdateScreen(Screen, Chunk)

    for Roww  in range(NumberOfRows-3):
        for Columnn in range(NumberOfColumns-3):
            Screen = [Board[Roww +3-i][Columnn+i] for i in range(4)]
            OutComeSum += UpdateScreen(Screen, Chunk)
    return OutComeSum

def OutComeSum_position(Board, Chunk):
    OutComeSum = 0  
    center_array = [int(row[NumberOfColumns // 2]) for row in Board]
    center_count = center_array.count(Chunk)
    OutComeSum += center_count * 3

    verticalOutComeSum(Board,Chunk,OutComeSum)

    horizontalOutComeSum(Board,Chunk,OutComeSum)

    SlashedOutComeSum(Board,Chunk,OutComeSum)

    return OutComeSum

#checking how many pieces of that Token are in the screen and how many Idle spaces are in the screen
def UpdateScreen(Screen, Token):
    OutComeSum = 0
    opp_Chunk = PlayerType.ComputerAI
    if Token ==PlayerType. ComputerAI:
        opp_Chunk = PlayerType.AgentAI
# If there are two pieces of the Token and two Idle spaces in the screen, the score is increased by 2
    if Screen.count(Token) == 2 and Screen.count(PlayerType.Idle) == 2:
        OutComeSum += 2
# If there are three pieces of the Token and one Idle space in the screen, the score is increased by 5
    elif Screen.count(Token) == 3 and Screen.count(PlayerType.Idle) == 1:
        OutComeSum += 5
# If there are four pieces of the Token in the screen, the score is increased by 100
    elif Screen.count(Token) == 4:
        OutComeSum += 100
# If there are three pieces of the opposing player's Token and one Idle space in the screen, the score is decreased by 4
# This is because having three pieces in a row with one Idle space means that the 
# Opposing player could complete a four in a row and win the game if the Idle space is not blocked

    if Screen.count(opp_Chunk) == 3 and Screen.count(PlayerType.Idle) == 1:
        OutComeSum -= 4

    return OutComeSum

# Check if Agent won the game
def hasWon(Board, Token):
    Xdictionary = [0, -1, -1, -1]
    Ydictionary = [1, 0, -1, 1]
    for Roww in range(5, -1, -1):
        for Columnn in range(0, 7):
            for i in range(4):
                newX = Roww
                newY = Columnn
                if Board[newX][newY] == 0:
                    continue
                Cnter = 0
                for j in range(3):
                    newX = newX + Xdictionary[i]
                    newY = newY + Ydictionary[i]
                    if (newX < 0 or newX > 5 or newY < 0 or newY > 6):
                        break

                    if Token == Board[newX][newY]:
                        Cnter += 1

                if Cnter == 3 and Token == Board[Roww][Columnn]:
                    return True

    return False
