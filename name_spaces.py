def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
# inner_function() # функция является локальным эелемтом функции test_function,
# поэтому ее интерпретатор не видит в глобальном пространстве
