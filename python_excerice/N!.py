    def fact(n):
        if n==1:
            return n
        else:
            return n*fact(n-1)



    def fact_iter(n):
        sum=1
        i = 0
        if n==0 or n==1:
            return 1

        else:
            for i in range(2,n+1):
                sum = sum*i
        return   sum


    def fibon(n):
        if n==0 or n==1 :
            return 1
        else:
            return fibon(n-1) + fibon(n-2)




