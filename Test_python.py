# Вивід усього окрім "banana"
#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
  #if x == "banana":
    #continue
  #print(x)

#for x in range(6):
  #print(x)

#def my_function(fname):
  #print(fname + " Refsnes")

#my_function("Max")

#def tri_recursion(b):
  #if(b > 0):
    #result = b + tri_recursion(b - 1)
    #print(result)
  #else:
    #result = 0
  #return result

#print("\n\nRecursion Приклад Results")
#tri_recursion(10)

#dct = {'Alice': 34, 'Bob': 27, 'John': 45}

#x = dct['Alice']

#print(x)
def custom_sum(lst):
    total = 0
    for element in lst:
        total += element
    return total

my_list = [3, 8, 2, 10, 5]
result = custom_sum(my_list)
print(result)