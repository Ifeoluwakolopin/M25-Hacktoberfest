def leap_year_checker(year: int):
  #To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400
  #source: https://thatascience.com/learn-python/comments-and-docstrings/
  
  #if it is not the end of a century...
  if str(year)[:2] != "00": 
    if year % 4 == 0: #...and it is divisible by 4
      return True
    else:
      return False #...and it is not divisible by 4
  
  #if it is the end of a century...
  else: 
    if year % 400 == 0: #...and it is divisible by 400
      return True
    else: #...and it is not divisible by 400
      return False