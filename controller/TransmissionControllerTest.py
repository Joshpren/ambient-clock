import unittest

from controller.TransmissionController import TransmissionController


class MyTestCase(unittest.TestCase):


    def test_hour_transmission(self):
        cut = TransmissionController(120)
        minute = 53
        second = 59
        actual_darkening, actual_brightening = cut.hour_transmission(minute, second)
        expected_darkening = 0.0
        ecpected_brightening = 1
        self.assertEqual(expected_darkening, round(actual_darkening), 2)  # add assertion here
        self.assertEqual(ecpected_brightening, round(actual_brightening), 2)  # add assertion here

        cut = TransmissionController(60)
        minute = 47
        second = 59
        actual_darkening, actual_brightening =  cut.hour_transmission(minute, second)
        expected_darkening = 0.0
        ecpected_brightening = 1
        self.assertEqual(expected_darkening, round(actual_darkening),2)  # add assertion here
        self.assertEqual(ecpected_brightening, round(actual_brightening), 2)  # add assertion here

        cut = TransmissionController(12)
        minute = 59
        second = 59
        actual_darkening, actual_brightening = cut.hour_transmission(minute, second)
        expected_darkening = 0.0
        ecpected_brightening = 1
        self.assertEqual(expected_darkening, round(actual_darkening), 2)  # add assertion here
        self.assertEqual(ecpected_brightening, round(actual_brightening), 2)  # add assertion here

    def test_minute_transmission(self):
        cut = TransmissionController(120)
        minute = 53
        second = 59
        actual_darkening, actual_brightening = cut.hour_transmission(minute, second)
        expected_darkening = 0.0
        ecpected_brightening = 1
        self.assertEqual(expected_darkening, round(actual_darkening), 2)  # add assertion here
        self.assertEqual(ecpected_brightening, round(actual_brightening), 2)  # add assertion here

        cut = TransmissionController(60)
        minute = 47
        second = 59
        actual_darkening, actual_brightening =  cut.hour_transmission(minute, second)
        expected_darkening = 0.0
        ecpected_brightening = 1
        self.assertEqual(expected_darkening, round(actual_darkening),2)  # add assertion here
        self.assertEqual(ecpected_brightening, round(actual_brightening), 2)  # add assertion here

        cut = TransmissionController(12)
        minute = 59
        second = 59
        actual_darkening, actual_brightening = cut.hour_transmission(minute, second)
        expected_darkening = 0.0
        ecpected_brightening = 1
        self.assertEqual(expected_darkening, round(actual_darkening), 2)  # add assertion here
        self.assertEqual(ecpected_brightening, round(actual_brightening), 2)  # add assertion here



if __name__ == '__main__':
    unittest.main()
    MyTestCase().hour_transmission()
