from pymilvus import connections

# Connect to Milvus
connections.connect(alias="default", host='localhost', port='19530')

# Check if connection is successful
if connections.has_connection("default"):
    print("Connection to Milvus successful.")
else:
    print("Connection to Milvus failed.")
