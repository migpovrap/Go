from FP2324P2 import go

def main():
    while True:
        try:
            size = int(input("Select the size of the board (9, 13, or 19): "))
            if size not in {9, 13, 19}:
                raise ValueError
            break
        except ValueError:
            print("Invalid. Choose form the list 9, 13, or 19.")
    go(size, (), ())

if __name__ == "__main__":
    main()