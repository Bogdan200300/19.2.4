import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 3, 3) == 9

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 10, 8) == 2

    def test_devision_success(self):
        assert self.calculator.division(self, 30, 3) == 10

    def test_zero_devision(self):
        with pytest.raises(ZeroDivisionError):  # raises - метод для обработки исключений
            self.calculator.division(self, 1, 0)

    def test_adding_success(self):
        assert self.calculator.adding(self, 15, 30) == 45

    def teardown(self):
        print('Выполнение метода Teardown')