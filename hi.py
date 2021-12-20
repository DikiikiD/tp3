import unittest
import time
from functions import aboba, realNotSum, NotSum, Sum, Maxim, Mimim
class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(aboba), Sum(aboba))

    def test_notsum(self):
        self.assertEqual(realNotSum(aboba), NotSum(aboba))

    def test_miniman(self):
        self.assertEqual(min(aboba), Mimim(aboba))

    def test_maximal(self):
        self.assertEqual(max(aboba), Maxim(aboba))

    def test_time_measure_max(self):  # Сравниваем скорость функции max и Maxim, если Maxim оказалась быстрее, то ошибки не будет
        start_time = time.time()
        max(aboba)
        time_of_real = time.time() - start_time
        start_time = time.time()
        Maxim(aboba)
        time_of_fake = time.time() - start_time
        self.assertLessEqual(time_of_real, time_of_fake)

    def test_time_measure_min(self):
        start_time = time.time()
        min(aboba)
        time_of_real = time.time() - start_time
        start_time = time.time()
        Mimim(aboba)
        time_of_fake = time.time() - start_time
        self.assertLessEqual(time_of_real, time_of_fake)

    def test_time_measure_sum(self):
        start_time = time.time()
        sum(aboba)
        time_of_real = time.time() - start_time
        start_time = time.time()
        Sum(aboba)
        time_of_fake = time.time() - start_time
        self.assertLessEqual(time_of_real, time_of_fake)

    def test_time_measure_notsum(self):  # Сравниваем скорость функции max и Maxim, если Maxim оказалась быстрее, то ошибки не будет
        start_time = time.time()
        realNotSum(aboba)
        time_of_real = time.time() - start_time
        start_time = time.time()
        NotSum(aboba)
        time_of_fake = time.time() - start_time
        self.assertLessEqual(time_of_real, time_of_fake)

    def test_same_or_not(self):
        self.assertEqual([0, 1, 1, 1, 1, 1, 1, 2], aboba)

if __name__ == '__main__':
    unittest.main()

# Пункт 5 - тк работаем с целыми числами, то такой ошибки возникнуть не может
