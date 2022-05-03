import unittest


class Action1CompatTest(unittest.TestCase):
    def test_action1_compat(self):
        from compat.action_1 import action_1 as action_1_compat
        from deprecated.class1 import action_1 as action_1_deprecated

        dict_from_compat = action_1_compat()
        dict_from_deprecated = action_1_deprecated()

        self.assertDictEqual(dict_from_compat, dict_from_deprecated)
