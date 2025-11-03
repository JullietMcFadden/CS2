'''
Authors: Julliet Mc Fadden
Date: 11/1/2025
Description: Calculates cost of shipping a certain package 
Bugs: 
Challenges: 
'''
def get_data():
    '''
    gets the data needed to later calculate the cost
    Returns:
        returns: data types needed in correct format
    '''                         
    data = input('').split(',')                                                                                         #split the input data when there is a comma and turns into a list                                                                                                 #
    return float(data[0]), float(data[1]), float(data[2]), int(data[3]), int(data[4])                                   #returns each index of data as its correct data type(int of float)

def get_post_type(length,height,thickness):
    '''
    figures out the type of postage
    Args:
        length (float): length of package
        height (float): height of package
        thickness (float): thickeness of package
    Returns:
        returns: str of type of postage 
    '''                         
    if length>=3.5 and length<=4.25 and (height>=3.5 and height<=6) and (thickness>=0.007 and thickness<=0.016):
        return "postcard"
    elif (length>4.25 and length<6) and (height>6 and height<11) and (thickness>=0.007 and thickness<=0.015):
        return "large postcard"
    elif (length>=3.5 and length<=6.125) and (height>=5 and height<=11) and (thickness>0.016 and thickness<0.25):
        return "envelope"
    elif (length>6.125 and length<24) and (height>=11 and height<=18) and (thickness>=0.25 and thickness<=0.5):
        return "large envelope"
    elif (length>24) or (height>18) or (thickness>0.5) and (length + 2*(height + thickness)<=84):
        return "package"
    elif (length>24) or (height>18) or (thickness>0.5) and 84 < length + 2*(height + thickness) <= 130:
        return "large package"
    else:
        return "unmailable"

def get_zones(zip):
    '''
    Figures out the zone from the zip
    Args:
        zip (str): zipcode
    Returns:
        returns: int of the zone
    '''                         
    if (zip>=1 and zip<=6999):
        return 1
    elif (zip>=7000 and zip<=19999):
        return 2
    elif (zip>=20000 and zip<=35999):
        return 3
    elif (zip>=36000 and zip<=62999):
        return 4
    elif (zip>=63000 and zip<=84999):
        return 5
    elif (zip>=85000 and zip<=99999):
        return 6
    else:
        return -1                                                                                                       #return -1 to identify when zipcode is not a valid option for later to be unmailible

def get_distance(startzone, endzone):
    '''
    Determines distance in zones
    Args:
        startzone (int): starting zone for package
        endzone (int): starting zone for package
    Returns:
        return: distance between zones 
    '''                         
    if startzone == -1 or endzone == -1:                                                                                #if each of zip codes = -1 (meaning invalid so unmailible)
        return -1                                                                                                       #return -1 to signify unmailable for later
    return abs(endzone - startzone)                                                                                     #return absolute value of end-start

def calc_cost(post_type,distance):
    '''
    calculates cost to mail the package
    Args:
        post_type (str): type of package
        distance (int): distance between zones
    Returns:
        return: final cost of package
    '''                         
    if post_type == "unmailable" or distance == -1:                                                                     #if unmailible or distnace = -1(meaning zipcode was invalid so unmailible)
        return "unmailable"
    elif post_type == "postcard":
        return 0.20 + distance*0.03
    elif post_type == "large postcard":
        return 0.37 + distance*0.03
    elif post_type == "envelope":
        return 0.37 + distance*0.04
    elif post_type == "large envelope":
        return 0.60 + distance*0.05
    elif post_type == "package":
        return 2.95 + distance*0.25
    elif post_type == "large package":
        return 3.95 + distance*0.35
    
def main():
    length,height,thickness,startzip,endzip = get_data()                                                                #set the 5 values returned in the list into the values within the list in that order
    post_type = get_post_type(length, height, thickness)
    startzone = get_zones(startzip)
    endzone = get_zones(endzip)
    distance = get_distance(startzone,endzone)
    final_cost = calc_cost(post_type,distance)

    if final_cost == 'unmailable':                                                                                      
        print('unmailable')
    else:
        final_cost = f'{final_cost:.2f}'                                                                                #format number so it will go to 2 decimal places

        if final_cost.startswith("0."):                                                                                 #if number starts with 0.
            print(final_cost[1:])                                                                                       #excludes first in sequence
        else:
            print(final_cost)
main()
