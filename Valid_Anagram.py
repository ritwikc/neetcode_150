class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = dict()
        t_freq = dict()
        t_set=set()
        
        flag=True
        for i in s:
            if i in s_freq:
                s_freq[i] = s_freq[i]+1
            else:
                s_freq[i]=1
         
        for i in t:
            if i in t_freq:
                t_freq[i] = t_freq[i]+1
            else:
                t_freq[i]=1
                t_set.add(i)
        
        for i in s_freq:
            if i in t_freq:
                if s_freq[i] != t_freq[i]:
                    flag=False
                    break
                else:
                    t_set.remove(i)
                    flag=True
            else:
                flag=False
                break
        if flag==True:
            if len(t_set) > 0:
                flag=False
        
        return(flag)
