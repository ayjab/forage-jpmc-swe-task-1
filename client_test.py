import unittest
from client3 import getDataPoint, getRatio  

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  def test_getRatio_calculateRatio(self):
    test1 = {'price_a': 120.48, 'price_b': 0}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(test1['price_a'], test1['price_b']), None)

    test2 = {'price_a': 120.48, 'price_b': 121.2}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(test2['price_a'], test2['price_b']), test2['price_a']/test2['price_b'])

    test3 = {'price_a': 0, 'price_b': 0}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(test3['price_a'], test3['price_b']), None)

if __name__ == '__main__':
    unittest.main()
