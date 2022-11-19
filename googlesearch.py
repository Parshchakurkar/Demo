#importing webbrowser module as wb

import webbrowser as wb

#defining variable to get data search over google
search = input("what you want to search on google\n")

wb.open("https://www.google.com/search?q="+search)
