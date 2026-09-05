# VMware Solution SDDC Security Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Reference/ocvssecurityrules.htm
- Fetched: 2026-09-05 03:07 CDT

# VMware Solution SDDC Security Rules

Learn about the security rules required for the subnet and VLANs in a functioning VMware Solution SDDC in Oracle Cloud Infrastructure.

This topic details the security rules the Console's Create SDDC workflow configures for the new SDDC's subnet and VLANs.
Important  
  
If you do not use the workflow to create an SDDC, ensure that you configure the SDDC's networking resources with these security rules. Otherwise, provisioning the SDDC will fail. If you want stricter security rules, you can update them after the SDDC is active. See[VMware Products and Solutions Ports Requirements](https://ports.esp.vmware.com/)for requirements.
All VLANs and subnets that are created using the Console workflow are configured with the following security rules:

Direction Source Protocol Source Port Destination Port Description
Ingress VCN CIDR 1 All All traffic for all ports All traffic for all ports Allow traffic from VCN CIDR
Ingress VCN CIDR2 All All traffic for all ports All traffic for all ports Allow traffic from VCN CIDR
