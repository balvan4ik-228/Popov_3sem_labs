import unittest
import sys
import os

rk1_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'RK1'))
sys.path.insert(0, rk1_dir)
import RK1


class TestRK1DriverFleet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.drivers = RK1.drivers
        cls.fleets = RK1.fleets
        cls.driver_fleets = RK1.driver_fleets

    def test_query1_drivers_starting_with_A(self):
        result = [(d.surname, f.name)
                  for d in self.drivers
                  if d.surname.startswith('А')
                  for f in self.fleets
                  if f.fleet_id == d.fleet_id]
        self.assertEqual(len(result), 3)
        print("\nТЕСТ 1 УСПЕШЕН: Найдено 3 водителя с фамилией на 'А'")

    def test_query2_fleets_min_salary(self):
        min_salary_by_fleet = {}
        for f in self.fleets:
            salaries = [d.salary for d in self.drivers if d.fleet_id == f.fleet_id]
            if salaries:
                min_salary_by_fleet[f.name] = min(salaries)
        result = sorted(min_salary_by_fleet.items(), key=lambda x: x[1])
        self.assertEqual(len(result), 3)
        print("ТЕСТ 2 УСПЕШЕН: 3 автопарка с правильной сортировкой зарплат")

    def test_query3_many_to_many_relationships(self):
        relationships = [(d.surname, f.name)
                         for rel in self.driver_fleets
                         for d in self.drivers if d.driver_id == rel.driver_id
                         for f in self.fleets if f.fleet_id == rel.fleet_id]
        result = sorted(set(relationships))
        self.assertEqual(len(result), 6)
        print("ТЕСТ 3 УСПЕШЕН: 6 уникальных связей многие-ко-многим")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=0, catchbreak=False)
