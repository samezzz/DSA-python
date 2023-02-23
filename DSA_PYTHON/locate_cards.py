def locate_card(cards, query):
  #  Create a variable position with the value 0
  position = 0 
  
  #  Set up a loop for repetition
  while True:
    # Check if element at the current position matches the query
    if cards[position] == query:
      # Answer found! Return and exit...
      return position
    
      #  Increment the position
    position += 1
      #  Check if we have reached the end of the array
    if position == len(cards):
        return -1

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_card(cards, query)
print(result)
print(result == output)

test = {
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 7
  },
  'output': 3   
}

# locate_card(test['input']['cards'], test['input']['query']) == test['output'] is the same as what is below
locate_card(**test['input']) == test['output']

tests = []
# query occurs in the middle
tests.append(test)

tests.append({
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 1
  },
  'output': 6
})

# query is the first element
tests.append({
  'input': {
    'cards': [4, 2, 1, -1],
    'query': 4
  },
  'output': 0
})

# query is the last element
tests.append({
  'input': {
    'cards': [3, -1, -9, -127],
    'query': -127
  },
  'output': 3
})

# card contains just one element
tests.append({
  'input': {
    'cards': [6],
    'query': 6
  },
  'output': 0
})

# cards does not contain query
tests.append({
  'input': {
    'cards': [9, 7, 5, 2, -9],
    'query': 4
  },
  'output': -1
})

# cards is empty
tests.append({
  'input': {
    'cards': [],
    'query': 7
  },
  'output': -1
})

# numbers can repeat in cards
tests.append({
  'input': {
    'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
    'query': 3
  },
  'output': 8
})

# query occurs multiple times
tests.append({
  'input': {
    'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
    'query': 6
  },
  'output': 2
})

def locate_card(cards, query):
  position = 0
  while position < len(cards):
    if cards[position] == query:
      return position
    position += 1
  return -1