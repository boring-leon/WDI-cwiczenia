#weryfikująca, czy ciąg znaków jest palindromem 
#return text[::-1].lower() == text.lower()

def isPalindrome(text):
    text = text.lower()
    for index in range(0, len(text)): 
      if text[index] != text[len(text) - index - 1]:
            return False
        
    return True


while True:
    text = str(input("Podaj wyraz: "))
    if isPalindrome(text):
        print("Podany wyraz jest palindromem")
    else:
        print("Podany wyraz nie jest palindromem")