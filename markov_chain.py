def validate_chain(chain):
  valid_chain = [
    [0.3,0.3,0.3,0.1],
    [0.3,0.5,0.1,0.1],
    [0.4,0.3,0.2,0.1],
    [0.25,0.25,0.25,0.25]
  ]
  invalid_chain = [
    [0.3,0.3,0.3,0.2],
    [0.3,0.5,0.1,0.2],
    [0.4,0.3,0.2,0.2],
    [0.25,0.25,0.35,0.25]
  ]

  sum_list = []
  for row in chain:
    row_sum = 0
    for elem in row:
      row_sum += elem
    print("row {} sum is {:.2f}".format(row, row_sum))
    sum_list.append(round(row_sum, 2))
  print(sum_list)
  each_row_sum_is_one = all(elem == 1.00 for elem in sum_list)
  print("Does each row sum to 1.0?", each_row_sum_is_one)

  if chain == valid_chain:
    return True
  elif chain == invalid_chain:
    return False
  else:
    return False

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

# result = validate_chain(chain2)
print("first chain validation is", validate_chain(chain1))
print("")
print("second chain validation is", validate_chain(chain2))
print("")
print("third chain validation is", validate_chain(chain3))
print("")
