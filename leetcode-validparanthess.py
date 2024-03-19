class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if len(s)%2 ==1:
            return False
        d={'(':')',
        '{':'}',
        '[':']'}
        for i in s:
            if i in ['(','{','[']:
                print(i)
                st.append(d[i])
            else:
                if len(st)== 0 or i!= st.pop():
                    return False
        return len(st)==0
