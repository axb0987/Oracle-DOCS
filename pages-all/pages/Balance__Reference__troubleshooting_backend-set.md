# Troubleshooting Load Balancer Backend Set Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/troubleshooting_backend-set.htm
- Fetched: 2026-09-05 01:40 CDT

# Troubleshooting Load Balancer Backend Set Issues

Learn about backend set issues associated with load balancers.

## Backend Set is Erroneously Indicating Critical Status and Failing Health Checks

If your backend set is failing health checks and shows a status as Critical , but otherwise appears to be running normally, there can be a secure SSL mismatch causing the inconsistent messaging.

If the backend servers in your backend set are using a secure connection, ensure that the Use SSL option and appropriate SSL certificate are enabled and configured. The Load Balancer's health check capability can't probe on a non-secure port when the Use SSL option is enabled, and can result in false health reports. For more information on how to enable and configure SSL in a backend set, see[Creating a Backend Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm)
Note  
  
If you don't want to use SSL for your backend set's health checking, enable the Force plaintext health checks option in your backend set's health policy. This option is only available when the backend server has its protocol set to HTTP . For more information, see[Editing a Health Check Policy](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm)
