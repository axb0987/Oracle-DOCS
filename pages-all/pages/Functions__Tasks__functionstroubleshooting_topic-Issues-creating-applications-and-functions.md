# Issues creating applications and functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-creating-applications-and-functions.htm
- Fetched: 2026-09-05 02:09 CDT

# Issues creating applications and functions

Find out how to troubleshoot problems when creating applications and functions with OCI Functions.

You might encounter these issues when creating applications and functions with OCI Functions.

## Creating a new application displays an error message in the New Application dialog

If you've already reached the limit for the number of applications in your tenancy, you might see a message similar to the following in the New Application dialog when trying to create a new application:
```

```

Double-check how many applications already exist in your tenancy. Compare that with the number of applications you're allowed to create. See[OCI Functions Capabilities and Limits](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Concepts/functionsoverview.htm#limits).

If you've exceeded the number of applications allowed in your tenancy, consider:
- Deleting unwanted applications (see[Deleting an Application](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingapplications.htm)).
- Requesting an increase to the application limit (see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)
