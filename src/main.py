import os
import sys
import logging


def main():

    # Logging
    logger = logging.getLogger(__name__)
    logger.info('CUDF')

if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    main()