# Configuring VMware Solution SDDC Network Connectivity
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity.htm
- Fetched: 2026-09-05 03:08 CDT

# Configuring VMware Solution SDDC Network Connectivity

Use quick action workflows in the Console to configure network connectivity for a Software-Defined Data Center (SDDC). You can configure network connectivity from the SDDC to an on-premises network, the Oracle Services Network, the internet, and VCN resources.

## About the SDDC Workflows

The SDDC quick action workflows make it easy for you to configure connectivity between an SDDC and various network resources within and outside of the VCN. Each workflow decides whether the required networking resources for connectivity already exist, and tries to create or update them as needed. These networking resources can include gateways, subnets, route tables, rules, and network security groups. To use a workflow successfully, you must have the proper permissions for using and managing the applicable resources. See[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm)for information about networking resource permissions. Resource creation also relies on limits and remaining capacity to create more resources.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

## Network Connectivity Configurations

- [Connecting a VMware Solution SDDC to an On-premises Network](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_Your_Onpremises_Network.htm)
- [Connecting a VMware Solution SDDC to the Oracle Services Network](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_the_Oracle_Services_Network.htm)
- [Connecting a VMware Solution SDDC to the Internet](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_the_Internet_Through_a_NAT_Gateway.htm)
- [Connecting a VMware Solution SDDC to Other Resources in the VCN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_Other_Resources_in_the_VCN.htm)
