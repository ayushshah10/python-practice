
class VowelIterator:
    def __init__(self, text):
        self.text = text
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start,len(self.text)+1):
             if self.text[i] in 'aeiouAEIOU':
                 ans = self.text[i]
                 self.start+=1
                 return ans
             self.start+=1

text = "abcdeapshah"
iterator = VowelIterator(text)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))



