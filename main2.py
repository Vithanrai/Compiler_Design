
# Returns 'true' if the character is a DELIMITER.
def is_delimiter(ch):
    if ch == ' ' or ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '(' or ch == ')' or ch == '{' or \
            ch == '}' or ch == '<' or ch == '>' or ch == '=' or ch == '[' or ch == ']' or ch == ',' or ch == ';':
        return True
    return False


# Returns 'true' if the character is an OPERATOR.
def is_operator(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '<' or ch == '>' or ch == '=':
        return True
    return False


# Returns 'true' if the string is a VALID IDENTIFIER.
def valid_identifier(string):
    if string[0] == '0' or string[0] == '1' or string[0] == '2' or string[0] == '3' or string[0] == '4' or string[0] == '5' or \
            string[0] == '6' or string[0] == '7' or string[0] == '8' or string[0] == '9' or is_delimiter(string[0]) == True:
        return False
    return True


# Returns 'true' if the string is a KEYWORD.
def is_keyword(string):
    if string == 'if' or string == 'else' or string == 'while' or string == 'do' or string == 'break' or string == 'continue' or \
            string == 'int' or string == 'char' or string == 'float' or string == 'double' or string == 'return' or string == 'case' or\
            string == 'sizeof' or string == 'long' or string == 'short' or string == 'typedef' or string == 'switch' or \
            string == 'unsigned' or string == 'void' or string == 'static' or string == 'struct':
        return True
    return False


# Returns 'true' if the string is an INTEGER.
def is_integer(string):
    leng = len(string)
    if leng == 0:
        return False
    for i in range(leng):
        if string[i] != '0' and string[i] != '1' and string[i] != '2' and string[i] != '3' and string[i] != '4' and string[i] != '5' \
                and string[i] != '6' and string[i] != '7' and string[i] != '8' and string[i] != '9' or string[i] == '-' and i > 0:
            return False
    return True


# Returns 'true' if the string is a REAL NUMBER.
def is_real_number(string):
	leng = len(string)
	hasDecimal = False

	if leng == 0:
		return False
	for i in range(leng):
		if string[i] != '0' and string[i] != '1' and string[i] != '2' and string[i] != '3' and string[i] != '4' and string[i] != '5'\
			and string[i] != '6' and string[i] != '7' and string[i] != '8' and string[i] != '9' and string[i] != '.' or\
            string[i] == '-' and i > 0:
			return False
		if string[i] == '.':
			hasDecimal = True
	return hasDecimal


# Returns 'true' if a string is a PUNCTUATION
def is_punctuation(ch):
    if ch == '(' or ch == ')' or ch == '[' or ch == ']' or ch == '{' or ch == '}' or ch == ',' or ch == ';'\
            or ch == ':':
        return True
    return False


# Extracts the SUBSTRING.
def sub_string(string, left, right):
    """
    subStr = [right - left + 2]
    for i in range(left, right+1):
        subStr[i - left] = str[i]
        subStr[right - left + 1] = None
        """
    sub_str = string[left:right]
    return sub_str


# Parsing the input STRING.
def parse(string):
    left = 0
    right = 0
    leng = len(string)
    while right <= leng and left <= right:
        if is_delimiter(string[right]) == False:
            right += 1
        if is_delimiter(string[right]) == True and left == right:
            if is_operator(string[right]) == True:
                print(string[right] + " IS AN OPERATOR\n")
            right+=1
            left = right
        elif is_delimiter(string[right]) == True and left != right or right == len and left != right:
            sub_str = sub_string(string, left, right)
            if is_keyword(sub_str)==True:
                print(sub_str + " IS A KEYWORD\n")
            elif is_integer(sub_str) == True:
                print(sub_str + " IS AN INTEGER\n")
            elif is_punctuation(sub_str)==True:
                print(sub_str + 'IS A PUNCTUATION')
            elif is_real_number(sub_str)==True:
                print(sub_str + " IS A REAL NUMBER\n")
            elif valid_identifier(sub_str)==True and is_delimiter(string[right+1]) == False:
                print(sub_str + " IS A VALID IDENTIFIER\n")
            elif valid_identifier(sub_str)==False and is_delimiter(string[right+1]) == False:
                print(sub_str + " IS NOT A VALID IDENTIFIER\n")
            left = right
    return 0


# DRIVER FUNCTION
# maximum length of string is 100 here
string = 'int a=b+1c;'
parse(string)  # calling the parse function
