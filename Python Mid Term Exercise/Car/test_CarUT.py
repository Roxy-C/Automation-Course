import unittest
from car import Car
from infrastracture import Infrastracture

logger = Infrastracture()

class TestCarMethods(unittest.TestCase):
    def setUp(self):
        self.car = Car()

    def test_startEngine(self):
        """Test 001
        Tests starting the engine"""
        
        self.car.startEngine()
        self.assertTrue(self.car.engineStatus)
        logger.log("Test 1 Done")

    def test_startEngine_Neg(self):
        """Test 002
        Tests starting the engine while the engine already on"""
        
        self.car.startEngine()
        self.assertRaises(Exception, self.car.startEngine)
        logger.log("Test 2 Done")

    def test_stopEngine(self):
        """Test 003
        Tests stopping the engine after being started"""
        
        self.car.startEngine()
        self.car.stopEngine()
        self.assertFalse(self.car.engineStatus)
        logger.log("Test 3 Done")

    def test_stopEngine_Neg(self):
        """Test 004
        Tests stopping the engine while being off"""
        
        self.assertRaises(Exception, self.car.stopEngine)
        logger.log("Test 4 Done")

    def test_drive(self):
        """Test 005
        Tests an ordinary drive.
        Car will be started, driven for 500km in 120 km/h"""
        
        self.car.startEngine()
        self.car.drive(500, 120)
        self.assertEqual(self.car.fuel, 25)
        self.assertEqual(self.car.gear, 6)
        logger.log("Test 5 Done")

    def test_drive_Neg(self):
        """Test 006
        Trying to drive the car while being short on fuel
        Starts by driving the whole tank up, then trying to drive with an empty tank"""
        
        self.car.startEngine()
        self.car.drive(1000, 150)
        self.car.stop()
        self.assertRaises(Exception, self.car.drive, 200, 120)
        logger.log("Test 6 Done")

    def test_stop(self):
        """Test 007
        Tests an ordinary stop.
        Drives a certain distance and stopping"""
        
        self.car.startEngine()
        self.car.drive(1000, 150)
        self.car.stop()
        self.assertEqual(self.car.velocity, 0)
        self.assertEqual(self.car.gear, 0)
        logger.log("Test 7 Done")

    def test_stop_Neg(self):
        """Test 008
        rying to stop while car is static"""
        
        self.car.startEngine()
        self.assertRaises(Exception, self.car.stop)
        logger.log("Test 8 Done")

    def test_refuel(self):
        """Test 009
        Tests refueling method
        refueling a valid volume of fuel"""
        
        self.car.startEngine()
        self.car.drive(1000, 150)
        self.car.stop()
        self.car.stopEngine()
        self.car.refuel(40)
        self.assertEqual(self.car.fuel, 40)
        logger.log("Test 9 Done")

    def test_refuel_Neg(self):
        """Test 010
        Tests refueling method
        refueling while engine is on"""
        
        self.car.startEngine()
        self.assertRaises(Exception, self.car.refuel, 10)
        logger.log("Test 10 Done")

if __name__ == '__main__':
    unittest.main()