import sys



sys.stdout = open('output.txt','w')
sys.stdin = open('input.txt','r')



if __name__ == '__main__':
    print('Hello World')