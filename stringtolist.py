#converts string to list and removes spaces and digits
str=mystring
import re
def str_to_list( str ) :
	str1=str.replace(" ","")
	str2=re.sub('[6-9]+', '', str1)
	str3=list(str2)
	return str3
