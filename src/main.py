import logging
import os
import sys

import cudf
import cupy


def main():

    # Logging
    logger = logging.getLogger(__name__)
    logger.info('CUDF')

    # Simple Graphics Processing Units Calculations
    numbers = cupy.random.randint(low=1, high=15, size=200000)
    frequency = cudf.Series(data=numbers).value_counts()

    frame = cudf.DataFrame(data={'value': frequency.index, 'frequency': frequency})
    logger.info(frame)


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Activate graphics processing units
    os.environ['CUDA_VISIBLE_DEVICES']='0'

    main()
