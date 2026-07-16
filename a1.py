basket1 = {"apple", "banana", "mango", "grapes", "apple"}
basket2 = {"banana", "kiwi", "banana", "kiwi"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)
basket1.add("orange")
print("Basket 1 after adding orange:", basket1)
common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets:", common_fruits)
union=basket1.union(basket2)
print("All of both baskets:", union)
diff=basket1.difference(basket2)
print("Difference in baskets:", diff)
sym=basket1.symmetric_difference(basket2)
print("Symmetric difference in baskets:", sym)