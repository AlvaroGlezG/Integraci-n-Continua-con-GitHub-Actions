from app.operaciones import resto


class TestClass:
    def test_resto(self):
        assert resto(4, 5) == 4
        assert resto(-1, -2) == -1
        assert resto(-7, 5) == 3
        assert resto(-7, 9) == 2
