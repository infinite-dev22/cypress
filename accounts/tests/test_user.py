from unittest import TestCase


class TestUserType(TestCase):
    def setUp(self) -> None:
        UserType.objects.create("HeadTecher", )
        pass

    def test_save(self):
        self.fail()


class TestBaseUser(TestCase):
    def test_save(self):
        self.fail()
