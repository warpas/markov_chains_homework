def validate_chain(chain):
  sum_list = []
  row_lenths = []
  for row in chain:
    row_sum = 0
    for elem in row:
      row_sum += elem
    # print("row {} sum is {:.2f}".format(row, row_sum))
    sum_list.append(round(row_sum, 2))
    row_lenths.append(len(row))
  # print(sum_list)
  # print(row_lenths)
  each_row_sum_is_one = all(elem == 1.00 for elem in sum_list)
  # print("Does each row sum to 1.0?", each_row_sum_is_one)
  chain_length = len(chain)
  every_row_same_length = all(elem == chain_length for elem in row_lenths)
  # print("Does each row have {} values? {}".format(len(chain), every_row_same_length))
  return each_row_sum_is_one and every_row_same_length

chain1 = [
  [0.3,0.3,0.3,0.1],
  [0.3,0.5,0.1,0.1],
  [0.4,0.3,0.2,0.1],
  [0.25,0.25,0.25,0.25]
]

chain2 = [
  [0.3,0.3,0.3,0.2],
  [0.3,0.5,0.1,0.2],
  [0.4,0.3,0.2,0.2],
  [0.25,0.25,0.35,0.25]
]

chain3 = [
  [0.5, 0.5],
  [0.9, 0.1]
]

chain4 = [
  [0.5, 0.5],
  [0.9, 0.1],
  [0.7, 0.3]
]

chain4 = [
  [0.5, 0.4, 0.1],
  [0.75, 0.1, 0.15],
  [0.5, 0.3, 0.2]
]

chain5 = [
  [0.5, 0.5],
  [0.9, 0.1],
  [0.7, 0.3]
]

# result = validate_chain(chain2)
print("first chain validation is", validate_chain(chain1))
print("")
print("second chain validation is", validate_chain(chain2))
print("")
print("third chain validation is", validate_chain(chain3))
print("")
print("fourth chain validation is", validate_chain(chain4))
print("")
print("fourth chain validation is", validate_chain(chain5))
print("")
