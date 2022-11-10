from src.main import Foo


class TestFoo:
    def test_do_job(self):
        assert Foo.do_job() == "done"
