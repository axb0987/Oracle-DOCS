# Adding Applications to Network Security Groups (NSGs)
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingnsgs.htm
- Fetched: 2026-09-05 02:09 CDT

# Adding Applications to Network Security Groups (NSGs)

Find out how to attach Network Security Groups (NSGs) to applications with OCI Functions.

Network security groups (NSGs) enable you to define ingress and egress rules that apply to particular VNICs and other resources in a VCN. Unlike a security list, which is attached to a subnet and which has security rules that apply to all the resources in that entire subnet, you can add individual resources to an NSG. Using NSGs rather than security lists gives you more granular control over the security rules that apply to individual resources. For more information about NSGs, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).

You can add an OCI Functions application to one or more NSGs (up to a maximum of five). Adding an application to an NSG enables you to define ingress and egress rules that apply to all the functions in that particular application. The ingress and egress rules defined for the NSG determine the access that the application's functions have to other network resources.

Using NSGs is useful when you have specified the same subnet for multiple applications that have different access requirements. You can add the applications to different NSGs, enabling you to apply different security rules to the functions running in those applications. For example, you might want functions in one application to access a database and object storage, and functions in a second application to access the database and make an external call through a NAT gateway to a REST service on the public internet. Using NSGs enables you to have both applications in the same subnet without compromising network security.

You can add or remove an application to or from an NSG using the Console, the OCI CLI, and the API.

## Required IAM Policy for Adding Applications to NSGs

Before you can add applications to NSGs, the group to which you belong must have permission to use NSGs. See[Policy Statement to Give OCI Functions Users Access to Network Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#usernetworkpolicy).

## Using the Console

To add or remove an existing OCI Functions application to or from a network security group (NSG) using the Console:
- On the Applications list page, select the application that you want to add to an NSG, or to remove from an NSG.. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).

On the Details tab, the Network security groups field shows the NSGs to which the application has already been added (if any).
- 

To add the application to an NSG:
- Select Add beside Network security groups .
- In the Edit network security groups panel, select Network security group and select the NSG to which you want to add the application.

The NSG can be in the same compartment or a different compartment, but must be in the same VCN as the subnets specified for the application.
- If you want to add the application to multiple NSGs, select Another network security group and select additional NSGs (up to a maximum of five).
- Select Save changes .
- 

To remove the application from an NSG:
- Select Edit beside Network security groups .
- In the Edit network security groups panel, select the X button beside the NSG(s) from which you want to remove the application.

The application need not be added to any NSGs.
- Select Save changes .

The ingress and egress rules defined for the NSGs shown in the Network security groups field on the application's Details tab now apply to functions in the application.

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to add or remove an application to or from an NSG:
- [CreateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/CreateApplication)
- [UpdateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/UpdateApplication)
