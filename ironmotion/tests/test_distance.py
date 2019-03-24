from unittest import TestCase
from ironmotion import distance


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


if __name__ == "__main__":
    unittest.main()
