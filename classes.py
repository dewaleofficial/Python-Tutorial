import csv

class items():
    
    #create a list of items for all stores
    all=[]

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

        #everytime an instance is created we want to append to the list
        #it should be in the init function because the init function is called once the class is loaded
    
        items.all.append(self)        

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
        return self.price

    #create a class method to connect to csv and instantiate some objects
    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            itemly = list(reader)

        for item in itemly:
            items(
                store=item.get('store'),
                name=item.get('name'),
                price=item.get('price'),
                quantity=item.get('quantity'),
                withInk=item.get('withInk')
            )


    #static method
    @staticmethod
    def isnumber(num):#can take any argument
    # we want to count out the float that are point 0 i.e 5.0, 10.0
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    #allows you vew your instances an an object
    def __repr__(self):
        return f"items('{self.store}', '{self.name}','{self.price}', '{self.quantity}', '{self.withInk}')"


#item1 = items("aliexpress", "book", 100, 10)
#item2 = items("olx", "pencil", 200, 10 )
#tem3 = items("jumia", "pen", 300, 10, True )
#item4 = items("amazon", "ruler", 400, 10 )
#item5 = items("konga", "eraser", 500, 10  )

#print all the instances of all
#print(items.all)

#lets print all the names of the store
#for instance in items.all:
#    print (instance.store)


#item1.withtitle = "New book"

#item1.pay_rate = 0.7

#print(item1.name)

#print(item1.withtitle)

#print(item2.withInk)

#print (item1.calculate_total_price())

#print(item1.pay_rate)
#print(items.pay_rate)

#to view all attributes associated with an object
#print(item1.__dict__)
#print(item1.apply_discount())
#item1.apply_discount()
#print(item1.price)

items.instanciate_from_csv()
print(items.all)
