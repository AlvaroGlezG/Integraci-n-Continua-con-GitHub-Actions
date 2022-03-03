from app.rot13_cipher import rot13


class TestClass:
    def test_rot13(self):
        assert rot13('hola') == 'a'
        assert rot13('ordenador') == 'e'
        assert rot13('porque falla') == 'a'
        assert rot13('mesa') == 'a'
