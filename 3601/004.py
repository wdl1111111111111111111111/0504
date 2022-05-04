class Solution:
    def trans(self , s: str, n: int) -> str:
        if len( ''.join( s.split(" ")[::-1]))==n:
            s_new=s
        else:
             s_new= ' '.join( s.split(" ")[::-1])
        c=''
        for word in s_new:
            if word.isupper():
                c+=word.lower()
            elif word.islower():
                c+=word.upper()
            else:
                c+=" "
        return c