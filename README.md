# document-processing-scale
### How to build full this system?
#### 1. build base hadoop v3.3.1-java 8 from ./dps-hadoops/base
```sh
    docker build -t duynguyenngoc/dps-hadoop-base:3.3.1
```
#### 2. build datanode hadoop v3.3.1-java 8 from ./dps-hadoops/datanode
```sh
    docker build -t duynguyenngoc/dps-hadoop-datanode:3.3.1
```
#### 3. build historyserver hadoop v3.3.1-java 8 from ./dps-hadoops/historyserver
```sh
    docker build -t duynguyenngoc/dps-hadoop-historyserver:3.3.1 .
```