# Практика по курсу GB Hadoop

## Урок 1 - Введение в Hadoop

- Скачать файлы для образа hadoop
- Запустить коменду 

`docker build -t img-hdp-hadoop .`
- После сбор образа, запустить его командой 

`docker run -it --name gbhdp \
-p 50090:50090 \
-p 50075:50075 \
-p 50070:50070 \
-p 8042:8042 \
-p 8088:8088 \
-p 8888:8888 \
-p 4040:4040 \
-p 4044:4044 \
--hostname localhost \
img-hdp-hadoop`
- Ввести команды в bash внутри hadoop:

    + ls - выводит папки и файлы
    + pwd - выводит директорию в которой сейчас находимся
    + Можем посмотреть процессы которые запущены:
        - для этого надо установить `sudo apt-get install net-tools`
        - далее выполнить `netstat -tulpn`
        для просмотра на каких портах запущены java процессы
        ![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок2.PNG)
        - `jps -m`  команда, чтобы узнать что это за процесс в java
        ![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок1.PNG)
        - можно в браузере открыть namenode 
        ![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок3.PNG)
        - nodemanager
        ![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок4.PNG)
        ![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок6.PNG)
        ![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок7.PNG)
        - `exit`для выхода из bash
        ![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок5.PNG)
        - для поторного запуска контейнера `docker start -i gbhdp`
        - `docker rm gbhdp`  - удалить контейнер
        - `docker rmi img-hdp-hadoop` - удалить образ
        - `docker system prune` - удалить все кэши и остаточные файлы

## Домашнее задание
1. Разверните у себя hadoop кластер внутри docker контейнера
2. Проверьте работоспособность кластера, посмотрев на статус ресурс менеджера, нейм ноды и дата ноды
3. Остановите кластер
4. Вы пришли в компанию, в которой планируют строить Data Lake и DWH с нуля. Текущих данных около 15 Тб. Ежегодный прирост данных составляет ~500 Гб. Какую технологию вы бы предложили использовать и почему?

----


