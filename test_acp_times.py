#! /bin/python3
"""

nose tests for acp times

"""
from acp_times import open_time
from acp_times import close_time
import arrow

def test_fail():
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert not open_time(50,200,test_start_time) == arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert not close_time(50,200,test_start_time) == arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')

def test_open_200():
    """
    Is desired open times
	"""
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert open_time(50,200,test_start_time) == arrow.get('2016-11-21 17:28:00', 'YYYY-MM-DD HH:mm:ss')
    
    
def test_close_200():
    """
    Is desired open times
	"""
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    print (test_start_time)
    print (close_time(50,200,test_start_time))
    print (arrow.get('2016-11-21 17:28:00', 'YYYY-MM-DD HH:mm:ss'))
    
    assert close_time(50,200,test_start_time) == arrow.get('2016-11-21 19:20:00', 'YYYY-MM-DD HH:mm:ss')
    assert close_time(203,200,test_start_time) == arrow.get('2016-11-22 5:30:00', 'YYYY-MM-DD HH:mm:ss')

    
def test_str():
    """
    tests syntax
    """
    test_start_time = arrow.get('2016-11-21 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    start_time = "13:00"
    #start_time = start_time+":00"
    start_date = "2014-12-30"
    #brevet_dist = request.args.get('dist', 0,type=int)
    start = arrow.get( start_date +" "+ start_time, 'YYYY-MM-DD HH:mm')
    print (start)
    assert not start == arrow.get('2014-12-30 13:00:00', 'YYYY-MM-DD HH:mm:ss')

   