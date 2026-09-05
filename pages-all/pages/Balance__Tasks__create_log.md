# Enabling a Load Balancer Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_log.htm
- Fetched: 2026-09-05 01:40 CDT

# Enabling a Load Balancer Log

Enable an access or error log for a load balancer.

For prerequisite information, see[Logging for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Logging.htm).
Note  
  

You can only enable an access or error log when there no existing logs of that type present. A load balancer can only have one access and one error log each.

## Using the Console

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Monitoring and find the Logs section.
All logs are displayed in a table.
- From the Actions menu for the log category you want, select Enable log .
The Enable resource log opens.
- Enter the following information:

- Compartment : Select the compartment within which the log file resides from the list.
- Log group : Select an existing log group from the list or select Create new group . The Create log group panel opens, where you can enter the name and description of a new logging group within which your log resides.
- Log name : Enter the name of the log.

For more information on log and log groups, including naming syntax guidelines, see[Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm).
- (Optional) Select Show advanced options to use these features. The Log retention panel appears.
- Select the time period in months each error logging entry is to be retained from the Log retention list.
- (Optional) Apply any tags to the log. For more information, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
- Select Enable log .
- To enable the request ID option to help track requests and troubleshoot logs, select Edit next to Request ID
Use the toggle button to enable the request ID. The Request ID can help you with tracking and managing a request by providing a unique request identifier exposed in HTTP request and response headers.

When the request ID is enabled, the default header name X-Request-Id is included in the HTTP request header from the load balancer to the backend server and HTTP header responses. If not enabled, the load balancer won't add this unique request ID header to the request passed through to the load balancer backend server or to the response returned.
