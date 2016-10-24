#! /bin/python3
"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
             
#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#
prox = 0.10  # this is the percent amount of the total brevet_dist_km that the 
             # last checkpoint can be off by before using special rule 
finish_close_200 = {"hours":13,"minute":30} #special case for closing a 200km brevet
increment = 200 #this is the number of km that separate each "leg" of the brevet, ie: 0-200,200-400,400-600
brevet_distances = [200,300,400,600,1000]
min_speeds = [15.0,15.0,15.0,11.428,13.333]
max_speeds = [34.0,32.0,30.0,28.0,26.0]
max_speed_table = {}
min_speed_table = {}
#builds the tables of min and max speeds correlated with their distances as keys
for i in range(len(brevet_distances)):
    max_speed_table[brevet_distances[i]] = max_speeds[i]
    min_speed_table[brevet_distances[i]] = min_speeds[i]

def legs(amount,speed):
    """
    Args: 
        amount : number, the control distance in km
        speed: list,  min speeds or max speeds
    Returns:  
        number of hours as a float point from brevet start to open or close control points
    
    """
 
    i = 0
    sum = 0
    while amount > increment and i < 3:
        sum += increment/speed[i]
        amount -= increment
        i += 1
    
    sum += amount/speed[i]
    
    return sum

def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    
    is_approx = (control_dist_km >= brevet_dist_km and control_dist_km <= (brevet_dist_km+(prox*brevet_dist_km)))
    max_speed = max_speed_table[brevet_dist_km]
	
    if (is_approx):
        control_dist_km = brevet_dist_km
    
   
    start_time = arrow.get(brevet_start_time)
    min_hour = legs(control_dist_km,max_speeds)
    min_minute = round((min_hour%1)*60)
    min_hour = int(min_hour)
    open_hour = start_time.replace(hours=+min_hour, minute=+min_minute)
    
    return open_hour.isoformat()

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """	
    start_time = arrow.get(brevet_start_time)
    is_approx = (control_dist_km >= brevet_dist_km and control_dist_km <= (brevet_dist_km+(prox*brevet_dist_km)))
    min_speed = min_speed_table[brevet_dist_km]
   
    
    for times in brevet_distances:
        if (is_approx) and (times == brevet_dist_km):
            if brevet_dist_km == 200:
                close_hour = start_time.replace(hours=+(finish_close_200["hours"]), minute=+(finish_close_200["minute"]))
                return close_hour.isoformat()
            else:
                control_dist_km = brevet_dist_km
    

    max_hour = legs(control_dist_km,min_speeds)
    max_minute = round((max_hour%1)*60)
    max_hour = int(max_hour)
    close_hour = start_time.replace(hours=+max_hour, minute=+max_minute)
    
    return close_hour.isoformat()


