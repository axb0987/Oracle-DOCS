# Security Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_overview.htm
- Fetched: 2026-09-05 03:04 CDT

# Security Overview

Oracle's cloud infrastructure and services provide effective and manageable security that enables you to run your mission-critical workloads and to store your data with confidence.

Oracle Cloud Infrastructure (OCI) security is based on the following core pillars. For each pillar, OCI has multiple solutions that maximize the security and compliance of the cloud platform. CUSTOMER ISOLATION Lets you deploy your application and data assets in an environment that is fully isolated from other tenants and from Oracle staff. DATA ENCRYPTION Protects your data at-rest and in-transit to help meet your security and compliance requirements for cryptographic algorithms and key management. SECURITY CONTROLS Limits access to your services and segregates operational responsibilities to reduce the risk associated with malicious and accidental user actions. VISIBILITY Provides comprehensive log data and security analytics to audit and monitor actions on your resources. This visibility enables you to meet your audit requirements and reduce operational risk. SECURE HYBRID CLOUD Lets you use your existing security assets, such as user accounts and policies. Lets you use third-party security solutions when accessing your cloud resources and securing your data and application assets in the cloud. HIGH AVAILABILITY Provides fault-independent data centers that enable highly available, scalable architectures and are resilient against network attacks. VERIFIABLY SECURE INFRASTRUCTURE Follows rigorous processes and uses effective security controls in all phases of cloud service development and operation. OCI adheres to Oracle's strict security standards through third-party audits, certifications, and attestations. Our secure infrastructure helps you demonstrate compliance readiness to internal security and compliance teams, customers, auditors, and regulators.

Oracle also employs some of the world's experts in information, database, application, infrastructure, and network security. When you use OCI, you directly benefit from our deep expertise and continuous investments in security.

## Basic Security Considerations

The following principles are fundamental to using any application securely. Follow them as you plan, develop, deploy, and run your resources in Oracle Cloud Infrastructure.
- Keep software up to date. Use the latest product release and any patches that apply to it.
- Limit privileges as much as possible. Give users only the access necessary to perform their work. Review user privileges periodically to determine relevance to current work requirements.
- Monitor system activity. Establish who is expected to access which system components and the frequency of access, and then monitor those components.
- Learn about and use the Oracle Cloud Infrastructure security features. For more information, see[Security Services](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm).
- Use secure best practices. For more information, see[Security Best Practices](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/configuration_security.htm).
- Keep up to date on security information. Oracle regularly issues security-related patch updates and security alerts. Install all security patches as soon as possible. See the[Critical Patch Updates and Security Alerts](http://www.oracle.com/technetwork/topics/security/alerts-086861.html)website.

## Basic Resource Protection

As you plan your Oracle Cloud Infrastructure deployment, consider which resources need to be protected, how much access to grant to those resources, and the impact of security failure to those resources.

### Which resources must be protected?
- Customer data, such as credit card numbers
- Internal data, such as proprietary source code
- System components (protected from external attacks or intentional system overloads)

### Who are you protecting data from?

Analyze your workflows to determine who needs access to what data. For example, you must protect your subscribers' data from other subscribers, but someone in your organization needs to access that data to manage it.

Consider carefully how much access to give a system administrator. A system administrator might be able to manage your system components without needing to access the system data.

### What happens if protections on a strategic resource fail?

Sometimes, a fault in your security scheme is just an inconvenience. At other times, a fault might damage you or your customers. Understanding the security ramifications of each resource helps you protect it.

## Shared Security Model

Security in Oracle Cloud Infrastructure is a shared responsibility between you and Oracle. We use best-in-class security technology and operational processes to secure our cloud services. However, for you to securely run your workloads in OCI, you must know your security and compliance responsibilities.

In a shared, multi-tenant compute environment, we're responsible for the security of the underlying cloud infrastructure (such as data center facilities, and hardware and software systems). You're responsible for securing your workloads and securely configuring your cloud resources (such as compute, network, storage, and database).

In a fully isolated, single-tenant, bare metal server with no Oracle software on it, your responsibility increases because you own the entire software stack (operating systems and above) on which you deploy your applications. In this environment, you're responsible for the following tasks:
- Securing your workloads
- Securely configuring your services (compute, network, storage, database)
- Ensuring that the software components that you run on the bare metal servers are securely configured, deployed, patched, and managed

Specifically, your responsibilities and Oracle's responsibilities can be divided into the following areas.

### Identity and Access Management (IAM)

You're responsible for protecting your cloud access credentials and setting up individual user accounts. You are also responsible for managing and reviewing access for your own employee accounts and for all activities that occur under your tenancy.

Oracle is responsible for providing effective IAM services such as identity management, authentication, authorization, and auditing.

### Workload Security

You're responsible for protecting and securing the operating system and application layers of your compute instances from attacks and compromises. This protection includes patching applications and operating systems, configuring operating systems, and protecting against malware and network attacks.

Oracle is responsible for providing secure images that are hardened and have the latest patches. Oracle also lets you to use the same third-party security solutions that you already use on-premises.

### Data Classification and Compliance

You're responsible for correctly classifying and labeling your data and meeting any compliance obligations. You're also responsible for auditing your solutions to ensure that they meet your compliance obligations.

### Host Infrastructure Security

You're responsible for securely configuring and managing your compute (virtual hosts, containers), storage (object, file, local storage, block volumes), and platform (database configuration) services.

Oracle shares responsibility with you to ensure that the service is optimally configured and secured. This responsibility includes hypervisor security and the configuration of permissions and network access controls.

### Network Security

You're responsible for securely configuring network elements such as virtual networking, load balancing, DNS, and gateways. You ensure that hosts can communicate correctly and that devices can attach or mount the correct storage devices.

Oracle is responsible for providing a secure network infrastructure. L3/4 DDoS protection is included with all Oracle Cloud Infrastructure accounts and no configuration or monitoring is required.

### Client and Endpoint Protection

Your enterprise uses various hardware and software systems, such as mobile devices and browsers, to access your cloud resources. You're responsible for securing all clients and endpoints that you allow to access OCI services.

### Physical Security

Oracle is responsible for protecting the global infrastructure that runs services offered in OCI. This infrastructure consists of hardware, software, networking, and facilities.

## Infrastructure Security Model

Oracle Cloud Infrastructure's security model is built around people, processes, tools, and a common security "platform" of methodologies and approaches from which we build our products.

We apply this model to the following core security components that we use to protect and secure our customers and business: security culture, security design and controls, secure software development, personnel security, physical security, and security operations.

### Security Culture

A security-first culture is vital to building a security-minded organization. All OCI team members understand the role that security plays in our business, and they are actively engaged in managing and improving our products' security posture. We have also implemented the following mechanisms to help us create and maintain a security-aware culture:
- Security-minded leadership: Senior leadership is actively involved in security planning, monitoring, and management. We define and measure ourselves against security metrics and include security as a component in team evaluation processes.
- Embedded expertise: Security team members work closely with product development teams. This approach enables our security organization to build a deep understanding of product-development processes and system architectures. This approach also helps teams solve security challenges quickly and drive security initiatives more effectively.
- Common security standards: We integrate security into our products and operations. For example, we establish a security standards baseline. This baseline provides a single security point of reference and establishes clear and actionable guidelines. We frequently update this baseline to incorporate learned lessons and reflect emerging business factors. We also create support materials to help our teams implement security controls. These materials include reference architectures, implementation guides, and access to security experts.
- Openness, constructive debate, and encouraged escalation: Security issues can be addressed only when the people who can fix them are aware of them. We encourage escalation, and we work to create an environment in which raising issues early and often is rewarded.
- Security training awareness: We maintain robust security and awareness training programs that reinforce our security culture. We require in-depth security training sessions for all new employees and annual refresher trainings. We also provide security training that is tailored to specific job roles. All our software developers attend secure development training that establishes baseline security requirements for product development and provides best practices. We also provide engaging and innovative forms of security awareness training, such as guest speakers and interactive forums.

### Security Designs and Controls

We integrate security into our cloud products and operations through a centralized methodology. This methodology defines our approach for several core security areas, and together these areas form the security foundation from which we build our products. This approach helps us apply best practices and lessons learned from one product across the business, thus raising the security of all our products.
- User authentication and access control: A least-privilege approach is used to grant access to production systems. Approved lists of service team members are periodically reviewed to revoke access when the need cannot be justified. Access to production systems also requires multifactor authentication (MFA). The security team grants MFA tokens, and the tokens of inactive members are disabled. All access to production systems is logged, and the logs are stored for security analysis.
- Change management: We follow a rigorous change management and deployment process that uses proprietary testing and deployment tools. All changes deployed in our production environment are tested and approved before they are released. This process ensures that changes operate as intended and can be rolled back to a previous state to recover gracefully from bugs or operational issues. We also track the integrity of critical system configurations to ensure that they align with the expected state.
- Vulnerability management: We use internal penetration testing teams and external industry experts to help us identify potential vulnerabilities in our products. These experts help us improve the security of our products, and we work to incorporate the lessons that we learn into our future development work. We also periodically scan OCI hosts for vulnerabilities by using industry-standard scanners. We determine whether the scan results apply to the OCI environment, and product teams apply required patches as needed.
- Incident response: We have strong processes and mechanisms to enable us to respond to and address incidents as they arise. Incident response teams are ready to detect and respond to events 24/7. Critical staff members carry paging devices so we can call on the expertise needed to resolve issues.

We also have a process to help us learn from our incidents. We perform root cause analysis through our Corrective Action/Preventative Action (CAPA) process. CAPAs help us discover process gaps and changes that we can make after an incident occurs. CAPAs are a common language that we can use to reflect on an issue and capture steps to improve future operational readiness. CAPAs contain the root cause of an issue, what is required to contain or fix the issue, and what steps we must take to ensure that the issue does not recur. Our leadership team reviews all CAPAs, looks for cross-organizational applications for learned lessons, and ensures that actions are implemented in a timely manner.
- Security logging and monitoring: We have automated mechanisms for logging security-relevant events (for example, API calls and network events) in the infrastructure, and for monitoring the logs for anomalous behavior. The security team tracks and triages the alerts generated by monitoring mechanisms.
- Network security: By default, customer communications with OCI services use the latest Transport Layer Security (TLS) ciphers and configuration to secure customer data in transit, and to prevent any man-in-the-middle attacks. As a further defense, customer commands to the services are digitally signed by using public keys to prevent any tampering. The services also deploy industry-leading tools and mechanisms to mitigate distributed denial of service (DDoS) attacks and maintain high availability.
- Control plane security: OCI backend (control plane) hosts are securely isolated from customer instances by using network access control lists (ACLs). Your instances are provisioned and managed by software agents that must interact with the backend hosts. Only authenticated and authorized software agents can successfully interact with these backend hosts. For these hosts, pre-production environments (for example, development, testing, and integration) are separated from production environments so that any development and test activities do not impact production systems.
- Server security and media management: Our hardware security team is responsible for designing and testing the security of the hardware used to deliver OCI services. This team works with our supply chain and tests hardware components to validate them against rigorous OCI hardware security standards. This team also works closely with our product development functions to ensure that hardware can be returned to a pristine, safe state after customers release the hardware.
- Secure host wipe and media destruction: OCI instances are securely wiped after customers release the hardware. This secure wipe restores hardware to a pristine state. We have re-engineered the platform with proprietary hardware components that allow us to wipe and reinitialize the hardware in a secure manner. When the underlying hardware has reached end-of-life, the hardware is securely destroyed. Before leaving our data centers, drives are rendered unusable by using industry-leading media destruction devices.

### Secure Software Development

Secure software development requires consistently applied methodologies that conform to clear security objectives and principles. We build security practices into every element of our product development life cycle. We have formal security product development standards that are a roadmap and guide for developers. These standards discuss general security knowledge areas such as design principles and common vulnerabilities, and provide specific guidance on topics such as data validation, data privacy, and user management.

Our secure product development standards evolve and expand over time to address the common issues affecting code, new threats as they are discovered, and new use cases by our customers. The standards incorporate insights and learned lessons; they do not live in isolation, nor are they an "after the fact" addition to software development. They are integral to language-specific standards such as C/C++, Java, PL/SQL, and others, and are a cornerstone of our secure development programs and processes.

Security assurance analysis and testing verify the security qualities of our products against various types of attacks. Two broad categories of tests are used: static analysis and dynamic analysis. These tests fit differently in the product development life cycle and typically find different categories of issues, so they are used together by our product teams.

### Personnel Security

We strive to hire the best, and we invest in our employees. We value training, we require baseline security training for all our employees, and we also require specialized training to keep our teams informed about the latest security technologies, exploits, and methodologies. Our annual corporate training programs cover our information security and privacy programs, among many others. We also engage with various industry groups and send our employees to specialist conferences to collaborate with other industry experts on emerging challenges. The objectives of our security training programs are to help our employees better protect our customers and products, to enable employees to grow in their knowledge areas around security, and to further our mission to attract and retain the best talent.

We hire people with strong ethics and good judgment. Our employees undergo pre-employment screening as permitted by law, including criminal background checks and prior-employment validation. We also use team and employee performance evaluation processes to recognize good performance and help our teams and employees identify opportunities for growth. Security is a component of our team evaluation processes. This approach shows how teams are performing against our security standards and enables us to identify best practices and improvement areas for critical security processes.

### Physical Security

Oracle Cloud Infrastructure data centers are designed for the security and availability of customer data. This design begins with our site selection process. Candidate build sites and provider locations undergo an extensive risk-evaluation process. This process considers the following criteria, among others: environmental threats, power availability and stability, vendor reputation and history, neighboring facility functions (for example, high-risk manufacturing or high-threat targets), and geopolitical issues.

OCI data centers align with Uptime Institute and Telecommunications Industry Association (TIA) ANSI/TIA-942-A Tier 3 or Tier 4 standards and follow a N2 redundancy methodology for critical equipment operation. Data centers housing OCI services use redundant power sources and maintain generator backups to prevent widespread electrical outage. Server rooms are closely monitored for air temperature and humidity, and fire suppression systems are in place. Data center staff are trained in incident response and escalation procedures to address security or availability events that might occur.

Our layered approach to physical security starts with the site build. Data center facilities are durably built with steel, concrete, or comparable materials and are designed to withstand impact from a light vehicle strike. Our sites are staffed with security guards who are ready to respond to incidents 24/7. The exterior of each site is secured with perimeter barriers and vehicles are actively monitored by guards and cameras that cover the building perimeter.

All persons entering our data centers must first go through security at the site entrances, which are staffed with security guards. Persons without site-specific security badges must present government-issued identification and have an approved access request granting them access to the data center building. All employees and visitors must always wear visible, official identification badges. Other security measures between the entrance and server rooms vary depending on the site build and risk profile.

Data center server rooms are built with more security, including cameras that cover the server rooms, two-factor access control, and intrusion-detection mechanisms. Physical barriers are in place to create isolated security zones around server and networking racks that span from the floor (including below the raised floor where applicable) to the ceiling (including above ceiling tiles where applicable).

Access to data centers is carefully controlled and follows a least-privilege access approach. Authorized personnel must approve all access to server rooms and access is granted only for the necessary period. Access usage is audited, and data center leadership periodically reviews access provisioned within the system. Server rooms are isolated into secure zones that are managed on a zone-by-zone basis. Access is provisioned only for those zones required by personnel.

### Security Operations

The Oracle Cloud Infrastructure Security Operations team is responsible for monitoring and securing the unique OCI hosting and virtual networking technologies. This team directly works and trains with the Oracle engineers who develop these technologies.

We monitor emerging internet security threats daily and implement appropriate response and defense plans to address risks to the business. When we determine that urgent changes are recommended and they are in the scope of the customers' responsibilities, we issue security alert bulletins to those customers to ensure their protection.

When a detected or reported security issue affects OCI servers or networks, Security Operations staff is available 24/7 to respond, escalate, or take required corrective action. When necessary, we escalate and coordinate with external parties (including network and hosting service providers, hardware vendors, or law enforcement) to protect OCI, our customers, and our network's security and reputation.

When the Security Operations team responds to a security issue, they act according to our documented process, and all actions are logged according to compliance requirements. Care is always taken to protect the goals of service and data integrity, privacy, and business continuity.

## Customer Data Protection

Customer data protection is critically important. We take steps to meet all legal and compliance requirements regarding data security.

### Data Rights and Ownership

Oracle Cloud Infrastructure customers retain all ownership and intellectual property rights in and to their content. We strive to be transparent with our data protection processes and law enforcement requests that we might receive.

### Data Privacy

OCI has features that help customers align with common data privacy principles. See[Oracle Cloud Infrastructure Privacy Features](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/oci-privacy-features.pdf).

### Law Enforcement Requests

Except as otherwise required by law, Oracle promptly notifies customers of any subpoena, judicial, administrative, or arbitral order of an executive or administrative agency or other governmental authority that it receives and that relates to the personal data that Oracle is processing on the customer's behalf. Upon customer request, Oracle provides customers with reasonable information in its possession relevant to the law enforcement request and any assistance reasonably required for them to respond to the request in a timely manner.

### Compliance

We operate under practices aligned with the ISO/IEC 27002 Code of Practice for information security controls, from which we have identified a comprehensive set of security controls that apply to our business. These security controls and our operations undergo external audits. We pursue a broad suite of industry and government certifications, audits, and regulatory programs. See[Oracle Cloud Compliance](https://www.oracle.com/corporate/cloud-compliance/)
