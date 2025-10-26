import unittest
from app import add, multiply

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)

if __name__ == '__main__':
    unittest.main()
```

**requirements.txt** :
```
# Aucune dépendance pour cet exemple simple