# Adding Security Attributes to Applications, and Applying ZPR Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm
- Fetched: 2026-09-05 02:09 CDT

# Adding Security Attributes to Applications, and Applying ZPR Policies

Find out how to add security attributes to applications and how to apply Zero Trust Packet Routing (ZPR) policies with OCI Functions.

Using Zero Trust Packet Routing (ZPR) with OCI Functions enables you to implement fine-grained, least-privilege access control over interactions between functions and other OCI resources. ZPR is especially useful in environments where sensitive data or critical operations are distributed across multiple OCI resources, and strict separation and control of resource access is required. Using ZPR helps you to mitigate risks associated with unauthorized access and ensure that only explicitly permitted traffic flows between protected resources, supporting both compliance needs and organizational security policies.

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

To use ZPR with OCI Functions, you add security attributes to an application in a ZPR-enabled tenancy. Having added a security attribute to an application, the functions in the application can only access other OCI resources if access is allowed by a ZPR policy.

Security attributes are defined in a security attribute namespace. To add a security attribute to an application, an IAM policy must grant the group to which you belong access to the namespace in which the security attribute is defined. For more information, see[Required IAM policy for adding security attributes to applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm#functionsusingzpr_topic_permissions).

To enable functions in an application to which you have added a security attribute to access other OCI resources, a suitable ZPR policy must exist. If such a ZPR policy does not exist, you have to create one. If security attributes have also been added to the other resources, you can create a ZPR policy that explicitly allows functions to access resources with those security attributes. If security attributes have not been added to the other resources that you want functions to access, you can use`'osn-services-ip-addresses'`as the endpoint to create a more permissive ZPR policy. Without a suitable ZPR policy, functions' access to other resources is blocked at the network level and connection errors might occur within function code. For more information, see[Required ZPR policy to enable applications (and functions) to access other resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm#functionsusingzpr_topic_ziprpolicy).
Important  
  

In order to successfully invoke functions in an application to which you have added a security attribute, a suitable ZPR policy must exist to enable access to the Oracle Cloud Infrastructure Registry repositories containing the images on which the functions are based. If a suitable ZPR policy does not exist, functions cannot be invoked successfully because images cannot be pulled from the repositories.

For more information about the ZPR policy to create, see[Required ZPR policy to enable function images to be pulled from Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm#functionsusingzpr_topic_zprpolicy_for_registry).

Note the following points:
- To see the applications to which security attributes have been added, use the ZPR Console page (see[Listing Protected Resources](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/list-protected-resources.htm)in the ZPR documentation.). The ZPR Console page also displays VNICs created by OCI Functions, with the display name of each VNIC set to the OCID of the owning application.
- Having added security attributes to an application, you can use the Network Path Analyzer to help debug any network connectivity issues encountered by functions in the application.
- Using security attributes and ZPR policies to restrict access to OCI Functions resources from other OCI services at the network level is not currently supported.
- If you have added a security attribute to an application, and the ZPR Console, CLI, or API is subsequently used to delete the security attribute from the security attribute namespace, you have to manually remove the security attribute from the application. If you do not remove the deleted security attribute from the application, 502 errors are returned when functions in the application are invoked.

You can add or remove security attributes to or from applications using the Console, the OCI CLI, and the API.

## Required IAM policy for adding security attributes to applications

Before you can add a security attribute to an application, an IAM policy must grant the group to which you belong permission to use the security attribute namespace containing the security attribute.

For example:
```

```

For more information, see[Policy Statement to Give OCI Functions Users Access to Security Attribute Namespaces](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#functionscreatingpolicies_topic_Create_a_Policy_to_Give_Oracle_Functions_Users_Access_to_ZPR).

Note that if a suitable IAM policy to use the security attribute namespace does not exist, you cannot add the security attribute to the application. The security attribute is not shown in the Console, and attempts to add the security attribute using the OCI CLI or the API return a 404 - Not Found error message.

## Required ZPR policy to enable applications (and functions) to access other resources

When you add a security attribute to an OCI Functions application, the functions in that application can only access other resources if a ZPR policy grants the application access to those resources.

If a suitable ZPR policy does not already exist you have to create one. For example, using the following syntax:
```

```

where:
- `<vcn-security-attribute>`is a security attribute (and value) that has been added to the VCN in which the application's subnet resides. For example,`VCN-Network:myVCN`.
- `<application-security-attribute>`is the security attribute (and value) that you have added to the application. For example,`functions-app:myFuncAppA`
- `<destination-security-attribute>`is a security attribute (and value) that has been added to the resource that you want functions in the application to access. For example,`DB-Server:App1`

For example:
```

```

For more information about ZPR policies, syntax, and examples, see[Zero Trust Packet Routing Policy](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/zpr-policy-overview.htm)in the ZPR documentation.

## Required ZPR policy to enable function images to be pulled from Oracle Cloud Infrastructure Registry

To successfully invoke functions in an application to which you have added a security attribute, a ZPR policy must exist to enable access to the Oracle Cloud Infrastructure Registry repositories containing the images on which the functions are based.

If a suitable ZPR policy does not already exist, you have to create a ZPR policy using the following syntax:
```

```

where:
- `<vcn-security-attribute>`is a security attribute (and value) that has been added to the VCN in which the application's subnet resides. For example,`VCN-Network:myVCN`
- `<application-security-attribute>`is the security attribute (and value) that you have added to the application. For example,`functions-app:myFuncAppA`

For example:
```

```

If a suitable ZPR policy does not exist, when a function is invoked, OCI Functions is unable to pull the image from Oracle Cloud Infrastructure Registry and returns the following error message:
```

```

For more information about ZPR policies, syntax, and examples, see[Zero Trust Packet Routing Policy](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/zpr-policy-overview.htm)in the ZPR documentation.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingzpr.htm#)
- 

To add or remove security attributes to or from an existing OCI Functions application using the Console:
- On the Applications list page, select the application that you want to add or remove security attributes to or from. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).

The Security tab shows the security attributes that have already been added to the application (if any).
- 

To add a security attribute to the application:
- On the Security tab, select Add , and in the Add security attributes dialog:
- Select the security attribute namespace that contains the security attribute.
- Select the security attribute.
- Enter the security attribute value.
- If you want to add multiple security attributes to the application, select Add security attribute and select additional security attributes (up to a maximum of three).
- Select Add security attributes .
- 

To remove a security attribute from the application:
- On the Security tab, select Delete from the Actions menu (three dots) beside the security attribute you want to delete.
- Confirm that you want to delete the security attribute.

The security attributes shown on the application's Security tab now apply to the application.
- 

Use the[oci fn application create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/application/create.html)command and required parameters to create an application:

```

```

Use the[oci fn application update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/application/update.html)command and required parameters to update an application:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to add or remove security attributes to or from an application:
- [CreateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/CreateApplication)
- [UpdateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/UpdateApplication)
