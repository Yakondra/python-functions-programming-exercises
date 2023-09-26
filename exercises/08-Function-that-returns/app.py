def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######

dollar_value=137
dolaryen= (euro_to_yen(dollar_to_euro(dollar_value)))
print(dolaryen)