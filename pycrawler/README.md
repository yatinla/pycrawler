pycrawler
=================

The idea is given some arbitrarily complex json along the lines of
what you get from json.dumps for the following

   a = [ 'top1', 'top2', [{'sub0':['t11', 't12'], 'foo':{'sub1':{'a':1, 'f':'wrong', 'c':3}, 
            'sub2':{'d':4, 'e':5, 'sub3':{'f':'right', 'g':7}}, 'sub4':{'h':8, 'i':9}}},'sub00'], 'top3']

Given a path find the value of attribute 'f' along that path

   js = json.dumps(a)
   print 'js: ', js

   p = json.loads(js)

   print crawl(p, ('foo','sub2','sub3','f'))

   output: 'right'
