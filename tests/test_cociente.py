from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(4, 5) == 0
        assert cociente(-1, -2) == 0
        assert cociente(-7, 5) == -2
        assert cociente(-7, 9) == -1
