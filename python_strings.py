# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
#   - my_last_name
#       -set this equal to your last name
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
#   - current_year
#       -set this equal to 2020
my_first_name = 'corey'
my_last_name = 'Anderson'
my_year_of_birth ='1998'
current_year = '2020'



# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)
print (my_first_name)
print(my_last_name)
print (my_first_name [+0])
print (my_last_name [-1])
print (my_first_name[+0:+1])
print (my_last_name [-1:-2])

#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times
c = my_first_name + (' ') + my_last_name
print (c)
print (my_first_name * 6) 



# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
print (c, 'was born in', my_year_of_birth)
print (c, 'was born in', my_year_of_birth, my_first_name, 'enjoyed celebrating',current_year)

# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year


# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case