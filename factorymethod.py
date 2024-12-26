from abc import ABC, abstractmethod

# Abstract Product class
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Product A
class ConcreteProductA(Product):
    def operation(self):
        return "Product A"

# Concrete Product B
class ConcreteProductB(Product):
    def operation(self):
        return "Product B"

# Abstract Creator class
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def some_operation(self):
        product = self.factory_method()
        return f"Creator: {product.operation()}"

# Concrete Creator A
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

# Concrete Creator B
class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Usage
creator = ConcreteCreatorA()
print(creator.some_operation())  # Output: Creator: Product A

creator = ConcreteCreatorB()
print(creator.some_operation())  # Output: Creator: Product B
