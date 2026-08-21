'''
First test:
x = [1,2,3]
y = x

print("Before:")
print("x:", x)
print("y:", y)

y.append(4)

print("\nAfter:")
print("x:",x)
print("y:",y)
'''

'''
Second test:
x = [1,2,3]
y = x

print (x is y)
print (x == y)

y = x.copy()

print (x is y)
print (x == y)
'''
'''
Thrid test
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
print(add_item("C"))
'''
'''
def add_item(item, items= None): # items=None: The caller didn't provide a list.
    if items is None:
        items = [] # If the caller didn't provide a list, create a new one.

    items.append(item)
    return items


print(add_item("A"))
print(add_item("B"))
print(add_item("C"))

my_list = ["x", "y"]

print(add_item("z", my_list))
print(my_list)

a = add_item("A")
b = add_item("B")

print(a is b)
print(a == b)

'''
def clean_text(text):
    text = text.strip()
    text = text.lower()
    return text


def count_words(text):
    words = text.split()
    return len(words)


def process_document(doc):
    cleaned_text = clean_text(doc)
    word_count = count_words(cleaned_text)
    return word_count


document = "   HELLO WORLD   "

result = process_document(document)

print(result)