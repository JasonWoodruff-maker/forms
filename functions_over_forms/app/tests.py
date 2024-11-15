from django.test import SimpleTestCase

class TestFontTimes(SimpleTestCase):
    def test_(self):
        response = self.client.get("/warmup-2/font-times/?string_input=Cho&integer_input=2")
        self.assertContains(response, 'ChoCho')

    def test_1(self):
        response = self.client.get("/warmup-2/font-times/?string_input=Cho&integer_input=3")
        self.assertContains(response, 'ChoChoCho')

    def test_2(self):
        response = self.client.get("/warmup-2/font-times/?string_input=Abc&integer_input=3")
        self.assertContains(response, 'AbcAbcAbc')

class TestNoTeenSum(SimpleTestCase):
    def test_(self):
        response = self.client.get("/logic-2/no-teen-sum/?integer_1=1&integer_2=2&integer_3=3")
        self.assertContains(response, 6)

    def test_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?integer_1=2&integer_2=13&integer_3=1")
        self.assertContains(response, 3)

    def test_2(self):
        response = self.client.get("/logic-2/no-teen-sum/?integer_1=2&integer_2=1&integer_3=14")
        self.assertContains(response, 3)

class TestXYZThere(SimpleTestCase):
    def test_(self):
        response = self.client.get("/string-2/xyz-there/?given_string=abcxyz")
        self.assertContains(response, True)

    def test_1(self):
        response = self.client.get("/string-2/xyz-there/?given_string=abc.xyz")
        self.assertContains(response, False)

    def test_2(self):
        response = self.client.get("/string-2/xyz-there/?given_string=xyz.abc")
        self.assertContains(response, True)
    
class TestCenteredAverage(SimpleTestCase):
    def test_(self):
        response = self.client.get("/list-2/centered-average/?given_amount_1=1&given_amount_2=2&given_amount_3=3&given_amount_4=4&given_amount_5=100&given_amount_6=&given_amount_7=")
        self.assertContains(response, 3)
    def test_1(self):
        response = self.client.get("/list-2/centered-average/?given_amount_1=1&given_amount_2=1&given_amount_3=5&given_amount_4=5&given_amount_5=10&given_amount_6=8&given_amount_7=7")
        self.assertContains(response, 5)
    def test_2(self):
        response = self.client.get("/list-2/centered-average/?given_amount_1=-10&given_amount_2=-4&given_amount_3=-2&given_amount_4=-4&given_amount_5=-2&given_amount_6=0&given_amount_7=")
        self.assertContains(response, -3)



