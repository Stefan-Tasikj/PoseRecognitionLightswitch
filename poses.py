import numpy as np

def calculate_angle(a,b,c):
    #calculates angle between two lines defined by three vertices
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    radians=np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle=np.abs(radians*180.0/np.pi)
    #The following code simply returns the angle from 0-180 degrees, since arms aren't supposed to bend more than that
    if angle>180.0:
        angle=360-angle
    return angle
def matches_pose(bodyparts):
    #takes a dictionary with bodypart keys
    #Checks if the given set of coordinates for the landmarks match with the pose for a left handed salute
   angle = calculate_angle(bodyparts['Lshoulder'],bodyparts['Lelbow'], bodyparts['Lwrist'])
   angle2 = calculate_angle(bodyparts['Rshoulder'],bodyparts['Lshoulder'], bodyparts['Lelbow'])
   if angle>20 and angle<70 and angle2>90 and angle2<180:
       return True
   else:
       return False
