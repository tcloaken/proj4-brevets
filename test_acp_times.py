#! /bin/python3
"""

nose tests for acp times

"""

from acp_times import open_time
from acp_times import close_time
import arrow

def test_fail():
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert not open_time(50,200,test_start_time) == arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert not close_time(50,200,test_start_time) == arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()

def test_open_200():
    """
    Is desired open times
	"""
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert open_time(50,200,test_start_time) == arrow.get('2016-11-21 17:28:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    
    
def test_close_200():
    """
    Is desired close times
	"""
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    #print (test_start_time)
    #print (close_time(50,200,test_start_time))
    #print (arrow.get('2016-11-21 17:28:00', 'YYYY-MM-DD HH:mm:ss'))
    
    assert close_time(50,200,test_start_time) == arrow.get('2016-11-21 19:20:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(203,200,test_start_time) == arrow.get('2016-11-22 05:30:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    
def test_open_1000():
    """
    Is desired open times for 1000km brevet
	"""
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert open_time(50,1000,test_start_time) == arrow.get('2016-11-21 17:28:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(100,1000,test_start_time) == arrow.get('2016-11-21 18:56:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(150,1000,test_start_time) == arrow.get('2016-11-21 20:25:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(250,1000,test_start_time) == arrow.get('2016-11-21 23:27:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(400,1000,test_start_time) == arrow.get('2016-11-22 04:08:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(450,1000,test_start_time) == arrow.get('2016-11-22 05:48:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(600,1000,test_start_time) == arrow.get('2016-11-22 10:48:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(790,1000,test_start_time) == arrow.get('2016-11-22 17:35:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(890,1000,test_start_time) == arrow.get('2016-11-22 21:09:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(900,1000,test_start_time) == arrow.get('2016-11-22 21:31:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert open_time(1005,1000,test_start_time) == arrow.get('2016-11-23 01:05:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    
 

def test_close_1000():
    """
    Is desired close times for 1000km brevet
	"""
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert close_time(50,1000,test_start_time) == arrow.get('2016-11-21 19:20:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(100,1000,test_start_time) == arrow.get('2016-11-21 22:40:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(150,1000,test_start_time) == arrow.get('2016-11-22 02:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(250,1000,test_start_time) == arrow.get('2016-11-22 08:40:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(400,1000,test_start_time) == arrow.get('2016-11-22 18:40:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(450,1000,test_start_time) == arrow.get('2016-11-22 22:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(600,1000,test_start_time) == arrow.get('2016-11-23 08:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(790,1000,test_start_time) == arrow.get('2016-11-24 00:38:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(890,1000,test_start_time) == arrow.get('2016-11-24 09:23:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(900,1000,test_start_time) == arrow.get('2016-11-24 10:15:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert close_time(1005,1000,test_start_time) == arrow.get('2016-11-24 19:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()

    
    """
def test_str():
    """
    #tests syntax
    """
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    start_time = "13:00"
    #start_time = start_time+":00"
    start_date = "2014-12-30"
    #brevet_dist = request.args.get('dist', 0,type=int)
    start = arrow.get( start_date +" "+ start_time, 'YYYY-MM-DD HH:mm')
    print (start)
    assert not start == arrow.get('2014-12-30 13:00:00', 'YYYY-MM-DD HH:mm:ss')

   """