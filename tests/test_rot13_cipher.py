from app.rot13_cipher import rot13


class TestClass:
    def test_rot13(self):
        assert rot13('hola', 13) == 'UBYN'
        assert rot13('ordenador', 13) == 'BEQRANQBE'
        assert rot13('porque falla', 13) == 'CBEDHRMSNYYN'
        assert rot13('mesa', 13) == 'ZRFN'
