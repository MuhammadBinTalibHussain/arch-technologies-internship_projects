import math
import os
import time

ROWS   = 6
COLS   = 7
EMPTY  = 0
PLAYER = 1
AI     = 2

GREEN = "\033[92m"
WHITE = "\033[97m"
WINBG = "\033[42m\033[97m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
RESET = "\033[0m"

# Clear the terminal screen
def clr():
    os.system("cls" if os.name == "nt" else "clear")

# Create a new empty board
def newBoard():
    return [[EMPTY] * COLS for _ in range(ROWS)]

# Make a deep copy of the board
def copyBoard(board):
    return [row[:] for row in board]

# List columns that still have room
def validColumns(board):
    result = []
    for c in range(COLS):
        if board[0][c] == EMPTY:
            result.append(c)
    return result

# Drop a piece into a column, return landing row (-1 if full)
def dropPiece(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return row
    return -1

# Check whether the board is completely full
def isFull(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

# Check if a player has four in a row, return the winning cells
def checkWin(board, player):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + k] == player for k in range(4)):
                return [(r, c + k) for k in range(4)]

    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + k][c] == player for k in range(4)):
                return [(r + k, c) for k in range(4)]

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + k][c + k] == player for k in range(4)):
                return [(r + k, c + k) for k in range(4)]

    for r in range(ROWS - 3):
        for c in range(3, COLS):
            if all(board[r + k][c - k] == player for k in range(4)):
                return [(r + k, c - k) for k in range(4)]

    return None

# Score a single 4-cell window for the AI
def scoreWindow(window, player):
    opp      = PLAYER if player == AI else AI
    pCount   = window.count(player)
    oppCount = window.count(opp)
    empty    = window.count(EMPTY)

    if pCount == 4:
        return 100
    elif pCount == 3 and empty == 1:
        return 5
    elif pCount == 2 and empty == 2:
        return 2

    if oppCount == 4:
        return -100
    elif oppCount == 3 and empty == 1:
        return -4

    return 0

# Score the whole board for the AI
def heuristic(board):
    score = 0

    centreCol = [board[r][COLS // 2] for r in range(ROWS)]
    score += centreCol.count(AI) * 3

    for r in range(ROWS):
        for c in range(COLS - 3):
            w = [board[r][c + k] for k in range(4)]
            score += scoreWindow(w, AI)

    for c in range(COLS):
        for r in range(ROWS - 3):
            w = [board[r + k][c] for k in range(4)]
            score += scoreWindow(w, AI)

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            w = [board[r + k][c + k] for k in range(4)]
            score += scoreWindow(w, AI)

    for r in range(ROWS - 3):
        for c in range(3, COLS):
            w = [board[r + k][c - k] for k in range(4)]
            score += scoreWindow(w, AI)

    return score

nodesSearched = 0

# Pick the best move using minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing):
    global nodesSearched
    nodesSearched += 1

    if checkWin(board, AI):
        return None, 10000 + depth

    if checkWin(board, PLAYER):
        return None, -(10000 + depth)

    if isFull(board) or depth == 0:
        return None, heuristic(board)

    cols = validColumns(board)
    cols.sort(key=lambda c: abs(c - COLS // 2))

    if maximizing:
        bestScore = -math.inf
        bestCol   = cols[0]
        for col in cols:
            b2 = copyBoard(board)
            dropPiece(b2, col, AI)
            _, score = minimax(b2, depth - 1, alpha, beta, False)
            if score > bestScore:
                bestScore = score
                bestCol   = col
            alpha = max(alpha, bestScore)
            if beta <= alpha:
                break
        return bestCol, bestScore

    else:
        bestScore = math.inf
        bestCol   = cols[0]
        for col in cols:
            b2 = copyBoard(board)
            dropPiece(b2, col, PLAYER)
            _, score = minimax(b2, depth - 1, alpha, beta, True)
            if score < bestScore:
                bestScore = score
                bestCol   = col
            beta = min(beta, bestScore)
            if beta <= alpha:
                break
        return bestCol, bestScore

# Print the board to the terminal
def displayBoard(board, winCells=None):
    winSet = set(winCells) if winCells else set()

    print()
    print("  " + BOLD + "  1   2   3   4   5   6   7" + RESET)
    print("  " + "─" * 29)

    for r in range(ROWS):
        rowStr = "  |"
        for c in range(COLS):
            v = board[r][c]
            if (r, c) in winSet:
                cell = WINBG + BOLD + "●" + RESET
            elif v == PLAYER:
                cell = WHITE + "●" + RESET
            elif v == AI:
                cell = GREEN + "●" + RESET
            else:
                cell = DIM + "·" + RESET
            rowStr += " " + cell + " |"
        print(rowStr)

    print("  " + "─" * 29)
    print("  " + WHITE + ".. You" + RESET + "   " + GREEN + ".. AI" + RESET)
    print()

DIFFICULTIES = {
    "1": ("Easy",   3),
    "2": ("Medium", 5),
    "3": ("Hard",   7),
}

# Ask the user to choose a difficulty level
def pickDifficulty():
    clr()
    print("╔══════════════════════════════════════════╗")
    print("║              CONNECT FOUR                ║")
    print("╠══════════════════════════════════════════╣")
    print("║                                          ║")
    print("║   Choose AI difficulty:                  ║")
    print("║                                          ║")
    print("║   1)  Easy   (depth 3)                   ║")
    print("║   2)  Medium (depth 5)  <- recommended   ║")
    print("║   3)  Hard   (depth 7)                   ║")
    print("║                                          ║")
    print("╚══════════════════════════════════════════╝")
    print()
    while True:
        c = input("  Choice (1-3): ").strip()
        if c in DIFFICULTIES:
            name, d = DIFFICULTIES[c]
            print()
            print("  AI set to", BOLD + name + RESET, "(looks", d, "moves ahead).")
            time.sleep(1)
            return d
        print("  Please enter 1, 2, or 3.")

# Ask the user for their next move
def getPlayerMove(board):
    cols = validColumns(board)
    while True:
        raw = input("  " + WHITE + "Your move" + RESET + " (column 1-7): ").strip()
        if not raw.isdigit():
            print("  Type a number between 1 and 7.")
            continue
        col = int(raw) - 1
        if col not in cols:
            print("  That column is full or out of range. Try another.")
            continue
        return col

# Play one full game, return 'player', 'ai', or 'draw'
def playGame(depth):
    global nodesSearched
    board = newBoard()

    while True:
        clr()
        displayBoard(board)
        col = getPlayerMove(board)
        dropPiece(board, col, PLAYER)

        win = checkWin(board, PLAYER)
        if win:
            clr()
            displayBoard(board, win)
            print("  " + WINBG + BOLD + " You win! Well played! " + RESET)
            print()
            return "player"

        if isFull(board):
            clr()
            displayBoard(board)
            print("  " + DIM + "It's a draw." + RESET)
            print()
            return "draw"

        displayBoard(board)
        print("  " + GREEN + "AI is thinking..." + RESET)

        nodesSearched = 0
        t0 = time.time()
        aiCol, aiScore = minimax(board, depth, -math.inf, math.inf, True)
        elapsed = round(time.time() - t0, 2)

        dropPiece(board, aiCol, AI)

        print("  " + GREEN + "AI dropped in column", aiCol + 1, RESET)
        print("  " + DIM + "Nodes searched:", str(nodesSearched) + "  |  Time:", str(elapsed) + "s  |  Score:", aiScore, RESET)
        time.sleep(0.8)

        win = checkWin(board, AI)
        if win:
            clr()
            displayBoard(board, win)
            print("  " + GREEN + BOLD + "AI wins this round." + RESET)
            print()
            return "ai"

        if isFull(board):
            clr()
            displayBoard(board)
            print("  " + DIM + "It's a draw." + RESET)
            print()
            return "draw"

# Run the difficulty menu and the main game loop
def main():
    depth  = pickDifficulty()
    scores = {"player": 0, "ai": 0, "draw": 0}

    while True:
        result = playGame(depth)
        scores[result] += 1

        print("  Score  ->  ",
              WHITE + "You: " + str(scores["player"]) + RESET,
              " ",
              GREEN + "AI: " + str(scores["ai"]) + RESET,
              " ",
              DIM + "Draws: " + str(scores["draw"]) + RESET)
        print()

        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            clr()
            print("  Thanks for playing!")
            print()
            break

if __name__ == "__main__":
    main()