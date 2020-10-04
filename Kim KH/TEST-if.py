# Megacity > 10,000,000
# Large Metropolitan area > 1,500,000
# Metropolitan Area > 500,000
# Medium size urban area > 200,000
# Small urban area > 50,000



my_city_name = 'Bogota'
City2 = 'Tokyo'
my_city_population = 6500000

if my_city_population > 10000000:
    print('My city is a Megacity')

elif my_city_population > 1500000:
    print('My city is a Large Metropolitan Area')
else:
    print('My city is neither a Megacity nor a large metropolitan area')

print('------------------------------------------------')



population_ct1 = 6500000
population_ct2 = 37435191
population_ct3 = 29399141
population_ct4 = 26317104
population_ct5 = 9963452
population_ct6 = 12628266

ct1 = 'Bogota'
ct2 = 'Tokyo'
ct3 = 'Delhi'
ct4 = 'Shanghai'
ct5 = 'Seoul'
ct6 = 'Paris'
Cities = (population_ct1,population_ct2,population_ct3,population_ct4,population_ct5,population_ct6)
for i in Cities:
    if i > 10000000:
        print(i, "is a Megacity")

    elif i > 1500000:
        print(i, "is a Large Metropolitan area")

    elif i > 500000:
        print(i, "is a Metropolitan area")

    elif i > 200000:
        print(i, "is a Medium size urban area")

    elif i > 50000:
        print(i, "is a urban area")

    else:
        print (i, "is a just small size city")

print('------------------------------------------------')
city1 = 'Bogota'
city1_population = 6500000
city2 = 'Seoul'
city2_population = 9963452

if city1_population > 10000000:
    print('city1 is a Metropolitan area')
elif city1_population > city2_population:
    print('city1 is bigger than the city')
else:
    print('city2 is bigger than city1')