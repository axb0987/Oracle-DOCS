# Assigning Reserved Public IPv4 Addresses to API Gateways
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayassigningreservedIPaddressestoAPIgateways.htm
- Fetched: 2026-09-05 01:37 CDT

# Assigning Reserved Public IPv4 Addresses to API Gateways

Find out how to assign reserved public IPv4 addresses. to API gateways with the API Gateway service.

When you create a public IPv4 single stack API gateway or a public IPv4/IPv6 dual stack API gateway, you can specify that the API gateway is to be assigned a reserved public IPv4 address. A reserved public IPv4 address is a separate OCI resource with its own OCID. Having assigned a reserved public IPv4 address to an API gateway, if you subsequently delete the API gateway and replace it with a new API gateway, you can re-use the same reserved public IPv4 address and assign it to the new API gateway. As a result, you do not have to rewrite any existing network configuration, since the API gateway's IP address has not changed.

Before you can create a new API gateway and assign it a reserved public IPv4 address, a suitable reserved public IPv4 address must already exist. For more information about reserved public IPv4 addresses and how to create them, see[Reserved IPv4 Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/reserved-ipv4-addresses.htm).

When creating a new API gateway, use attributes of the API gateway resource to specify that the API gateway is to use a reserved public IPv4 address:
- `ipMode`Set this attribute to`IPV4`or`DUAL_STACK`.
- `ipv4AddressConfiguration`Use this attribute to specify the reserved public IPv4 address for the new API gateway, using the following field:
- `reservedIpIds`: Specify the OCID of a reserved public IPv4 address resource to use for the API gateway.

Note the following:
- Only reserved public IPv4 addresses are supported. You can only assign reserved public IPv4 addresses to public IPv4-enabled API gateways. You cannot assign reserved public IPv4 addresses to private API gateways.
- Having created an API gateway without a reserved public IPv4 address, you cannot subsequently assign the API gateway a reserved public IPv4 address. You can only specify a reserved public IPv4 address when you create an API gateway.

Prequisites for Assigning Reserved Public IPv4 Addresses to API Gateways

Provided you already have the necessary IAM permissions to create API gateways (including the`manage virtual-network-family`permission), no additional permissions are required to assign a reserved public IPv4 address to an API gateway.

## Creating IPv4 single stack API gateways with reserved public IPv4 addresses

You can create IPv4 single stack API gateways with reserved public IPv4 addresses using the CLI or the API (you cannot use the Console).

When using the CLI, the command syntax is as follows:
```

```

For example, to create a public IPv4 single stack API gateway with a reserved public IPv4 address:
```

```

## Creating IPv4/IPv6 dual stack API gateways with reserved public IPv4 addresses

You can create IPv4/IPv6 dual stack API gateways with reserved public IPv4 addresses using the CLI or the API (you cannot use the Console).

When using the CLI, the command syntax is as follows:
```

```

For example:
- 

To create a public IPv4/IPv6 dual stack API gateway with a reserved public IPv4 address and an ephemeral IPv6 address:
```

```

- 

To create a public IPv4/IPv6 dual stack API gateway with a reserved public IPv4 address and a manually specified IPv6 address:
```

```
