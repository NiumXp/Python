frase = "Oi, eu não sou o Cleber!"

#Method ONE!
print(' '.join([word.capitalize() for word in frase.split(' ')]))

#Method TWO!
print(' '.join([word[0].upper() + word[1:] for word in frase.split(' ')]))

#Method THREE!
dictionarie = {word: word.title() for word in frase.split(' ')}
print(' '.join([dictionarie[word] for word in frase.split(' ')]))

del dictionarie

#Method FOUR!
print(frase.title())

#Method FIVE!
from string import capwords
print(capwords(frase))

#Method SIX!
class FakeString(str):
    def __init__(self, obj=None):
        if not obj:
            self.obj = self
        else:
            self.obj = obj
        super(FakeString, self).__init__()

    def __str__(self):
        return str(self.obj).title()

fake_frase = FakeString(frase)
print(fake_frase)
del fake_frase

#Method SEVEN!
def title_frase(frase: str):
    return frase.title()

print(title_frase(frase))

#Method EIGHT!
frase_listed = frase[::-1].split(' ')[::-1]
print(' '.join([word[-1].upper() + word[-2::-1] for word in frase_listed]))
del frase_listed

#Method NINE!
from string import ascii_lowercase, ascii_uppercase

dictionarie = {}
for index in range(26):
    dictionarie[ascii_lowercase[index]] = ascii_uppercase[index]

print(' '.join([dictionarie[word[0].lower()] + word[1:] for word in frase.split(' ')]))

#Method TEN!
#Em breve ;-;
