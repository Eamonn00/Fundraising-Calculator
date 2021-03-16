def num_check(question, error, num_type):
  valid = false
  while not valid
    try:

      response = num_type(input(question))

      if response <= 0:
        print(error)
      else:
        return response
    
    except ValueError:
      print(error)
