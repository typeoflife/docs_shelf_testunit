import unittest
from docs_shelf import main, docs_now


class Test_docs_shell_UnitTest(unittest.TestCase):

    def test_main_find_people(self):
        self.assertEqual(main('p', '11-2'), 'Геннадий Покемонов')

    def test_main_find_shelf(self):
        self.assertEqual(main('s','11-2'), 'Номер полки 1')

    def test_main_show_full_docs(self):
        self.assertEqual(main('l'),docs_now)

    def test_main_add_doc(self):
        self.assertEqual(main('a','777', 'passport', 'Nik', '3'), 'Документ создан')

    def test_main_del_doc(self):
        self.assertEqual(main('d', '10006'), "Документ удален")

    def test_main_move_doc(self):
        self.assertEqual(main('m', '11-2', shelf='3'), "Документ 11-2 перемещен на полку 3")

    def test_main_add_shelf(self):
        self.assertEqual(main('as', shelf='4'), 'Полка с номером 4 создана')

if __name__ == 'main':
    unittest.main()
