#03/08/2023 Project_001 codecademy_challenges
# We are creating a function has two parameters base and exponent. We want to test out the output which is base to the power. If the output is larger than or equal to 5000 then return True, else return False. and we can also test it with different value of base and power. It works
# Write your large_power function here:
def large_power(base, exponent):
  output = base**exponent
  if output >= 5000:
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
