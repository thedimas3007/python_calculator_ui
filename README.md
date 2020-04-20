﻿ # Калькулятор на Python с графическим интерфейсом

Все исходники лежат в директории src/

* При изменении UI нужно прописать: `pyuic5 "./src/gui.ui" -x -o ./src/gui.py`
* Для установки зависимостей пропишите в терминале/командной строке: `pip install -r requirements.txt`

## Описание файлов:

  * *src/gui.py* - интерфейс приложения, понятный для Python
  * *src/gui.ui* - интерфейс приложения, понятный для Qt Designer
  * *src/main.py* - главный код калькулятора
  * *requirements.txt* - файл с нужными библиотеками для установки
  * *README.md* - файл с описанием

При возникновении какой либо ошибке пишите о ней подробно в **Issues**, вот пример:
* Версия Python - *3.7.4*
* Разрядность Python (только Windows) - *32bit*
* Версия ОС и архитектура - *Windows 64bit*
* Ошибка - *KeyboardInterrupt*


В следующих версиях реализую логгинг

Тестировалось на:
* Windows 10 *64bit* + Python 3.7.4 *32bit* На Windows работает только на 32bit версии Python
* Mac OS 10.15.4 *64bit* + Python 3.8.2
* Ubuntu 19.10 *64bit* + Python 3.7.5
