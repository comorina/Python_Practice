# This is a Squirrel story base problem.
# Here in this user give (first input) place name where squirrel saw nutshell bundles.
# Second input gave after seen the bundles squirrel what, action taked.

# input format:

# fist input : okala

# second input : collect all and run away.


# output : 
# Squirrel was very hungry. She passed from okala and saw the bundles, and she feeling very happy and start jumpping, she collect and run away.

 # Creating class here
class Nutshell:                             
    def __init__(self, place, action):      # Consturctor
        self.place = place
        self.action = action
    
    def story(self):
        print("Squirrel was very hungry. She passed from {0} and saw the bundles of nutshells, and she feeling very happy and start jumpping, she {1}.".format(self.place, self.action))


# Here the main function: 

if __name__ == '__main__':
    place = input("Enter the any place name : ")
    action = input("Enter an action which are taken by Squirrel : ")
    obj = Nutshell(place, action)   # creating object 
    obj.story()
