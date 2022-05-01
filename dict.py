import cairo


cardict={
    'brand': 'ford',
    'model': 'Tesla',
    'year': '2022'
}
print(cardict['brand'])
print(cardict['model'])
print(cardict['year'])

# Using the "get method instead of print"
x=cardict.get('model')
print(x)
s=cardict.get('year')
print(s)
u=cardict.get('brand')
print(u)


#keys  & Values  NB Note they are keys and not key, values and not value

y=cardict.keys()
print (y)
z=cardict.values()
print(z)

#getting the length of dictionary
print(len(cardict))

#adding to the dictionary

cardict['color']= 'white'

print(cardict)
print(cardict.keys())
print(cardict.values())