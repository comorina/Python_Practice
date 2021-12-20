import sys 
sys.stdout = open('output.txt','w')
sys.stdin = open('input.txt','r')



if __name__ == '__main__':
    def fib(limit):
        a =0; b=1
        while a<limit:
            yield a
            a,b = b, a+b

    for i in fib(5):
        print(i)    

    #def fibb(x):
      #  if x == 0:
       #     return 0
      #  if x == 1:
      #      return 0
       # result = fibb(x-1)+fibb(x-2); print(result)
       # return 
    #fibb(5)