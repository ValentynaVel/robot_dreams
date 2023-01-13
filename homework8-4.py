# 4. Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що і менеджер контексту
# із попереднього завдання.

a = 4
b = 2
counter = 2
while counter:
    try:
        print("=" * 10)
        value = int(a/b)
    except Exception as e:
        print(type(e), e)
    else:
        print(value)
    finally:
        print("=" * 10)
        counter -= 1
