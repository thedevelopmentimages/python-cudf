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

        :return:
            frame: A frequency table
        """

        self.__logger.info('Sampling: A random sample of 200,000 integers within [1  16), i.e., [1  15]')
        numbers: np.ndarray = cupy.random.randint(low=1, high=16, size=200000)

        # Frequencies
        frequency: cudf.Series = cudf.Series(data=numbers).value_counts()
        frame = cudf.DataFrame(data={'value': frequency.index, 'frequency': frequency})

        return frame
