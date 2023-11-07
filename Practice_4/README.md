# Отчет по Лабораторной работе №1
## Rsyslog. Сервер
1. На ВМах настроил сеть на Сетевой мост
2. На первой ВМ (сервере) скачаем rsyslog
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/1.png)
3. Запустим сервис и включим режим автозагрузки. Проверим работоспособность
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/2.png)
4.Чтобы настроить rsyslog в качестве реципиента/сервера ведения журнала, необходимо установить протокол (либо UDP, либо TCP,   либо оба), который он будет использовать для удаленного приема системного журнала, а также      порт, который он прослушивает. Также нужно определить набор правил для обработки удаленных журналов:
    - первая строка - куда сохраняются логи
    - вторая строка - откуда и что сохраняется
    - третья строка - указывает rsyslog прекратить обработку сообщений после их записи в файл. Если вы не укажете «&~», сообщения будут записаны в локальные файлы.
  Для этого редактируем файл /etc/rsyslog.conf
  ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/3.png)
5. Перезапускам сервис
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/4.png)

## Rsyslog. Клиент
1. На второй ВМ (клиенет) скачаем rsyslog. Запустим его и включим режим автозагрузки. Проверим работоспособность
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/5.png)
2. Отредактируем файл /etc/rsyslog.conf, добавив в конец файла правило пересылки логов
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/6.png)
3. Перезапускам сервис
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/7.png)
5. Проверим работоспособность - наличие новой директории в /var/log. И попробуем создать SSH логи
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/8.png)

## Loki
1. Развернем на сервре Loki используя docker compose
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/9.png)
2. Запускаем
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/10.png)
3. На клиенте установим Promtail - агент, который читает и отправляет логи на сервер. Распакуем его и файлы создадим
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/11.png)
   Создадим файл конфигурации /etc/promtail/promtail.conf
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/12.png)
   Создаем юнит
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/13.png)
4. Перезапускаем сервис
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/14.png)
5. Для проверки на клиенте зайдем под именем нового пользователя
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/15.png)
   Просмотрим на сервере логи
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/16.png)

## Signoz
1. Клонируем репозитрий для сервера - https://github.com/SigNoz/signoz.git
   Запускаем контейнер.
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/17.png)
2. Клонируем репозитрий для клиента - https://github.com/SigNoz/sample-nodejs-app.git
   Редактируем docker-compose файл.
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/18.1.png)
   Запускаем контейнер.
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/18.png)
3. Сделам пару запросов к клиентскому приложению
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/19.png)
5. Теперь в Signoz можем наблюдать логи
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/20.png)
   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_4/images/21.png)







   
