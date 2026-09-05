# Creating an Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps-task.htm
- Fetched: 2026-09-05 02:07 CDT

# Creating an Application

Find out how to create applications with OCI Functions.

In OCI Functions, an application is a logical grouping of functions. The properties you specify for an application determine resource allocation and configuration for all functions in that application. You have to create a function within an application, so at least one application must exist before you can create a function in OCI Functions.

For more information about applications, see[Applications](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsconcepts.htm#applications).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps-task.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps-task.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingapps-task.htm#)
- 

- Confirm that you have completed the steps in the[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsquickstartguidestop.htm).
- On the Applications list page, select the compartment specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionscreatefncontext.htm)). If you need help finding the list page, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/list-applications.htm).
- 

Select Create Application and specify the following details:
- Name: A name for the new application (for example, acmeapp). Avoid entering confidential information.
- VCN compartment: The compartment containing the VCN (virtual cloud network) in which to run functions.
- VCN: The VCN (virtual cloud network) in which to run functions. For example, a VCN called acme-vcn-01
- Subnets compartment: The compartment containing the subnet (or subnets) in which to run functions.
- Subnets in &lt;compartment-name&gt;: The subnet (or subnets, up to a maximum of three) in which to run functions. For example, a public subnet called Public Subnet IHsY:US-PHOENIX-AD-1).

A public subnet requires an internet gateway in the VCN, and a private subnet requires a service gateway in the VCN. If a regional subnet has been defined, as a best practice, select that subnet to make it easier to implement failover across availability domains. If a regional subnet hasn't been defined and you need to meet high availability requirements, select multiple subnets. We recommend that the subnets are in the same region as the Docker registry that's specified in the Fn Project CLI context. For more information, see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionscreatefncontext.htm).

Specifying a private subnet for an application doesn't prevent access from the internet to the invoke endpoints of functions in the application. Use identity policies to control access to function invoke endpoints. For details, see[Controlling Access to Invoke and Manage Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsrestrictinguseraccess.htm).
- 

Shape: The processor architecture of the compute instances on which to deploy and run functions in the application. All the functions in the application are deployed and run on compute instances with the same architecture. The function's image must contain the necessary dependencies for the architecture you select, as follows:
- Select the Generic_ARM shape if you always want functions in the application to run on compute instances with an Arm-based architecture. If you select this single architecture shape for the application, the function's image must contain the necessary dependencies for the Arm architecture (in either a single architecture image, or a multi-architecture image).
- Select the Generic_X86 shape if you always want functions in the application to run on compute instances with an x86-based architecture. If you select this single architecture shape for the application, the function's image must contain the necessary dependencies for the x86 architecture (in either a single architecture image, or a multi-architecture image).
- Select the Generic_X86_ARM shape if you want functions to run on compute instances with whichever architecture has sufficient capacity. In this case, OCI Functions selects the architecture on which to run functions based on available capacity. If you select this multi-architecture shape for the application, every function's image must contain the necessary dependencies for both the Arm architecture and the x86 architecture (in a multi-architecture image).

Note that you cannot change the application's shape after you have created the application. See[Selecting a Single Architecture or Multi-Architecture Application Shape on which to run a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsspecifyingcomputearchitectures.htm#functionsspecifyingapplicationfunctionarchitectures).
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Security attributes: If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- 

Select one of the following options:
- To create the application now, select Create . The new application appears in the list of applications.
- To create the application later using Resource Manager and Terraform, select Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To create a new application in OCI Functions using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, create a new application by entering:

```

```

where:
- `<app-name>`is the name of the new application. Avoid entering confidential information.
- `<subnet-ocid>`is the OCID of the subnet (or subnets, up to a maximum of three) in which to run functions. Note that a public subnet requires an internet gateway in the VCN, and a private subnet requires a service gateway in the VCN. If a regional subnet has been defined, best practice is to select that subnet to make failover across availability domains simpler to implement. If a regional subnet has not been defined and you need to meet high availability requirements, specify multiple subnets (up to three) by including`--subnet-id <subnet-ocid>`in the command multiple times. Oracle recommends that the subnets are in the same region as the Docker registry that's specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionscreatefncontext.htm)).

Note that specifying a private subnet for an application does not prevent access from the internet to the invoke endpoints of functions in the application. Use identity policies to control access to function invoke endpoints (see[Controlling Access to Invoke and Manage Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsrestrictinguseraccess.htm)).

For example:

```

```

An application is created in OCI Functions, in the tenancy and region implied by the subnet OCID and belonging to the compartment specified in the Fn Project CLI context file.
- 

Verify that the new application has been created by entering:

```

```

For example:
```

```

Using the OCI CLI

Use the[oci fn application create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/application/create.html)command and required parameters to create an application:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/CreateApplication)
