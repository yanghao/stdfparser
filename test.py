import sys
import logging
import struct
import os

from stdfparser import parser

class tt(parser):
    def take(self, typsub):
        print "======================= %s =======================" % str(self.Cur_Rec)
        for i,j in self.Cur_Rec.fieldMap:
            print i+' : '+str(self.data[i])

    def setup(self): pass

    def cleanup(self): pass

    def file_setup(self): pass

    def file_cleanup(self): pass

def do():
    log = logging.getLogger('prod_data_ftp')
    lvl = logging.INFO
    logging.basicConfig(level=lvl)
    x = tt()
    x.Rec_Set = [] #
    x.Rec_Nset = []
    x.parse(sys.argv[1:])

do()
print 'Job Done!'
