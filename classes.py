class items():
    
    pay_rate = 0.8 #class/global attribute(discount of 20% across all sales)


    def __init__(self,store: str, name: str, price: float, quantity:int,  withInk = False):

        #validate values being inserted 
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # assign int values
        self.store = store
        self.name = name
        self.price=price
        self.quantity = quantity
        self.withInk = withInk
        

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
        return self.price



item1 = items("ade_book_store", "ade", 100, 10)
item2 = items("olx", "pencil", 200, 10, True )

item1.withtitle = "New book"

item1.pay_rate = 0.7

#print(item1.name)

#print(item1.withtitle)

#print(item2.withInk)

#print (item1.calculate_total_price())

#print(item1.pay_rate)
#print(items.pay_rate)

#to view all attributes associated with an object
#print(item1.__dict__)
#
print(item1.apply_discount())
#item1.apply_discount()
#print(item1.price)

