import os
import sys
import unittest

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
from text_tokeniser import TextTokeniser

# pylint: disable=pointless-string-statement, f-string-without-interpolation, line-too-long
# these lint details I disable are all needed in the tests


class testTextTokeniser(unittest.TestCase):
    # no local variables, its a test

    def test_sentences1(self):
        str1: str = f"""This class chops large strings into smaller strings.
I am making this a class so all the stupid UTF8 boundary-cases are shouved in one place, 
		and the rest of the code will be more readable.
TODO findout if tokenise returns something useful.

Due to current expected text source, this deals with Lists,
		$Tomorrow it may gain capacity for transforming Streams. 

I haven't injected the deps' here, as I can't see swapping it would make sense."""
        obj = TextTokeniser(str1)
        dat = obj.convert_sentences()

        """Test against initial sample [1] """
        self.assertTrue(isinstance(dat, list))
        """Test against initial sample [2] """
        self.assertEqual(len(dat), 5)
        # this is to check no CharBuffer, or Py2 str etc or some other not useful thing
        # leSigh
        """Test against initial sample [3] """
        self.assertTrue(isinstance(dat[0], str))
        # loosing terminal fullstop is expected, lead capital letter isn't
        """Test against initial sample [4] """
        self.assertTrue(dat[0], "This class chops large strings into smaller strings")

    def test_sentences2(self):
        str1: str = (
            f"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque scelerisque, sapien eget eleifend auctor, dolor metus hendrerit nunc, ac suscipit erat lorem at libero. Vivamus eu turpis id ligula consectetur lacinia. Duis malesuada lorem sem. Sed facilisis in urna id lobortis. Mauris in porta risus. Cras ut bibendum dolor, a pulvinar sem. Vivamus luctus condimentum quam, nec convallis tellus mollis in. Nulla egestas, ligula et malesuada hendrerit, quam sem condimentum erat, vel venenatis felis orci porttitor felis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut consectetur diam nunc, eget laoreet ante sollicitudin vel. Quisque gravida et quam in feugiat. Phasellus fermentum quam a nunc mattis fermentum in ac eros. Fusce in nunc nulla. Donec eu nisi ultricies, fermentum arcu a, tempus est."""
        )
        obj = TextTokeniser(str1)
        dat = obj.convert_sentences()

        """Test against ipsum lorem sample [1] """
        self.assertTrue(isinstance(dat, list))
        """Test against ipsum lorem sample [2] """
        self.assertEqual(len(dat), 15)
        # this is to check no CharBuffer, or Py2 str etc or some other not useful thing
        # leSigh
        """Test against ipsum lorem sample [3] """
        self.assertTrue(isinstance(dat[0], str))
        # loosing terminal fullstop is expected, lead capital letter isn't
        """Test against ipsum lorem sample [4] """
        self.assertTrue(
            dat[0],
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque scelerisque, sapien eget eleifend auctor, dolor metus hendrerit nunc, ac suscipit erat lorem at libero",
        )

    def test_words1(self):
        str1: str = f"""This class chops large strings into smaller strings.
I am making this a class so all the stupid UTF8 boundary-cases are shouved in one place, 
		and the rest of the code will be more readable.
TODO findout if tokenise returns something useful.

Due to current expected text source, this deals with Lists,
		$Tomorrow it may gain capacity for transforming Streams. 

I haven´t injected the deps´ here, as I can´t see swapping it would make sense.
"""
        obj = TextTokeniser(str1)
        dat = obj.convert_words()

        """Test against initial sample [1] """
        self.assertTrue(isinstance(dat, list))
        """Test against initial sample [2] """
        self.assertEqual(len(dat), 77)
        """Test against initial sample [3] """
        self.assertEqual(dat[0], "This")
        """Test against last sample [4] """
        self.assertEqual(dat[len(dat) - 1], "sense")


if __name__ == "__main__":
    unittest.main(verbosity=2)
