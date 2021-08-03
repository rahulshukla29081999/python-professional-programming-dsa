# #Without Dictionary COmprehension 
old_price={"tea":1.05,"coffee":2.3,"bread":2.5,"sugar":2.5}
new_price=dict()
for key,Value in old_price.items():
    if Value >2:
        new_price[key]=Value *10.6
    else:
        new_price[key]=Value
print(new_price)


#Dictionary Comprehension
old_price={"tea":10.6,"coffee":2.3,"bread":2.5,"sugar":2.5}

new_price={key:Value*1.5 if Value>2 else Value for (key,Value) in old_price.items()}
print(old_price)




