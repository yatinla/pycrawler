#!/usr/bin/env python
 
def crawl2(n,key):
   ''' A crawler that can crawl a json-like structure of
       nested dictionaries without knowing the structure
       to find the value of a particular key
   '''
   
   def crawler(n,key):
      print 'crawler n is ', n
      for x in n:
         print 'crawler x is ', x
         if isinstance(x,dict):
            print 'x is ', x
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

def crawl(n,key):
   ''' A crawler that can crawl a json-like structure of
       nested dictionaries without knowing the structure
       to find the value of a particular key
   '''
   print 'n is ', n
   for x in n:
      if isinstance(x,dict):
         print 'x is ', x
         for k,v in x.iteritems():
            if k == key:
               print 'found it'
               yield v
               ''' Caller is expected to break its loop at 
                   this point....
               '''
            elif isinstance(v,dict):
               yield v
               
if __name__ == '__main__':

   a = [{'foo':{'sub1':{'a':1, 'b':2, 'c':3}, 'sub2':{'d':4, 'e':5, 'sub3':{'f':6, 'g':7}}, 'sub4':{'h':8, 'i':9}}}]

   p = []
   n = a
   while True:
      for i in crawl(n,'f'):
         if isinstance(i,dict):
            p.append(i)
         else:
            print 'found it with crawl v1: ', i
            p = [] # To break
            break

      if len(p) == 0:
         break
      else:
         n = p
         p = []
       
   print 'Trying v2'

   result = crawl2(a,'f')

   if result:
      print 'crawl2 found it: ', result
   else:
      print 'crawl2 failed'


