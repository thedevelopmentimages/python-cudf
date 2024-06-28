import pytest

import src.algorithms.example


class TestExample:

    @pytest.fixture
    def minimum(self) -> int:
        """

        :return: The expected minimum value
        """

        return 1

    @pytest.fixture
    def maximum(self) -> int:
        """

        :return: The expected upper boundary value
        """

        return 16

    @pytest.fixture
    def instances(self) -> int:
        """

        :return: The expected number of instances
        """

        return 200000

    @staticmethod
    def test_exc(minimum: int, maximum: int, instances: int):

        example = src.algorithms.example.Example()
        data = example.exc()
        print(data)

        assert data['value'].min() >= minimum, 'Minima error'
        assert data['value'].max() < maximum, 'Maxima error'
        assert data['frequency'].sum() == instances, 'Instances error'
