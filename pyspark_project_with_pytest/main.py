import pyspark.sql.functions as f

def filter_spark_data_frame(
    dataframe,
    column_name = 'age',
    value = 20
):
    return dataframe.where(f.col(column_name) > value)