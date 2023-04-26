"""
Problem 1603: Design Parking System
URL: https://leetcode.com/problems/design-parking-system
Runtime: 144 ms, Beat: 13.7%
Memory: 16.8 MB, Beat: 6.87%

Description:
Design a parking system for a parking lot. The parking lot has three kinds
of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:
    ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for
    each parking space are given as part of the constructor.

    bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the
    parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3
    respectively. A car can only park in a parking space of its carType. If there is no space available, return false,
    else park the car in that size space and return true.

Example: Input:
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
"""
import unittest


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if self.spaces.get(carType) > 0:
            self.spaces[carType] -= 1
            return True
        else:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = ParkingSystem(3, 2, 1)
        self.testCase1 = [3, 1, 3, 2, 2, 1, 1, 3, 2, 1]

    def test_test_case_1(self):
        result = []
        for car in self.testCase1:
            result.append(self.s.addCar(car))
        self.assertEqual([True, True, False, True, True, True, True, False, False, False], result)


if __name__ == "__main__":
    unittest.main()