# Отчет по Практичсекой работе №6
## 0. Исходные данные

![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/topology.png)
![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/route-table.png)

## 1. Проверка связи между маршрутизаторами
1. Определим IP-адрес порта S0/0/0 на маршрутизаторе RA

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/1.1.png)

2. Отправим с маршрутизатора RB эхо-запрос на IP-адрес интерфейса S0/0/0 маршрутизатора RA

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/1.2.png)
   
3. Отправим с ПК B эхо-запрос на IP-адрес компьютера ПК A.<br>
   Каковы результаты эхозапроса? Почему? Пинг не проходит, так как компьютеры не видят друг друга - туннель GRE не был настроен

   ![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/1.3.png)

## 2. Настройка туннелей GRE

1. Настройка туннеля GRE на роутере RA

![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/2.1.png)

2. Настройка туннеля GRE на роутере RB

![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/2.2.png)

3. Настроим маршрутизацию между сетями 192.168.Х.Х

![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/2.3.png)


## 3. Проверка связи между маршрутизаторами

![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/3.1.png)

## 4. Успешное выполнение задания

![](https://github.com/timMong/MIREA_TOIB_2023/blob/main/Practice_6/images/4.1.png)
