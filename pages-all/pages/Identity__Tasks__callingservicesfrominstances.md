# Calling Services from an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm
- Fetched: 2026-09-05 02:15 CDT

# Calling Services from an Instance

This topic describes how you can authorize instances to call services in Oracle Cloud Infrastructure.

## Introduction

This procedure describes how you can authorize an instance to make API calls in Oracle Cloud Infrastructure services. After you set up the required resources and policies, an application running on an instance can call Oracle Cloud Infrastructure public services, removing the need to configure user credentials or a configuration file.

## Concepts
DYNAMIC GROUP Dynamic groups allow you to group Oracle Cloud Infrastructure instances as principal actors, similar to user groups. You can then create policies to permit instances in these groups to make API calls against Oracle Cloud Infrastructure services. Membership in the group is determined by a set of criteria you define, called matching rules . MATCHING RULE When you set up a dynamic group, you also define the rules for membership in the group. Resources that match the rule criteria are members of the dynamic group. Matching rules have a specific syntax you follow. See[Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Writing). INSTANCE PRINCIPALS The IAM service feature that enables instances to be authorized actors (or principals) to perform actions on service resources. Each compute instance has its own identity, and it authenticates using the certificates that are added to it. These certificates are automatically created, assigned to instances and rotated, preventing the need for you to distribute credentials to your hosts and rotate them.

## Security Considerations

Any user who has access to the instance (who can SSH to the instance), automatically inherits the privileges granted to the instance. Before you grant permissions to an instance using this procedure, ensure that you know who can access it, and that they should be authorized with the permissions you are granting to the instance.

All compute instance principals are granted the`compartment_inspect`permission. You cannot revoke this permission. This permission allows the instance to ListCompartments in the tenancy to retrieve the following information:
- Compartment names
- Compartment descriptions
- [Free-form tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm)applied to compartments
- [Automatic tag defaults](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingautomaticdefaulttags.htm)applied to compartments. These tags, such as CreatedBy and CreatedOn, are in the Oracle-Tag namespace and are automatically added by Oracle.

## Process Overview

The following steps summarize the process flow for setting up and using instances as principals. The subsequent sections provide more details.
- 

Create a[dynamic group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Managing_Dynamic_Groups). In the dynamic group definition, you provide the matching rules to specify which instances you want to allow to make API calls against services.
- 

Create a policy granting permissions to the dynamic group to access services in your tenancy (or compartment).
- 

A developer in your organization configures the application built using the Oracle Cloud Infrastructure SDK to authenticate using the instance principals provider. The developer deploys the application and the SDK to all the instances that belong to the dynamic group.
- 

The deployed SDK makes calls to Oracle Cloud Infrastructure APIs as allowed by the policy (without needing to configure API credentials).
- 

For each API call made by an instance, the[Audit service](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)logs the event, recording the OCID of the instance as the value of`principalId`in the event log. See[Contents of an Audit Log Event](https://docs.oracle.com/iaas/Content/Audit/Reference/logeventreference.htm)for more information.

## Steps to Enable Instances to Call Services

Perform these tasks to enable an instance to call services:

[Create a Dynamic Group and Matching Rules](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#Creating)

[Write Policies for Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#Writing)

[Configure the SDK, CLI, or Terraform](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#Configur)

### Creating a Dynamic Group and Matching Rules

See[Managing Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Managing_Dynamic_Groups).

### Writing Policies for Dynamic Groups

After you have created a dynamic group, you need to create policies to permit the dynamic groups to access Oracle Cloud Infrastructure services.

Policy for dynamic groups follows the syntax described in[How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/policies.htm#How_Policies_Work). Review that topic to understand basic policy features.

The syntax to permit a dynamic group access to resources in a compartment is:
```

```

The syntax to permit a dynamic group access to a tenancy is:
```

```

Here are a few example policies:

To allow a dynamic group (FrontEnd) to use a load balancer in a specific compartment (ProjectA):
```

```

To allow a dynamic group to launch instances in a specific compartment:
```

```

For more sample policies, see[Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/commonpolicies.htm#top).

## Configuring the SDK, CLI, or Terraform

For information about SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

### For the SDK for Java:

In your SDK for Java, create an`InstancePrincipalsAuthenticationDetailsProvider`object. For example:

```

```

### For the SDK for Python:

In your SDK for Python, create an`oci.auth.signers.InstancePrincipalsSecurityTokenSigner`object. For example:

```

```

To refresh the token without waiting, use the following command:
```

```

### Enabling Instance Principal Authorization for the CLI

To enable instance principal authorization from the CLI, you can set the authorization option (`auth`) for a command. For example:

```

```

You also can set the following environment variable:
```

```

If both are set, the value set for`auth`takes precedence over the environment variable.

For information about using the CLI, see[Working with the Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### Enabling Instance Principal Authorization for Terraform

To enable instance principal authorization in Terraform, you can set the`auth`attribute to "InstancePrincipal" in the provider definition as shown in the following sample:

```

```

Note that when you use instance principal authorization you do not need to include the`tenancy_ocid`,`user_ocid`,`fingerprint`, and`private_key_path`attributes.

## FAQs

[How do I query the instance metadata service to query the certificate on the instance?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

Use this curl command:`curl http://169.254.169.254/opc/v1/identity/cert.pem`

[How frequently is the certificate rotated on each instance?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

The certificate is rotated multiple times each day.

[What happens if I receive a 401-Not Authenticated error?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

If you receive a 401-Not Authenticated error, check the following issues:
- Try to run the command again. Sometimes the certificate rotation and the request occur at the same time.
- The certificate might be expired. Verify the certificate is valid.

[Can I change the frequency at which the certificate is rotated?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

No. You can't change the frequency at which the certificate is rotated. However, you can change the policy on the dynamic group. If you think an instance has been compromised, you can either change the policy on the dynamic group to revoke permissions for all members of the group, or you can remove the instance from the dynamic group. See[Can I remove an instance from a dynamic group?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#Can)

[What happens if the certificate is rotated in the middle of a long running operation?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

The token expiration is independent of the certificate expiration period. And, it also depends on the application you are interacting with. For example, if Object Storage does not have a multipart PUT operation, then it does not matter how long the operation runs.

[Are the certificates accessible for all users on an instance?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

Yes. Ensure that only users who should be granted the access that you have granted to the dynamic group, have access to the instance.

[Are dynamic groups created at the tenancy level?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

Yes.

[Can I remove an instance from a dynamic group?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

Yes. You can remove it by modifying the matching rule to exclude it. See below for an example.

[Can I exclude specific instances in a compartment from the dynamic group?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#)

Yes. For example, assume you want to exclude two specific instances in a compartment from the dynamic group. Write a matching rule like this:
```

```
