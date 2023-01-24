from exams.project_11_12_2022.test_11_12_21.project.team import Team
import unittest


class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Shumen")

    def test_correct_initializing(self):
        self.assertEqual("Shumen", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_team_name_is_not_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.team = Team("Shumen1999")
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_member_is_added(self):
        name_age = {'a': 20, 'b': 25}
        result = self.team.add_member(**name_age)
        self.assertEqual("Successfully added: a, b", result)
        self.assertEqual(2, len(self.team.members))

    def test_add_member_member_in_players(self):
        self.team.members = {'a': 20, 'b': 25}
        name_age = {'a': 20, 'b': 25}
        result = self.team.add_member(**name_age)
        self.assertEqual({'a': 20, 'b': 25}, self.team.members)
        self.assertEqual(2, len(self.team.members))

    def test_remove_member_removed(self):
        self.team.members = {'a': 20, 'b': 25}
        result = self.team.remove_member("a")
        self.assertEqual("Member a removed", result)
        self.assertEqual(1 , len(self.team.members))

    def test_remove_member_not_exist(self):
        self.team.members = {'a': 20, 'b': 25}
        result = self.team.remove_member("c")
        self.assertEqual("Member with name c does not exist", result)
        self.assertEqual(2, len(self.team.members))

    def test_correct_gt_(self):
        self.team.members = {'a': 20, 'b': 25}
        self.team_2 = Team("ST")
        self.team_2.members = {'a': 20}
        result = self.team.__gt__(self.team_2)
        self.assertEqual(True , result)

    def test_not_correct_gt(self):
        self.team.members = {'a': 20, 'b': 25}
        self.team_2 = Team("ST")
        self.team_2.members = {'a': 20, 'b': 25}
        result = self.team.__gt__(self.team_2)
        self.assertEqual(False, result)

    def test_correct_len_(self):
        self.team.members = {'a': 20, 'b': 25}
        self.assertEqual(2, len(self.team))

    def test_correct_add_teams(self):
        self.team.members = {'a': 20, 'b': 25}
        self.team_2 = Team("ST")
        self.team_2.members = {'c': 20, 'd': 25}
        result = self.team.__add__(self.team_2)
        self.assertEqual("ShumenST" , result.name)
        self.assertEqual({'a': 20, 'b': 25,'c': 20, 'd': 25}, result.members)
        self.assertEqual(4 , len(result))

    def test_correct_str_(self):
        self.team.members = {'a': 20, 'b': 25}
        result = self.team.__str__()
        self.assertEqual("Team name: Shumen\nMember: b - 25-years old\nMember: a - 20-years old", result)

if __name__ == "__main__":
    unittest.main()
