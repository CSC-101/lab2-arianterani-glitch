#Task 3a
def smallest(n:float, m: float) -> float:
   if n < m:
      return n                # For which calls below is this statement evaluated? Neither, both function calls return m.
   # If returning n is to be desired, either the inputs must change or the statement must be rewritten "n <= m"
   else:
      return m

first = smallest(3, 2)  # What is the value of 1st? It is 2.
second = smallest(2, 2) # What is the value of 2nd? Is this a reasonable result? Why or why not? Second: 2.
# It is reasonable, since both inputs are equal and return the smallest value!
print()


#Task 3b
def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
      return a - b            # In general, when will a call to this function evaluate this statement? answer1 will.
   elif b > c:
      return b + c            # In general, when will a call to this function evaluate this statement? answer2 will.
   else:
      return 2 * c            # In general, when will a call to this function evaluate this statement? answer3 will.


answer1 = function2(3, 2, 1)  #What is the value of answer1? answer1: 1
answer2 = function2(2, 3, 1)  #What is the value of answer2? answer2: 4
answer3 = function2(2, 1, 3)  #What is the value of answer3? answer3: 6
print()