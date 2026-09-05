# Assigning IPv4 and IPv6 Addresses to API Gateways
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningIPv4IPv6addressestoAPIgateways.htm
- Fetched: 2026-09-05 01:37 CDT

# Assigning IPv4 and IPv6 Addresses to API Gateways

Find out how to assign IPv4 and IPv6 addresses to API gateways with the API Gateway service.

You can use API Gateway to create:
- Public and private IPv4 single stack API gateways, enabled for IPv4 only. (Default behavior) API clients can connect to API gateways using ephemeral IPv4 addresses. In addition, public IPv4 single stack API gateways also support the use of reserved public IPv4 addresses (see[Assigning Reserved Public IPv4 Addresses to API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningreservedIPaddressestoAPIgateways.htm)).
- Public and private IPv4/IPv6 dual stack API gateways, enabled for both IPv4 and IPv6. API clients can connect to API gateways using ephemeral IPv4 and IPv6 addresses. You can optionally specify an IPv6 address to use for the API gateway. Public IPv4/IPv6 dual stack API gateways also support the use of reserved public IPv4 addresses (see[Assigning Reserved Public IPv4 Addresses to API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningreservedIPaddressestoAPIgateways.htm)).
- Public and private IPv6 single stack API gateways, enabled for IPv6 only. API clients can connect to API gateways using ephemeral IPv6 addresses. You can optionally specify an IPv6 address to use for the API gateway.

The term 'IPv4-enabled API gateway' correctly describes both an IPv4 single stack API gateway, and also an IPv4/IPv6 dual stack API gateway. Similarly, the term 'IPv6-enabled API gateway' correctly describes both an IPv6 single stack API gateway, and also an IPv4/IPv6 dual stack API gateway.

An API gateway communicates with its backends using the IP addresses of the API gateway, so the API gateway's backends must be reachable over that IP protocol. For example, for an IPv6 single stack API gateway, if a backend only accepts IPv4 traffic, then communication between the API gateway and the backend will fail. For a dual stack API gateway, the API gateway uses IPv4 or IPv6 for backend communication as available.

When you create an API gateway, the existing VCN and subnet that you specify for the API gateway must be compatible with the API gateway's address family. An IPv4 single stack API gateway is compatible both with an IPv4 single stack subnet, and with an IPv4/IPv6 dual stack subnet. An IPv4/IPv6 dual stack API gateway is only compatible with an IPv4/IPv6 dual stack subnet. An IPv6 single stack API gateway is only compatible with an IPv4/IPv6 dual stack subnet.

When you create an IPv4/IPv6 dual stack API gateway, or an IPv6 single stack API gateway, the IPv6-enabled subnet that you specify for the API gateway must have a stateful ingress rule (defined in a network security group or security list) to allow IPv6 traffic, such as:
- State: Stateful
- Source Type: CIDR
- Source CIDR: ::/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 443

For more information about IPv6 addressing in a VCN, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)in the Networking service documentation.

When creating a new API gateway, use attributes of the API gateway resource to specify the API gateway's IP address family and whether to create a single stack or a dual stack API gateway as follows:
- `ipMode`Set this attribute to:
- `IPV4`if you want the new API gateway to be an IPv4 single stack API gateway.
- `DUAL_STACK`if you want the new API gateway to be an IPv4/IPv6 dual stack API gateway.
- `IPV6`if you want the new API gateway to be an IPv6 single stack API gateway.

If you do not specify a value for the`ipMode`attribute during API gateway creation, then default behavior is to create an IPv4 single stack gateway with an ephemeral IPv4 address.
- `ipv4AddressConfiguration`In the case of an API gateway with`ipMode`set to`IPV4`or to`DUAL_STACK`use this optional attribute to specify details of an IPv4 address for the new API gateway, using the following field:
- `reservedIpIds`: Use this field to optionally specify the OCID of a reserved public IPv4 address to use for the API gateway (see[Assigning Reserved Public IPv4 Addresses to API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningreservedIPaddressestoAPIgateways.htm)).

If you do not specify a value for the`ipv4AddressConfiguration`attribute during creation of an IPv4 single stack or IPv4/IPv6 dual stack API gateway, then default behavior is to create an API gateway with an ephemeral IPv4 address.
- `ipv6AddressConfiguration`In the case of an API gateway with`ipMode`set to`DUAL_STACK`or`IPV6`, use this optional attribute to specify details of an IPv6 address for the new API gateway, using the following fields:
- `addresses`: Use this field to optionally specify an IPv6 address to use for the API gateway. If you don't specify an IPv6 address, an IPv6 address is generated. Note that each API gateway must have a unique IPv6 address within its subnet. If you attempt to assign the same IPv6 address to more than one gateway in a subnet, the API gateway creation will fail.
- `subnetCidrs`: If the subnet you specify for an API gateway has been assigned multiple IPv6 prefixes, use this field to specify the IPv6 prefix from which to generate the IPv6 address.

If you do not specify a value for the`ipv6AddressConfiguration`attribute during creation of an IPv4/IPv6 dual stack or IPv6 single stack API gateway, then default behavior is to create an API gateway with an ephemeral IPv6 address.

Note the following:
- Having created an API gateway, you cannot change its`ipMode`attribute (the API gateway's IP address family and whether it's a single stack or a dual stack API gateway), or its`ipv4AddressConfiguration`and`ipv6AddressConfiguration`attributes.
- You can enable both private API gateways and public API gateways for IPv6 traffic (as IPv6 single stack API gateways, or as IPv4/IPv6 dual stack API gateways).
- If you create a rate-limiting policy and specify that the maximum number of requests threshold is to apply to the number of requests per client:
- For IPv4-enabled API gateways, rate limiting is based on individual API client IPv4 addresses.
- For IPv6-enabled API gateways, rate limiting is based on the API client’s IPv6 /64 prefix rather than the full address. API clients that have the same IPv6 /64 prefix are considered to be the same client, for rate limiting purposes.

For more information, see[Limiting the Number of Requests to API Gateway Back Ends](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylimitingbackendaccess.htm).
- For IPv6-enabled API gateways, the value of the`Simultaneous connections per IP address`internal limit that specifies the maximum number of simultaneous connections from a single IP address to an API gateway is based on the API client’s IPv6 /64 prefix rather than the full address. For more information, see[API Gateway Invocation Limits](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Reference/apigatewaylimits.htm#gatewayinvocationlimits).
- You can only create IPv6-enabled API gateways in realms and regions where VCNs support IPv6.

Prerequisites for Assigning IPv4 and IPv6 Addresses to API Gateways

Provided you already have the necessary IAM permissions to create IPv4 single stack API gateways (including the`manage virtual-network-family`permission), no additional permissions are required to create IPv4/IPv6 dual stack API gateways, or IPv6 single stack API gateways.

## Creating IPv4 single stack API gateways

Creating public and private IPv4 single stack API gateways is the default behavior. You can create public and private IPv4 single stack API gateways, using the Console, the API, and the CLI (see[Creating an API Gateway](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm#top)).

Alternatively, you can use the CLI or the API to create public IPv4 single stack gateways with reserved public IPv4 addresses (see[Assigning Reserved Public IPv4 Addresses to API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningreservedIPaddressestoAPIgateways.htm)).

When using the CLI, the command syntax is as follows:
```

```

For example:
- 

To create a public IPv4 single stack API gateway with an ephemeral IPv4 address:
```

```

- 

To create a public IPv4 single stack API gateway with a reserved public IPv4 address:
```

```

For more information about reserved public IPv4 addresses, see[Assigning Reserved Public IPv4 Addresses to API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningreservedIPaddressestoAPIgateways.htm).

## Creating IPv4/IPv6 dual stack API gateways

You can create public and private IPv4/IPv6 dual stack API gateways using the CLI or the API (you cannot use the Console).

When using the CLI, the command syntax is as follows:
```

```

For example:
- 

To create a public IPv4/IPv6 dual stack API gateway with ephemeral IPv4 and IPv6 addresses:
```

```

- 

To create a public IPv4/IPv6 dual stack API gateway with an ephemeral IPv4 address and a manually specified IPv6 address:
```

```

- 

To create a public IPv4/IPv6 dual stack API gateway with a reserved public IPv4 address and a manually specified IPv6 address:
```

```

For more information about reserved public IPv4 addresses, see[Assigning Reserved Public IPv4 Addresses to API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningreservedIPaddressestoAPIgateways.htm).

## Creating IPv6 single stack API gateways

You can create public and private IPv6 single stack API gateways using the CLI or the API (you cannot use the Console).

When using the CLI, the command syntax is as follows:
```

```

For example:
- 

To create a publicIPv6 single stack API gateway with an ephemeral IPv6 address:
```

```

- 

To create a public IPv6 single stack API gateway with a manually specified IPv6 address:
```

```
