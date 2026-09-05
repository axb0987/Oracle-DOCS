# Verifying Your Configuration for Function Development
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsverifyingconfig.htm
- Fetched: 2026-09-05 02:09 CDT

# Verifying Your Configuration for Function Development

Find out how to verify that your tenancy and development environment are ready for function development with OCI Functions.
Before using OCI Functions, it's a good idea to confirm that you have successfully completed the prerequisite steps for using OCI Functions as described in[Preparing for Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Concepts/functionsprerequisites.htm)and the[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartguidestop.htm). Specifically, that you have:
- set up your tenancy (see[Tenancy Configuration Notes for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringtenancies.htm))
- set up your development environment (see[Client Environment Configuration Notes for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringclient.htm))

If you have successfully completed the configuration tasks, the Fn Project CLI will be able to communicate with the API endpoint.

To confirm that the Fn Project CLI can communicate with the API endpoint:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, try and view a list of applications that have been defined in OCI Functions by entering:

```

```

- 

If you see either of the following, you can proceed to create and deploy functions because your system is configured correctly:
- A message indicating that no applications have been found, which is expected if this is the first time the tenancy has been configured for OCI Functions.
- A list of applications that have already been created, which is expected if other users are already using the tenancy for functions development.
- 

If you see an error message, it's likely that the Fn Project CLI cannot communicate with the API endpoint due to some incorrect configuration. Do the following:
- Review the configuration tasks to confirm you completed them as instructed (see[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartguidestop.htm),[Tenancy Configuration Notes for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringtenancies.htm), and[Client Environment Configuration Notes for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringclient.htm)).
- Review the solutions for common problems (see[Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm)
