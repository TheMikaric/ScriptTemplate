import unittest as ut
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import mylogiclib as lib

class TestMylogiclibpy(ut.TestCase):

    def test_find_train_num(self): # Test only the cases you actually might encounter during the work
        self.assertEqual(lib.find_train_num('Moja vozic 2463.001 najjaci ','Desiro'),'2463.001')
        self.assertEqual(lib.find_train_num('Ne ipak je vozic ET1.11 najjaci na svetu','aby'),'ET1.11')
        with self.assertRaises(NameError):
            lib.find_train_num('Sample tekst nebitno','nepostojeca flota')
        with self.assertRaises(IndexError):
            lib.find_train_num('Sample tekst bez flote naravno','Desiro')
        self.assertEqual(lib.find_train_num('2466.666','mireo'),'2466.666')
        self.assertEqual(lib.find_train_num('ET0.00','flirt'),'ET0.00')

    def test_extract_between_strings(self):
        self.assertEqual(lib.extract_between_strings('jedna mala maca','jedna','maca'),['mala'])
        self.assertEqual(lib.extract_between_strings('jedna mala maca','nijedna','maca'),[])
        self.assertEqual(lib.extract_between_strings('vise prva struka vise druga struka','vise','struka'),['prva','druga'])
        self.assertEqual(lib.extract_between_strings('abcabcdsfjhk','a','c'),['b','b'])
        self.assertEqual(lib.extract_between_strings('jajara ','jaja',''),['ra'])


if __name__=='__main__':
    ut.main()