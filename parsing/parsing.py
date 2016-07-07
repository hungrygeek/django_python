# now I am putting ingredient in one list and amount inanother list and other info in other list as well. 
# I can also put it all in one list in tuples.


ingredient_file = open('ingredient_list','r+');
ingredient_file_str = ingredient_file.read();
ingredient_list = ingredient_file_str.split('\n');

test = open('testfile','r+');
teststr = test.read();

parsedingredient = teststr.split('\n');
if len(parsedingredient) == 1:
	parsedingredient = teststr.split(',');
if len(parsedingredient) == 1:
	parsedingredient = teststr.split(';');

for emptyitem in parsedingredient:
	if emptyitem =='':
		parsedingredient.remove(emptyitem);

# this amount_of_ingredietn list still have one problem. it doesnot parse numbers such as '1/2' of '1/3' it only take the first int from it. which will be a big problem. still working on this bit.
ingredient_name = [];
i=0;
for full_ingredient_str in parsedingredient:
	for single_ingredient in ingredient_list:
		if single_ingredient in full_ingredient_str:
			ingredient_name.insert(i,single_ingredient);
			i = i+1;


amount_of_ingredient = [];
i=0;
for ingredientstr in parsedingredient:
	for s in ingredientstr.split():
		if s.isdigit():
			amount_of_ingredient.insert(i,s);
			i = i+1;


# print result

for ingredient in parsedingredient:
	print ingredient;

print amount_of_ingredient;

print ingredient_name;



