# Running MapReduce on hdfs

Create a hdfs directory
```shell
hdfs dfs -mkdir /folder
```

Add your dataset into the hdfs directory
```shell
hdfs dfs -put data.json /folder
```

Run hadoop jar
```shell
hadoop jar /home/USER/hadoop-3.3.3/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
    -mapper "$PWD/mapper.py" \
    -reducer "$PWD/reducer.py" \
    -input /folder/data.json \
    -output /folder/output
```

Print output onto terminal
```shell
hdfs dfs -cat /folder/output/part-00000
```
