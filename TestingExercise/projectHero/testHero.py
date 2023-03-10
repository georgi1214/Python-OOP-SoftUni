from unittest import TestCase, main

from Mini_projects.MiniProjectsWithRandom.projectMovieLibrrary import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("werty", 1, 100, 100)
        self.enemy = Hero("enemy", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("werty", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(58.6, self.hero.health)
        self.assertEqual(150.5, self.hero.damage)

    def test_battle_against_me_raise(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_not_enought_health_raise(self):
        self.hero.health = -1
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))


    def test_enemy_not_health_raise(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_player_health_after_damage(self):
        self.hero.health = 50
        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(result, "Draw")

    def test_player_win_improve(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual(result, "You win")

    def test_player_lose_improve(self):
        self.hero.health = 5
        self.enemy.health = 300
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(205, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)
        self.assertEqual(result, "You lose")

    def test_correct_str(self):
        result = str(self.hero)
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    main()