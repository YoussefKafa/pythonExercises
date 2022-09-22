import textwrap
string="AAABBBCCC"
#print( textwrap.wrap(string,3)) ['AAA','BBB','CCC']


#or

wrapper=textwrap.TextWrapper(width=3)
wrappedText=wrapper.wrap(text=string)
print(wrappedText)