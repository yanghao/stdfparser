import sys
sys.path.insert(0, r'/home/hua/git/STDF_Player/stdf_parser')
sys.path.insert(0, r'/home/hua/git/STDF_Player/logformat')
import logging
import struct
import os
from getopt import getopt

from stdfparser import parser
from logformat import LogFormat

class tt(parser):
    def take(self, typsub):
        print "======================= %s =======================" % str(self.Cur_Rec)
        for i,j in self.Cur_Rec.fieldMap:
            print i+' : '+str(self.data[i])

    def setup(self): pass
#        self.log.info('In setup() function')

    def cleanup(self): pass
#        self.log.info('In Cleanup() function')

    def file_setup(self):
        self.rr = [[] for i in range(17)]

    def file_cleanup(self): pass
#       n = 0
#       for x in self.rr:
#           r = {}
#           for i in x:
#               if r.has_key(i):
#                   r[i] += 1
#               else:
#                   r[i] = 1
#           k = r.keys()
#           k.sort()
#           print '========= %s ===========' % str(340000+n)
#           for i in k:
#               print str(i)+' : '+str(r[i])
#           n += 1



def do():
    log = logging.getLogger('prod_data_ftp')
    lvl = logging.INFO
    logging.basicConfig(level=lvl, format=LogFormat)
    #x = test()
    #x.go_through(sys.argv[1])
    x = tt()
    x.Rec_Set = [] #
    #x.Rec_Nset = ['EtsrV3', 'Etsr'] # now all records are supported.
    x.Rec_Nset = []
    #x.Rec_Set = [ 'Far', 'Mir', 'Mrr', 'Wir', 'Wrr', 'Hbr', 'Sbr',
    #       'Tsr', 'Pir', 'Prr', 'Fdr', 'Ftr', 'Pdr', 'Ptr',
    #       'Brr', 'Wtr', 'EtsrV3', 'Gtr', 'Adr', 'Epdr',
    #       'Gdr'] #, 'Shb', 'Ssb', 'Sts', 'Scr']
#x.parse([r'C:\UserData\huyangha\home_resources\stdf_parser\data\test.std'])
    x.parse(sys.argv[1:])
#    x.count(sys.argv[1:])

#    import cProfile
#    cProfile.run('do()')
do()
print 'Job Done!'
