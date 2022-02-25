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
        #add double under score to block access from outside source(make private)
        self.__name = name
        self.__price=price
        self.quantity = quantity
        self.withInk = withInk

        #everytime an instance is created we want to append to the list
        #it should be in the init function because the init function is called once the class is loaded
    
        items.all.append(self)        

    @property
    #read-only attribute
    def name(self):
        print("you are trying to get name")
        return self.__name

# set new nvalue for name
    @name.setter
    def name(self, value):
        if len(value)>10:
            raise Exception("name too long")
        else:
            self.__name = value

#lets enapsulate the price attribute
    @property
    def price(self):
        return self.__price

    def calculate_total_price(self):
        return self.__price*self.quantity

    def apply_discount(self):
        self.__price = self.__price*self.pay_rate
        return self.__price

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
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
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
        return f"items('{self.store}', '{self.name}','{self.__price}', '{self.quantity}', '{self.withInk}')"

#ABSTRACTION  - Show only important attribute and hide unnecessary information
#make the methods private and unaccessible outside this class 
    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
            You have {self.name} at price {self.price}
        """
        pass
    def __send(self):
        pass

    def send_email(self):
        self.__conect()
        self.__prepare_body()
        self.__send()
