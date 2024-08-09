# KMP법으로 문자열 검색하기

def KMP_match(txt:str, pat:str) -> int:
    pt = 0
    pp = 0
    skip = [0] * (len(pat)+1)

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip = pp
        elif pp == 0:
            pt += 1
            skip[pt] =pp
        else:
            pp = skip[pp]

    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp ==0:
            pt += 1
        else:
            pp = skip[pp]

    return pt-pp if pp==len(pat) else -1



if __name__=='__main__':
    s1=int(input('텍스트를 입력하세요.:'))
    s2=int(input('패턴을 입력하세요.:'))

    idx = KMP_match(s1,s2)

    if idx == -1:
        print('일치하는 패턴이 없습니다.')

    else:
        print(f'{idx+1}번째 문자가 일치합니다.')