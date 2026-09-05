# Load Balancing
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/originmanagement_topic-load_balancing.htm
- Fetched: 2026-09-05 03:11 CDT

# Load Balancing

Describes how to configure load balancing for multiple origins for an edge policy.

Configure load balancing when you have multiple origins associated with an edge policy.

## Using the Console

Load balancing is only enabled when at least two origins have been defined. To define more origins, see[Adding Origins and Origin Groups](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/../Origin/add_origin.htm#top).

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy where you want to configure custom headers for the origins.
The edge policy's details page opens.
- Select Settings under WAF Policy .
The Settings list appears.
- Select the Origin Settings tab.
- Select Edit .

The Origin Management Settings dialog box appears.
- Complete the following:

Note  
  
The section on health checks is described in[Health Checks](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/originmanagement_topic-health_checks.htm#top). Ignore that functionality for configuring load balancers for multiple origins.
- Select one of the following load balancing methods:
- IP_HASH : All incoming requests from the same client IP address go to the same content origination server. IP_HASH load balancing method uses origin weights when choosing which origin to which the hash is initially assigned.
- ROUND_ROBIN : Forwards requests sequentially to the available origin servers. The first request is to the first origin server, the second request is to the next origin server, and so on. After it sends a request to the last origin server, it starts again with the first origin server. When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater weight. Over time, origins receive requests in proportion to their weight.
- STICKY_COOKIE : Adds a session cookie to the first response from the origin server and identifies the server that sent the response. The client's next request contains the cookie value, and NGINX routes the request to the origin server that responded to the first request. STICKY_COOKIE load balancing method falls back to Round Robin for the first request.
- Enable Origin Compression : (optional) Check to enable GZIP compression of origin responses.
Note  
  
Compression methods other than GZIP compression that come to the infrastructure are forwarded unaltered to the origin.
- Select Save Changes .
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/../Bot/publishing_changes.htm#PublishChanges)
