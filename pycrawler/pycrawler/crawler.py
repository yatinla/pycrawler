#!/usr/bin/env python

import json
               
def crawl(n,path):
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
                  yield v
                  ''' Caller is expected to break its loop at 
                      this point....
                  '''
               elif isinstance(v,dict):
                  yield v
         else:
             try:
                i = iter(x)
                for j in i:
                    if isinstance(j,dict):
                        yield j   
             except:
                pass

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
            return i

      if len(p) == 0:
         return None
      else:
         n = p
         p = []

if __name__ == '__main__':

   ''' Here there are two keys named 'f' and crawl3 will find the one in sub3 only '''


   ''' This one is complex and still works '''
   a1 = [ 'top1', 'top2', {'sub0':['t11', 't12'], 'foo':{'sub1':{'a':1, 'f':'wrong', 'c':3}, 
            'sub2':{'d':4, 'e':5, 'sub3':{'f':'right', 'g':7}}, 'sub4':{'h':8, 'i':9}}}, 'top3']

   ''' But this one fails presumably because the nested list doesn't get iterated over ''' 
   a2 = [ 'top1', 'top2', [{'sub0':['t11', 't12'], 'foo':{'sub1':{'a':1, 'f':'wrong', 'c':3}, 
            'sub2':{'d':4, 'e':5, 'sub3':{'f':'right', 'g':7}}, 'sub4':{'h':8, 'i':9}}},'sub00'], 'top3']

   result = crawl(a1, ('foo','sub2','sub3','f'))

   if result:
      print 'crawl found in a1 ', result
   else:
      print 'crawl failed'

   result = crawl(a2, ('foo','sub2','sub3','f'))

   if result:
      print 'crawl found in a2 ', result
   else:
      print 'crawl failed'

   js1 = json.dumps(a1)
   print 'js1: ', js1
   js2 = json.dumps(a2)
   print 'js2: ', js2

   d1 = json.loads(js1)
   d2 = json.loads(js2)

   result = crawl(d1, ('foo','sub2','sub3','f'))

   if result:
      print 'crawl found in d1 ', result
   else:
      print 'crawl failed'

   result = crawl(d2, ('foo','sub2','sub3','f'))

   if result:
      print 'crawl found in d2 ', result
   else:
      print 'crawl failed'


