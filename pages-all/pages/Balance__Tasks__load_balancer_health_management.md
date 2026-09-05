# Health Check Policies for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/load_balancer_health_management.htm
- Fetched: 2026-09-05 01:41 CDT

# Health Check Policies for Load Balancers

Set up and use health checks to decide the availability of backend servers for a load balancer.

A health check is a test to confirm the availability of backend servers. A health check can be a request or a connection attempt. Based on a time interval you specify, the load balancer applies the health check policy to continuously monitor backend servers. If a server fails the health check, the load balancer takes the server temporarily out of rotation. If the server later passes the health check, the load balancer returns it to the rotation.

You configure your health check policy when you create a backend set. You can configure TCP-level or HTTP-level health checks for your backend servers. As an option, you can use SSL with TCP and HTTP health checks.
- TCP-level health checks attempt to make a TCP connection with the backend servers by establishing a TCP three-way handshake.
- HTTP-level health checks send requests to the backend servers at a specific URI and validate the response based on the status code or entity data (body) returned. HTTP health checks for backend sets configured with the Use SSL option use HTTPS for health checks unless also configured to use plain text health checks.

The service provides application-specific health check capabilities to help you increase availability and reduce your application maintenance window.

The backend set's Details page provides the same Overall Health status indicator found in the load balancer's list of backend sets. It also includes counters for the Backend Health status values reported by the backend set's backend servers.

The health status counter badges indicate the following:
- The number of child entities reporting the indicated health status level.
- If a counter corresponds to the overall health, the badge has a fill color.
- If a counter has a zero value, the badge has a light gray outline and no fill color.

Here is a list of health check-related topics:

[Health Status Indicators for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Health_Status.htm)

[Understanding Load Balancer Health Issues](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/understanding_health_issues.htm)

[Common Side Effects of Load Balancer Health Check Misconfigurations](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/common_side_effects_health_misconfiguration.htm)

[Load Balancer Health Check Best Practices](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/health_check_best_practices.htm)

[Creating a Custom Python Healthcheck Page for Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_custom_health_page.htm)

You can perform the following health check management tasks:

[Get a load balancer's health check policy details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_health-checker.htm)

[Edit a load balancer's health check policies.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm)
