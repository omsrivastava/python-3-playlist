class Tab:
  menu = [
    { "name": "Roti", "price": 10 },
    { "name": "Dal", "price": 10 },
    { "name": "Paneer", "price": 10 },
    { "name": "Lassi", "price": 10 },
    { "name": "Tadka", "price": 10 },
    { "name": "Parathe", "price": 10 },
  ]

  def __init__(self):
    self.items = []
  
  def add(self, item, quantity = 1):
    flag = 0
    for dish in self.menu:
      if dish['name'] == item:
        # print(dish)
        if len(self.items) > 0:
          for i in range(len(self.items)):
            if self.items[i]["dish"] == dish:
              self.items[i]['quantity'] += quantity
              break

            else:
              self.addDish(dish, quantity)
              break
        else:
          self.addDish(dish, quantity)

        flag = 1
        break
      else:
        continue
    if flag == 0:
      print('Dish not found in menu')
    else:
      print('Order updated')
  
  def addDish(self, dish, quantity):
    self.items.append({
      "dish": dish,
      "quantity": int(quantity),
    })

  def print_bill(self, gst):
    if (len(self.items) > 0):
      totalPrice = 0
      print(f'{"Dishes":20} {"Qty":10} {"Price($)":15} {"Amount($)"}')

      for item in self.items:
        price = item["quantity"] * item["dish"]["price"]
        totalPrice += price
        print(f'{item["dish"]["name"]:12} {item["quantity"]:10} {item["dish"]["price"]:12} {price:15}')
      
      print("-"*60)

      gstAmount = (gst/100) * totalPrice
      total = totalPrice + gstAmount
      print(f'{"Total Amount":47} $ {totalPrice:.2f}')

      print(f'GST ({gst}{"%)":40} $ {gstAmount:.2f}')
      print("="*60)
      print(f'{"Total":47} $ {total:.2f}')
    else:
      print('Nothing has been ordered yet')