from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(4, 5) == 0.8
        assert division(-1, -2) == 0.5
        assert division(-7, 5) == -1.4
        assert division(-7, 9) == -0.7777777777777778
