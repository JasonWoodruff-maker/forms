from django.test import SimpleTestCase
from app.views import *


# Create your tests here.
class TestHeyYou(SimpleTestCase):
    def test_hey_nate(self):
        response = self.client.get("/heyyou/?x=bcca")
        self.assertContains(response, "Hey, bcca!")

    def test_hey_bcca(self):
        response = self.client.get("/heyyou/?x=Jason")
        self.assertContains(response, "Hey, Jason!")

    def test_hey(self):
        response = self.client.get("/heyyou/?x=Tim")
        self.assertContains(response, "Hey, Tim!")


class TestAgeIn(SimpleTestCase):
    def test_age_in_2050_born_2000(self):
        response = self.client.get("/age/?birthyear=2000&cur_year=2050")
        self.assertContains(response, "50")

    def test_age_in_2050_born_0(self):
        response = self.client.get("/age/?birthyear=2025&cur_year=2050")
        self.assertContains(response, "25")

    def test_age_in_2010_born_1995(self):
        response = self.client.get("/age/?birthyear=1980&cur_year=2020")
        self.assertContains(response, "40")


class TestOrderTotal(SimpleTestCase):
    def test_order_total_0_0_0(self):
        response = self.client.get("/order/?fries=2&drinks=2&burgers=2")
        self.assertContains(response, "14.0")

    def test_order_total_1_1_1(self):
        response = self.client.get("/order/?fries=1&drinks=1&burgers=2")
        self.assertContains(response, "11.5")

    def test_order_total_2_3_4(self):
        response = self.client.get("/order/?fries=1&drinks=1&burgers=1")
        self.assertContains(response, "7.0")
