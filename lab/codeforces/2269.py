import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    
    ans= 2*((2**(n-k))+ k)-2
    print(ans)

def main():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)
    
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()