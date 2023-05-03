def mutate_string(string, pos, char):
    list1 = list(string)
    list1[pos-1] = char
    string = "".join(list1)
    return string

if __name__ == "__main__":
    s = input()
p, c = input().split()
s_new = mutate_string(s, int(p), c)
print(s_new)