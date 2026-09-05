# IP Addresses, Hostnames, and Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningIPaddresseshostnameendpoint.htm
- Fetched: 2026-09-05 01:37 CDT

# IP Addresses, Hostnames, and Endpoints

Find out how the IP addresses and hostnames of API gateways are related to API deployment endpoints in different realms, with the API Gateway service.

## OC1 realm

In the OC1 realm, in all cases (IPv4 single stack API gateways, IPv4/IPv6 dual stack API gateways, and IPv6 single stack API gateways), an API gateway's hostname attribute is an automatically generated domain name in the format`<gatewayidentifier>.apigateway.<region-identifier>.oci.customer-oci.com`, where:
- `<gateway-identifier>`is the string of characters that identifies the API gateway. For example,`lak...sjd`(abbreviated for readability).
- `<region-identifier>`is the identifier of the region in which the API gateway has been created. See[Availability by Region](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayprerequisites.htm#regional-availability).

For example,`lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com`

For an API deployment deployed on an API gateway, the API deployment's endpoint is in the format`<hostname>/<deployment-path>`, where`<deployment-path>`comprises a path prefix and one or more route paths.

For example:
```

```

In the OC1 realm, an API gateway's hostname resolves to IP addresses as follows:
- IPv4 single stack API gateways: In the OC1 realm, an IPv4 single stack API gateway's hostname resolves to the API gateway's IPv4 address. So if the API gateway's IPv4 address is`192.0.2.2`, the API gateway's hostname of`lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com`resolves to`192.0.2.2`.
- IPv4/IPv6 dual stack API gateways: In the OC1 realm, an IPv4/IPv6 dual stack API gateway's hostname resolves to both the API gateway's IPv4 and IPv6 addresses. So if the API gateway's IPv4 address is`192.0.2.2`, and the API gateway's IPv6 address is`2001:db8:abcd:1234::1`, the API gateway's hostname of`lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com`resolves to both`192.0.2.2`and`2001:db8:abcd:1234::1`.
- IPv6 single stack API gateways: In the OC1 realm, an IPv6 single stack API gateway's hostname resolves to the API gateway's IPv6 address. So if the API gateway's IPv6 address is`2001:db8:abcd:1234::1`, the API gateway's hostname of`lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com`resolves to`2001:db8:abcd:1234::1`.

## Realms other than OC1
In realms other than OC1, an API gateway's hostname attribute depends on whether it is an IPv4 single stack API gateway, an IPv4/IPv6 dual stack API gateway, or an IPv6 single stack API gateways, as follows:
- IPv4 single stack API gateways: In realms other than OC1, an IPv4 single stack API gateway's IPv4 address is used as the API gateway's hostname. So if the API gateway's IPv4 address is`192.0.2.2`, the API gateway's hostname is also`192.0.2.2`. Since an API deployment's endpoint includes the hostname of the API gateway on which it is deployed, the endpoints of an API deployment deployed on an IPv4 single stack API gateway in a region other than OC1 include the IPv4 address. For example,`https://192.0.2.2/v1/hello`
- IPv4/IPv6 dual stack API gateways: In realms other than OC1, only an IPv4/IPv6 dual stack API gateway's IPv4 address is used as the API gateway's hostname. The IPv6 address is not used. So if the API gateway's IPv4 address is`192.0.2.2`, the API gateway's hostname is also`192.0.2.2`. Since an API deployment's endpoint includes the hostname of the API gateway on which it is deployed, the endpoints of an API deployment deployed on an IPv4/IPv6 dual stack API gateway in a region other than OC1 include the IPv4 address. For example,`https://192.0.2.2/v1/hello`
- IPv6 single stack API gateways: In realms other than OC1, an IPv6 single stack API gateway's IPv6 address is used as the API gateway's hostname. So if the API gateway's IPv6 address is`2001:db8:abcd:1234::1`, the API gateway's hostname is also`2001:db8:abcd:1234::1`. Since an API deployment's endpoint includes the hostname of the API gateway on which it is deployed, the endpoints of an API deployment deployed on an IPv6 single stack API gateway in a region other than OC1 include the IPv6 address. For example,`https://2001:db8:abcd:1234::1/v1/hello`

## Viewing an API gateway's hostname

You can view an API gateway's hostname:
- 

Using the Console, on the Details tab of the API gateway details page
- 

Using the CLI, by entering the command`oci api-gateway gateway get --gateway-id <gateway-ocid> | jq .data.hostname`command.

Note that this command uses the`[](https://jqlang.org)jq`processor to parse the JSON output.

For example:
```

```

## Viewing an API deployment's endpoints

You can view an API deployment's endpoint:
- 

Using the Console, on the Details tab of the API deployment details page.
- 

Using the CLI, by entering the command`oci api-gateway deployment get --deployment-id <deployment-ocid> | jq .data.endpoint`command.

Note that this command uses the`[](https://jqlang.org)jq`processor to parse the JSON output.

For example:
```

```
