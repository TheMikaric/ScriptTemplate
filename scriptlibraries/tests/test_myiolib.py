import unittest as ut
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import myiolib as lib 

class TestMyiolibpy(ut.TestCase):

    def test_load_config(self):
        self.assertEqual(lib.load_config('dummyconfig.yaml','scriptlibraries\\tests'),('2','1','3','4',5,6,7,False,True))

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
        self.assertEqual(lib.read_all_pdfs('scriptlibraries\\tests'),[None, 'strana1 \n  strana2 ', 'razmaknuti ', 'sample! ', 'Ћирлилица бајо :0 ', None, None, 'Osvete celave latinice '])

if __name__=='__main__':
    ut.main()