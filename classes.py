from all_items import items
from phones import Phone

phone1 = Phone("olx", "samsung", 100, 20)

phone2 = Phone("jumia", "infinix", 80, 20)

#print(phone2.apply_discount())

item1 = items("olx", "samsung", 100, 20)
item1.name = "others"
#item1.price = 1000
item1.apply_discount()

print(item1.name)
print(item1.price)


item1.send_email()
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

#items.instanciate_from_csv()
#print(items.all)
