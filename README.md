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
        - `docker start -i gbhdp` - для поторного запуска контейнера 
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

    *Комент учителя)*

    При факторе репликации равном 3-м, каждый блок будет продублирован 3 раза. При очень неудачном стечении обстоятельств, если из строя будут выведены 3 ноды, содержащие один и тот же реплицированный блок, мы уже получим потерю данных. Значит, максимум в таком случае составит 2 ноды. При очень удачном стечении обстоятельств, если из строя будут выводиться ноды, но всегда на кластере будет оставаться хоть одна реплика каждого блока, то из строя может быть выведено (400 / 3) * 2, округленное вниз, что равно 266 нодам. Но на практике чаще всего стоит бояться отключения уже 3 нод в кластере. Допустим, один сервер вмещает 100 000 блоков (14 терабайтные жесткие диски). Значит, при отключении 1 сервера точно затронуты блоки на 399 оставшихся нодах: так как распределение случайное, то каждая нода хранила у себя около 100 000 / 399 = 250 блоков от отключенного сервера. Потом отключается второй случайный сервер. Мы знаем что оставшиеся ноды хранили около 250 копий блоков из первой упавшей ноды, значит теперь точно среди оставшихся 398 нодах есть такие, на которых осталось только по 1 блоку. Вывод 3 случайной ноды приведет к потере данным с вероятностью до (250/398) * 100%=63%. Но это если на них стоят по одному 14 терабайтному диску. На реальном сервере вполне могут поставить от 8 до 32 дисков до 14 тб каждый. В этом случае вероятность потери данных уже 100%.

----

## Урок 3 - YARN & MR

### **Практика**

`echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py | sort -k1,1` - запуск программы и сортировка выходных значений

`echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py | sort -k1,1 | /home/hduser/reducer.py` - и выполнение слежующей программы

` ls hadoop/share/hadoop/tools/lib/` - утилиты которые будут забирать из stdin и подставлять в stdout

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок18.PNG)

`hadoop-streaming-2.10.1.jar` - нужная утилита

`hadoop jar ./hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar \`


`> -D mapred.reduce.tasks=2` - конфигурация, указали, что у задачи должно быть 2 редьюсера

`> -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py` - указываем мапер(1 арг - откуда загружать, 2 арг - куда загружать)

`hadoop jar ./hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py -file /home/hduser/reducer.py -reducer /home/hduser/reducer.py -input /user/hduser/ppkm -output /user/hduser/ppkm.out` - итоговая команда запуска

`hdfs dfs -ls /user/hduser/ppkm.out` - посмотреть результат, смотреть можно только когда появится файл *_SUCCESS

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок19.PNG)

1. Разверните кластер hadoop, соберите WordCount приложение, запустите на датасете ppkm_sentiment и выведите 10 самых редких слов*

    *[Решение](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screepts/reducer.py)*

2. Измените маппер в WordCount так, чтобы он удалял знаки препинания и приводил все слова к единому регистру

    *[Решение](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screepts/mapper.py)*


### **На подумать**

1. Может ли стадия Reduce начаться до завершения стадии Map? Почему?

    *Ответ*: нет, так как после этапа map следует операция data shuffle

    *Комент учителя)*

    На самом деле это вопрос с подвохом, так как есть фаза reduce и этап reduce. Фаза Reduce состоит из трёх этапов: шафл, сортировка, свертка. Непосредственно свертка начнется только после окончания сортировки, а это невозможно пока не будут получены все данные от мапперов. При этом, этап шафла можно начать до завершения всех мапперов, изменив поле mapreduce.job.reduce.slowstart.completedmaps в конфиге


2. Приведите пример Map only и Reduce задачи.

    *Ответ*: 
    
    1. Map only:
    
        - Фильтрация данных (например, «Найти все записи с IP-адреса 123.123.123.123» в логах web-сервера)
        
        - Преобразование данных («Удалить колонку в csv-логах»)
        
        - Загрузка и выгрузка данных из внешнего источника («Вставить все записи из лога в базу данных»)

    2. Reduce only задача невозможна, так как входные данные должны быть ключ-значение из map

3. У вас есть два датасета с одинаковыми ключами. Вам нужно их объединить, суммировав значения с одинаковыми ключами. Как это сделать в MapReduce?

    *Ответ*: задача похожа на word count, только в этом случае часть map просто получает и отдает ключ-значение, далее в части reduce значения по отсортированным ключам можно сложить

4. На кластере лежит датасет, в котором ключами является id сотрудника и дата, а значением размер выплаты. Руководитель поставил задачу рассчитать среднюю сумму выплат по каждому сотруднику за последний месяц. В маппере вы отфильтровали старые записи и отдали ключ-значение вида: id-money. А в редьюсере суммировали все входящие числа и поделили результат на их количество. Но вам в голову пришла идея оптимизировать расчет, поставив этот же редьюсер и в качестве комбинатора, тем самым уменьшив шафл данных. Можете ли вы так сделать? Если да, то где можно было допустить ошибку? Если нет, то что должно быть на выходе комбинатора?

    *Ответ*: нет, так как данные могут быть распределены не равномерно по нодам, тогда среднее будет посчитано неверно. На выходе комбинатора значения можно передавать в виде сторки {сумма_зп}_{кол-во выплат}, при условии что мапер возвращает строку {сумма_зп}_{1}

### Вопросы:

1. На этапе партиционирования данные перемешиваются и отправляются на соседние сервера для редьюса, получается что итоговые файлы будут чуть более точные чем после комбинатора, но мы получим же по сути несколько средьюсенных файлов с разным результатом, а не один, и эти несколько файлов надо объединять и еще раз редьюсить? Не понимаю как из нескольких редьсеров получается один файл

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок17.PNG)

Вы говорили, что данные распределяюся по формуле, но получается, что например, значения с ключом 'A' может разлететься по 2ум редьюсерам для рассчета, если таких ключей окажется слишком много

2. Что такое key.hashcode()? и как он выглядит? 

3. Как в интерфейсе посмотреть выполнение MapReduce?

### Полезные ссылки:

1. https://habr.com/ru/post/270453/

2. https://habr.com/ru/post/74792/

----

## Урок 4 - Hive & HUE

### **Теория**

- Модель данных:
    1. Tables/ Таблицы
    2. Partitions/ Секции
    3. Buckets/ Сегменты

- DDL:
    ```
    CREATE TABLE mytable(id INT, nameSTRING, age INT, city STRING) # объявляем схему
    COMMENT 'This is a simple table' # комментарий для читаемости
    PARTITIONED BY (city STRING) # партиционирование
    ROW FORMAT DELIMITED # строки разделяются  '\n'
    FIELDS TERMINATED BY ',' # поля разделяются запятой
    STORED AS TEXTFILE; # хранится в виде текстового файла

    # таблица создается в спец директории warehouse и полностью находиться под управлением Hive
    ```

    ```
    CREATE EXTERNAL TABLE my_external_table(id INT, name STRING, age INT, city STRING)
    LOCATION '/user/ivanov/mytable';

    # таблица не создается в warehouse, у hive сохраняется только ссылка на нее
    ```
- DML:
    ```
    LOAD DATA LOCAL INPATH '/home/ivanov/peoples.txt'
    INTO TABLE mytable;
     
     # файл peoples.txt находиться в локальной файловой системе и будет скопирован в директорию warehouse
    ```

    ```
    LOAD DATA INPATH '/user/ivanov/peoples.txt'
    INTO TABLE mytable;

    # файл peoples.txt находится в HDFS и будет скопирован в директорию warehouse
    ```
- Запросы

    ```
    SHOW TABLES;

    SELECT p.*, o.*
    FROM mytable p
    JOIN orders p
    ON (p.id = o.id);

    SHOW FUNCTIONS;

    DESCRIBE FUNCTION lenght; # посмотреть описание фун-ции

    ```

- Типы функций:
    - UDF - применяются построчно
    - UDAF - используются совместно с GROUP BY оператором
    - UDTF - применяются на таблицу целиком
    - можно расширить библиотеку своими функциями, добавив в classpath hive

- 



### **Практика**

`wget https://downloads.apache.org/hive/hive-2.3.9/apache-hive-2.3.9-bin.tar.gz` - скачать архив с hive

`tar xzf apache-hive-2.3.9-bin.tar.gz` - распаковать архив

Действуют только в текущей сессии:

    `1. export HIVE_HOME=/home/hduser/hive/` - задаем системную переменную, 

    `2. export PATH=$PATH:$HIVE_HOME/bin` - задаем системную переменную, чтобы откуда угодно можно было обращаться к hive

Вставим эти переменные в файлик, чтобы они не затирались при закрытии сессии

`ls -a` - посмотреть скрытыте файлы

`vi .bashrc` - открываем редактор vim

`shift + g` - чтобы переместиться вниз блокнота vi 

`shift + a` - переход в конец файла и включается режим ввода



`schematool -dbType derby -initSchema` - инициализация бд

`hive` - команда для запуска hive

`hive -e 'show tables;'` - исполнение команды без захода в оболочку

`hive -f show.sql` - запуск скрипта в файле

Поднимим сервер Hive:

`vi ~/hive/conf/hive-site.xml` - создадим файл с настройками

`hiveserver2 &> /dev/null &` - запускаем сервер, вывод логов перенаправляем и консоль возвращаем в свое пользование

`netstat -tulpn` - запущенные порты

`beeline -u jdbc:hive2://localhost:10000` - консольная утилита для подключения к hive **Почему то не подключилось**

`!q` - выход из билайна



3. Составьте запрос, который выведет имя набора (sets.name) с самым большим количеством деталей (sets.num_parts)
```
select name, year, num_parts
from lego_sets
where num_parts in (select MAX(num_parts) from lego_sets);
```

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок20.PNG)

4. Составьте запрос, который выведет в каком году (sets.year) вышло больше всего наборов

```
select year, count(year) as count_year
from lego_sets
group by year
order by count_year desc
limit 1;   
```

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок21.PNG)

5. Составьте запрос, который выведет общее количество деталей (inventory_parts.quantity) для каждого из цветов (colors.name)

```
select c.name, count(p.quantity) as count_quantity
from lego_inv_parts p
join lego_colors c on (p.color_id=c.id)
group by c.name
order by count_quantity desc
limit 5;
```

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок22.PNG)

6. * Измените Dockerfile так, чтобы вместе с Hadoop устанавливался и запускался Hive



## Урок 5 - Форматы хранения

### **Практика**

`show columns from lego_inv_parts;` - показать названия колонок из таблицы

`hdfs dfs -ls /user/hive/warehouse/` - местопопложение файлов, которые залиты как таблицы в hive

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок23.PNG)

`SET parquet.compression=SNAPPY;`

`SET parquet.compression=GZIP;`

`SET parquet.compression=uncompressed;` - установить тип сжатия для паркета

`-du` - disk usage

`create table lego_inv_parts_par_snappy(inventory_id INT, part_num STRING, color_id INT, quantity INT, is_spare STRING) stored as parquet;` - создание таблицы со сжатем

`insert overwrite table lego_inv_parts_par_snappy select * from lego_inv_parts; ` - наполнение таблицы

![](https://github.com/stitsyuk98/big_data_hadoop/blob/main/screenshots/Снимок24.PNG)

2. Сравните степень сжатия (отношения несжатого файла к сжатому) таблицы в которой есть колонки типа STRING с таблицей без колонок этого типа

    **Решение**: было создано 2 таблицы без компрессии, для одной были все стобцы типа int(итоговый вес: 1218831, без сжатия 5837588, отношение сжатия 0,2087), для 2ой - string(итоговый вес: 1274900, без сжатия 5837588, отношение сжатия 0,2183). Тип int занимает меньше места.

3. Чем AVRO отличается от CSV?

    **Ответ**: AVRO имеет схему, т е можно разделить файл
