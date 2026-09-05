# Securing Your Tenancy
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/securing_your_tenancy.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Your Tenancy

Learn how to get started with securing an Oracle Cloud Infrastructure tenancy.

Before your begin, get familiar with the security concepts and features in Oracle Cloud Infrastructure. See:
- [Security Overview](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_overview.htm)
- [Security Services](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_features.htm)
- [Security for Core Services](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_core_services.htm)
- [Security Checklist for Oracle Cloud Infrastructure](https://docs.oracle.com/en/solutions/oci-security-checklist)

In a shared, multi-tenant compute environment, Oracle is responsible for the security of the underlying cloud infrastructure (such as data center facilities, and hardware and software systems). You are responsible for securing your workloads and configuring the security of your services (such as compute, network, storage, and database).

Security of an Oracle Cloud Infrastructure tenancy is based on a combination of factors, all of which must be thought through and securely configured. Take a hierarchical view of security configuration. Start by addressing foundational security issues, and then address the security of specific infrastructure resources. The following steps provide a high-level roadmap for configuring the security of a tenancy.

- Define a security model that meets the workload requirements for your tenancy.

- Number of compartments
- Number of users with administrative rights
- Administrative roles and permissions
- (Optional) Provision identity domains in the IAM service.

Consider creating identity domains if you want to separate different user populations (development and production, for example), or if these user populations require different authentication settings.

See[Do You Have Access to Identity Domains?](https://docs.oracle.com/iaas/Content/HealthChecks/known-issues.htm)and[IAM Identity Domain Types](https://docs.oracle.com/iaas/Content/Identity/sku/overview.htm).
- Provision users, groups, compartments , and policies in the IAM service.

Create mechanisms for authenticating users and authorizing users to access tenancy resources in a least-privilege manner.

See[Securing IAM](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/iam_security.htm).
- (Optional) Provision security zones for hosting cloud resources that must comply with Oracle's security best practices.

If a user attempts to create or update a resource in a security zone, and this operation violates a security zone policy, then the action is denied.

See[Security Zones](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_features.htm#Security_Zones_Service).
- (Optional) Enable Cloud Guard to detect and respond to common security issues.

See[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_features.htm#Cloud_Guard).
- Provision master encryption keys and secret credentials.

See[Vault](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_features.htm#Vault_Service).
- Provision and secure cloud networks.

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . Use private subnets to host resources that do not require internet access.

See[Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/networking_security.htm).
- Provision and secure cloud storage.

Depending on your data storage requirements, your options include[Database](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/dbaas_security.htm),[Block Volume](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/blockstorage_security.htm),[Object Storage](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/objectstorage_security.htm), and[File Storage](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/filestorage_security.htm).

Compliance and regulatory requirements are an important factor in determining an appropriate data storage security architecture.

Refer to the specific service in[Security Best Practices](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/configuration_security.htm).
- Provision and secure the other services in your tenancy that your organization requires.

For example,[Compute](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/compute_security.htm)or[Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/oke_security.htm).

Refer to the specific service in[Security Best Practices](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Reference/configuration_security.htm).
- Periodically review Audit logs to ensure that user actions are in accordance with your initial security configuration.

See[Audit](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_features.htm#Audit_Service).

If you enabled[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Tasks/../Concepts/security_features.htm#Cloud_Guard)
