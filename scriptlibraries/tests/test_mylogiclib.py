import unittest as ut
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import mylogiclib as lib

class TestMylogiclibpy(ut.TestCase):

    def test_resolve_file_name(self):
        self.assertEqual(lib.resolve_file_name('A','B'),"B\\A")
        self.assertEqual(lib.resolve_file_name('the_underscored','underscored_too'),'underscored_too\\the_underscored')
        self.assertEqual(lib.resolve_file_name('file',''),'file')
        with self.assertRaises(NameError):
            lib.resolve_file_name('','subfolder')

    def test_read_pdf(self): # Whenever you update the pdf files in tests file also update test_read_all_pdfs 
        self.assertEqual(lib.read_pdf('sample.pdf','scriptlibraries\\tests'),'sample! ')
        self.assertEqual(lib.read_pdf('sample_cyrilic_content.pdf','scriptlibraries\\tests'),'Ћирлилица бајо :0 ')
        self.assertEqual(lib.read_pdf('Ћирличнинасловуву.pdf','scriptlibraries\\tests'),'Osvete celave latinice ')
        self.assertEqual(lib.read_pdf('razmaknuti test.pdf','scriptlibraries\\tests'),'razmaknuti ')
        with self.assertRaises(FileNotFoundError):
            lib.read_pdf('nepostojeci.pdf')
        self.assertEqual(lib.read_pdf('multipage.pdf','scriptlibraries\\tests'),'strana1 \n  strana2 ')

    def test_read_all_pdfs(self): # If you add any files at all to the tests folder you must update this pdf!
        self.assertEqual(lib.read_all_pdfs('scriptlibraries\\tests'),['strana1 \n  strana2 ', 'razmaknuti ', 'sample! ', 'Ћирлилица бајо :0 ', None, 'Osvete celave latinice '])

    def test_find_train_num(self):
        self.assertEqual(lib.find_train_num('Moja vozic 2463.001 najjaci ','Desiro'),'2463.001')
        self.assertEqual(lib.find_train_num('Ne ipak je vozic ET1.11 najjaci na svetu','aby'),'ET1.11')
        with self.assertRaises(NameError):
            lib.find_train_num('Sample tekst nebitno','nepostojeca flota')
        with self.assertRaises(IndexError):
            lib.find_train_num('Sample tekst bez flote naravno','Desiro')
        self.assertEqual(lib.find_train_num('2466.666','mireo'),'2466.666')
        self.assertEqual(lib.find_train_num('ET0.00','flirt'),'ET0.00')

if __name__=='__main__':
    ut.main()