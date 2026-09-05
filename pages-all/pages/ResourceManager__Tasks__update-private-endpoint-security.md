# Managing Security Attributes for a Private Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoint-security.htm
- Fetched: 2026-09-05 02:56 CDT

# Managing Security Attributes for a Private Endpoint

Add or remove security attributes for a private endpoint in Resource Manager.

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoint-security.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoint-security.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoint-security.htm#)
- 

- On the Private endpoints list page, find the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm).
- From the Actions menu (three dots) for the private endpoint, select Add security attributes .
- In the Add security attributes dialog window, add or delete security attributes to the private endpoint.
- Select Add security attributes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/update.html)oci resource-manager private-endpoint update`command and`--security-attributes`parameter to manage security attributes for a private endpoint.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/UpdatePrivateEndpoint)operation and`securityAttributes`
