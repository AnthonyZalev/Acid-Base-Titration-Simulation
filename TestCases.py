import Titration
import unittest
from DataBase import DataBase

from Solutions import Solution


class Testing(unittest.TestCase):

    def setUp(self):
        pass

    def test_one(self):
        reader = DataBase()
        self.solutions = reader.read_json_file("Solutions")

        analyte_molarity = .1
        analyte_volume = .025

        titrant_molarity = .1
        titrant_volume = .050

        for solution in self.solutions:
            if solution.get("name") == "Sodium Hydroxide":
                titrant = Solution(solution.get("name"), solution.get("Ka"), titrant_molarity,
                                   titrant_volume, solution.get("charge"))
            elif solution.get("name") == "Acetic":
                analyte = Solution(solution.get("name"), solution.get("Ka"), analyte_molarity,
                                   analyte_volume, solution.get("charge"))

        self.assertEqual(12.522876739501951, Titration.DeterminePH(titrant, analyte))



