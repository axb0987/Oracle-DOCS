# Troubleshooting Load Balancer HTTP Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/troubleshooting_http.htm
- Fetched: 2026-09-05 01:40 CDT

# Troubleshooting Load Balancer HTTP Issues

Learn about HTTP issues associated with load balancers.

## HTTP 400 Bad Request Header or Cookie

One possible solution is to increase the HTTP request header size on the load balancer. By default, the size limit is 8 KB, but raising it to 64 KB resolves the issue. This solution is only supported for HTTP. You can create a rule to increase the HTTP header size to address it. There is also a rule for handling special characters in the header name that might also result in similar failures.

See[HTTP Header Rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/managingrulesets.htm#HTTPHeaderRules)for more information.

## HTTP 502 Bad Gateway Errors

In addition to monitoring and management, load balancing logging helps you to identify, isolate, and troubleshoot issues with your load balancer infrastructure. The following procedure illustrates how to troubleshoot a`502 Bad Gateway`error encountered when deploying a new web application,`example.com`. The example uses an Oracle Cloud Infrastructure public load balancer as the front end in a development environment. The task fails with a`502 Bad Gateway`error on the browser. Troubleshoot the issue using load balancer access and error logs, as follows:
- Confirm the error using the`curl`utility, as follows:
```

```

```

```

- Search the load balancer access and error logs for "`lbStatusCode`" and "`backendStatusCode`."
- If the results include`backendStatusCode: 502`, then:

Possible causes :
- Issue is an improperly configured backend.
- Backend is likely another reverse proxy or LB.

Possible resolutions :
- Examine upstream proxy logs to determine why the`502`error is being returned.
- Resolve any issues on the ultimate backend that's causing the upstream proxy to return a`502`error.
- If the results include`backendStatusCode: 504`, then:

Possible causes :
- When a`504`error occurs from the backend, it typically indicates that the backend is another proxy or load balancer service instance. The error typically occurs when a proxy is unable to connect to an upstream server in a specified amount of time.
- Examine the logs of the upstream system to determine what is causing the upstream proxy from connecting to the backend.

Possible resolutions :
- Increase the amount of time for the connection timeout.
- Determine why the backend is taking longer to respond than usual using a utility, such as`tcpdump`, and built-in application tools.
- If the results include`backendStatusCode: 500`, then:
Possible causes :
- When a`500`error occurs from the backend, it typically indicates a server-side error, commonly known as an "Internal Server Error." Backend applications typically cause this error.
- Inability to connect to upstream resources, such as databases, APIs, and services.

Possible resolutions :

Resolve application-level issue that is causing the error.
- If the results include`backendStatusCode:`with no error code, then:
- Typically, when no backend status code accompanies`lbStatusCode: 502`, no backend is available to send the connections.
- You might also notice a`No healthy backends available in associated backendSet`message in the load balancer error Logs.
- Ensure that the backends are healthy. If the backends are healthy, then confirm that the health check is properly configured.

## HTTP 504

The 504 HTTP error typically indicates that the backend server is being used as another proxy or load balancer service instance. This error usually occurs when a proxy is unable to connect to an upstream server in a specified amount of time. Examine the logs of the upstream system to determine what is causing the upstream proxy from connecting to the backend server.

Possible solutions include:
- 

Increasing the amount of time for the connection timeout.
- 

Determining why the backend server is taking longer to respond than usual using a utility, such as tcpdump, and built-in application tools.

See[HTTP 502 Bad Gateway Errors](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/troubleshooting_http.htm#HTTP502)
