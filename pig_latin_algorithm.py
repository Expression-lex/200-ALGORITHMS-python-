def pig_latin(word):
    vowels =['a','e','i','o','u']
    front =None

    for index, char in enumerate(word):
         if char in vowels:
             front = word[index:]
             back = word[:index]
             break
    
    if not front:
        return 'No vowels!'

    translation = front + back + 'ay'
    return translation

print(pig_latin('small'))