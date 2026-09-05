# Service Discovery Use Case
- Source: https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/servicediscovery.htm
- Fetched: 2026-09-05 02:11 CDT

# Service Discovery Use Case

This use case shows how you can get the list of your service entitlement IDs.

Important  
  
The My Services dashboard and APIs are deprecated.

## Discover Current Service Entitlement IDs

Many of the My Services API operations require you to specify the`serviceEntitlementId`. To get the list of all your service entitlement IDs, use the[GET ServiceEntitlements](https://docs.oracle.com/iaas/api/#/en/itas/latest/MSServiceEntitlements/resource_MSServiceEntitlementsResource_get_GET)operation. This operation returns information that you can use to make more specific requests using the[Oracle Cloud My Services API.](https://docs.oracle.com/iaas/api/#/en/itas/latest/)

Example:

```

```

Note  
  

In the examples, &lt;domain&gt; is the identity domain ID. An identity domain ID can be either the IDCS GUID that identifies the identity domain for the users within Identity Cloud Service (IDCS) or the Identity Domain name for a traditional Cloud Account.

Example payload returned for this request:

```

```

[To obtain the IDCS GUID](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/servicediscovery.htm#)

Go to the Users page in My Services dashboard and click Identity Console . The URL in the browser address field displays the IDCS GUID for your identity domain. For example:

```

```

In the above URL,`idcs-105bbbdfe5644611bf7ce04496073adf`
