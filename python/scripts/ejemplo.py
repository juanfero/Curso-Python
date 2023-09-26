
'''
from my_functions import get_totals, calc_total

def get_total(orders):
  # Tu código aquí 👇
  totals=get_totals(orders)
  return calc_total(totals)

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)


'''
'''

def get_totals(orders):
   return [order['total'] for order in orders]

def calc_total(totals):
   return sum(totals)

'''