# this is a simple prototype to clarify the possible flow to automation and highlight the main result.

# ETL Automation Workflow Testing




# Local Spark 
## install spak locally
## Spark cluster:
install  spark on Ubuntu: https://phoenixnap.com/kb/install-spark-on-ubuntu
examples:/home/rosasilva/Downloads/spark-3.3.0-bin-hadoop3/examples/src/main/python/sql

## config. You need start spark Master and one job:
($ pwd) spark: /opt/spark
### start master:
```
/opt/spark/sbin/start-master.sh
```

locate jdk:  update-alternatives --config java 
jdk: /usr/lib/jvm/java-11-openjdk-amd64

### config
```
export HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=$HADOOP_HOME/lib/native"
```

### start slave worker process:
```
/opt/spark/sbin/start-slave.sh spark://gitlab:7077
```

### For spark to use the postgres driver 
pyspark --packages org.postgresql:postgresql:42.2.10


### spark configuration:
spark_session = SparkSession.builder.master("ip").enableHiveSupport().getOrCreate()

spark_session.conf.set("spark.executor.memory", '8g')
spark_session.conf.set('spark.executor.cores', '3')
spark_session.conf.set('spark.cores.max', '3')
spark_session.conf.set("spark.driver.memory", '8g')
sc = spark_session.sparkContext


## Install libs:
pip (to check: pip --version )
python  (to check: python3 --version)

```
pip install -r requirements.txt
```

## command to generate BDD skeleton run:
```
pytest-bdd generate src/tests/features 
```


## Papermill 
Libs example:
 ```
 import papermill as pm

pm.execute_notebook(
   'path/to/input.ipynb',
   'path/to/output.ipynb',
   parameters = dict(alpha=0.6, ratio=0.1)
)
```

### load notebook from:
Local file system: local
HTTP, HTTPS protocol: http://, https://
Amazon Web Services: AWS S3 s3://
Azure: Azure DataLake Store, Azure Blob Store adl://, abs://
Google Cloud: Google Cloud Storage gs://

### cli:

```
papermill ./notebooks/connection.ipynb  ./reports/connection_report.ipynb  -p db db-test 
```


#command BDD run scenarios:
```

pytest
or 

behave tests/features/prototype.feature  
```

Custom message fail: https://docs.pytest.org/en/stable/how-to/capture-warnings.html#custom-failure-messages

video Netflix: https://www.youtube.com/watch?v=7ER9tqiNack&t=2s

## Spark library to testing: 
https://pypi.org/project/pyspark-test/
assertDataframeEqual(df,df)

example: https://medium.com/@davisjustin42/writing-pyspark-unit-tests-1e0ef6187f5e
https://mungingdata.com/pyspark/testing-pytest-chispa/


# Best parctices:
create small, reusable and well-named function;


## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://git.worten.net/qa/etl.git
git branch -M main
git push -uf origin main
```

# ETL Testing: what should we test?
## Consistency: for example, all values are in unique way? dollar != $ != USD;
## Acuracy: is all data valid and in a pattern?
## Vality: rules for a specific attibute, per table and per attibute;
## Completeness: values null are treated, total of records by attribute load from sourge to target;
## uniqueness: duplication of data per table;
## Timeliness:data in a given period of time;
## Integrity: correct e full load from source to target;
## Profiling: number of records per table.




# Why should we have ETL Automation testing?
## Ad-hoc testing for any strategy in Quality Assurance can be time-consuming, inefficient and inconsitency.



