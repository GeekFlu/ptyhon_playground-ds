import unittest

from problem_4 import is_user_in_group, Group


class ActiveDirectoryTests(unittest.TestCase):

    def test_active_directory_search(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)
        self.assertTrue(is_user_in_group(sub_child_user, parent))
        self.assertFalse(is_user_in_group("not_in_group", parent))

        self.assertFalse(is_user_in_group(None, parent))
        self.assertFalse(is_user_in_group(sub_child_user, None))
        self.assertFalse(is_user_in_group(None, None))
        self.assertFalse(is_user_in_group("  ", parent))


if __name__ == "__main__":
    unittest.main()
