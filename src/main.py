"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry point.  Use this simple template as a starting point for
    rapids.ai dependent, i.e., GPU (Graphics Processing Unit) accelerated, programs.

    If run as-is, a sample 200,000 integers, within [1  16), will be generated, and
    the frequency of each distinct number determined.

    :return:
    """

    # Logging
    logger = logging.getLogger(__name__)
    logger.info('CUDF')

    # Numbers, frequency table.
    example = src.algorithms.example.Example()
    data = example.exc()
    logger.info(data.head())


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Activate graphics processing units
    os.environ['CUDA_VISIBLE_DEVICES']='0'

    # Modules
    import src.algorithms.example

    main()
