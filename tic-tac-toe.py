# Description: tic tac toe following Tech With Tim's online guide

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    #return board[pos] == ' '
    if board[pos] != ' ':
        return False
    else:
        return True

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9):')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This space is occupied!')
            else:
                print('Type use a number within the range!')
        except:
            print('Type a PROPER move!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # I know what it does, but not the syntax
    move = 0

    # Checks to win or block player
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    # Checks if the center is open, if it is - take centre (code was after edges loop)
    if 5 in possibleMoves:
        move = 5
        return move

    # Checks if the corners are open, if they are - select random corner
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # Checks if the edges are open, if they are - select random edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move

def selectRandom(list):
    import random
    ln = len(list)
    r = random.randrange(0, ln) # But wouldn't it also select a random figure between these two values?
    return list[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    printBoard(board)

    while not(isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('You Lose')
            break

        if isBoardFull(board):
            print('Tie Game')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie game')
                break
            else:
                insertLetter('O', move)
                print('Computer has placed \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('You Win')
            break


while True:
    answer = input('Welcome to Tic Tac Toe. Do you want to play? (Y/N)')

    if answer.lower() == 'y' or answer.lower() == 'yes':
        print('-----------------------------------')
        board = [' ' for x in range(10)]
        main()
    else:
        break