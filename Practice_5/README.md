# Отчет по Практичсекой работе №5
## Мандатное управление
1. Установим Astra Linux. Зададим параметры мандатного управления

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/1.png)

2. Зададим уровни целостности (я задал 1 и 4) для тестовых директорий и их содержимых в "Управление политикой безопасности" - "Режим эксперта".

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/3.png)
   
3. Проверим работоспособность механизма МКЦ (запрет на запись "вверх" - NWU)<br>
   Пробую скопировать файл из директории большего уровня целостности в меньший - никак.

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/4.png)

   Если наоборот - все нормально.

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/5.png)

## Режим замкнутой программной среды (ЗПС)
1. Проверим работу механизма ЗПС (попытка запуска неподписанного исполняемого файла).<br>
   Для этого в Управлении политикой безопасности включаем следующие настройки:

  ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/6.png)

   Для этого мы попробуем запустить скрипт дополнения гостевой ОС.

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/7.png)

## Утилиты контроля целостности и регламентного контроля целостности: gostsum, afick
1. Gostsum - это утилита, которая вычисляет хэш-сумму файлов в соответствии с ГОСТ Р 34.11-2012.<br>
   Создалим файл и с помощью gostsum находим его хеш.<br>
   Затем изменим данный файл и снова находим хеш - видим, что значения хешей разные.

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/gostsum.png)

3. Afick - это утилита, которая следит за целостностью файловой системы ОС.<br>
   В конфигурационном файлы мы можем задать, за чем будем следить и какие правила использовать - я добавил /etc/ и применил стандартные правила MyRule.<br>
   Теперь представим ситуацию, что злоумышленник создал свою папку в директории /etc/.
  
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/afick1.png)

   Выполним команду - видим, что команда показала нам изменения в файловой системе ОС - создался файл.

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_5/images/afick2.png)
