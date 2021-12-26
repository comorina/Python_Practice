import sys

if __name__ == '__main__':
    sys.stdout = open('output.txt','w')
    sys.stdin = open('input.txt','r')


    def show(**y):
        print(y,type(y), sep="->")
        return 

    res = show(y=(7,55,'dd'))
    print(res)