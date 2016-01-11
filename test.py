from data import get_spam_train_data, get_spam_valid_data, get_college_data
from tree import c45, print_tree, get_entropy, split_data, find_best_threshold, find_best_threshold_fast, find_best_split, submission, accuracy
from unittest import TestCase
import unittest

class TreeTest(unittest.TestCase):
    def setUp(self):
        self.data = get_college_data()

    def test_entropy(self):
        self.assertAlmostEqual(get_entropy(self.data),  0.9709505944546686)

    def test_split(self):
        left, right = split_data(self.data, 0, 25)
        for point in left:
            self.assertLess(point.values[0], 25)
        self.assertEqual(len(left), 3)

        for point in right:
            self.assertGreaterEqual(point.values[0], 25)
        self.assertEqual(len(right), 7)

    def test_threshold(self):
        gain, thresh = find_best_threshold(self.data, 1)
        self.assertAlmostEqual(gain, 0.321928094887)
        self.assertEqual(thresh, 38000)

    def test_threshold_fast(self):
        gain, thresh = find_best_threshold_fast(self.data, 1)
        self.assertAlmostEqual(gain, 0.321928094887)
        self.assertEqual(thresh, 38000)
    
    def test_best_split(self):
        feature, thresh = find_best_split(self.data)
        self.assertEqual(feature, 1)
        self.assertEqual(thresh, 38000)
        left, right = split_data(self.data, feature, thresh)
        feature, thresh = find_best_split(left)
        self.assertEqual(feature, None)
        self.assertEqual(thresh, None)
        feature, thresh = find_best_split(right)
        self.assertEqual(feature, 0)
        self.assertEqual(thresh, 43)

    @unittest.skip("Comment out this line when ready.")
    def testsubmission(self):
        train = get_spam_train_data()
        valid = get_spam_valid_data()
        preds = submission(train, valid)
        acc = accuracy(valid, preds)
        print
        print "Your current accuracy is:", acc
        self.assertGreater(acc, .7)
        
if __name__ == '__main__':
    unittest.main()


