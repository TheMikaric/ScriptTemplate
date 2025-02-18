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

    def test_read_pdf(self):
        self.assertEqual(lib.read_pdf('sample.pdf','scriptlibraries\\tests'),'sample! ')
        self.assertEqual(lib.read_pdf('sample_cyrilic_content.pdf','scriptlibraries\\tests'),'Ћирлилица бајо :0 ')
        self.assertEqual(lib.read_pdf('Ћирличнинасловуву.pdf','scriptlibraries\\tests'),'Osvete celave latinice ')
        self.assertEqual(lib.read_pdf('razmaknuti test.pdf','scriptlibraries\\tests'),'razmaknuti ')
        with self.assertRaises(FileNotFoundError):
            lib.read_pdf('nepostojeci.pdf')

if __name__=='__main__':
    ut.main()