import parte1

def run():
  parte1.greeting("Jonathan")
  parte1.suma(5)
  keys, values=parte1.get_population()
  print(keys, values)
  print(parte1.a)
  result=parte1.population_by_country
  print(result)


data = [
      {
    "name": "John",
    "age": 36,
    "country": "Norway"
      },
      {
    "name": "pipe",
    "age": 23,
    "country": "Argentina"
      }

  ]

if __name__ == "__main__":
  run()