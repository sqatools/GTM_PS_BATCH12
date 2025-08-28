n = int(input("Enter size for T pattern : "))
def print_T_pattern(size):
    for row in range(size):
        for col in range(size):
            if row == 0 or col == size // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

print_T_pattern(n)