class Solution(object):
 
    def reverseString(self, s):
        def val(f,l):
            if f>l:
                return
            s[f],s[l]=s[l],s[f]
            return val(f+1,l-1)
        val(0,len(s)-1)

        