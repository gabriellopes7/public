"""
CHALLENGER:
One man can works in two days, on Thuesday and on Thursday,
if he can works in both days, he will buy a television 50' and he will eat ice cream to celebrate,
if he can works only one day, he will buy a television 32' and he will eat ice cream to celebrate,
if he can't works in both days, he won't buy anything.
"""

work_on_thuesday = None
work_on_thursday = None

if work_on_thuesday == True and work_on_thursday == True:
    print("He will buy a television 50' and he will eat ice cream to celebrate")
elif ((work_on_thuesday == True and work_on_thursday == False) or (work_on_thuesday == False and work_on_thursday == True)):
    print("He will buy a television 32' and he will eat ice cream to celebrate")
else:
    print("He won't buy anything")
