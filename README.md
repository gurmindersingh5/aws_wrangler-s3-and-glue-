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

                                                                                                                               
                                                                                                                               
<img width="934" alt="Screenshot 2024-07-08 at 3 22 16 AM" src="https://github.com/gurmindersingh5/aws_wrangler-s3-and-glue-/assets/123150161/0a6f400f-d3e6-4b5a-bdf5-51dcd2bce545">

