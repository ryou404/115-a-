import sys

def main():
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        a = int(tokens[0])
        b = int(tokens[1])
        print(f"{a}+{b}={a + b}")

if __name__ == "__main__":
    main()