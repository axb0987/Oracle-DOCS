# Process Overview for Calling Services from Compute Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/Process_Overview.htm
- Fetched: 2026-09-05 02:20 CDT

# Process Overview for Calling Services from Compute Instances

Process flow for setting up and using Compute instances.

The following steps summarize the process flow for setting up and using Compute instances as principals. The subsequent sections provide more details.

- Create a[dynamic group](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/../dynamicgroups/managingdynamicgroups.htm). In the dynamic group definition, you provide the matching rules to specify which Compute instances you want to allow to make API calls against services.
- Create a policy granting permissions to the dynamic group to access services in your tenancy (or compartment).
- A developer in your organization configures the application built using the Oracle Cloud Infrastructure SDK to authenticate using the instance principals provider. The developer deploys the application and the SDK to all the Compute instances that belong to the dynamic group.
- The deployed SDK makes calls to Oracle Cloud Infrastructure APIs as allowed by the policy (without needing to configure API credentials).
- For each API call made by an instance, the[Audit service](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)logs the event, recording the OCID of the instance as the value of`principalId`
