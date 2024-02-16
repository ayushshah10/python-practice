    
# class VowelIterator:

#     def __iter__(self):
#         self.a = 'abcde'
#         return self

#     def __next__(self):
#         for i in self.a:
#             if i in 'aeiouAEIOU':
#                 return i

# myclass = VowelIterator()
# myiter = iter(myclass)

# print(next(myiter))
a = "abcde"
vowelIter = iter(i for i in a if i in 'aeiou')
print(next(vowelIter))
print(next(vowelIter))