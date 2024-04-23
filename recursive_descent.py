def match(expected):
    global i
    if i < len(s) and s[i] == expected:
        i += 1
        return True
    return False

def S():
    return match('a') and A() and match('c')

def A():
    return match('b') and A() or True


def B():
    return match('b')

s = list(input("Enter the string: "))
i = 0

print("Grammar:")
print("S -> aAc")
print("A -> b | bA")
print("B -> b\n")

if S() and i == len(s):
    print("String is accepted")
else:
    print("String is not accepted")
