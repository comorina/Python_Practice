import sys



sys.stdout = open('output.txt','w')
sys.stdin = open('input.txt','r')


# lambda is anonymous function means he don't need to declare name of function.
# if you are not declare variable value in lambda function like lambda a=0, b=1 then you must be pass variable value in x(0,1) otherwise you get error.
if __name__ == '__main__':
    
  
    x= lambda a, b: a/b
    #x = lambda a=5, b=5: a+b
    print(x(9,3))