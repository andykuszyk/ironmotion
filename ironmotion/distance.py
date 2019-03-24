import numpy as np
from math import sqrt


def simple(A, B):
    """
    Calculates the simple distance between the two sets of vectors, A and B, by
    obtaining the total translation for each (the final vector minus the first)
    and calculating the mean square error between these two tranlsation vectors.

    Elements of A and B are assumed to be array-like and are converted to Numpy 
    arrays internally.
    """
    A_np = [np.array(t) for t in A]
    B_np = [np.array(t) for t in B]

    A_translation = A_np[-1] - A_np[0]
    B_translation = B_np[-1] - B_np[0]

    if len(A_translation) != len(B_translation) and len(A_translation) != 3:
        raise Exception('A and B should both be comprised of three element vectors')

    error = A_translation - B_translation
    return sqrt(error[0] ** 2 + error[1] ** 2 + error[2] ** 2)
