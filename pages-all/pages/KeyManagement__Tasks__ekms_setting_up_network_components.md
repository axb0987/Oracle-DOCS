# Setting Up Networking Components
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_setting_up_network_components.htm
- Fetched: 2026-09-05 02:35 CDT

# Setting Up Networking Components

Learn about configuring External Key Management (EKMS) network components.
To allow your external key manager to communicate with Oracle Cloud Infrastructure (OCI), you must have a Virtual Cloud Network (VCN) available in your OCI tenancy. The VCN provides a customizable private network with complete control to your cloud networking environment. For EKMS, you must configure the following networking components in the OCI Networking service:
- VCN
- Subnets
- Internet Gateways
- Routing Tables
- Security Rules

You can use the following example scenario to guide your networking configuration:

## Creating a VCN

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- On the Virtual cloud networks page, select Create VCN .
- In the Create VCN workflow, provide the following details:
- Name: Enter a name for the VCN.
- Compartment: Select a compartment for the VCN.
- Under IPv4 CIDR Blocks , set the following parameters:
- IPv4 CIDR Blocks: Provide IPV4 CIDR blocks for the VCN. For example, 10.0.0.0/16.
- Select Create VCN .

See[Creating a VCN](https://docs.oracle.com/iaas/Content/Network/Tasks/create_vcn.htm)in the Networking documentation for more information.

## Configuring Subnet

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- On the Virtual Cloud Networks list view page, select the name of the VCN you're configuring to view its details page.
- Select Subnets , then select Create Subnet .
- In the Create Subnet workflow, provide the following details:
- Name: Enter a name for the subnet.
- Compartment: Select a compartment for the subnet.
- Under IPv4 CIDR Blocks , set the following parameters:
- IPv4 CIDR Blocks: Provide IPV4 CIDR blocks for the Subnet. Select private subnet or public subnet depending on your requirements. For example, 10.0.0.0/16.
- Select Create Subnet .

See[Creating a Subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/create_subnet.htm)in the Networking documentation for more information.

## Creating Internet Gateway

Complete the following steps to configure an internet gateway.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- On the Virtual Cloud Networks list view page, select the name of the VCN you're configuring to view its details page.
- Select Gateways , then select Create Internet Gateway .
- In the Create Internet Gateways workflow, provide the following details:
- Name: Enter a name for the internet gateway.
- Compartment: Select a compartment for the internet gateway.
- Select Advanced options , then in the Routable Table Association section, add the route table you need. In this example configuration, the default route table is used.
- Select Create Internet Gateway .

See

## Creating a Routing Table

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- On the Virtual Cloud Networks list view page, select the name of the VCN you're configuring to view its details page.
- Select Routing , then select Create Route Table .
- In the Create Routing Table workflow, provide the following details:
- Name: Enter a name for the routing table.
- Compartment: Select a compartment for the routing table.
- Under Route Rules , select + Another Route Rule . In this example scenario, access to the VCN is through the internet, so the example route rule has 0.0.0.0/0 for the destination CIDR value.
- Select Create .

## Creating a Security List

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- On the Virtual Cloud Networks list view page, select the name of the VCN you're configuring to view its details page.
- Select Security , then select Create Security List .
- In the Create Security List page, provide the following details:
- Name: Enter a name for the routing table.
- Compartment: Select a compartment for the routing table.
- Under Allow Rules for Ingress , select + Another ingress Rule and provide the following details:
- Stateless: Enable this option using the switch.
- Source Type: Select CIDR.
- Source CIDR: Provide the source CIDR address.
- IP Protocol: Select the IP protocol as TCP.
-
