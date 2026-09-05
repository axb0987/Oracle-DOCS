# Configuring Your Tenancy for API Gateway Development
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringtenancies.htm
- Fetched: 2026-09-05 01:37 CDT

# Configuring Your Tenancy for API Gateway Development

Find out about the high-level list of tasks to configure your tenancy for API Gateway.

Before you can start using the API Gateway service to create API gateways and deploy APIs on them, you have to set up your tenancy for API gateway development.

When a tenancy is created, an Administrators group is automatically created for the tenancy. Users that are members of the Administrators group can perform any operation on resources in the tenancy. API Gateway service users are typically not members of the Administrators group, and do not have to be. However, a member of the Administrators group does need to perform a number of administrative tasks to enable users to use the API Gateway service.

To set up your tenancy for API gateway development, you have to complete the following tasks in the order shown in this checklist (the instructions in the topics below assume that you are a tenancy administrator):

Task # Tenancy Configuration Task Done?
1[Create Groups and Users to Use API Gateway, if these don't exist already](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggroupsusers.htm)
2[Create Compartments to Own Network Resources and API Gateway Resources in the Tenancy, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingcompartment.htm)
3

[Create a VCN to Use with API Gateway, If One Doesn't Already Exist](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingvcn.htm)

See[Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewaynetworkconfigexample.htm)for details of typical network configurations.
4[Create Policies to Control Access to Network and API Gateway-Related Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm), and more specifically:
- [Create a Policy to Give API Gateway Users Access to API Gateway-Related Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#user-policy-on-apigw)
- [Create a Policy to Give API Gateway Users Access to Network Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#usersnetworkpolicy)
- [Create a Policy to Enable API Gateway Users to Create Certificate Associations](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#apigatewaycreatingpolicies_topic-Create_a_Policy_to_Allow_API_Gateway_Users_to_Manage_Certificate_Associations)
- [Create a Policy to Give API Gateway Users Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#usersfunctionspolicy)
- [Create a Policy to Give API Gateways Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy)
- [Create a Policy to Give API Gateways Access to Credentials Stored as Secrets in the Vault Service](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy-5)
