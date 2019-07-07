"""
Sha Lai
This script contains utilities for multuprocessing.
"""

from multiprocessing import Pool
import multiprocessing

#============================ Classes ==============================#
# The following two classes are used to by-pass the restriciton on 
# multiprocessing module. Use it on outer processes.
class NoDaemonProcess(multiprocessing.Process):
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)
    
class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess

#========================== End of Section =========================#  