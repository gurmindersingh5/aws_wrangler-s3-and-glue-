+----------------------------+
|        Start               |
+----------------------------+
             |
             v
+----------------------------+
|  Upload Data to S3 Bucket  |
+----------------------------+
             |
             v
+----------------------------+
|  Trigger Lambda Function   |
|  on S3 Upload Event        |
+----------------------------+
             |
             v
+----------------------------+
| Lambda Function Execution  |
+----------------------------+
             |
             v
+-----------------------------+
| Retrieve S3 Event Details  |
| (Bucket Name & Object Key) |
+-----------------------------+
             |
             v
+-----------------------------+
|  Read JSON Data from S3    |
+-----------------------------+
             |
             v
+-----------------------------+
|  Process Data              |
|  (Normalize, Extract       |
|  Specific Columns)         |
+-----------------------------+
             |
             v
+-----------------------------+
| Write Processed Data to    |
| New S3 Bucket in Parquet   |
| Format                     |
+-----------------------------+
             |
             v
+-----------------------------+
| Create/Update Glue Catalog  |
| (Database & Table) which can|
| furthur be queried using    |
| Athena                      |
+-----------------------------+
             |
             v
+----------------------------+
|          End               |
+----------------------------+
