# Creating an API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_create_api_gateway.htm
- Fetched: 2026-09-05 02:34 CDT

# Creating an API Gateway

Learn how to create an API gateway for TLS connectivity to external KMS.

The following procedure provides details only related to FQDN configuration. For complete configuration, see[Creating API Gateway](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm#top).

- Open the navigation menu and select Developer Services
- Under API Management, select Gateways .
- In API Gateway page, select Create Gateway .
- In the Create Gateway page, provide the following details:

- Name: The name of the API gateway for the external key manager.
- Type: The type of API gateway to create. Select Private for the API gateway (and the APIs deployed on it) to be accessible only from the same subnet in which the API gateway is created.
- Compartment: The compartment in which you want to create the API gateway.
- Under Network , provide the following details
- VCN: The VCN in which you want to create the API gateway.
- Subnet: The name of the private subnet in which you want to create the API gateway.
- Under Certificate , select the TLS certificate that you have already uploaded in the API Gateway's Certificates service.
- Select Show Advanced Options and under Certificate authorities , provide the following details:

- Type: Select the certificate type.
- Certificate bundle/authority: select + Additional Certificate authorities to select the CA bundle that you uploaded in the CA Certificate service.
-
