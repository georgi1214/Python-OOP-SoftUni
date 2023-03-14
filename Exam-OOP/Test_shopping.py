from project.shopping_cart import ShoppingCart
from unittest import TestCase


class ShoppingCartTests(TestCase):
    SHOP_NAME = "Shop"
    BUDGET = 90

    def setUp(self) -> None:
        self.shop = ShoppingCart(self.SHOP_NAME, self.BUDGET)

    def test_init(self):
        self.assertEqual(self.SHOP_NAME, self.shop.shop_name)
        self.assertEqual(self.BUDGET, self.shop.budget)
        self.assertEqual({}, self.shop.products)

    def test_shop_name_if_first_char_not_upper_raises_error(self):
        with self.assertRaises(ValueError) as error:
            self.shop.shop_name = 'shop'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_shop_name_if_not_only_letters_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.shop.shop_name = 'shop1'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

        # with self.assertRaises(ValueError) as error:
        #     self.shop.shop_name = 'sh*op'
        #
        # self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_shop_name_it_is_correct(self):
        result = self.shop.shop_name = self.SHOP_NAME

        self.assertEqual("Shop", result)

    def test_add_to_cart_product_price_is_equal_raise_error(self):
        product_name = "product"
        with self.assertRaises(ValueError) as error:
            self.shop.add_to_cart(product_name, 100)

        self.assertEqual(f"Product {product_name} cost too much!", str(error.exception))

    def test_add_to_cart_product_price_is_greater_raise_error(self):
        product_name = "product"
        with self.assertRaises(ValueError) as error:
            self.shop.add_to_cart(product_name, 101)

        self.assertEqual(f"Product {product_name} cost too much!", str(error.exception))

    def test_add_to_cart_product_name_with_price(self):
        product_name = "product"
        price = 20

        result = self.shop.add_to_cart(product_name, price)

        self.assertEqual(f"{product_name} product was successfully added to the cart!", result)

    def test_remove_from_cart_if_product_exist_in_products(self):
        product_name = "product"
        self.shop.add_to_cart(product_name, 20)
        self.shop.add_to_cart("product2", 40)

        result = self.shop.remove_from_cart(product_name)

        self.assertEqual(f"Product {product_name} was successfully removed from the cart!", result)
        self.assertEqual({"product2": 40}, self.shop.products)

    def test_remove_from_cart_if_product_does_not_exist_raise_error(self):
        product_name = "product"

        with self.assertRaises(ValueError) as error:
            self.shop.remove_from_cart(product_name)

        self.assertEqual(f"No product with name {product_name} in the cart!", str(error.exception))

    def test_add_if_is_correct_self_with_other(self):
        self_test = ShoppingCart("Shop", 100)
        self_test.add_to_cart("product_in_self", 60)
        other = ShoppingCart('Store', 200)
        other.add_to_cart("product1", 30)

        expected_products = {"product_in_self": 60, "product1": 30}
        actual = self_test.__add__(other)

        self.assertEqual("ShopStore", actual.shop_name)
        self.assertEqual(300, actual.budget)
        self.assertEqual(expected_products, actual.products)

    def test_buy_products_if_total_sum_is_greater_than_the_budget_raise_error(self):
        self.shop.add_to_cart("product1", 80)
        self.shop.add_to_cart("product2", 25)
        total_sum = sum(self.shop.products.values())

        with self.assertRaises(ValueError) as error:
            self.shop.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with {total_sum - self.BUDGET:.2f}lv!"
                         , str(error.exception))

    def test_buy_product_is_successfully_bought(self):
        self.shop.add_to_cart("product1", 30)
        self.shop.add_to_cart("product2", 25)
        total_sum = 55

        result = self.shop.buy_products()

        self.assertEqual(f'Products were successfully bought! Total cost: {total_sum:.2f}lv.', result)
