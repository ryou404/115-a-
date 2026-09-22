import sys

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        for _ in range(n):
            print("Hello world!")

if __name__ == "__main__":
    main()