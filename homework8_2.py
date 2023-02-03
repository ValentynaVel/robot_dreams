# 2 Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".

class MyCustomExeption(Exception):
    pass

raise MyCustomExeption('Custom exception is occured')


