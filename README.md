# RT-testing
settings.py - содержит данные для ввода
test_RT.py - содержит тесты для проверки автоматической смены таба, авторизации, наличия элементов на странице

Необходимо установить библиотеки:
-pytest
-selenium
-pytest-selenium

Запустить тесты командой: python -m pytest -v --driver Chrome --driver-path path\to\chromedriver.exe/test_RT.py


Каждый тест открывает страницу браузера. Возможно появление формы вода капчи, в этом случае необходимо войти вручную в личный кабинет, после чего продолжить тестирование.
