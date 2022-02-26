# Практика по курсу GB Hadoop

## Урок 1 - Введение в Hadoop

### **Практика**

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

### **На подумать)**

Вы пришли в компанию, в которой планируют строить Data Lake и DWH с нуля. Текущих данных около 15 Тб. Ежегодный прирост данных составляет ~500 Гб. Какую технологию вы бы предложили использовать и почему?

Технология Hadoop не подходит, так как данных слишком мало. Нужно использовать другие решения в зависимости от данных и задачь их использования.

----

## Урок 2 - HDFS

### **Практика**

Синтаксис:

`hadoop fs -<command> -<option> <uri>` - первый hadoop

`hdfs dfs -<command> -<option> <uri>` - второй hadoop

URI:  `hdfs://<NameNode-Host>:<Port>/user/home`

_____scheme___________authority____hdfs path

Ex: `hdfs dfs -ls hdfs://localhost:9000/`

`hdfs dfs -ls /` - корневая директория

`hdfs dfs -ls /user/hduser/` - рабочая директория пользователя hduser и пути без корня являются относительными рабочей

`hdfs dfs -mkdir /user/hbuser/lesson2` - создать папку

`hdfs dfs -ls file:///` - обращение к локальной файловой системе

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок8.PNG)

`hdfs dfs -ls hdfs://localhost:9000/user/hd{use,smth}r` - перечисление папки

`vi 1.txt` -  создать файл в редакторе vim, чтобы перейти в режим ввода надо нажать `i`, затем нажать esc чтобы выйти в командный режим, чтобы сохранить и выйти нажать `:wq`

`hdfs dfs -put 1.txt /user/hduser/lesson2/` - переместить файл из локального хранилища в dfs

Для чтения файла:

`hdfs dfs -cat lesson2/1.txt`

`hdfs dfs -text lesson2/1.txt`

`hdfs dfs -chmod -r lesson2/1.txt` - изменеие прав

`hdfs dfs -chmod u-r lesson2/1.txt` - отнять права на чтение только у юзера

`hdfs dfs -chown hive less  on2/1.txt` - изменить пользователя кот принадлежит файл

`hdfs dfs -chown hive:hivegroup lesson2/1.txt` - изменить группу

`hdfs dfs -du lesson2` - выведет размер файла или директории

`hdfs dfs -du -s lesson2` - выведет размер всей директории целиком

`hdfs dfs -du -s -h lesson2` - выведет размер всей директории целикомб переведет размер в читаемый вид

`hdfs dfs -mv lesson2/1.txt 2.txt` - переместили файл с переименованием

`hdfs dfs -rm -r lesson2` - удалить дерикторию

`hdfs dfs -get 2.txt .` - получить файл локальную файловую систему

`docker cp archive gbhdp:/home/hduser/` - скопировать папку в контейнер

`hdfs dfs -chmod -R +rwx ppkm` - выдать права всем пользователям

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок9.PNG)

`hdfs dfs -getfacl 2.txt` - читаемый формат прав на файл

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок10.PNG)

`hdfs dfs -setrep -w 3 2.txt` - ожидание пока файл реплицируется

`hdfs fsck 2.txt` - подробная инфа по файлу

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок11.PNG)

`hdfs fsck 2.txt -files -blocks -locations` - определить в каких блоках находится файл

![папака с 3мя файлами](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок12.PNG)

![файл больше 128мб](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок16.PNG)

Второй способ узнать имя блока — открыть файл в браузере HDFS в веб-интерфейсе NodeManager

`head /tmp/hadoop-hduser/dfs/data/current/BP-28129341-127.0.0.1-1645281000241/current/finalized/subdir0/subdir0/blk_1073741826` - посмотреть блок локально

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок15.PNG)

`hdfs dfsadmin -report` - отчет(лучше не запускать на боевых кластерах)

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок13.PNG)

`hdfs dfsadmin -metasave meta.txt` - создает файл кот генерирует только нейм нода, инфа о блоках

`ls hadoop/logs/meta.txt`

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок14.PNG)


### **На подумать**

1. У вас 20 файлов, каждый размером 130 мб. Сколько блоков будет аллоцировано в NameNode, при условии, что размер блока по умолчанию у вас 128 мб, а фактор репликации равен 3?

    *Ответ*: 20(файлов) * 2(блока) * 3(репликации) = 120 блоков
    
    *Комент учителя)*
    
        Чаще всего у студентов возникает два вопроса: почему все 2мб кусочки не поместить в один блок? Понять это проще, если задуматься о двух вещах:
    Во-первых, мы ничего не знаем о времени создания этих файлов. Если они создаются раз в час/день, то неймнода выделит для них по 2 блока и не будет заниматься поиском тех блоков, куда она могла бы их вместить. К тому же, такой поиск повлиял бы на скорость работы кластера.
    Во-вторых, если бы hdfs каким-то образом объединял блоки, то мы не смогли бы удалить файл или дописать информацию ему в конец. Ведь его конец был бы перемешан с другими файлами.
    Именно поэтому вопросами компактизации (объединения маленьких файлов) занимаются сами разработчики, так как только они знают - можно объединять эти файлы или нет.
    И второй вопрос: почему не делить размер данных поровну по 75 мб на блок? Тут как раз дело в том, что сплитование происходит непосредственно во время записи на диск по достижении определенного порога. Если бы мы пытались как-то балансировать размер блоков, то тогда данные пришлось бы накапливать в памяти перед записью, что сразу же влияет на скорость записи и на использование RAM у приложения.

2. У вас 1 файл, размером 1.56 Тб. Сколько блоков будет аллоцировано в NameNode, при условии, что размер блока по умолчанию у вас 128 мб, а фактор репликации равен 3?

    *Ответ*: (1.56тб * 1024 * 1024 / 128) (кол-во блоков) * 3 (репликации) = 38 340 блоков

3. В вашей компании развернут Hadoop кластер из 400 нод. Фактор репликации равен 3. Сколько единовременно может быть выведено машин из строя, чтобы не было потери данных?

    *Ответ*: Если выведены реплицированные ноды, то ответ 2, иначе 400 / 3 * 2 = 266 примерно
