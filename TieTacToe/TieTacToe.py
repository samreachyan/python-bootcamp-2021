import random

board = [' ' for _ in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


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


def isBoardFull(board):
    return not ' ' in board


# def isWon(board):
#     return (board[1] == board[2] == board[3] != ' ') or (board[4] == board[5] == board[6] != ' ') or (
#         board[7] == board[8] == board[9] != ' ') or (board[1] == board[4] == board[7] != ' ') or (
#         board[2] == board[5] == board[8] != ' ') or (board[3] == board[6] == board[9] != ' ') or (
#         board[1] == board[5] == board[9] != ' ') or (board[3] == board[5] == board[7] != ' ')


def isWinner(board, letter):
    return (board[1] == board[2] == board[3] == letter) or (board[4] == board[5] == board[6] == letter) or (
        board[7] == board[8] == board[9] == letter) or (board[1] == board[4] == board[7] == letter) or (
        board[2] == board[5] == board[8] == letter) or (board[3] == board[6] == board[9] == letter) or (
        board[1] == board[5] == board[9] == letter) or (board[3] == board[5] == board[7] == letter)


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def computerMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return selectRandom(possibleMoves)


def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not isBoardFull(board) and not isWinner(board, 'X') and not isWinner(board, 'O'):
        if not isBoardFull(board):
            playerMove()
            printBoard(board)
        else:
            print('The game is a draw!')
            break

        if not isBoardFull(board):
            move = computerMove()
            if move == 0:
                print('The computer is too dumb, and lost!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)

    if isWinner(board, 'X'):
        print('X is the winner!')
    elif isWinner(board, 'O'):
        print('O is the winner!')
    else:
        print('The game is a draw!')


if __name__ == '__main__':
    main()
