import unittest
from RK1 import *


class Test_Program(unittest.TestCase):
    directs = [
        Dir(1, 'Документы'),
        Dir(2, 'Личное'),
        Dir(3, 'Учеба'),
        Dir(4, 'Работа'),
    ]

    files = [
        File(1, 'РК1_ПиКЯП.py', 950, 3),
        File(2, 'Хоккей_Билеты.pdf', 1838, 2),
        File(3, 'Алгоритмы_книга.pdf', 101560, 1),
        File(4, 'Отчет1.docx', 147, 4),
        File(5, 'Модель.jpg', 48, 2),
    ]

    files_dirs = [
        FileDir(1, 1),
        FileDir(1, 3),
        FileDir(2, 1),
        FileDir(2, 2),
        FileDir(3, 1),
        FileDir(3, 3),
        FileDir(3, 4),
        FileDir(4, 4),
        FileDir(5, 2),
        FileDir(5, 3),
        FileDir(5, 4),
    ]

    def test_g1(self):
        one_to_many = [(f.name, f.size, d.name)
                       for d in directs
                       for f in files
                       if f.dir_id == d.id]

        self.assertEqual(g1_solution(one_to_many),
                         {'Личное': [('Хоккей_Билеты.pdf', 1838), ('Модель.jpg', 48)]})

    def test_g2(self):
        one_to_many = [(f.name, f.size, d.name)
                       for d in directs
                       for f in files
                       if f.dir_id == d.id]

        self.assertEqual(g2_solution(one_to_many),
                         [('Документы', 101560), ('Личное', 1838), ('Учеба', 950), ('Работа', 147)])

    def test_g3(self):
        many_to_many_temp = [(d.name, fd.dir_id, fd.file_id)
                             for d in directs
                             for fd in files_dirs
                             if d.id == fd.dir_id]

        many_to_many = [(f.name, f.size, dir_name)
                        for dir_name, dir_id, file_id in many_to_many_temp
                        for f in files if f.id == file_id]

        self.assertEqual(g3_solution(many_to_many),
                         [('РК1_ПиКЯП.py', 950, 'Документы'), ('Хоккей_Билеты.pdf', 1838, 'Документы'), ('Алгоритмы_книга.pdf', 101560, 'Документы'),
                          ('Хоккей_Билеты.pdf', 1838, 'Личное'), ('Модель.jpg', 48, 'Личное'), ('Алгоритмы_книга.pdf', 101560, 'Работа'), ('Отчет1.docx', 147, 'Работа'), ('Модель.jpg', 48, 'Работа'), ('РК1_ПиКЯП.py', 950, 'Учеба'), ('Алгоритмы_книга.pdf', 101560, 'Учеба'), ('Модель.jpg', 48, 'Учеба')])


if __name__ == '__main__':
    unittest.main()