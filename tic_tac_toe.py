mat = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
x = "X"
o = "O"
border = 9 * "-"


def print_grid():
    print(border)
    for i in range(3):
        print(f"| {' '.join(mat[i])} |")
    print(border)


def get_coordinates(sym):
    global mat
    while True:
        coords = input("Enter coordinates: ").split()
        try:
            row = int(coords[0])
            col = int(coords[1])
            assert 1 <= row <= 3
            assert 1 <= col <= 3
        except IndexError:
            continue
        except ValueError:
            print("You should enter numbers!")
            continue
        except AssertionError:
            print("Coordinates should be from 1 to 3!")
            continue
        if mat[row - 1][col - 1] == " ":
            mat[row - 1][col - 1] = sym
            break
        else:
            print("This cell is occupied! Choose another one!")


def wins_check_diagonal(matrix, sym):
    sym_counter = 0
    for i in range(0, 3):
        if matrix[i][i] == sym:
            sym_counter += 1
    if sym_counter == 3:
        return True
    else:
        sym_counter = 0
        for i in range(0, 3):
            if matrix[i][abs(i - 2)] == sym:
                sym_counter += 1
        if sym_counter == 3:
            return True
        return False


def wins_check_horizontal(matrix, sym):
    for i in range(0, 3):
        if matrix[i] == [sym, sym, sym]:
            return True
        return False


def wins_check_vertical(matrix, sym):
    sym_counter = 0
    for i in range(0, 3):
        if matrix[i][0] == sym:
            sym_counter += 1
    if sym_counter == 3:
        return True
    else:
        sym_counter = 0
        for i in range(0, 3):
            if matrix[i][1] == sym:
                sym_counter += 1
        if sym_counter == 3:
            return True
        else:
            sym_counter = 0
            for i in range(0, 3):
                if matrix[i][2] == sym:
                    sym_counter += 1
            if sym_counter == 3:
                return True
            return False


def game_state_check():
    grid_list = [i for j in mat for i in j]
    if wins_check_horizontal(mat, x) or wins_check_vertical(mat, x) or wins_check_diagonal(mat, x):
        print("X wins")
        return True
    elif wins_check_horizontal(mat, o) or wins_check_vertical(mat, o) or wins_check_diagonal(mat, o):
        print("O wins")
        return True
    elif " " in grid_list:
        return False
    else:
        print("Draw")
        return True


def play_game():
    print_grid()
    print("X starts!")
    while True:
        get_coordinates(x)
        print_grid()
        if game_state_check():
            break
        get_coordinates(o)
        print_grid()
        if game_state_check():
            break


def main():
    play_game()


if __name__ == "__main__":
    main()
