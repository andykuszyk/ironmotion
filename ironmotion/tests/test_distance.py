from unittest import TestCase
from ironmotion import distance
from math import sqrt


class TestDistance(TestCase):
    def test_simple_when_AB_are_same_should_return_zero(self):
        A = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8)
        ]
        B = A

        mse = distance.simple(A, B)

        self.assertEqual(mse, 0, "Results should be zero, because A and B are the same")

    def test_simple_when_AB_are_separated_should_return_error(self):
        A = [(0, 0, 0), (1, 1, 1)]
        B = [(1, 1, 1), (3, 3, 3)]

        mse = distance.simple(A, B)

        self.assertEqual(mse, sqrt(3), "The result should be the root of the sum of the differences squared.")

if __name__ == "__main__":
    unittest.main()
