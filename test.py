from LRUCache import *

import unittest

class TestLRUCache(unittest.TestCase):

    def test_insert(self):
        cache=LRUCache(4,4)
        cache.insertData(1,'data-1')
        self.assertEqual('data-1', cache.getData(1))
    
    def test_more_data_insert(self):
        cache=LRUCache(4,4)
        cache.insertData(1,'data-1')
        cache.insertData(2,'data-2')        
        self.assertEqual('data-2', cache.getData(2))
    
    def test_eviction_full_cache(self):
        cache=LRUCache(4,2)
        cache.insertData(1,'data-1')
        cache.insertData(2,'data-2')
        cache.insertData(3,'data-3')      
        self.assertEqual(None, cache.getData(1))
    
    def test_least_recently_used_not_evicted(self):
        cache=LRUCache(4,2)
        cache.insertData(1,'data-1')
        cache.insertData(2,'data-2')
        cache.getData(2)
        cache.insertData(3,'data-3')      
        self.assertEqual('data-2', cache.getData(2))
    
    # Single linked list test
    def test_store_more_data_with_same_hash(self):
        cache=LRUCache(4,2)
        cache.insertData(1,'data-1')
        cache.insertData(5,'data-2')
        res1=cache.getData(1)
        res2=cache.getData(5)
        self.assertEqual('data-1'+'data-2', res1+res2)  
    
    
        

if __name__ == '__main__':
    unittest.main()
