#iterative
S="mujhe lectures do"
L=len(S)
for i in range(L-1,-1,-1):
    print(S[i],end='')
#recursion
def rev(S):
    if len(S)==0:
        return S
    else:
        return rev(S[1:])+S[0]
