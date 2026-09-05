# Error Code 431 When Getting Reachable IP Address
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/431-reachable.htm
- Fetched: 2026-09-05 02:57 CDT

# Error Code 431 When Getting Reachable IP Address

Troubleshoot error code 431 when getting a reachable IP address for a private endpoint.

When you send a request to[get the reachable IP address for a private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/get-private-endpoint-reachable-ip.htm)([GetReachableIp](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ReachableIp/GetReachableIp)), you receive the error message[`RequestHeaderFieldsTooLarge`(error code 431)](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm#apierrors_431__http_status_431_error_codes).

This error code indicates that the request header exceeds the maximum allowable size for a request.

This error can occur when the requesting user belongs to too many[identity provider (IdP) groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm#overview). The size of the header is also increased by the job OCID passed with the[GetReachableIp](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ReachableIp/GetReachableIp)request.

To remedy this issue, perform one of the following actions:
- Ask another user with fewer IdP group memberships to send the request.
-
