# Отчет по Лабораторной работе №3 " Анализ защищенности с использованием Kali Linux и Damn Vulnerable Linux (DVL)"

## Задание 1. Начальная настройка

Устанавливаем Kali и DVL. Определим IP на DVL

![](./images/1_Define_DVL_IPs.png)

## Задание 2. Сканирование Сети и Уязвимостей

1. Nmap

![](./images/2_Nmap.png)

2. OpenVAS

![](./images/3.1_OpenVAS_results.png)
![](./images/3.2_OpenVAS_results.png)

## Задание 3. Пентестинг Веб-Приложений
1. XSS<br>
Тестируем приложение

![](./images/4.1_XSS.png)

Перехватываем и меняем запрос

![](./images/4.2_XSS.png)

Успешное выполнение

![](./images/4.3_XSS.png)

3. CSRF<br>
Тестируем приложение

![](./images/5.1_CSRF.png)

Перехватываем и меняем запрос

![](./images/5.2_CSRF.png)

Успешное выполнение

![](./images/5.3_CSRF.png)

## Задание 4. Анализ Безопасности Системы

1. Metasploit<br>
Задаем нужные параметры
 
![](./images/6.1_MSF.png)

Получаем пароль root пользователя

![](./images/6.2_MSF.png)

2. JohnTheRipper<br>
С помощью найденного пароля заходим в SSH и подключаемся к MySQL - находим учетку
 
![](./images/7.1_John.png)

Ломаем пароль учетки "admin"

![](./images/7.2_John.png)

## Задание 5. Сетевая Защита и Защита От Вторжений

1. Wireshark<br>
Детект аномальных запросов

![](./images/8.1_Wireshark.png)

2. Snort<br>
Правила защиты

![](./images/8.2_Snort.png)
