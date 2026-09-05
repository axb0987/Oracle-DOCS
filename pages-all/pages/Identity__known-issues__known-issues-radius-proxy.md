# Radius Proxy Known Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/known-issues/known-issues-radius-proxy.htm
- Fetched: 2026-09-05 02:23 CDT

# Radius Proxy Known Issues

Known issues for working with radius proxy in IAM.

## Changes in the RADIUS Proxy Configuration

If any RADIUS Proxy configuration is changed in IAM, restart RADIUS Agent and RADIUS Proxy by completing the following steps so that the new configuration is reflected.

- `<radius_proxy_installer_location>/oracle_radius_proxy/radius_agent/scripts/src/radius_agent.py restart`.
- Verify if the configuration is updated in:`<radius_proxy_installer_location>/radius_proxy/conf/radius_proxy.conf`or`<radius_proxy_installer_location>/radius_proxy/conf/radius_clients.conf`.
- `/sbin/service idcs_radiusd restart`.

## Change an IP Address from CIDR Format

You can't add an IP address in CIDR format using the IAM user interface. If the IP address of the Oracle Database is in CIDR format, use the following request from the Postman collection. Go to RADIUS Proxy , RADIUS App , Modify , and then Update RADIUS App (IP Address in CIDR format) .

```

```

The Postman collection is contained in a single Postman collection file and organized into folders within the collection. Folders are organized based on use cases, use scenarios, and so on, and include variations of API use. Download the collection and environment files from[GitHub](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/api-radius-proxy-radius-proxy-definition.html)
