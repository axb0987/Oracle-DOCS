# Disabling and Re-Enabling Load Balancer Logging
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/disable_log.htm
- Fetched: 2026-09-05 01:40 CDT

# Disabling and Re-Enabling Load Balancer Logging

Disable and subsequently re-enable access or error logging for a load balancer.

## Using the Console

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Monitoring and find the Logs section.
All logs are displayed in a table.
- From the Actions menu for the log category you want, select Disable .
- When prompted, confirm the disabling.
- To disable the request ID option, select Edit next to Request ID .
Use the toggle button to disable the request ID. The Request ID helps you track and manage a request by providing a unique request identifier exposed in HTTP request and response headers.

When the request ID is disabled, the load balancer won't add this unique request ID header to the request passed through to the load balancer backend or to the response returned. To enable the request ID, see[Enabling a Log](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_log.htm).
