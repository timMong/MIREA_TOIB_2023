# Отчет по Лабораторной работе №1
## Шаг 1. Начальная настройка
1. На ВМах настроил сеть на Сетевой мост
2. На первой ВМ запустим Keycloack с помощью Docker
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/1.png)
3. На второй ВМ запсутим Nextcloud с помощью Docker-compose
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/2.png)

## Шаг 2. Настроим сервер Keycloack
1. В браузере переходимна на веб-интерфейс KeyCloak
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/3.png)
2. Затем переходим в Administrative console с помощью учетных данных, используемых при запуске контейнера.<br>
   Создадим собственный Realm: На боковой панели кликаем на Master - Create Realm - Задаем имя - Save.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/4.png)
3. Создадим пользователей appadmin и user: На боковой панели кликаем на Users - Add User - Задаем необходимые значения - Create.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/5.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/6.png)
4. Зададим им пароли: Users - Выбираем пользователя - Credentials - Задаем пароль.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/7.png)
5. Создадим клиента в Keycloack: На боковой панели кликаем на Clients - Creeate client - Задаем необходимые значения - Create.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/8.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/9.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/10.png)
6. Создадим роли admin и user: На боковой панели кликаем на Clients - Выбираем нашего клиента - Roles - Create role - Задаем необходимые       значения - Save.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/11.png)

## Шаг 3. Настройка Nextcloud
1. Настроим аутентификацию на Nextcloud: Скачаем в App "Social Login".<br>
   Затем перейдем в Административные настройки - Social Login - Custom Open ID Connet - Задаем необходимые параметры.<br>
  ---
  > Endpoints можно найти в Realm Settings - OpenID Endpoint Configuration.<br>
  > Секрет можно найти в Clients - Выбираем наш - Credentials.<br>
  ---
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/12.png)
 Видим, что появилась ссылка на Keycloak
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/13.png)
При нажатии она перенапрвляет на Keycloak
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/14.png)

## Шаг 4. Настройка 2FA
1. В Keycloak переходим в Authentication - Browser - Browser Conditional OTP - Выбираем Required.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/15.png)
Сканируем QR-код, прописываем данные
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/16.png)
Успешно попадаем на страницу
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/17.png)
