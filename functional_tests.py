from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicit_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# User navigates to homepage
		self.browser.get('http://localhost:8000')

		# User notices title in homepage
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# User enters to-do item

		# User enters "Buy peacock feathers" into text box
		# User hits enter.
		# Page is updated with the list "1: Buy peacock feathers"

		# User adds another item in text box.
		# Enters "Use peacock fathers to make a fly"

		# Page updates and shows both items on the page

		# URL for user's items is generated and displayed
		# User visits URL and verified that to-do list is
		# still there

		# User exits

if __name__ == '__main__':
	unittest.main(warnings='ignore')
