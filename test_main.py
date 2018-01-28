import main

def test_get_distance_1():
    distance = main.get_distance(53.2451022, -6.238335) #test case for user id 4
    assert distance < 100

def test_get_distance_2():
    distance = main.get_distance( 53.038056, -7.653889) #test case for user id 26
    assert distance < 100

# Run using command python -m pytest
