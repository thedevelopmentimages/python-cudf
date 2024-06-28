"""Module example.py"""
import logging

import cudf
import cupy
import numpy as np
import pandas as pd


class Example:
    """
    Class Example
    """

    def __init__(self):
        """
        Constructor
        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self) -> pd.DataFrame:
        """
        
        Random numbers
        """

        # A sample of 200,000 random integers within [1 16)
        numbers: np.ndarray = cupy.random.randint(low=1, high=16, size=200000)
        frequency: cudf.Series = cudf.Series(data=numbers).value_counts()

        # Frequencies
        frame = cudf.DataFrame(data={'value': frequency.index, 'frequency': frequency})

        return frame
