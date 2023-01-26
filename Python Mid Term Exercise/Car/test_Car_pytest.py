import pytest
from car import Car
from infrastracture import Infrastracture

logger = Infrastracture()

@ pytest.fixture
def car():    
    return Car()


@pytest.mark.one
def test_startEngine(car):
    """Test 001
    Tests starting the engine"""
    
    try:    
        car.startEngine()
        assert car.engineStatus
        logger.log("Test 1 Done")
        
    except Exception as e:
        logger.log(e)

@pytest.mark.two
def test_startEngine_Neg(car):
    """Test 002
    Tests starting the engine while the engine already on"""
       
    car.startEngine()
    with pytest.raises(Exception):
        car.startEngine()
        car.startEngine()
    logger.log("Test 2 Done")
    
@pytest.mark.three       
def test_stopEngine(car):
    """Test 003
    Tests stopping the engine after being started"""
    
    try:    
        car.startEngine()
        car.stopEngine()
        assert not car.engineStatus
        logger.log("Test 3 Done")
        
    except Exception as e:
        logger.log(e)
    
@pytest.mark.four
def test_stopEngine_Neg(car):
    """Test 004
    Tests stopping the engine while being off"""
       
    with pytest.raises(Exception):
        car.stopEngine()
    logger.log("Test 4 Done")
    
@pytest.mark.five
def test_drive(car):
    """Test 005
    Tests an ordinary drive.
    Car will be started, driven for 500km in 120 km/h"""
    
    try:
        car.startEngine()
        car.drive(500, 120)
        assert car.fuel == 25 and car.gear == 6
        logger.log("Test 5 Done")

    except Exception as e:
        logger.log(e)
    
@pytest.mark.six    
def test_drive_Neg(car):
    """Test 006
    Trying to drive the car while being short on fuel
    Starts by driving the whole tank up,
    then trying to drive with an empty tank"""
    
    with pytest.raises(Exception):
        car.startEngine()
        car.drive(2500, 150)
        car.stop()
        car.drive(200, 120)
    logger.log("Test 6 Done")

@pytest.mark.seven
def test_stop(car):
    """Test 007
    Tests an ordinary stop.
    Drives a certain distance and stopping"""
    
    try:
        car.startEngine()
        car.drive(1000, 150)
        car.stop()
        assert car.velocity == 0 and car.gear == 0
        logger.log("Test 7 Done")

    except Exception as e:
        logger.log(e)
    
@pytest.mark.eight
def test_stop_Neg(car):
    """Test 008
    Trying to stop while car is static"""
    
    with pytest.raises(Exception):
        car.startEngine()
        car.stop()
    logger.log("Test 8 Done")

@pytest.mark.nine
def test_refuel(car):
    """Test 009
    Tests refueling method
    refueling a valid volume of fuel"""
    
    try:
        car.startEngine()
        car.drive(1000, 150)
        car.stop()
        car.stopEngine()
        car.refuel(40)
        assert car.fuel == 40
        logger.log("Test 9 Done")

    except Exception as e:
        logger.log(e)
    
@pytest.mark.ten
def test_refuel_Neg(car):
    """Test 010
    Tests refueling method
    refueling while engine is on"""
    
    with pytest.raises(Exception):
        car.startEngine()
        car.refuel(10)
    logger.log("Test 10 Done")
