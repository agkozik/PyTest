import time
from pytest import mark


@mark.long
class SeveralLongTests:

    def test_result1_with_sleep(self):
        time.sleep(2)
        print("Result 1 has completed")

    def test_result2_with_sleep(self):
        time.sleep(2)
        print("Result 2 has completed")

    def test_result3_with_sleep(self):
        time.sleep(2)
        print("Result 3 has completed")

    def test_result4_with_sleep(self):
        time.sleep(2)
        print("Result 4 has completed")

    def test_result5_with_sleep(self):
        time.sleep(2)
        print("Result 5 has completed")

    def test_result6_with_sleep(self):
        time.sleep(2)
        print("Result 6 has completed")

    def test_result7_with_sleep(self):
        time.sleep(2)
        print("Result 7 has completed")

    def test_result8_with_sleep(self):
        time.sleep(2)
        print("Result 8 has completed")
