#!/bin/bash
bash scripts/data_collection.sh
bash scripts/data_storage.sh
sqoop import-all-tables --connect jdbc:postgresql://hadoop-04.uni.innopolis.ru/team17_projectdb --username team17 --password hgVwomtl0OIAe7cF --compression-codec=snappy --compress --as-avrodatafile --warehouse-dir=project/warehouse --m 1