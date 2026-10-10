import contextlib, inspect, io, json, os, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import textstats
from textstats import TextStats, count_text, count_file
import textstats.io as acquisition

class FileAPI(unittest.TestCase):
 def test_exports_signatures(self):
  self.assertEqual(set(textstats.__all__),{'TextStats','count_text','count_file'})
  for fun,first in [(count_text,'text'),(count_file,'path')]:
   s=inspect.signature(fun);self.assertEqual(list(s.parameters),[first,'strip_bom']); self.assertEqual(s.parameters['strip_bom'].kind,inspect.Parameter.KEYWORD_ONLY);self.assertIs(s.parameters['strip_bom'].default,True);self.assertEqual(s.return_annotation,TextStats)
  with self.assertRaises(TypeError):count_file('unused',False)
 def test_real_file_matrix_and_preservation(self):
  samples=['','\ufeff','\ufeff\ufeff','\ufeff\r\n','a\r\nb\rc\n','a\u2028b\u0085c\u2029d','α\tβ\n😊','\r\n\r\n','one\ufefftwo','\ufeff\ufeff\nend','\x00 a\x00\n','a\r\r\nb\n\r']
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'source.txt'
   for sample in samples:
    original=sample.encode('utf-8');p.write_bytes(original)
    for path in [p,str(p)]:
     for policy in [True,False]:
      with self.subTest(sample=repr(sample),path=type(path).__name__,policy=policy):
       out,err=io.StringIO(),io.StringIO()
       with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):actual=count_file(path,strip_bom=policy)
       self.assertEqual(actual,count_text(sample,strip_bom=policy));self.assertEqual(p.read_bytes(),original);self.assertEqual((out.getvalue(),err.getvalue()),('',''))
 def test_real_errors_no_partial(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'bad';p.write_bytes(b'good\n\xfftail')
   with self.assertRaises(UnicodeDecodeError):count_file(p)
   self.assertEqual(p.read_bytes(),b'good\n\xfftail')
   with self.assertRaises(FileNotFoundError):count_file(Path(tmp)/'missing')
 def test_binary_acquisition_closure_and_exceptions(self):
  class Stream:
   def __init__(self,data=None,error=None):self.data=data;self.error=error;self.closed=False;self.reads=[]
   def __enter__(self):return self
   def __exit__(self,*args):self.close()
   def close(self):self.closed=True
   def read(self,*args):
    self.reads.append(args)
    if self.error:raise self.error
    result=self.data;self.data=b'';return result
  for data,error,expected in [(b'a\r\nb\r',None,TextStats(2,2)),(b'\xff',None,UnicodeDecodeError),(None,OSError('controlled read'),OSError)]:
   stream=Stream(data,error)
   with patch('builtins.open',return_value=stream) as opener,patch('pathlib.Path.open',return_value=stream) as popener:
    if isinstance(expected,type):
     with self.assertRaises(expected):count_file(Path('controlled'))
    else:self.assertEqual(count_file(Path('controlled')),expected)
   self.assertTrue(stream.closed);self.assertTrue(stream.reads)
   calls=opener.call_args_list+popener.call_args_list
   self.assertTrue(any('rb' in str(call) for call in calls))
  with patch('builtins.open',side_effect=PermissionError('controlled unreadable')),patch('pathlib.Path.open',side_effect=PermissionError('controlled unreadable')):
   with self.assertRaises(PermissionError):count_file(Path('controlled'))

if __name__=='__main__':unittest.main(verbosity=2)
