from unittest.mock import Mock, call
import unittest

from simple_factory_pattern.sushi_store import SushiStore


class SushiStoreTest(unittest.TestCase):
    def test_order_sushi(self):
        # Create mock objects
        sushi = Mock()
        prepared_sushi = Mock()
        boxed_sushi = Mock()

        # Stubbing the methods
        sushi.prepare.return_value = prepared_sushi
        prepared_sushi.box.return_value = boxed_sushi

        simple_sushi_factory = Mock()
        simple_sushi_factory.create_sushi.return_value = sushi

        # Instantiate SushiStore with the mock factory
        target = SushiStore(simple_sushi_factory)

        # Asserting the result
        self.assertEqual(target.order_sushi('Foo'), boxed_sushi)

        # Verifying the calls
        simple_sushi_factory.create_sushi.assert_called_once_with('Foo')
        sushi.prepare.assert_called_once()
        prepared_sushi.box.assert_called_once()


if __name__ == '__main__':
    unittest.main()
