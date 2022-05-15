def naive_string_match(T, P):
    n = len(T)
    m = len(P)
    shift = []
    for i in range(n - m + 1):
        for j in range(m):
            if T[i + j] != P[j]:
                break
            if j == m - 1:
                shift.append(i)
    return shift

def prefix_function(P):
    m = len(P)
    pi = []
    pi.append(0)
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]
        if P[k] == P[q]:
            k = k + 1
        pi.append(k)
    return pi

def kmp_string_match(T, P):
    n = len(T)
    m = len(P)
    shift = []
    pi = prefix_function(P)
    q = 0
    for i in range(0, n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            shift.append(i - m + 1)
            q = pi[q - 1]
    return shift

table = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^',
        '_','`','{','|','}','~', ' ', '\n', '—', '\t', '＂','＃','＄','％','＆','＇','（','）','＊','＋','，','－',
        '／','：','；','＜','＝','＞','＠','［','＼','］','＾','＿','｀','｛','｜','｝','～','｟','｠','｢','｣','、',
        '〃','〈','〉','《','》','「','」','『','』','【','】','〔','〕','〖','〗','〘','〙','〚','〛','〜','〝','〞',
        '〟','〰','–','—','‘','’','‛','“','”','„','‟','…','‧','﹏','﹑','﹔','·','！','？','｡','。']
table_map = {'0' : 0,'1' : 1,'2' : 2,'3' : 3,'4' : 4,'5' : 5,'6' : 6,'7' : 7,'8' : 8,'9' : 9,
            'a' : 10,'b' : 11,'c' : 12,'d' : 13,'e' : 14,'f' : 15,'g' : 16,'h' : 17,'i' : 18,'j' : 19,'k' : 20,'l' : 21,'m' : 22,'n' : 23,
            'o' : 24,'p' : 25,'q' : 26,'r' : 27,'s' : 28,'t' : 29,'u' : 30,'v' : 31,'w' : 32,'x' : 33,'y' : 34,'z' : 35,
            'A' : 36,'B' : 37,'C' : 38,'D' : 39,'E' : 40,'F' : 41,'G' : 42,'H' : 43,'I' : 44,'J' : 45,'K' : 46,'L' : 47,'M' : 48,'N' : 49,
            'O' : 50,'P' : 51,'Q' : 52,'R' : 53,'S' : 54,'T' : 55,'U' : 56,'V' : 57,'W' : 58,'X' : 59,'Y' : 60,'Z' : 61,
            '!' : 62,'\"' : 63,'#' : 64,'$' : 65,'%' : 66,'&' : 67,'\'' : 68,'(' : 69,')' : 70,'*' : 71,'+' : 72,',' : 73,'-' : 74,'.' : 75,
            '/' : 76,':' : 77,';' : 78,'<' : 79,'=' : 80,'>' : 81,'?' : 82,'@' : 83,'[' : 84,'\\' : 85,']' : 86,'^' : 87,'_' : 88,'`' : 89,
            '{' : 90,'|' : 91,'}' : 92,'~' : 93, ' ' : 94, '\n' : 95, '—' : 96, '\t' : 97, '＂' : 98,'＃' : 99,'＄' : 100,'％' : 101,'＆' : 102,
            '＇' : 103,'（' : 104,'）' : 105,'＊' : 106,'＋' : 107,'，' : 108,'－' : 109,'／' : 110,'：' : 111,'；' : 112,'＜' : 113,'＝' : 114,
            '＞' : 115,'＠' : 116,'［' : 117,'＼' : 118,'］' : 119,'＾' : 120,'＿' : 121,'｀' : 122,'｛' : 123,'｜' : 124,'｝' : 125,'～' : 126,
            '｟' : 127,'｠' : 128,'｢' : 129,'｣' : 130,'、' : 131,'〃' : 132,'〈' : 133,'〉' : 134,'《' : 135,'》' : 136,'「' : 137,'」' : 138,
            '『' : 139,'』' : 140,'【' : 141,'】' : 142,'〔' : 143,'〕' : 144,'〖' : 145,'〗' : 146,'〘' : 147,'〙' : 148,'〚' : 149,'〛' : 150,
            '〜' : 151,'〝' : 152,'〞' : 153,'〟' : 154,'〰' : 155,'–' : 156,'—' : 157,'‘' : 158,'’' : 159,'‛' : 160,'“' : 161,'”' : 162,
            '„' : 163,'‟' : 164,'…' : 165,'‧' : 166,'﹏' : 167,'﹑' : 168,'﹔' : 169,'·' : 170,'！' : 171,'？' : 172,'｡' : 173,'。' : 174}

def bmbc(P):
    m = len(P)
    bc = []
    for i in range(len(table)):
        bc.append(m)
    for i in range(m - 1):
        bc[table_map[P[i]]] = m - i - 1
    return bc

def suffix(P):
    m = len(P)
    suff = []
    for i in range(m):
        suff.append(m)
    g = m - 1
    f = m - 1
    for i in range(m - 2, -1, -1):
        if i > g and suff[i + m - 1 - f] < i - g:
            suff[i] = suff[i + m - 1 - f]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and P[g] == P[g + m - 1 - f]:
                g = g - 1
            suff[i] = f - g
    return suff

def bmgs(P):
    m = len(P)
    suff = suffix(P)
    gs = []
    for i in range(m):
        gs.append(m)
    j = 0
    for i in range(m - 2, -1, -1):
        if suff[i] == i + 1:
            while j < m - i - 1:
                if gs[j] == m:
                    gs[j] = m - i - 1
                j = j + 1
    for i in range(m - 1):
        gs[m - 1 - suff[i]] = m - 1 - i
    return gs



def bm_string_match(T, P):
    n = len(T)
    m = len(P)
    shift = []
    bc = bmbc(P)
    gs = bmgs(P)
    s = 0
    out = False
    while s <= n - m:
        i = m - 1
        while P[i] == T[s + i]:
            if i == 0:
                shift.append(s)
                s = s + gs[0]
                out = True
                break
            else:
                i = i - 1
        if out:
            out = False
            continue
        else:
            s = s + max(gs[i], bc[table_map[T[s + i]]] - m + i + 1)
    return shift

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="string match, some special char cannot use by the command line and you better use the file to input",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-itf', '--input-text-file', dest='input_text_path', default="",
        help="input path of a text file")
    parser.add_argument(
        '-ipf', '--input-pattern-file', dest='input_pattern_path', default="",
        help="input path of a pattern file")
    parser.add_argument(
        '-it', '--input-text', dest='input_text', default="",
        help="input path of a text")
    parser.add_argument(
        '-ip', '--input-pattern', dest='input_pattern', default="",
        help="input path of a pattern")
    parser.add_argument(
        '-o', '--output-file', dest='output_file', default="",
        help="path of recording output file")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    T = ''
    P = ''
    if len(args.input_text_path) == 0 and len(args.input_text) == 0:
        raise ValueError('need the input text file or input text')
    if len(args.input_pattern_path) == 0 and len(args.input_pattern) == 0:
        raise ValueError('need the input pattern file or input pattern')
    if len(args.input_text_path) != 0:
        with open(args.input_text_path, encoding='utf8') as f:
            T = f.read()
    else:
        T = args.input_text
    if len(args.input_pattern_path) != 0:
        with open(args.input_pattern_path, encoding='utf-8') as f:
            P = f.read()
    else:
        P = args.input_pattern
    
    n = len(T)
    m = len(P)
    if m > n:
        raise ValueError('the length of pattern is longer than the text')
    if m == 0:
        raise ValueError('the length of pattern is zero')
    for i in range(n):
            if T[i] not in table:
                ValueError('the letter in the text is beyond which is supported')
    for i in range(m):
            if P[i] not in table:
                ValueError('the letter in the text is beyond which is supported')

    import time
    start = time.time()
    s_1 = naive_string_match(T, P)
    t_1 = time.time()
    s_2 = kmp_string_match(T, P)
    t_2 = time.time()
    s_3 = bm_string_match(T, P)
    t_3 = time.time()
    fail = False
    for i in range(max(len(s_1), len(s_2), len(s_3))):
        if s_1[i] == s_2[i] and s_1[i] == s_3[i]:
            continue
        else:
            fail = True
            print('error')
            return
    if not fail:
        print('right')
    print('shift list:', s_1)
    print(f"naive time:{t_1 - start}s, kmp time:{t_2 - t_1}s, bm time:{t_3 - t_2}s")
    if len(args.output_file) != 0:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write('right')
            f.write('\n')
            f.write('shift list:')
            for i in range(len(s_1)):
                f.write(str(s_1[i]))
                f.write(' ')
            f.write('\n')
            f.write(f"naive time:{t_1 - start}s, kmp time:{t_2 - t_1}s, bm time:{t_3 - t_2}s")

if __name__ == "__main__":
    main()