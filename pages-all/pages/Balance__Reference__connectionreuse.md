# Load Balancer Timeout Connection Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/connectionreuse.htm
- Fetched: 2026-09-05 01:40 CDT

# Load Balancer Timeout Connection Settings

Configure the timeout settings for your load balancer.

Oracle Cloud Infrastructure load balancers support connection multiplexing. The load balancer can route many incoming requests from several clients to the destination backend server through a few (one or many) backend connections.

After your load balancer connects a client to a backend server, the connection can be closed because of inactivity. Also, you can configure load balancer listeners to control the maximum idle time allowed during each TCP connection or HTTP request and response pair. We recommend that you don't allow your backend servers to close connections to the load balancer.

The following timeout settings affect your load balancer's behavior:
- Keep-alive setting between the load balancer and the client

The Load Balancer service sets the keep-alive value to maintain the connection for 10,000 transactions or until it has been idle for 65 seconds, whichever limit occurs first.
Note  
  
You can't change the value of this setting.
- Keep-alive setting between the load balancer and backend server

The load balancer closes backend server connections that are idle for more than 300 seconds. See[Keep-Alive Settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/connectionreuse.htm#keep-alive-settings)for more information.
- Idle Timeout in Seconds

You can set the duration of the idle timeout when you create a listener as described in[Creating a Load Balancer Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/managinglisteners_topic-Creating_Listeners.htm). This setting applies to the time allowed between two successive receive or two successive send network input/output operations during the HTTP request-response phase. See[Idle Timeout Settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/connectionreuse.htm#idle-timeout)for more information.

## Keep-Alive Settings

The Load Balancer service doesn't honor keep-alive settings from backend servers. The load balancer closes backend server connections that are idle for more than 300 seconds. We recommend that you don't allow your backend servers to close connections to the load balancer. To prevent possible 502 errors, ensure that your backend servers do not close idle connections in less than 310 seconds.

The Load Balancer service sets the keep-alive value to maintain the connection for 10,000 transactions or until it has been idle for 65 seconds, whichever limit occurs first.

## Idle Timeout Settings

When you create or edit a TCP or HTTP listener, you can specify the maximum idle time in seconds using the Idle Timeout In Seconds option. This setting applies to the time allowed between two successive receive or two successive send network input/output operations during the HTTP request-response phase. If the configured timeout has elapsed with no packets sent or received, the client's connection is closed. For HTTP and WebSocket connections, a send operation doesn't reset the timer for receive operations and a receive operation doesn't reset the timer for send operations. See[Creating a Load Balancer Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/managinglisteners_topic-Creating_Listeners.htm)for more information on how to apply this option.
Note  
  
This timeout setting doesn't apply to idle time between a completed response and a later HTTP request.

The default timeout values are:
- 300 seconds for TCP listeners.
- 60 seconds for HTTP listeners.

Change the timeout parameter if either the client or the backend server requires more time to send data. Some examples include:
- The client sends a database query to the backend server and the database takes over 300 seconds to run. Therefore, the backend server doesn't send any data within 300 seconds.
- The client uploads data using the HTTP protocol. During the upload, the backend doesn't send any data to the client for more than 60 seconds.
- The client downloads data using the HTTP protocol. After the initial request, it stops sending data to the backend server for more than 60 seconds.
- The client starts sending data after establishing a WebSocket connection, but the backend server doesn't send data for more than 60 seconds.
- The backend server starts sending data after establishing a WebSocket connection, but the client doesn't send data for more than 60 seconds.

The maximum timeout value is 7200 seconds. Contact[Create a service request](https://support.oracle.com)to file a service request to increase this limit for your tenancy. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)
