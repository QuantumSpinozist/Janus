import pytest
import sys
import time
sys.path.insert(0,'/home/aaron/Schreibtisch/PythonProjects/Janus/code')

from watch import Watch

test_watch = Watch('study')



# Name test
def test_name():
    assert test_watch.name == 'study'


# test start stop
def test_start_stop():
    assert test_watch.get_time() == 0.0
    test_watch.start()
    time.sleep(5)
    test_watch.stop()
    assert int(test_watch.get_time()) == 5

# test two clocks running in parallel
def test_parallel():
    w1 = Watch('1')
    w2 = Watch('2')
    assert w1.get_time() == 0.0
    assert w2.get_time() == 0.0
    w1.start()
    w2.start()
    time.sleep(5)
    w1.stop()
    assert int(w1.get_time()) == 5
    time.sleep(5)
    w2.stop()
    assert int(w2.get_time()) == 10






