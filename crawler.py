#!/usr/bin/env python
 
def crawl(n,key):
   ''' A generator crawler that can crawl a json-like structure of
       nested dictionaries without knowing the structure
       to find the value of a particular key.  
   '''
   for x in n:
      if isinstance(x,dict):
         for k,v in x.iteritems():
            if k == key:
               print 'found it'
               yield v
               ''' Caller is expected to break its loop at 
                   this point....
               '''
            elif isinstance(v,dict):
               yield v

def crawl2(n,key):
   ''' A crawler that can crawl a json-like structure of
       nested dictionaries without knowing the structure
       to find the value of a particular key
   '''
   
   def crawler(n,key):
      for x in n:
         if isinstance(x,dict):
            for k,v in x.iteritems():
               if k == key:
                  print 'found it'
                  yield v
                  ''' Caller is expected to break its loop at 
                      this point....
                  '''
               elif isinstance(v,dict):
                  yield v

   p = []
   r = n
   while True:
      for i in crawler(r,key):
         if isinstance(i,dict):
            p.append(i)
         else:
            print 'found it: ', i
            return i

      if len(p) == 0:
         return None
      else:
         r = p
         p = []

               
def crawl3(n,path):
   ''' A crawler that can crawl a json-like structure of
       nested dictionaries without knowing the structure
       to find the value of particular key nested in a
       particular path.  The key appears at the end of
       the path tuple which is like ('foo', 'bar', 'final')

       So for example I want to find the value of the key 'final'
       but it must appear under the path 'foo'/'bar'
   '''
   def crawler(n,key):
      for x in n:
         if isinstance(x,dict):
            for k,v in x.iteritems():
               if k == key:
                  print 'found it'
                  yield v
                  ''' Caller is expected to break its loop at 
                      this point....
                  '''
               elif isinstance(v,dict):
                  yield v

   p = []
   r = n
   value = None
   for key in path:
      while True:
         for i in crawler(r,key):
            if isinstance(i,dict):
               p.append(i)
            else:
               print 'found child of key ', key
               value = i

         if len(p) == 0:
            break
         else:
            r = p
            p = []

   return value

def test_crawl(a, key):
   p = []
   n = a
   while True:
      for i in crawl(n,'f'):
         if isinstance(i,dict):
            p.append(i)
         else:
            print 'found it with crawl v1: ', i
            return i

      if len(p) == 0:
         return None
      else:
         n = p
         p = []

if __name__ == '__main__':

   ''' Here there are two keys named 'f' and crawl3 will find the one in sub3 only '''

   a = [{'foo':{'sub1':{'a':1, 'f':'wrong', 'c':3}, 'sub2':{'d':4, 'e':5, 'sub3':{'f':'right', 'g':7}}, 'sub4':{'h':8, 'i':9}}}]

   print 'Test crawl v1'
   v = test_crawl(a,'f')

   if v:
      print 'v1 found ', v
   else:
      print 'v1 failed'
       
   print 'Trying v2'

   result = crawl2(a,'f')

   if result:
      print 'crawl2 found ', result
   else:
      print 'crawl2 failed'

   result = crawl3(a, ('foo','sub2','sub3','f'))

   if result:
      print 'crawl3 found ', result
   else:
      print 'crawl3 failed'


