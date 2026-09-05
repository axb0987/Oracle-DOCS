# Create Compartments to Own Network Resources and API Gateway Resources in the Tenancy, if they don't exist already
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingcompartment.htm
- Fetched: 2026-09-05 01:37 CDT

# Create Compartments to Own Network Resources and API Gateway Resources in the Tenancy, if they don't exist already

Find out how to create compartments for use with API Gateway.

Before users can start using the API Gateway service to create API gateways and deploy APIs on them, as a tenancy administrator you have to create:
- a compartment to own network resources (a VCN, a public or private regional subnet, and other resources such as an internet gateway, a route table, security lists and/or network security groups)
- a compartment to own API Gateway resources (API gateways, API deployments)

Note that the same compartment can own both network resources and API Gateway-related resources. Alternatively, you can create two separate compartments for network resources and API Gateway-related resources.

If suitable compartments already exist, there's no need to create new ones.

To create a compartment to own network resources and/or API Gateway-related resources in the tenancy:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments . A list of the compartments in your tenancy is displayed.
- Select Create Compartment and create a new compartment (see[Creating a Compartment](https://docs.oracle.com/iaas/Content/Identity/compartments/To_create_a_compartment.htm)). Give the compartment a meaningful name (for example,`acme-network`,`acme-api-gateway-compartment`, ) and description. Avoid entering confidential information.
Tip
