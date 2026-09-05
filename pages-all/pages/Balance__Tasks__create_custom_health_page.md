# Creating a Custom Python Healthcheck Page for Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_custom_health_page.htm
- Fetched: 2026-09-05 01:40 CDT

# Creating a Custom Python Healthcheck Page for Load Balancer

Develop a custom Python healthcheck page for a load balancer.

You can create your own custom[Python healthcheck page](https://pypi.org/project/py-healthcheck/)to do a more thorough check of your load balancer. Healthcheck is a library to write simple healthcheck functions you can use to monitor your application. A healthcheck page is useful for asserting that your dependencies are running correctly and your application can respond to HTTP requests.

You can use the Tornado or Flask application for creating the custom healthcheck page. The following example shows how you can configure a healthcheck page using Tornado.
```

```

In the preceding example, the test page is doing more than just ensuring the HTTP application is listening. This example checks for a`redis`client and waits for a response to ensure that the full application is healthy before returning a`200`status code. Some other command examples would be to check for disk space or the availability of an upstream dependency. In your healthcheck configuration, specify the following:
- 

`/healthcheck`as your path
- 

`flask default 5000`as port
- 

`200`
