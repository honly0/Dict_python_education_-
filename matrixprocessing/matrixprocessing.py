def read_matrix_with_size(size_prompt: str, matrix_prompt: str):
    n, m = map(int, input(size_prompt).split())
    print(matrix_prompt)
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix, n, m


def read_matrix(size_prompt: str, matrix_prompt: str):
    n, m = map(int, input(size_prompt).split())
    print(matrix_prompt)
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix


def print_number(x: float) -> str:
    s = f"{x:.2f}"
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(print_number(x) for x in row))


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("The operation cannot be performed.")
        return
    n, m = len(a), len(a[0])
    result = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]
    print("The result is:")
    print_matrix(result)


def multiply_by_constant(a, const):
    n, m = len(a), len(a[0])
    result = [[a[i][j] * const for j in range(m)] for i in range(n)]
    print("The result is:")
    print_matrix(result)


def multiply_matrices(a, b):
    n, m = len(a), len(a[0])
    n2, m2 = len(b), len(b[0])
    if m != n2:
        print("The operation cannot be performed.")
        return
    result = [[0.0 for _ in range(m2)] for _ in range(n)]
    for i in range(n):
        for j in range(m2):
            s = 0.0
            for k in range(m):
                s += a[i][k] * b[k][j]
            result[i][j] = s
    print("The result is:")
    print_matrix(result)


def transpose_main_diagonal(a):
    n, m = len(a), len(a[0])
    result = [[a[j][i] for j in range(n)] for i in range(m)]
    return result


def transpose_side_diagonal(a):
    n, m = len(a), len(a[0])
    result = [[0.0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - 1 - j][n - 1 - i] = a[i][j]
    return result


def transpose_vertical(a):
    return [list(reversed(row)) for row in a]


def transpose_horizontal(a):
    return list(reversed(a))


def determinant(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n != m:
        raise ValueError("Determinant is defined only for square matrices")

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0.0
    for j in range(n):
        
        minor = []
        for r in range(1, n):
            row = []
            for c in range(n):
                if c == j:
                    continue
                row.append(matrix[r][c])
            minor.append(row)
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det


def inverse_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n != m:
        raise ValueError("Inverse is defined only for square matrices")

    
    aug = [row[:] + [0.0] * n for row in matrix]
    for i in range(n):
        aug[i][n + i] = 1.0

    
    for col in range(n):
        
        pivot_row = None
        for r in range(col, n):
            if abs(aug[r][col]) > 1e-9:
                pivot_row = r
                break
        if pivot_row is None:
            raise ValueError("Matrix is singular")

        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        pivot = aug[col][col]
        
        for c in range(2 * n):
            aug[col][c] /= pivot

        
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            for c in range(2 * n):
                aug[r][c] -= factor * aug[col][c]

    
    inverse = [row[n:] for row in aug]
    return inverse


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "0":
            break

        elif choice == "1":
            a, n1, m1 = read_matrix_with_size("Enter size of first matrix: ",
                                              "Enter first matrix:")
            b, n2, m2 = read_matrix_with_size("Enter size of second matrix: ",
                                              "Enter second matrix:")
            add_matrices(a, b)
            print()

        elif choice == "2":
            a, n, m = read_matrix_with_size("Enter size of matrix: ",
                                            "Enter matrix:")
            const = float(input("Enter constant: "))
            multiply_by_constant(a, const)
            print()

        elif choice == "3":
            a, n1, m1 = read_matrix_with_size("Enter size of first matrix: ",
                                              "Enter first matrix:")
            b, n2, m2 = read_matrix_with_size("Enter size of second matrix: ",
                                              "Enter second matrix:")
            multiply_matrices(a, b)
            print()

        elif choice == "4":
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            t_choice = input("Your choice: ")

            matrix, n, m = read_matrix_with_size("Enter matrix size: ",
                                                 "Enter matrix:")

            if t_choice == "1":
                result = transpose_main_diagonal(matrix)
            elif t_choice == "2":
                result = transpose_side_diagonal(matrix)
            elif t_choice == "3":
                result = transpose_vertical(matrix)
            elif t_choice == "4":
                result = transpose_horizontal(matrix)
            else:
                continue

            print("The result is:")
            print_matrix(result)
            print()

        elif choice == "5":
            matrix, n, m = read_matrix_with_size("Enter matrix size: ",
                                                 "Enter matrix:")
            if n != m:
                print("The operation cannot be performed.")
            else:
                det = determinant(matrix)
                print("The result is:")
                print(print_number(det))
            print()

        elif choice == "6":
            matrix, n, m = read_matrix_with_size("Enter matrix size: ",
                                                 "Enter matrix:")
            if n != m:
                print("This matrix doesn't have an inverse.")
            else:
                det = determinant(matrix)
                if abs(det) < 1e-9:
                    print("This matrix doesn't have an inverse.")
                else:
                    inv = inverse_matrix(matrix)
                    print("The result is:")
                    print_matrix(inv)
            print()


if __name__ == "__main__":
    main()