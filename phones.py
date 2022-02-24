from all_items import items

class Phone(items):
    
    def __init__(self,store: str, name: str, price: float, quantity:int,  withInk = False, isBroken = 0):
    
        #super function allows us have access to all the attributes of the parent class
        super().__init__(
            store,name,price,quantity
            )

        #validate values being inserted 
        assert isBroken >= 0, f"isBroken {isBroken} is not greater than or equal to zero"

        # assign self object
       
        self.isBroken = isBroken