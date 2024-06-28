import logging
import os
import sys


def main():

    # Logging
    logger = logging.getLogger(__name__)
    logger.info('CUDF')

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

    import src.algorithms.example

    main()
