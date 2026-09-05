# Viewing Current Limit Values for OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsviewinglimits.htm
- Fetched: 2026-09-05 02:09 CDT

# Viewing Current Limit Values for OCI Functions

Find out how to view the current values of limits for OCI Functions.

OCI Functions has regional limits for the number of functions and applications you can create, and for the memory available for concurrent function execution and provisioned concurrency. These limits have default values, as shown in[Function Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Functions_Limits). The default values might have already been increased in your tenancy, perhaps in response to previous requests to increase capacity.

You can see the current values of the limits for OCI Functions using the Console.

## Using the Console to View Current Values of Limits for OCI Functions

To view the current values of the limits that apply to OCI Functions:
- 

Open the navigation menu and select Governance &amp; Administration . Under Tenancy Management , select Limits, Quotas and Usage .
- Select Functions from the Service list.
- 

Select the region from the Scope list.
- 

Select the root compartment from the Compartment list.

The current values of the following limits that apply to OCI Functions are shown:

Limit Name

Description
`application-count`Application count
`function-count`Function count
`total-concurrency-mb`Total memory for concurrent function execution
`provisioned-concurrency-mb`Total memory for provisioned concurrency

In some cases, you can request additional resources.
-
