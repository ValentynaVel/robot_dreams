# 3 Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед
# виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює. У випадку
#  виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.

class MyContextManager:
    def __enter__(self):
        print("="*10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Exception value: {exc_val} appeared.')
        print("="*10)

        # Your context manager should print the value of an exception if there is one. if exc_type: print(exc_value)
        # will make it works
        return True


a = 0
b = 6

with MyContextManager():
    print(b/a)

print('End of program')
