# Origin Management
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/originmanagement.htm
- Fetched: 2026-09-05 03:11 CDT

# Origin Management

Use the Web Application Firewall for origin management.

An origin is an endpoint (typically an IP address) of the application protected by the WAF. An origin can be an Oracle Cloud Infrastructure load balancer public IP address which can be used for high availability to an origin. When you[create a WAF policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#To_create_a_WAF_policy), you define a default origin and optional HTTP headers. An origin must be defined in your WAF policy to set up protection rules or other features. The details for the origin can be modified later in the Settings of the WAF policy. In the Origin Settings, you can modify or set up HTTP headers for outbound traffic from the WAF to the origin server. These name-value pairs are then available to the application.

## Origin Groups

Multiple origins can be defined for a WAF policy using Origin Groups. When at least two origins are configured, load balancing is enabled. You can group multiple origins in an origin group. An origin group can include origin servers and their weights. The weight of each origin in the origin group determines the priority when load balancing across origins in this group. Origins with higher weights receive larger proportions of client requests. Under origin groups, all origins are active. The grouping is for visual purposes only.

## Securing Your WAF

To secure your WAF, you must configure your servers to accept traffic from the WAF servers. Configure your origin's ingress rules to only accept connections from the following[CIDR ranges](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/../Concepts/gettingstarted.htm#secure)
