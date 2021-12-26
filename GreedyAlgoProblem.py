import sys
def Vote( name):
        if voted.get(name):
            print("Kick them out!")
        else:
            voted[name] = True
            print("Vote first!")

if __name__ == '__main__':

    sys.stdout = open('output.txt','w')
    sys.stdin = open('input.txt','r')
    
    
    voted = {}

    Vote("Shivam")
    Vote("RTam")
    Vote("Shivam")
    print(voted)