# Security Services
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm
- Fetched: 2026-09-05 03:04 CDT

# Security Services

Learn about the security services in Oracle Cloud Infrastructure that provide customer isolation, identity management, authorization, data encryption, vulnerability detection, monitoring, and more.

The following diagram illustrates the security services in Oracle Cloud Infrastructure.  
  

## Regions and Availability Domains

An Oracle Cloud Infrastructure region is the top-level component of the infrastructure. Each region is a separate geographic area with multiple, fault-isolated locations called availability domains. An availability domain is a subcomponent of a region and is independent and highly reliable. Each availability domain is built with fully independent infrastructure: buildings, power generators, cooling equipment, and network connectivity. With physical separation comes protection against natural and other disasters.

Availability domains within the same region are connected by a secure, high-speed, low-latency network, which allows you to build and run highly reliable applications and workloads with minimum impact to application latency and performance. All links between availability domains are encrypted.

For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Oracle Cloud Infrastructure also offers regions with specific characteristics to meet the security and compliance requirements of government organizations:
- [Oracle Cloud Infrastructure US Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govoverview.htm)
- [https://docs.oracle.com/iaas/Content/General/Concepts/govuksouth.htm](https://docs.oracle.com/iaas/Content/General/Concepts/govuksouth.htm)

## Identity and Access Management (IAM)
  
  

The Oracle Cloud Infrastructure Identity and Access Management service provides authentication and authorization for all Oracle Cloud Infrastructure resources and services. You can use a single tenancy shared by various business units, teams, and individuals while maintaining security, isolation, and governance.

IAM uses the components described in this section. To better understand how the components fit together, see[Example Scenario](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#Example). COMPARTMENT A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes of measuring usage and billing, access (through the use of policies), and isolation (separating the resources for one project or business unit from another). A common approach is to create a compartment for each major part of your organization. For more information, see[Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm). DYNAMIC GROUPS A special type of group that contains resources (such as compute instances) that match rules that you define (thus the membership can change dynamically as matching resources are created or deleted). These instances act as "principal" actors and can make API calls to services according to policies that you write for the dynamic group. FEDERATION A relationship that an administrator configures between an identity provider and a service provider. When you federate Oracle Cloud Infrastructure with an identity provider, you manage users and groups in the identity provider. You manage authorization in Oracle Cloud Infrastructure's IAM service. GROUP A collection of users who share a similar set of access privileges. Administrators can grant access policies that authorize a group to consume or manage resources within a tenancy. All users in a group inherit the same set of privileges. HOME REGION The region where your IAM resources reside. All IAM resources are global and available across all regions, but the master set of definitions reside in a single region, the home region. You must make changes to your IAM resources in your home region. The changes will be automatically propagated to all regions. For more information, see[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm). IDENTITY DOMAIN

An identity domain is a container for managing users and roles, federating and provisioning of users, secure application integration through Oracle Single Sign-On (SSO) configuration, and OAuth administration. It represents a user population in Oracle Cloud Infrastructure and its associated configurations and security settings (such as MFA). IDENTITY PROVIDER A trusted relationship with a federated identity provider. Federated users who attempt to authenticate to the Oracle Cloud Infrastructure console are redirected to the configured identity provider. After successfully authenticating, federated users can manage Oracle Cloud Infrastructure resources in the console just like a native IAM user. MFA Multifactor Authentication (MFA) is a method of authentication that requires the use of more than one factor to verify a user's identity. NETWORK SOURCE A group of IP addresses that is allowed to access resources in your tenancy. The IP addresses can be public IP addresses or IP addresses from a VCN within your tenancy. After you create the network source, you use policy to restrict access to only requests that originate from the IPs in the network source. RESOURCE A cloud object that you create and use when interacting with Oracle Cloud Infrastructure services. For example, compute instances , block storage volumes , virtual cloud networks ( VCNs ), subnets, databases, third-party applications, Software-as-a-Service (SaaS) applications, on-premises software, and retail web applications. ROLE A set of administrative privileges that can be assigned to a user in an identity domain. SECURITY POLICY A document that specifies who can access which resources, and how. You can write policies to control access to all of the[services](https://docs.oracle.com/iaas/Content/services.htm)within Oracle Cloud Infrastructure. Access is granted at the group and compartment level, which means you can write a policy that gives a group a specific type of access within a specific compartment, or to the tenancy itself. If you give a group access to the tenancy, the group automatically gets the same type of access to all the compartments inside the tenancy. For more information, see[Example Scenario](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm#Example)and[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm). The word "policy" is used by people in different ways: to mean an individual statement written in the policy language; to mean a collection of statements in a single, named "policy" document (which has an Oracle Cloud ID (OCID) assigned to it); and to mean the overall body of policies your organization uses to control access to resources. When you apply a policy, there might be a slight delay before the policy is effective. SIGN-ON POLICY A sign-on policy allows identity domain administrators, security administrators, and application administrators to define criteria that determine whether to allow a user to sign in to an identity domain. TAGS Tags allow you to organize resources across multiple compartments for reporting purposes or for taking bulk actions. TENANCY The root compartment that contains all your organization's Oracle Cloud Infrastructure resources. Oracle automatically creates your company's tenancy for you. Directly within the tenancy are your IAM entities (users, groups, compartments, and some policies; you can also put policies into compartments inside the tenancy). You place the other types of cloud resources (for example, instances, virtual networks, block storage volumes, etc.) inside the compartments that you create. Tenancy administrators can create users and groups and assign them least-privileged access to resources that are partitioned into compartments. USER An individual employee or system that needs to manage or use your company's Oracle Cloud Infrastructure resources. Users might need to launch instances, manage remote disks, work with your virtual cloud network, etc. End users of your application aren't typically IAM users. Users have one or more IAM credentials (see[User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm)).

### Compartments

A compartment is a group of resources that can be managed as a single logical unit, providing a streamlined way to manage large infrastructure. For example, you can create a compartment`HR-Compartment`to host a specific set of cloud networks, compute instances, storage volumes, and databases necessary for its HR applications.

Use compartments to clearly separate resources for one project or business unit from another project or business unit. A common approach is to create a compartment for each major part of an organization.

### Credentials

Each user has one or more credentials to authenticate themselves to Oracle Cloud Infrastructure. Users can generate and rotate their own credentials. In addition, a tenancy security administrator can reset credentials for any user within their tenancy.
- Console password: Used to authenticate a user to the Oracle Cloud Infrastructure Console.
- API key: All API calls are signed using a user-specific 2048-bit RSA private key. The user creates a public key pair, and uploads the public key in the Console.
- Auth token: Auth tokens are Oracle-generated token strings that you can use to authenticate with third-party APIs that do no support Oracle Cloud Infrastructure's signature-based authentication. For example, use an auth token to authenticate with a Swift client. To ensure sufficient complexity, the IAM service creates the token and you can't provide one.
- Customer secret key: Used by Amazon S3 clients to access the Object Storage service's S3-compatible API. To ensure sufficient complexity, the IAM service creates this password and you can't provide one.

Oracle Cloud Infrastructure supports federation with Microsoft Active Directory, Microsoft Azure Active Directory, and other identity providers that support the Security Assertion Markup Language (SAML) 2.0 protocol. Federated groups are mapped to native IAM groups, which determine the permissions of a federated user.

### Identity Domains

If Oracle Cloud Infrastructure upgraded your tenancy's home region, you can also create identity domains in the tenancy. An identity domain is a container for managing users and groups, federating and provisioning users, configuring single sign-on (SSO), and configuring OAuth. Each tenancy includes a default identity domain. See[Do You Have Access to Identity Domains?](https://docs.oracle.com/iaas/Content/Identity/getstarted/identity-domains.htm#identity_documentation__updated-identity-domains)

Use multiple identity domains in your tenancy if, for example, the security standards in your organization:
- Prevent development user IDs from existing in the production environments
- Require different administrators to have control over different user environments

Identity domains support OpenID Connect and OAuth to deliver a highly scalable, multi-tenant token service for securing programmatic access to custom applications from other custom applications.
- Use OAuth 2.0 to define authorization for your custom applications. The OAuth 2.0 framework is commonly used for third-party authorization requests with consent. Custom applications can implement both two-legged and three-legged OAuth flows.
- Use OpenID Connect to externalize authentication for your custom applications. OpenID Connect has an authentication protocol that provides federated SSO, using the OAuth 2.0 authorization framework as a way to federate identities in the cloud. Custom applications participate in an Open ID Connect flow.

### Policies

All customer calls to access Oracle Cloud Infrastructure resources are first authenticated by the IAM service (or federated provider) and then authorized based on IAM policies. You can create a policy that gives a set of users permission to access the infrastructure resources (network, compute, storage, and so on) within a compartment in the tenancy. These policies are flexible and are written in a human-readable form that is easy to understand and audit. A policy contains one or more policy statements that follow this syntax:
```

```

The following example policy enables the`GroupAdmins`group to create, update, or delete any groups:
```

```

The following example policy enables the`TestNetworkAdmins`group to create, update, or delete any networks in the`TestCompartment`compartment:
```

```

For more information, see:
- [Overview of IAM](https://docs.oracle.com/iaas/Content/Identity/getstarted/identity-domains.htm)
- [IAM Identity Domain Types](https://docs.oracle.com/iaas/Content/Identity/sku/overview.htm)
- [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)
- [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm)
- [IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)
- [User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm)
- [Federating with Identity Providers](https://docs.oracle.com/iaas/Content/Identity/federating/federating_section.htm)
- [Securing IAM](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/iam_security.htm)

## Cloud Guard
  
  

Use Cloud Guard to examine your Oracle Cloud Infrastructure resources for security weakness related to configuration, and to examine your operators and users for risky activities. Upon detection, Cloud Guard suggests corrective actions, and can be configured to automatically take certain actions. For example:
- Detect an instance that is publicly accessible (has a public IP address or is on a public subnet ) and stop the instance.
- Detect an Object Storage bucket that is publicly accessible and disable the bucket.
- Detect a user login from a suspicious IP address and restrict traffic from this address.
- Detect user activities that could indicate a compromised account or an insider threat.

Oracle recommends that you enable Cloud Guard in your tenancy. You can configure a Cloud Guard target to examine your entire tenancy (root compartment and all subcompartments), or you can configure targets to check only specific compartments .

Each target is associated with detector recipes, which define specific user actions or resource configurations that cause Cloud Guard to report a problem. Oracle provides several default Cloud Guard detector recipes, which you can use as-is or customize as needed. For example, you might want to change the risk level or settings associated with certain detector rules. As Cloud Guard adds new detector rules, they are automatically enabled in Oracle-managed recipes, and disabled in custom recipes.

The Threat Detector recipe in Cloud Guard contains a set of rules designed specifically to detect subtle patterns of activity in your tenancy that could eventually pose a security problem.

A Cloud Guard responder recipe defines the action or set of actions to take in response to a problem that a detector has identified. You can also use the Events and Notifications services to send notifications whenever Cloud Guard detects a type of problem for which you want to be notified. You can send notifications through email or Slack, or run custom code in the Functions service.

For more information, see[Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/home.htm).

## Vulnerability Scanning
  
  

Oracle Cloud Infrastructure Vulnerability Scanning Service helps improve your security posture by routinely checking compute instances and container images for potential vulnerabilities. The service generates reports with metrics and details about these vulnerabilities, and assigns each a risk level. For example:
- Ports that are unintentionally left open might be a potential attack vector to your cloud resources, or enable hackers to exploit other vulnerabilities.
- OS packages that require updates and patches to address vulnerabilities
- OS configurations that hackers might exploit
- Industry-standard benchmarks published by the[Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/)(CIS) for the target OS

You can also monitor these vulnerabilities in[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Cloud_Guard). Upon detection of a vulnerability, Cloud Guard suggests corrective actions, and can be configured to automatically take certain actions.

For more information, see[Scanning Overview](https://docs.oracle.com/iaas/Content/scanning/using/overview.htm).

## Security Zones
  
  

Security Zones let you be confident that your Compute, Networking, Object Storage, Database, and other resources comply with Oracle security principles and best practices. A security zone is associated with one or more compartments and a security zone recipe. When you create and update resources in a security zone, Oracle Cloud Infrastructure validates these operations against security zone policies in the zone's recipe. If any security zone policy is violated, then the operation is denied.

Here are some examples of security zone policies:
- Subnets in a security zone can't be public. All subnets must be private.
- The boot volume for a compute instance in a security zone must also be in a security zone.
- Object Storage buckets in a security zone must use a customer-managed master encryption key.
- You can't move certain resources like block volumes and compute instances from a security zone to a standard compartment.

You must enable Cloud Guard before you create security zones. Cloud Guard helps you detect policy violations in existing resources that were created before the security zone.

For more information, see[Overview of Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/security-zones.htm).

## Vault

You can use the Vault service to create and manage the following resources:
- Vaults
- Keys
- Secrets

A vault includes the encryption keys and secret credentials that you use to protect your data and connect to secured resources. As customer-managed resources, you have complete control over who has access to your vaults, keys, and secrets. You also control what authorized users and services can do with Vault resources. Levels of access might range from something as granular as whether an individual key can be used by a particular service to more broadly impactful lifecycle management activities, like whether a user can delete a key from a vault to prevent its use altogether.

Keys are stored on highly available and durable hardware security modules (HSM) that meet Federal Information Processing Standards (FIPS) 140-2 Security Level 3 security certification. Secrets and secret versions are base64-encoded and encrypted with master encryption keys, but do not reside within the HSM.

The key encryption algorithms that the Vault service supports includes the Advanced Encryption Standard (AES), the Rivest-Shamir-Adleman (RSA) algorithm, and the elliptic curve digital signature algorithm (ECDSA). You can create and use AES symmetric keys and RSA asymmetric keys for encryption and decryption. You can also use RSA or ECDSA asymmetric keys for signing digital messages.

[Security zone policies](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Zones_Service)require you to encrypt resources using customer-managed keys where possible. The following services support the use of customer-managed keys for resource encryption:
- Block Volume
- Kubernetes Engine
- Oracle Cloud Infrastructure Database
- File Storage
- Object Storage
- Streaming

For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).

## Security Advisor

Security Advisor helps you create cloud resources that align with Oracle's security principles and best practices. It also ensures that your resources meet the requirements enforced by[security zone policies](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Zones_Service). For example, you can quickly create resources that are encrypted with a customer-managed master encryption key using the[Vault](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Vault_Service)service.

For example, you can use Security Advisor to create the following resources:
- Object Storage bucket
- File Storage file system
- Compute instance (Compute) (and associated boot volume)
- Block Volume block storage volume

For more information, see[Overview of Security Advisor](https://docs.oracle.com/iaas/Content/SecurityAdvisor/Concepts/securityadvisoroverview.htm).

## Bastion

Oracle Cloud Infrastructure Bastion provides restricted and time-limited access to target resources that don't have public endpoints.  
  

Through the configuration of a bastion, you can let authorized users connect to target resources on private endpoints by way of Secure Shell (SSH) sessions. When connected, users can interact with the target resource by using any software or protocol supported by SSH. For example, you can issue Remote Desktop Protocol (RDP) commands or connect to a database by using Oracle Net Services. Targets can include resources like compute instances , DB systems , and Autonomous AI Transaction Processing databases.

Bastions reside in a public subnet and establish the network infrastructure needed to connect a user to a target resource in a private subnet . Integration with the IAM service provides user authentication and authorization. Bastions provide an extra layer of security by allowing you to specify what IP addresses can connect to a session hosted by the bastion.

For more information, see[Bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm).

## Threat Intelligence

Oracle Cloud Infrastructure Threat Intelligence aggregates threat intelligence data across many different sources and curates this data to provide actionable guidance for threat detection and prevention in Oracle Cloud Guard and other Oracle Cloud Infrastructure services.

Malicious actors often use known techniques to attack target environments. Contextual information about the threat indicators found in your environment can help you prioritize alerts and understand your threat landscape. Threat Intelligence provides insights from elite Oracle security researchers, our own unique telemetry, industry-standard open source feeds, and third-party partners.

When the Threat Detector recipe is enabled in Cloud Guard, it compares data from Threat Intelligence to your Audit logs and telemetry to detect suspicious activity and report it as a problem.

For more information, see[Threat Intelligence Overview](https://docs.oracle.com/iaas/Content/threat-intel/using/overview.htm).

## Web Application Firewall

Oracle Cloud Infrastructure Web Application Firewall (WAF) is a cloud-based, Payment Card Industry (PCI) compliant, security service that protects applications from malicious and unwanted internet traffic. WAF can protect any internet-facing endpoint, providing consistent rule enforcement across your applications.

Use WAF to create and manage protection rules for internet threats including Cross-Site Scripting (XSS), SQL Injection, and other OWASP-defined vulnerabilities. Unwanted bots can be mitigated while desirable bots are allowed to enter. You can also define and apply custom protection rules to your WAF configurations using the ModSecurity Rule Language.

Use WAF to create access rules that define explicit actions for requests that meet various conditions. For example, access rules can limit requests based on the geography or the signature of the request. A rule action can be set to log and allow, detect, block, redirect, bypass, or show a CAPTCHA for all requests that match the conditions.

For more information, see[Overview of Web Application Firewall](https://docs.oracle.com/iaas/Content/WAF/Concepts/overview.htm).

## Audit

The Oracle Cloud Infrastructure Audit service records all API calls to resources in a customer's tenancy and login activity from the Console. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Oracle Cloud Infrastructure Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request.

For more information, see[Overview of Audit](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)
