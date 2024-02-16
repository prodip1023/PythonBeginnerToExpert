'''
Text Type : str
Numeric Types : int,float,complex
Sequence Types : List,Tuple,Range
Set Type : set,frozenset
Mapping  : dict
Boolean Type : bool
Binary Type : bytes,bytearray,memoryview
Other Types: None,TypeVar(T)

'''

x = 10
name = "prodip"
age = 25.56789
is_student = True
#list
my_list = [1,2,"hello",3.4]
#tuple
my_tuple = (1,2,"world",4.5)
# complex
num = 3 + 4j
#range object
my_range = range(1,10)
#set and frozenset
my_set = {1,2,3,4}
my_frozen_set = frozenset([1,2,3,4])
# bytes
data = b'Hello World'
# bytearray
byte_arr = bytearray(b'Hello World')
# None
none_val = None
# memoryview
mem_view = memoryview(b'Hello World')



print(type(x))
print(type(name))
print(type(age))
print(type(is_student))
print(type(my_list))
print(type(my_tuple))
print(type(num))
print(type(my_range))
print(type(my_set))
print(type(my_frozen_set))
print(type(data))
print(type(byte_arr))
print(type(none_val))
print(type(mem_view))

# Type Conversion
str_conversion = str(age) # convert to string
int_conversion = int(age) # convert to integer
float_conversion = float(age) # convert to float
complex_conversion = complex(age) # convert to complex number
bool_conversion = bool(age) # convert to boolean value
print("String conversion: ", str_conversion)
print("Integer conversion: ", int_conversion)
print("Float conversion: ", float_conversion)
print("Complex Number conversion: ", complex_conversion)
print("Boolean conversion: ", bool_conversion)

# List Conversion
list_from_string = list('Hello World')
print("List from String: ", list_from_string)

# Tuple Concersion
tuple_from_list = tuple(my_list)
print("Tuple from List: ", tuple_from_list)

# range
print("Range values: ")
for i in my_range:
    print(i)
    




