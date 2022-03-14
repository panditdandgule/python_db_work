from abc import ABC,abstractmethod
from prodinfo import Product

class ProductServices(ABC):

    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def display_all_products(self):
        pass

    @abstractmethod
    def search_product(self):
        pass

    @abstractmethod
    def update_product(self):
        pass

    @abstractmethod
    def remove_prdoduct(self):
        pass

    @abstractmethod
    def max_product_price(self):
        pass
    @abstractmethod
    def min_product_price(self):
        pass

    @abstractmethod
    def display_vendors(self):
        pass