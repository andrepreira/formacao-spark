import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('Iniciando com Spark') \
    .config('spark.ui.port', '4050') \
    .getOrCreate()
    
data = [('Zeca','35'), ('Eva','29')]
colNames = ['Nome','Idade']

df = spark.createDataFrame(data,colNames)
print(df)
df.show()
df.toPandas()