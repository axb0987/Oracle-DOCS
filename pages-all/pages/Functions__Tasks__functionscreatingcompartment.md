# Creating Compartments to Own Network Resources and OCI Functions Resources in the Tenancy, if they don't exist already
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingcompartment.htm
- Fetched: 2026-09-05 02:08 CDT

# Creating Compartments to Own Network Resources and OCI Functions Resources in the Tenancy, if they don't exist already

Find out how to create compartments to own network resources and OCI Functions resources in the tenancy, if they don't exist already.

Before users can start using OCI Functions to create and deploy functions, as a tenancy administrator you have to create:
- a compartment to own network resources (a VCN, a public or private subnet, and other resources such as an internet gateway or service gateway, a route table, security lists)
- a compartment to own function-related resources (functions, applications)

Note that the same compartment can own both network resources and function-related resources. Alternatively, you can create two separate compartments for network resources and function-related resources.

If suitable compartments already exist, there's no need to create new ones.

For more information about creating a compartment to own network resources and/or function-related resources in the tenancy, see[To create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To)
