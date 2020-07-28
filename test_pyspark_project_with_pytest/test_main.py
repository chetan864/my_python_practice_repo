# from pyspark_project_with_pytest.main import filter_spark_data_frame
# from pyspark import SparkContext
# from pyspark.sql import SQLContext
# import pandas as pd
#
# # Spark Context initialisation
# def test_filter_spark_data_frame():
#     spark_context = SparkContext()
#     sql_context = SQLContext(spark_context)
#
#     # Input and Output dataframes
#     input = sql_context.createDataFrame(
#         [('charly', 15),
#          ('fabien', 18),
#          ('sam', 21),
#          ('sam', 25)
#          ('nick', 19),
#          ('nick', 40)],
#          ['name', 'age']
#     )
#
#     expected_output = sql_context.createDataFrame(
#         [('sam', 25),
#          ('sam', 21),
#          ('nick', 40)],
#          ['name', 'age']
#     )
#
#     real_output = filter_spark_data_frame(input)
#     real_output = get_sorted_dataframe(
#         expected_output.toPandas(),
#         ['age', 'name'],
#     )
#
#     # Equality assertion
#     pd.testing.assert_frame_equal(
#         expected_output,
#         real_output,
#         check_like=True,
#     )
#
#     #close the Spark Context
#     spark_context.stop()
#
#
# def get_sorted_dataframe(data_frame, columns_list):
#     return data_frame.sort_values(columns_list).reset_index(drop=True)