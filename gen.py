import sys
import random
table = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

num_T = eval(sys.argv[1])
num_P = eval(sys.argv[2])

def main():
    T = ''
    P = ''
    for i in range(num_T):
        choice = random.randint(0, len(table) - 1)
        T = T + (table[choice])
    for i in range(num_P):
        choice = random.randint(0, len(table) - 1)
        P = P + (table[choice])
    with open('./T.txt', 'w') as f:
        f.write(T)
    with open('./P.txt', 'w') as f:
        f.write(P)

main()
def test():
    T = ''
    with open('./a.txt', encoding='utf-8') as f:
        T = f.read()
    T = T * 10
    with open('./T.txt', 'w', encoding='utf-8') as f:
        f.write(T)
