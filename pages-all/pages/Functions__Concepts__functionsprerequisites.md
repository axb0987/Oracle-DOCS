# Preparing for Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsprerequisites.htm
- Fetched: 2026-09-05 02:07 CDT

# Preparing for Functions

Find out about the high-level tasks to perform before you can use OCI Functions.

Before you can deploy functions to OCI Functions, you have to perform the tasks described in the[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionsquickstartguidestop.htm)to configure:
- 

Your Oracle Cloud Infrastructure tenancy for function development.

When your tenancy is configured, you will have access, via a suitable policy and user account, to a compartment that has a VCN with at least one public subnet (and an internet gateway) or at least one private subnet (and a service gateway). For more information about these network components, see[Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm).
- 

Your client environment for functions development.

When your client environment is configured, you will have access to the Fn Project CLI, and a Docker registry in which to store images (this documentation assumes you will be using[Oracle Cloud Infrastructure Registry](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryoverview.htm)as your Docker registry and provides instructions accordingly).

Use the[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionsquickstartguidestop.htm)to complete these configuration tasks.

For additional information about the configuration tasks, see[Appendix: Configuration Notes for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsconfigurationappendix.htm).

For more information specifically about setting up VCN and subnet CIDR blocks for use with OCI Functions, see[CIDR Blocks and OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscidrblocks.htm).

## Availability by Region

OCI Functions is available in the Oracle Cloud Infrastructure regions listed at[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)
