import math
def pattern(name):

    list2 = []
    for i in range(len(name)):
        if name[i] == "A":
            print_A = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col == 0 or col == 5) and row != 0) or (
                        row == 0 or row == 5 and (col != 0 and col != 5)
                    ):
                        print_A[row][col] = "*"
            list2.append(print_A)

        if name[i] == "B":
            print_B = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (
                        col == 0
                        or ((row == 3 or row == 0 or row == 6) and col != 5)
                        or (col == 5 and (row != 3 and row != 0))
                    ):
                        print_B[row][col] = "*"
            list2.append(print_B)

        if name[i] == "C":
            print_C = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 and (row != 0 and row != 6)) or (
                        (row == 0 or row == 6) and col != 0
                    ):
                        print_C[row][col] = "*"
            list2.append(print_C)

        if name[i] == "D":
            print_D = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (
                        col == 0
                        or (col == 5 and (row != 0 and row != 6))
                        or ((row == 0 or row == 6))
                    ):
                        print_D[row][col] = "*"
            list2.append(print_D)

        elif name[i] == "E":
            print_E = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or row == 3 or row == 0 or row == 6:
                        print_E[row][col] = "*"
            list2.append(print_E)

        elif name[i] == "F":
            print_F = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or row == 3 or row == 0:
                        print_F[row][col] = "*"
            list2.append(print_F)

        elif name[i] == "G":
            print_G = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (
                        col == 0
                        or (col == 4 and (row != 1 and row != 2))
                        or (
                            (row == 0 and (col > 0 and col < 4))
                            or (row == 3 or col == 5)
                        )
                    ):
                        print_G[row][col] = "*"
            list2.append(print_G)

        elif name[i] == "H":
            print_H = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or col == 5 or row == 3:
                        print_H[row][col] = "*"
            list2.append(print_H)

        elif name[i] == "I":
            print_I = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 2 or ((row == 0 and row == 6) and col != 5):
                        print_I[row][col] = "*"

            list2.append(print_I)

        elif name[i] == "J":
            print_J = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 2 or (row == 0 and col != 2) or (row == 6 and col < 3):
                        print_J[row][col] = "*"

            list2.append(print_J)

        elif name[i] == "K":
            print_K = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or row + col == 3 or row - col == 3:
                        print_K[row][col] = "*"
            list2.append(print_K)

        elif name[i] == "L":
            print_L = [[" " for row in range(6)] for col in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or row == 6:
                        print_L[row][col] = "*"
            list2.append(print_L)

        elif name[i] == "M":
            print_M = [[" " for row in range(6)] for col in range(7)]
            for row in range(7):
                for col in range(6):
                    if (
                        col == 0
                        or col == 6
                        or ((row == col) and (col > 0 and col < 4))
                        or (row == 1 and col == 5)
                        or (row == 2 and col == 4)
                    ):
                        print_M[row][col] = "*"
            list2.append(print_M)

        elif name[i] == "N":
            print_N = [[" " for i in range(6)] for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or col == 5 or (row == col and (col > 0 and col < 5)):
                        print_N[row][col] = "*"
            list2.append(print_N)

        elif name[i] == "O":
            print_O = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (
                        (col == 0 or col == 4)
                        and (row != 0 and row != 6)
                        or row == 0
                        or row == 6
                        and (col > 0 and col < 4)
                    ):
                        print_O[row][col] = "*"
            list2.append(print_O)

        elif name[i] == "P":
            print_P = [[" " for i in range(7)] for j in range(6)]
            for row in range(6):
                for col in range(7):
                    if (
                        col == 0
                        or (col == 4 and (row == 1 or row == 2))
                        or ((row == 0 or row == 3) and (col > 0 and col < 4))
                    ):
                        print_P[row][col] = "*"

            list2.append(print_P)

        elif name[i] == "Q":
            print_Q = [[" " for i in range(7)] for j in range(6)]
            for row in range(6):
                for col in range(7):
                    if (
                        (col == 0 or col == 4)
                        and (row > 0 and row < 6)
                        or ((row == 0 or row == 6) and (col > 0 and col < 4))
                        or (row == 5 and col == 1)
                        or (row == 7 and col == 3)
                    ):
                        print_Q[row][col] = "*"
            list2.append(print_Q)

        elif name[i] == "R":
            print_R = [[" " for i in range(7)] for j in range(6)]
            for row in range(6):
                for col in range(7):
                    if (
                        col == 0
                        or (col == 4 and (row != 0 and row != 3))
                        or (row == 0 or row == 3 and (col > 0 and col < 4))
                    ):
                        print_R[row][col] = "*"
            list2.append(print_R)

        elif name[i] == "S":
            print_S = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (
                        ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4))
                        or (col == 0 and (row > 0 and row < 3))
                        or (col == 4 and (row > 3 and row < 6))
                    ):
                        print_S[row][col] = "*"
            list2.append(print_S)

        elif name[i] == "T":
            print_T = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 2 or row == 0:
                        print_T[row][col] = "*"

            list2.append(print_T)

        elif name[i] == "U":
            print_U = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col == 0 or col == 5) and row!=6) or (row==6 and (col!=0 and col!=5)):
                        print_U[row][col] = "*"

            list2.append(print_U)

        elif name[i] == "V":
            i = 0
            j = 6
            print_V = [[" " for i in range(7)] for j in range(6)]
            for row in range(4):
                for col in range(7):
                    if (row == col):
                     print_V[row][col]= "*"
                    elif(row==i and col ==j):
                        print_V[row][col]= "*"
                        i = i+1
                        j = j-1
                       

            list2.append(print_V) 
                
                
        elif name[i] == "W":
            i = 0
            j = 3
            print_W = [[" " for i in range(7)] for j in range(6)]
            for row in range(4):
                for col in range(7):
                    if (
                        col == 0
                        or col == 6
                        or (col == 5 and row == 2)
                        or (col == 4 and row == 1)
                    ):
                        print_W[row][col] = "*"
                    elif row == i and col == j:
                        print_W[row][col] = "*"

                        i = i + 1
                        j = j - 1

            list2.append(print_W)

        elif name[i] == "X":
          print_X = [[" " for i in range(7)] for j in range(6)]
          for row in range(6):
            for col in range(6):
                if row == col or row+col==5:
                    print_X[row][col] = "*"
          list2.append(print_X)

        elif name[i] == "Y":
            print_Y = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (
                        (col == 2 and row > 1)
                        or (row == col and col < 2)
                        or (row == 0 and col == 4)
                        or (row == 1 and col == 3)
                    ):
                        print_Y[row][col] = "*"
            list2.append(print_Y)

        elif name[i] == "Z":
            i = 1
            j = 4
            print_Z = [[" " for i in range(6)] for j in range(6)]
            for row in range(6):
                for col in range(6):
                    if row == 0 or row == 5:
                        print_Z[row][col] = "*"
                    elif row == i and col == j:
                        print_Z[row][col] = "*"
                        i = i + 1
                        j = j - 1

            list2.append(print_Z)
    return list2


name = input("Enter name: ")
length1 = int(input("Enter the length: "))
x = pattern(name)
y = []
for j in range(math.ceil(len(x) / length1)):
    y = x[:length1]
    for i in range(7):
        for letter in y:
            for col in range(6):
                print(letter[i][col], end=" ")
            print(" ", end="")
        if i == 3 and len(x) != length1:
            print("****", end="")
        print()
    x=x[length1:]