import unittest
from unittest.mock import MagicMock, patch

from scripts.dice_simulator import DiceSimulator

class TestDiceSimulator(unittest.TestCase):

    def test_print(self):
        dice = DiceSimulator(2, 6)
        dice_data = str(dice)
        self.assertEqual(dice_data, 'Dices: 2 Number of faces: 6')

    def test_get_dices_and_faces(self):
        dice = DiceSimulator(4, 12)

        self.assertEqual(dice.get_dices(), 4)
        self.assertEqual(dice.get_faces(), 12)

    @patch('random.randint')
    def test_roll(self, mock_randint):
        faces = MagicMock()
        dice = DiceSimulator(4, faces)

        mock_randint.side_effect = [10, 20, 30, 42]

        self.assertEqual(dice.roll(), [10, 20, 30, 42])
