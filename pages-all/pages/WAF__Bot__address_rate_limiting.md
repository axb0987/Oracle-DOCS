# Address Rate Limiting for Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/address_rate_limiting.htm
- Fetched: 2026-09-05 03:09 CDT

# Address Rate Limiting for Edge Policies

Describes the use and management of the allow rate limiting for an edge policy.

The address rate limiting configuration defines the number of allowed requests from a unique IP address and the resulting block response code when that threshold is exceeded.

## Enabling and Editing Address Rate Limiting

Describes how to enable and edit address rate limiting for an edge policy.

Use one of the following methods to enable and edit address rate limiting for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/address_rate_limiting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/address_rate_limiting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/address_rate_limiting.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci waas good-bot update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/good-bot/update.html)command and required parameters to enable and edit address rate limiting for an edge policy:

```

```

The`good-bots`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[UpdateWafAddressRateLimiting](https://docs.oracle.com/iaas/api/#/en/waas/latest/AddressRateLimiting/UpdateWafAddressRateLimiting)operation to edit and enable address rate limiting.

## Getting Address Rate Limiting Details

Describes how to get the details of the address rate limiting for an edge policy.

Use one of the following methods to get the details of the address rate limiting for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/address_rate_limiting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/address_rate_limiting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/address_rate_limiting.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci waas good-bot update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/good-bot/update.html)command and required parameters to get the details of the address rate limiting for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[GetWafAddressRateLimiting](https://docs.oracle.com/iaas/api/#/en/waas/latest/AddressRateLimiting/GetWafAddressRateLimiting)
