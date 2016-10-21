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
finish_close_200 = {"hours":13,"minute":30}
brevet_distances = [200,300,400,600,1000]
min_speeds = [15.0,15.0,15.0,11.428,13.333]
max_speeds = [34.0,32.0,30.0,28.0,26.0]
max_speed_table = {}
min_speed_table = {}
for i in range(len(brevet_distances)):
    max_speed_table[brevet_distances[i]] = max_speeds[i]
    min_speed_table[brevet_distances[i]] = min_speeds[i]

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
	
    if(is_approx): 
        control_dist_km = brevet_dist_km
    
    if brevet_dist_km == 200:
        max_speed = 34.0
    elif brevet_dist_km == 300:
        max_speed = 32.0
        
    elif brevet_dist_km == 400:
        max_speed = 30.0
        
    elif brevet_dist_km == 600:
        max_speed = 28.0
        
    elif brevet_dist_km == 1000:
        max_speed = 26.0
        
    
    min_hour = control_dist_km/max_speed
    min_minute = int((min_hour%1)*60)
    min_hour = int(min_hour)
    open_hour = brevet_start_time.replace(hours=+min_hour, minute=+min_minute)
    
    return open_hour

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
    
    is_approx = (control_dist_km >= brevet_dist_km and control_dist_km <= (brevet_dist_km+(prox*brevet_dist_km)))
    min_speed = min_speed_table[brevet_dist_km]
    if brevet_dist_km == 200 and is_approx:
        return brevet_start_time.replace(hours=+finish_close_200["hours"], minute=+finish_close_200["minute"])
    elif brevet_dist_km == 300:
        min_speed = 15.0
        
    elif brevet_dist_km == 400:
        min_speed = 15.0
        
    elif brevet_dist_km == 600:
        min_speed = 11.428
        
    elif brevet_dist_km == 1000:
        min_speed = 13.333
        
	
    max_hour = control_dist_km/min_speed
    max_minute = int((max_hour%1)*60)
    max_hour = int(max_hour)
    close_hour = brevet_start_time.replace(hours=+max_hour, minute=+max_minute)
    return close_hour


