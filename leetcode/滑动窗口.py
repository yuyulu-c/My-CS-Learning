
'''
最小覆盖子串-76
给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。
测试用例保证答案唯一。
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count=len(t)
        need={}
        for x in t:
            need[x]=need.get(x,0)+1
        left=0
        ans=(0,float('inf'))

        for right,x in enumerate(s):
            if x in need:
                need[x]-=1
                if need[x]>=0:
                    count-=1
            while count==0:
                if right-left<ans[1]-ans[0]:
                    ans=(left,right)
                left_char=s[left]
                if left_char in need:
                    need[left_char]+=1
                    if need[left_char]>0:
                        count+=1
                left+=1

        return '' if ans[1]==float('inf') else s[ans[0]:ans[1]+1]
