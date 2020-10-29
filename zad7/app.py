def isPalindrome(text):
    return text[::-1].lower().replace(" ", "") == text.lower().replace(" ", "")

while True:
    text = str(input("Podaj wyraz pierwszy: "))
    if isPalindrome(text):
        print("Podany wyraz jest palindromem")
    else:
        print("Podany wyraz nie jest palindromem")