BEELINE_CMD="beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team17 -p hgVwomtl0OIAe7cF"

$BEELINE_CMD -f sql/delete_dataset.hql

echo "Dataset deleted to free space"