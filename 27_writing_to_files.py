# we can write and append external files in python
staff = open("27_employees.txt", "a")
staff.write("Michael - Regional Manager\n")
staff.close()
banks = open("27_banklist.txt", "w")
banks.write("JP Morgan Chase\n")
banks.close()

# w mode also helps us to create file if suck file doesn't exist

user_list = open("27_user_list.txt", "w")
user_list.write("Mobius Topuria")
user_list.close()

# one more example with html file extension

main_page = open("27_mainpage.html", "w")
main_page.write("<HTML> This is my first website created by python </HTML>")
main_page.close()
