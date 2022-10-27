import unittest
from meriveden_korkeusvaihtelut import *
from statistics import mean


class TestSeaLevelMethods(unittest.TestCase):
    def setUp(self):
        self.actual: list = [234.5, 678.9, 789, 345.6, 456.7, 567.8, 123.4]
        self.small: list = [790.0, 778.0, 821.0, 809.0, 769.0, 778.0, 778.0]

    def test_median(self):
        self.assertAlmostEqual(1.5, get_median([0.5, 1.0, 2.0, 5.5]), 2)
        self.assertAlmostEqual(456.7, get_median(self.actual), 2)
        self.assertAlmostEqual(778.00, get_median(self.small), 2)

    def test_mean(self):
        self.assertAlmostEqual(456.557, get_mean(self.actual), 2)
        self.assertAlmostEqual(789.00, get_mean(self.small), 2)

    def test_variance(self):
        local_list = [5, 4, 2, 3, 1, 4, 5, 2]
        self.assertAlmostEqual(2.21, get_variance(local_list, mean(local_list)),
                               2)
        self.assertAlmostEqual(57490.69,
                               get_variance(self.actual, mean(self.actual)), 2)
        self.assertAlmostEqual(364.66667,
                               get_variance(self.small, mean(self.small)), 2)

    def test_deviation(self):
        self.assertAlmostEqual(239.77216169483, get_deviation(57490.69), 2)
        self.assertAlmostEqual(19.096247, get_deviation(364.66667), 2)


if __name__ == '__main__':
    unittest.main()
