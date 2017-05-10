from unittest import TestCase


class TestTask(TestCase):
    import cmptcomplexity.scripts.task as t
    task = t.Task('this_is_init_code(arg1, [1,2,3], __N__, "__N__",arg4)',
                  'this_is_clean_up_code(arg1, [1,2,3], __N__, "__N__",arg4)',
                  'this_is_invoke(arg1, [1,2,3], __N__, "__N__",arg4)')

    def test_stringify_init(self):
        self.assertEqual('this_is_init_code(arg1, [1,2,3], 20, "20",arg4)', self.task.stringify_init(20))

    def test_stringify_clean_up(self):
        self.assertEqual('this_is_clean_up_code(arg1, [1,2,3], 20, "20",arg4)', self.task.stringify_clean_up(20))

    def test_stringify_example_invoke(self):
        self.assertEqual('this_is_invoke(arg1, [1,2,3], 20, "20",arg4)', self.task.stringify_example_invoke(20))
