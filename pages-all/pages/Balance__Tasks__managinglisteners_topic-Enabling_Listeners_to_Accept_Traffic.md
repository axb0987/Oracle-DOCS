# Updating Security Rules to Permit Traffic to a Load Balancer Listener
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Enabling_Listeners_to_Accept_Traffic.htm
- Fetched: 2026-09-05 01:41 CDT

# Updating Security Rules to Permit Traffic to a Load Balancer Listener

Update the security rules to permit traffic to listener associated with your load balancer.

## Using the Console

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Under List Scope , select a compartment that you have permission to work in. The list of VCNs in the current compartment appears.
- Select the name of the VCN containing your load balancer, and then select Network security groups or Security lists . A list of the security groups or lists in the cloud network appears.
- Select the name of the NSG or security list that applies to your load balancer.
- Add or edit the existing rules to give access from the appropriate resources. An NSG's security rules appear on the Network security group details page. From there you can add, edit, or remove rules. The Security list details page provides access to separate tables in which you can add or edit Ingress rules or Egress rules . For details on rule configuration, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)
