class Solution(object):
    
    def intToRoman(self, num):
        def OneByOne(num, power):
            res=''
            for i in range(num):
                if power==1:
                    if num<4:
                        res+='I'
                    elif num==4:
                        return 'IV'
                    elif num==5:
                        return 'V'
                    elif num==6:
                        return 'VI'
                    elif num==7:
                        return 'VII'  
                    elif num==8:
                        return 'VIII'
                    elif num==9:
                        return 'IX'

                elif power==10:
                    if num<4:
                        res+='X'
                    elif num==4:
                        return 'XL'
                    elif num==5:
                        return 'L'
                    elif num==6:
                        return 'LX'
                    elif num==7:
                        return 'LXX'  
                    elif num==8:
                        return 'LXXX'
                    elif num==9:
                        return 'XC'

                elif power==100:
                    if num<4:
                        res+='C'
                    elif num==4:
                        return 'CD'
                    elif num==5:
                        return 'D'
                    elif num==6:
                        return 'DC'
                    elif num==7:
                        return 'DCC'  
                    elif num==8:
                        return 'DCCC'
                    elif num==9:
                        return 'CM'

                elif power==1000:
                    res+='M'
            return res
        arr=[]
        n=num
        output=""
        while n>0:
            arr.append(n%10)
            n=n//10
        for i in range(len(arr),0,-1):
            output+=OneByOne(arr[i-1],10**(i-1))
        return output

        
