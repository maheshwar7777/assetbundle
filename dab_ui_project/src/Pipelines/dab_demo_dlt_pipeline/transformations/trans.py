import dlt

@dlt.table

def trans_tble():
    return spark.range(10)