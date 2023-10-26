# Отчет по Лабораторной работе №1
## На ВМах настроил сеть на Сетевой мост
## На первой ВМ запустим Keycloack с помощью Docker
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/1.png)

## На второй ВМ запсутим Nextcloud с помощью Docker-compose.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/6.png)

## В браузере переходимна на веб-интерфейс KeyCloak
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/2.png)

## Затем переходим в Administrative console с помощью учетных данных, используемых при запуске контейнера.<br> Создадим собственный Realm: На боковой панели кликаем на Master - Create Realm - Задаем имя - Save.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/3.png)

## Создадим пользователей appadmin и user: На боковой панели кликаем на Users - Add User - Задаем необходимые значения - Create.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/4.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/5.png)

## Зададим им пароли: Users - Выбираем пользователя - Credentials - Задаем пароль.
(Для user не задал пароль - посмотрим что будет)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/11.png)

## Создадим клиента в Keycloack: На боковой панели кликаем на Clients - Creeate client - Задаем необходимые значения - Create.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/7.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/8.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/9.png)

## Создадим роли admin и user: На боковой панели кликаем на Clients - Выбираем нашего клиента - Roles - Create role - Задаем необходимые значения - Save.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/10.png)

## Надо связать роль и пользователя

## Настроим аутентификацию на Nextcloud: Скачаем в App "Social Login". Затем перейдем в Административные настройки - Social Login - Custom Open ID Connet - Задаем необходимые параметры.
Endpoints можно найти в Realm Settings - OpenID Endpoint Configuration.
Секрет можно найти в Clients - Выбираем наш - Credentials.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/12.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/13.png)

## Настроим 2FA: В Keycloak переходим в Authentication - Browser - Browser Conditional OTP - Выбираем Required.
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/14.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/15.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Laba_1/images/16.png)
