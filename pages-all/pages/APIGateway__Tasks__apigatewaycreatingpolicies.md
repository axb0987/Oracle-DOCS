# Create Policies to Control Access to Network and API Gateway-Related Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm
- Fetched: 2026-09-05 01:37 CDT

# Create Policies to Control Access to Network and API Gateway-Related Resources

Find out how to create policies for use with API Gateway.

Before users can start using the API Gateway service to create API gateways and deploy APIs on them, as a tenancy administrator you have to create a number of Oracle Cloud Infrastructure policies to grant access to API Gateway-related and network resources.

To grant access to API Gateway-related and network resources, you have to:
- 

Grant users access to API Gateway-related resources, network resources, and (optionally) function resources. More specifically, you have to:
- [Create a Policy to Give API Gateway Users Access to API Gateway-Related Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#user-policy-on-apigw)
- [Create a Policy to Give API Gateway Users Access to Network Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#usersnetworkpolicy)
- [Create a Policy to Give API Gateway Users Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#usersfunctionspolicy)
- Enable API Gateway users to associate a Certificates service certificate resource with an API gateway when setting up a custom domain name, if required. See[Create a Policy to Enable API Gateway Users to Create Certificate Associations](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#apigatewaycreatingpolicies_topic-Create_a_Policy_to_Allow_API_Gateway_Users_to_Manage_Certificate_Associations).
- Enable API Gateway users to associate a Certificate Authority (CA) or CA bundle in the Certificates service with an API gateway when setting up a custom trust store, if required. See[Create a Policy to Enable API Gateway Users to Manage CAs and CA Bundles](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#apigatewaycreatingpolicies_topic-Create_a_Policy_to_Allow_API_Gateway_Users_to_Manage_CA_bundles).
- 

Grant API gateways access to functions defined in OCI Functions, if required. If API Gateway users define a new API gateway with a serverless function in OCI Functions as an API back end, the API Gateway service verifies that the new API gateway will have access to the specified function. To provide access, you have to create a policy that grants API gateways access to functions defined in OCI Functions. See[Create a Policy to Give API Gateways Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy).
- Grant API gateways access to secrets stored in vaults in the Vault service, if required. If API Gateway users define an API gateway that caches response data in an external cache server (such as a Redis server), the credentials to authenticate with the cache server must be stored in the Vault service. Similarly, if API Gateway users define an API gateway that accesses an authorization server's introspection endpoint to validate tokens, the credentials to access the authorization server must be stored in the Vault service. See[Create a Policy to Give API Gateways Access to Credentials Stored as Secrets in the Vault Service](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy-5).

See[Details for API Gateway](https://docs.oracle.com/iaas/Content/Identity/Reference/apigatewaypolicyreference.htm)for more information about policies.

## Create a Policy to Give API Gateway Users Access to API Gateway-Related Resources

When API Gateway users define a new API gateway and new API deployments, they have to specify a compartment for those API Gateway-related resources. Users can only specify a compartment that the groups to which they belong have been granted access. To enable users to specify a compartment, you must create an identity policy to grant the groups access.

To create a policy to give users access to API Gateway-related resources in the compartment that will own those resources:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select Create Policy and create a new policy:
- 

Enter the following:
- Name: A meaningful name for the policy (for example,`acme-apigw-developers-manage-access`). The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description (for example,`Gives api-gateway developers access to all resources in the acme-apigw-compartment`). You can change this later if you want to.
- Compartment: The compartment that will own API Gateway-related resources.
- Select Show manual editor and enter the following policy statement to give the group access to all API Gateway-related resources in the compartment:

```

```

For example:

```

```

- (Optional) Select the Tags option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the policy giving API Gateway users access to API Gateway-related resources in the compartment.
Tip  
  
Normally, API gateways and API deployments are created in the same compartment. However, in large development teams with many API developers, you might find it useful to create separate compartments for API gateways and for API deployments. Doing so will enable you to give different groups of users appropriate access to those resources.

## Create a Policy to Give API Gateway Users Access to Network Resources

When API Gateway users define a new API gateway, they have to specify a VCN and a subnet in which to create the API gateway. Users can only specify VCNs and subnets that the groups to which they belong have been granted access. To enable users to specify a VCN and subnet, you must create an identity policy to grant the groups access. In addition, if you want to enable users to create public API gateways, the identity policy must allow the groups to manage public IP addresses in the compartment that owns the network resources.

To create a policy to give API Gateway users access to network resources:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select Create Policy and create a new policy:
- 

Enter the following:
- Name: A meaningful name for the policy (for example,`acme-apigw-developers-network-access`). The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description (for example,`Gives api-gateway developers access to all network resources in the acme-network compartment`). You can change this later if you want to.
- Compartment: The compartment that will own API Gateway-related resources.
- Select Show manual editor and enter the following policy statement to give the group access to network resources in the compartment (including the ability to manage public IP addresses):

```

```

For example:

```

```

- (Optional) Select the Tags option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the policy giving API Gateway users access to network resources and public IP addresses in the compartment.

## Create a Policy to Give API Gateway Users Access to Functions

When API Gateway users define a new API gateway, one option is to specify a serverless function defined in OCI Functions as the API back end. Users can only specify functions that the groups to which they belong have been granted access. If you want to enable users to specify functions as API back ends, you must create an identity policy to grant the groups access. Note that in addition to this policy for the user group, to enable users to specify functions as API back ends you also have to create a policy to give API gateways access to OCI Functions (see[Create a Policy to Give API Gateways Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy)).

Another reason to create an identity policy that grants groups access to OCI Functions is if you want to enable users to use the Console (rather than a JSON file) to define an authentication request policy and specify an authorizer function defined in OCI Functions (see[Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm)).

To create a policy to give API Gateway users access to functions defined in OCI Functions:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select Create Policy and create a new policy:
- 

Enter the following:
- Name: A meaningful name for the policy (for example,`acme-apigw-developers-functions-access`). The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description (for example,`Gives api-gateway developers access to all functions in the acme-functions-compartment`). You can change this later if you want to.
- Compartment: The compartment that will own API Gateway-related resources.
- Select Show manual editor and enter the following policy statement to give the group access to the functions in the compartment:

```

```

For example:

```

```

- (Optional) Select the Tags option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the policy giving API Gateway users access to functions in the compartment.

## Create a Policy to Enable API Gateway Users to Create Certificate Associations

API Gateway users can use a Certificates service certificate resource to set up a custom domain name for an API gateway. To enable users to associate a Certificates service certificate resource with an API gateway, you must create an identity policy to allow the groups to which the users belong to create certificate associations.

To create a policy to enable API Gateway users to associate a Certificates service certificate resource with an API gateway:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select Create Policy and create a new policy:
- 

Enter the following:
- Name: A meaningful name for the policy (for example,`acme-apigw-developers-certificate-association`). The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description (for example,`Gives api-gateway developers the ability to create certificate associations`). You can change this later if you want to.
- Compartment: The compartment that will own API Gateway-related resources.
- Select Show manual editor and enter the following policy statement to enable the group to associate a Certificates service certificate resource with an API gateway in the compartment:

```

```

For example:

```

```

- (Optional) Select the Tags option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the policy enabling API Gateway users to associate Certificates service certificate resources with API gateways in the compartment.

## Create a Policy to Enable API Gateway Users to Manage CAs and CA Bundles

In addition to the default certificate authority (CA) and CA bundle, API Gateway users can choose to add the root certificates of other CAs, and other CA bundles (referred to as custom CAs and custom CA bundles) to an API gateway's trust store. To customize an API gateway's trust store by adding a custom CA or CA bundle, users have to first create a CA resource or CA bundle resource in the Certificates service. See[Customizing Trust Stores for TLS Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm).

To enable users to add custom CAs and custom CA bundles to custom trust stores, you must create an identity policy to allow the groups to which the users belong to manage certificate authorities in the Certificates service.

To create a policy to enable API Gateway users to add custom CAs and custom CA bundles to custom trust stores:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select Create Policy and create a new policy:
- 

Enter the following:
- Name: A meaningful name for the policy (for example,`acme-apigw-developers-custom-ca-bundle`). The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description (for example,`Gives api-gateway developers the ability to add custom CAs and CA bundles`). You can change this later if you want to.
- Compartment: The compartment that will own API Gateway-related resources.
- Select Show manual editor and enter the following policy statement to enable the group to add custom CAs and custom CA bundles to the custom trust store of API gateways in the compartment:

```

```

For example:

```

```

- (Optional) Select the Tags option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the policy enabling API Gateway users to add custom CAs and custom CA bundles to custom trust stores.

## Create a Policy to Give API Gateways Access to Functions

When API Gateway users define a new API gateway, one option is to specify a serverless function defined in OCI Functions as the API back end. Before creating the API gateway, the API Gateway service verifies that the new API gateway will have access to the specified function through an IAM policy.

Note that in addition to this policy for API gateways, to enable users to specify functions as API back ends you also have to create a policy to give users access to OCI Functions (see[Create a Policy to Give API Gateway Users Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#usersfunctionspolicy)).

To create a policy to give API gateways access to functions defined in OCI Functions:
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- Select Create Policy and create a new policy:
- 

Enter the following:
- Name: A meaningful name for the policy (for example,`acme-apigw-gateways-functions-policy`). The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description (for example,`Gives API gateways access to functions in the acme-apigw-compartment`). You can change this later if you want to.
- Compartment: The compartment containing the function-related resources to which you want to grant access. If the resources are in different compartments, select a common parent compartment (for example, the tenancy's root compartment).
- Select Show manual editor and enter the following policy statement to give API gateways access to the compartment containing functions defined in OCI Functions:

```

```

where:
- `<functions-compartment-name>`is the name of the compartment containing the functions you want to use as back ends for API gateways.
- `<api-gateway-compartment-OCID>`is the OCID of the compartment containing the API gateways that you want to have access to the functions.

For example:

```

```

- (Optional) Select the Tags option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the policy giving API gateways access to functions defined in OCI Functions.

## Create a Policy to Give API Gateways Access to Credentials Stored as Secrets in the Vault Service

If API Gateway users define an API gateway that caches response data in an external cache server (such as a Redis server), the credentials to authenticate with the cache server must be stored in the Vault service. Similarly, if API Gateway users define an API gateway that accesses an authorization server's introspection endpoint to validate tokens, the credentials to authenticate with the authorization server must be stored in the Vault service. To enable API gateways to authenticate with the cache server or the authorization server, you have to create a policy that grants API gateways access to secrets in the Vault service.

To create a policy to give API gateways access to secrets in the Vault service:
- Log in to the Console as a tenancy administrator.
- 

Create a new dynamic group comprising one or more API gateways:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select a domain, and select the Dynamic groups tab. A list of the dynamic groups in the domain is displayed.
- Follow the instructions in[Creating a Dynamic Group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/To_create_a_dynamic_group.htm), and give the dynamic group a name (for example,`acme-apigw-dyn-grp`).
- 

When specifying a rule for the dynamic group, consider the following examples:
- 

If you want all API gateways in a compartment to be able to access secrets, enter a rule similar to the following that adds all API gateways in the compartment with the specified compartment OCID to the dynamic group:

```

```

- 

If you want a specific API gateway to be able to access secrets, enter a rule similar to the following that adds the API gateway with the specified OCID to the dynamic group:

```

```

- Select Create .

Having created a dynamic group that includes one or more API gateways, you can now create a policy to give the dynamic group access to one or more secrets.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- Select Create Policy and create a new policy:
- 

Enter the following:
- Name: A meaningful name for the policy (for example,`acme-apigw-dyn-grp-policy`). The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description (for example,`Gives dynamic group access to secrets in the Vault service`). You can change this later if you want to.
- Compartment: The compartment that will own API Gateway-related resources.
- Select Show manual editor and enter policy statements to grant the dynamic group access to one or more secrets in the Vault service.

When specifying a policy statement, consider the following examples:
- 

If you want API gateways in the`acme-apigw-dyn-grp`to be able to access all secrets in a compartment, enter a policy statement similar to the following:

```

```

- 

If you want API gateways in the`acme-apigw-dyn-grp`to be able to access a specific secret, enter a policy statement similar to the following:

```

```

- (Optional) Select the Tags option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
-
