# Issues creating API gateways
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm
- Fetched: 2026-09-05 01:39 CDT

# Issues creating API gateways

Find out how to troubleshoot problems when creating API gateways with the API Gateway service.

You might encounter the issues described in this topic when creating API gateways.

See also[Troubleshooting Guides for Creating API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides_creating-gateways.htm).

## Creating a new API gateway stalls with a state of Creating, or fails

It can take a few minutes to create a new API gateway. While it is being created, the API gateway is shown with a state of Creating on the Gateways list page. When it has been created successfully, the new API gateway is shown with a state of Active.

If you have waited more than a few minutes for the API gateway to be shown with an Active state (or if the API gateway creation operation has failed):
- Select the name of the API gateway, and select the Work requests tab to see an overview of the API gateway creation operation.
- Select the Create gateway operation to see more information about the operation (including error messages, log messages, and the status of associated resources) that will help to diagnose the cause of the problem.

## Creating a new API gateway returns a "VNIC attachment failed due to the limit for number of private IP addresses for this subnet" message

When creating a new API gateway, you might see the following message:
```

```

This message indicates that there are not enough private IP addresses available to create the API gateway in the specified subnet. An API gateway consumes three private IP addresses in the subnet.

To address this issue, use a subnet that has at least three available private IP addresses.

## Creating a new API gateway returns a "The limit for number of private IP addresses for this subnet has been exceeded" message

When creating a new API gateway, you might see the following message:
```

```

This message indicates that there are not enough private IP addresses available to create the API gateway in the specified subnet. An API gateway consumes three private IP addresses in the subnet.

To address this issue, use a subnet that has at least three available private IP addresses.

## Creating a new public API gateway returns a "The limit for number of public IP addresses for this compartment has been exceeded" message

When creating a new public API gateway, you might see the following message:
```

```

This message indicates that there are not enough public IP addresses available to create the public API gateway in the specified subnet's compartment. When creating a new public API gateway, an attempt is made to create a new public IP address in the subnet's compartment. The attempt to create the new public IP address fails if the quota for public IP addresses is exceeded in that compartment or tenancy. Note the public IP address is in addition to the three private IP addresses consumed by all API gateways.

To address this issue:
- If the compartment's quota is exceeded, contact your tenancy administrator to request additional public IP addresses for the compartment.
- If the tenancy's quota is exceeded, contact Oracle Support to request an increase to the tenancy's quota.

## Creating a new API gateway returns a "Work request was cancelled" message

When creating a new API gateway, you might see the following message:
```

```

This message indicates that you cancelled the work request to create the API gateway. The API gateway is shown with a status of Failed.

## Creating a new API gateway returns a "An unexpected error occurred. Contact Oracle Support for assistance" message

When creating a new API gateway, you might see the following message:
```

```

To address this issue, contact Oracle Support to request assistance.

## Creating a new API gateway returns an "Unknown resource &lt;subnet-ocid&gt;, make sure subnet exists,..." message and a 400 error

When creating a new API gateway using the Console, API, SDK, or CLI, you might see the following error message and a 400 error code:

```

```

This message indicates that the API Gateway service cannot access the subnet specified for the new API gateway.

To address this issue, double-check that:
- The subnet exists.
- You can access the subnet.
-
