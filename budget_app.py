import math

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    new_item = {
      'amount': amount,
      'description': description
    }
    self.ledger.append(new_item)
    return new_item
  
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({
        'amount': -amount,
        'description': description
      })
      return True
    return False

  def get_balance(self):
    sum = 0
    for i in self.ledger:
      sum += i.get("amount")
    return sum

  def transfer(self, amount, to_category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {to_category.name}')
      to_category.deposit(amount, f'Transfer from {self.name}')
      return True
    return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True

  def __str__(self):
    title = f'{math.ceil(((30 - len(self.name)) / 2)) * "*"}{self.name}{((30 - len(self.name)) // 2) * "*"}\n'
    text = ''
    for i in self.ledger:
      text += f'{i.get("description")[:23]}{(23-len(i.get("description")[:23])) * " "}'
      text += f'{(7-(len(str(format(i.get("amount"), ".2f"))[:7]))) * " "}{str(format(i.get("amount"), ".2f"))[:7]}\n'
    
    return f'{title}{text}Total: {format(self.get_balance(), ".2f")}'

food = Category('Food')
edu = Category('Edu')
clothing = Category('Clothing')
food.deposit(200, 'initial amount')
food.deposit(100, 'apple')
food.withdraw(45.67, 'foo')
food.transfer(10, edu)
edu.withdraw(5, 'something')
clothing.deposit(100, 'initial')
# print(food)
# print(edu)
# print(clothing)

def find_longest_name(categories):
  longest = categories[0].name
  for i in categories:
    if len(i.name) >= len(longest):
      longest = i.name
  return longest

def find_spent_percentage(category, categories):
  total_spent = 0
  for i in categories:
    for j in i.ledger:
      total_spent += j["amount"] if j["amount"] < 0 else 0
  
  cate_spent = 0
  for i in category.ledger:
    cate_spent += i["amount"] if i["amount"] < 0 else 0
  
  return abs(cate_spent) * 100 / abs(total_spent)

def create_spend_chart(categories):
  above_dashes = 'Percentage spent by category\n'
  for i in range(100, -1, -10):
    above_dashes +=f'{(3-len(str(i))) * " "}{i}| '
    for j in categories:
      above_dashes += 'o  ' if find_spent_percentage(j, categories) >= i else '   '
    above_dashes += '\n'
  above_dashes += "    -" + (len(categories) * 3 * "-")
  
  bellow_dashes = ''
  
  indx = 0
  while indx < len(find_longest_name(categories)):
    bellow_dashes += "\n     "
    for i in categories:
      try:
        bellow_dashes += i.name[indx] + "  "
      except:
        bellow_dashes += "   "
    indx += 1

  result = above_dashes + bellow_dashes
  return result
  

print(create_spend_chart([food, clothing, edu]))