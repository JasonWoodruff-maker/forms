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
        response = self.client.get("/logic-2/no-teen-sum/?int_1=1&int_2=2&int_3=3")
        self.assertContains(response, '6')

    def test_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?int_1=2&int_2=13&int_3=1")
        self.assertContains(response, '3')

    def test_2(self):
        response = self.client.get("/logic-2/no-teen-sum/?int1=2&int_2=1&int_3=14")
        self.assertContains(response, '3')

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
        response = self.client.get("/list-2/centered-average/?amount_1=1&amount_2=2&amount_3=3&amount_4=4&amount_5=100&amount_6=&amount_7=")
        self.assertContains(response, '3')
    def test_1(self):
        response = self.client.get("/list-2/centered-average/?amount_1=1&amount_2=1&amount_3=5&amount_4=5&amount_5=10&amount_6=8&amount_7=7")
        self.assertContains(response, '5')
    def test_2(self):
        response = self.client.get("/list-2/centered-average/?amount_1=-10&amount_2=-4&amount_3=-2&amount_4=-4&amount_5=-2&amount_6=0&amount_7=")
        self.assertContains(response, '-3')



