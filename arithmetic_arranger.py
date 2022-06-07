def arithmetic_arranger(problems):
  #init
  first_line = ""
  second_line = ""
  dash_line = ""
  result_line = "\n"

  if len(problems) > 5:
    return "Error: Too many problems."
  
  for string in problems:
    #extract datas
    datas = string.split(" ")
    n1 = datas[0]
    n2 = datas[2]
    sign = datas[1]

    #check for potential errors
    error = manage_errors(n1, n2, sign)
    
    if error:
      return error
      
    #update each line
    first_line += construct_first_line(n1, len(n2))

    second_line += construct_second_line(n1, n2, sign)
  
    longest_number = n2 if n1 < n2 else n1
    dash_line += construct_dash_line(len(longest_number))
  
    if len(problems) > 1:
      result_line += construct_result_line(n1, n2, sign)
  
  #return formatted result
  #arranged_problems = first_line + "\n" + second_line + "\n" + dash_line + result_line
  arranged_problems = first_line
  
  return arranged_problems



def manage_errors(first_number, second_number, sign):
  if sign != '+' and sign != '-':
    return 'Error: Operator must be \'+\' or \'-\'.'
  elif not first_number.isdigit() or not second_number.isdigit():
    return 'Error: Numbers must only contain digits.'
  elif len(first_number) > 4 or len(second_number) > 4:
    return 'Error: Numbers cannot be more than four digits.'
  else:
    return None

def construct_first_line(first_number, second_number_len):
  result = ""
  first_number_len = len(first_number)
  
  if second_number_len > first_number_len:
    i = 0
    while i < (2 + (second_number_len - first_number_len)):
      result += " "
      i += 1
  else:
    i = 0
    while i < (first_number_len + 2):
      result += " "
      i += 1

  result += first_number
  return result

def construct_second_line(first_number, second_number, sign):  
  return ""

def construct_dash_line(longest_number_length):  
  return ""

def construct_result_line(first_number, second_number, sign):  
  return ""