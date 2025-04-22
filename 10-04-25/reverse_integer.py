class Solution(object):
    def reverse(self, x):
        temp =""
        int_str =str(x)
        for i in range(len(int_str)-1,-1,-1):
            if "-" not in int_str:
                temp +=int_str[i]

            else:
                if i>0:
                    temp =temp+int_str[i]
                if i== 0 and "-" == int_str[i]:
                    temp =int_str[i]+temp
                    
        if int(temp) < -2**31 or int(temp) > 2**31 - 1:
            return 0
            
        return int(temp)
