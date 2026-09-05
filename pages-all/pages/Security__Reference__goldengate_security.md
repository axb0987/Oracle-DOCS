# Securing GoldenGate
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/goldengate_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing GoldenGate

This topic provides security information and recommendations for GoldenGate.

Oracle Cloud Infrastructure[GoldenGate](https://docs.oracle.com/iaas/goldengate/index.html)provides a secure and easily to use data replication solution in accordance with industry-leading security best practices.

## Security Responsibilities

To use GoldenGate securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.
- Encryption and Confidentiality: Encryption keys and secrets for GoldenGate are stored in wallets and vaults to protect your data and connect to secured resources.
- Network Security: Encrypted access to the GoldenGate deployment console is enabled over SSL on port 443 only. By default, access to the GoldenGate deployment console is only available from an OCI private endpoint from the customer's private network. Public endpoints can be configured allowing encrypted public access to the GoldenGate deployment console over SSL on port 443.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- GoldenGate Deployment Console Account Management: Access to the GoldenGate deployment console is managed in the OCI console. Accounts and permissions are managed in the GoldenGate deployment console.[Learn more about deployment users](https://docs.oracle.com/en/cloud/paas/goldengate-service/mkmbs/index.html).
- Network Security: You configure network connectivity to sources and targets (OCI GoldenGate database registrations). Ensure that these database registrations are secure and encrypted. Each OCI GoldenGate database registration can be secured using SSL by configuring the proper SSL parameters. See[Managing Database Registrations](http://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/goldengate-service&id=ggs-manage-dbregistration).
- Network Encryption: By default, all network connectivity to OCI GoldenGate is encrypted over SSL with Oracle provided certificates. Ensure that any certificate or encryption keys that you provide are current and valid.
- Auditing of Security Events: The OCI GoldenGate deployment console logs security events. You can access and review this log from the OCI GoldenGate deployment backup. Ensure that you monitor this log regularly.[Learn more about deployment backups](http://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/goldengate-service&id=ggs-deployment-backups).
- Patching: Ensure that OCI GoldenGate deployments are up to date. Updates are released monthly, and you must upgrade to the latest deployment patch level as soon as possible to prevent vulnerabilities.[Learn more about patching deployments](https://docs.oracle.com/en/cloud/paas/goldengate-service/stzee/index.html#articletitle).
- Audit of Remote Access over Load Balancer or Bastion: Ensure auditing of any remote access that is not directly to OCI GoldenGate is enabled and configured appropriately. See[Logging for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Logging.htm)for more information.

## IAM Policies

Use policies to limit access to GoldenGate.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

GoldenGate IAM recommendations:
- Assign least privilege access for IAM users and groups to resource types in`goldengate-family`.
- To minimize loss of data because of inadvertent deletes by an authorized user or malicious deletes, Oracle recommends giving the`GOLDENGATE_DEPLOYMENT_DELETE`and`GOLDENGATE_DATABASE_REGISTRATION_DELETE`permissions to the minimum possible set of IAM users and groups. Give these permissions only to tenancy and compartment administrators.
- GoldenGate only needs`USE`level access to capture data from database registrations.

Example policies:

[Prevent the Deletion of Deployments](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/goldengate_security.htm#)

Create this policy to allow the group`ggs-users`to perform all actions on deployments, except deleting them.
```

```

For more information about creating GoldenGate policies, see[Oracle Cloud Infrastructure GoldenGate Policies](https://docs.oracle.com/en/cloud/paas/goldengate-service/rmrrr/index.html#GUID-6A833E63-D784-4A21-BCB8-8D062870BAB0)
