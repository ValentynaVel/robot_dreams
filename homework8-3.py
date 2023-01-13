# 3 Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед
# виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює. У випадку
#  виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.

class MyContextManager:
    def __init__(self, value):
        self.value = value
    def __enter__(self):
        print("="*10)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("="*10)
        return True
with MyContextManager(1) as some_value:
    try:
        print(4/2)
    except Exception as e:
        print(type(e), e)
    finally:
        print(f'some value is {some_value}')
