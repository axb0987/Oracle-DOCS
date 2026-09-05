# Securing OCI Control Center
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/occ_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing OCI Control Center

This topic provides security information and recommendations for Oracle Cloud Infrastructure's Control Center service.

## Security Responsibilities

To use OCI Control Center securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all of the services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibility includes the following area:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure OCI Control Center in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/occ_security.htm#iam-policies)

## Routine Security Tasks

OCI Control Center does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to OCI Control Center.

A policy specifies who can access OCI Control Center resources and how. For more information, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For more information about OCI Control Center policies and to view more examples, see[Control Center Policies](https://docs.oracle.com/iaas/Content/control-center/policies-permissions.htm).

## Data Encryption

OCI Control Center uses standard Oracle Cloud Infrastructure encryption for all data stored at rest in the service. No configuration is necessary.

OCI Control Center does not use Vault keys. Internally, OCI Control Center stores data in an Autonomous AI Database that uses Vault keys. Oracle manages and secures these resources.

## Data Durability
