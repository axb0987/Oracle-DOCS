# Deploying the API Gateway with FQDN Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deploy_api_gateway.htm
- Fetched: 2026-09-05 02:34 CDT

# Deploying the API Gateway with FQDN Details

Learn how to deploy an API gateway for TLS connectivity to external KMS.

The following procedure provides details for deploying an API gateway with FQDN details. For complete deployment, see[Deploying API Gateway](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).

- Open the navigation menu and select Developer Services .
- Under API Management, select Gateways .
- In API Gateway page, a select an API gateway to view its details page.
- Under Resources , select Deployments and then select Create Deployment .
- In the Create Deployment page, provide the following details::

- Name: The name of the new API deployment. Avoid entering confidential information
- Path Prefix: Use path:`/<path-prefix>/ekm/v1`
- Compartment: The compartment in which to create the new API deployment.
- Select Next
- Under Route 1 , specify the following:

- Path: Configure:`/{path*}`.
- Methods: Select GET , POST .
- Backend Type: Select the backend type as HTTP and specify the URL as`https:// <your-ekm-fqdn> /<path-prefix>/ekm/v1/${request.path[path]}`
-
