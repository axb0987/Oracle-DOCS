# Connection Pooling to Improve Performance
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingconnectionpooling.htm
- Fetched: 2026-09-05 02:09 CDT

# Connection Pooling to Improve Performance

Find out about connection pooling to reduce the time required to establish a connection when a function is invoked for the first time with OCI Functions.

For functions that connect to external resources, you will typically include connection pooling code in the function to reduce the time required to establish a connection when the function is invoked for the first time.

Connection pooling is the reuse of existing pre-established connections to make HTTP requests, instead of creating a new connection for each service request.

Connection pooling to access resources (such as remote REST API endpoints and backend database instances) often improves application performance, concurrency, and scalability.

For sample connection pooling code to add to functions, see[Connection Pooling Sample Code](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdownloadingsamples_topic-Sample_functions-Connection-pooling.htm)
