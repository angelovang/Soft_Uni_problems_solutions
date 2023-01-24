import unittest

from Test.hero.project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.my_hero = Hero("Peter", 2, 150, 50)
        self.enemy_hero = Hero("Jon", 1, 100, 100)

    def test_correct_initialization(self):
        self.assertEqual("Peter", self.my_hero.username)
        self.assertEqual(2, self.my_hero.level)
        self.assertEqual(150, self.my_hero.health)
        self.assertEqual(50, self.my_hero.damage)

    def test_check_that_enemy_username_is_equal_to_my_name_exception(self):
        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(self.my_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_that_my_health_is_zero_or_negative_value_error(self):
        self.my_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.my_hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_that_enemy_hero_is_zero_or_negative_value_error(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.my_hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight Jon. He needs to rest", str(ve.exception))

    def test_result_after_battle_draw(self):
        self.my_hero.health = 100
        result = self.my_hero.battle(self.enemy_hero)

        self.assertEqual(0, self.my_hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_result_after_battle_you_win(self):
        result = self.my_hero.battle(self.enemy_hero)

        self.assertEqual(3, self.my_hero.level)
        self.assertEqual(55, self.my_hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("You win", result)

    def test_result_after_battle_you_lose(self):
        self.my_hero.level = 1
        self.enemy_hero.level = 2
        result = self.my_hero.battle(self.enemy_hero)

        self.assertEqual(3, self.enemy_hero.level)
        self.assertEqual(-50, self.my_hero.health)
        self.assertEqual(55, self.enemy_hero.health)
        self.assertEqual("You lose", result)

    def test_correct_str_presentation(self):
        result = str(self.my_hero)
        expected_result = "Hero Peter: 2 lvl\n" \
                          "Health: 150\n" \
                          "Damage: 50\n"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
