# Securing API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/apigw_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing API Gateway

This topic provides security information and recommendations for API Gateway.

## Security Responsibilities

To use API Gateway securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure API Gateway in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/apigw_security.htm#apigw_iam-policies)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/apigw_security.htm#apigw_network-security)

## IAM Policies

Use policies to limit access to API Gateway.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For information about API Gateway policies, see[Create Policies to Control Access to Network and API Gateway-Related Resources](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm).

## Network Security

Secure network access to your resources in API Gateway.

For information about API Gateway network security, see[Create Policies to Control Access to Network and API Gateway-Related Resources](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm)
