import unittest
import main
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text="python"
        result=main.cap_text(text)
        self.assertEqual(result,"Python") #when text gets passed in, it makes sure its Python
    def test_multiple_words(self):
        text="monty python"
        result=main.cap_text(text)
        self.assertEqual(result,"Monty Python")

if __name__=="__main__":
    unittest.main()
#go to cmd, run python tester.py

#to go into python mode from cmd, enter: python
#to quit, do quit()


