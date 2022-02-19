# document-processing-scale
### How to build full this system?
#### 1. build base hadoop v3.3.1-java 8 from ./dps-hadoops/base
#### 2. build datanode hadoop v3.3.1-java 8 from ./dps-hadoops/datanode
#### 3. build historyserver hadoop v3.3.1-java 8 from ./dps-hadoops/historyserver
....

Namenode: http://<dockerhadoop_IP_address>:9870/dfshealth.html#tab-overview
History server: http://<dockerhadoop_IP_address>:8188/applicationhistory
Datanode: http://<dockerhadoop_IP_address>:9864/
Nodemanager: http://<dockerhadoop_IP_address>:8042/node
Resource manager: http://<dockerhadoop_IP_address>:8088/