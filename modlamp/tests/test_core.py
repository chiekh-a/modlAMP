import unittest
from modlamp.sequences import Random


class TestCore(unittest.TestCase):
	sequences = ['GLFDIVKKVVGALG', 'GLFDIVKKVVGALG', 'GLFDIVKKVVGALK', 'ABCDEFGHAJKLMNOPQRSTUVWXYZ']
	R = Random(10, 20, 1)
	R.sequences = sequences

	def test_filter_unnatural(self):
		self.R.filter_unnatrual()
		self.assertNotIn('ABCDEFGHAJKLMNOPQRSTUVWXYZ', self.R.sequences)

if __name__ == '__main__':
	unittest.main()
