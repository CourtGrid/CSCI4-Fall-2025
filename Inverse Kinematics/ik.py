import math

#Using trigonometry to find the angles a 2 joint robot
#has to bend at in order to end up in a particular position

#Length of arms(known):
# a = 
# b = 

# Coordinate of first joint (beginning of arm(known)) (x,y)
# Coordinate of the end of the second arm (hand(known)) (q,p)

def inverse_kinematic():
    
    arm_a = 1
    arm_b = 1
    #arm_a is the arm connected to both joints and arm_b is connected to the hand

    joint_1 = [3,3]
    hand = [2,2]
    #In a 2D space, the coordinates for the first joint and the hypothetical hand.
    #The 2nd joint is unknown (and will remain unknown unfortunately. Spoiler alert: I never
    #Figure that bit out)

    side_c = math.dist(joint_1, hand)

    #(side_c**2) = (arm_a**2) + (arm_b) - 2*arm_a*arm_b*math.cos(C)
    #I rearranged the formula myself before I found the math website that explains
    #how to do this already gave the formal rearranged
    angle_c = math.acos(((arm_a**2) + (arm_b**2) - (side_c**2)) / (2*arm_a*arm_b))

    C = math.pi-angle_c

    print("Joint 2 is Bent at", math.degrees(C), "Degrees!")
    #If starting out the robot arms are in a straight line (180 degrees), this is how many degrees
    #this joint has to bend into 

    angle_a = math.acos(((side_c**2) + (arm_b**2) - (arm_a**2)) / (2*side_c*arm_b))

    weird_angle_bit = math.atan((hand[1]-joint_1[1])/(hand[0]-joint_1[0]))

    A = angle_a + weird_angle_bit
    
    print("Joint 1 is Bent at", math.degrees(A), "Degrees!")


print(inverse_kinematic())

#This folder SHOULD have an image that kind of helps to visualize what I was going for
