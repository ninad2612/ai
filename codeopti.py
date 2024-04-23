class Operand:
    def __init__(self, l, r):
        self.l = l
        self.r = r

def main():
    op = [Operand(input("left: "), input("right: ")) for _ in range(int(input("Enter the Number of Values: ")))]
    print("\nIntermediate Code:")
    for o in op:
        print(o.l + "=" + o.r)
    
    pr = []
    for i, o1 in enumerate(op):
        if i == 0 or o1.l != op[i-1].l:
            pr.append(o1)
    
    print("\nAfter Dead Code Elimination:")
    for p in pr:
        print(p.l + "=" + p.r)
    
    for i, p1 in enumerate(pr):
        for p2 in pr[i+1:]:
            if p1.r == p2.r:
                p2.l = ""
    
    print("\nAfter Common Subexpression Elimination:")
    for p in pr:
        if p.l != "":
            print(p.l + "=" + p.r)

if __name__ == "__main__":
    main()

# Enter the Number of Values: 5
# left: a
# right: 9
# left: b
# right: c+d
# left: e
# right: c+d
# left: f
# right: b+e
# left: r
# right: f
