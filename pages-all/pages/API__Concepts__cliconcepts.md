# Command Line Interface (CLI)
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm
- Fetched: 2026-09-05 01:35 CDT

# Command Line Interface (CLI)

The CLI is a small-footprint tool that you can use on its own or with the Console to complete Oracle Cloud Infrastructure tasks. The CLI provides the same core functionality as the Console, plus additional commands. Some of these, such as the ability to run scripts, extend Console functionality.

Tip  
  

Cloud Shell: The CLI is pre-configured with your credentials and ready to use immediately from within[Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro.htm). For more information on using the CLI from within Cloud Shell, see[Getting Started with Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/devcloudshellgettingstarted.htm#Getting_Started_with_Cloud_Shell).

Oracle Linux Cloud Developer image: The CLI is pre-installed on the Oracle Linux Cloud Developer platform image. For more information, see[Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/oci/developer-image.htm).

Oracle Autonomous Linux: The CLI is pre-installed on Oracle Autonomous Linux versions 7 and 8. For more information, See[Oracle Autonomous Linux Image](https://docs.oracle.com/iaas/oracle-linux/autonomous-linux/index.htm).

This CLI and sample is dual-licensed under the Universal Permissive License 1.0 and the Apache License 2.0; third-party content is separately licensed as described in the code.

The CLI is built on the Oracle Cloud Infrastructure SDK for Python and runs on[Mac, Windows, or Linux](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems). The Python code makes calls to Oracle Cloud Infrastructure APIs to provide the functionality implemented for the various services. These are REST APIs that use HTTPS requests and responses. For more information, see[About the API.](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm)

Installation: See[Quickstart](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/cliinstall.htm).

Reference: You can get immediate help on any CLI command. To get started, run`oci --help`from the command line. You can also view the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). This reference is derived from the APIs and help text in the Python source code.

## Requirements

To install and use the CLI, you must have:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the desired permissions. This account user can be you, another person, or a system that calls the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a list of other typical Oracle Cloud Infrastructure policies, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- A keypair used for signing API requests, with the public key uploaded to Oracle. Only the user calling the API should possess the private key. See[Configuring the CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm).
Note  
  
To use the CLI without a keypair, you can use token-based authentication. For more information, see[Token-based Authentication for the CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/clitoken.htm).
- A[supported version of Python on a supported operating system](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems).
- 

If you require FIPS-compliance, see[Using FIPS-validated Libraries](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/cliconfigure.htm#fips).

### Supported Python Versions and Operating Systems

This table lists the versions of Python supported by the CLI for each OS:

OS Supported Python Versions for CLI
Oracle Linux 8 3.6, 3.9 to 3.13
Oracle Linux 9 3.9 to 3.13
Ubuntu 20.04 3.10 to 3.13
Windows Desktop 10 &amp; 11 3.10 to 3.13
Windows Server (2016/2019/2022) 3.10 to 3.13
Note  
  

We no longer support Oracle Autonomous Linux 7.9, Oracle Linux 7.8 and Oracle Linux 7.9.

Newer versions of Python might not be immediately supported. The CLI might work on unlisted operating systems, but we don't test them for compatibility.

If you use the[CLI installer](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/../SDKDocs/cliinstall.htm)and don't have Python on your machine, the installer offers to automatically install Python for you. If you already have Python installed on your machine, you can use the`python --version`command to find out which version is installed.

## Services Supported

- Access Governance
- AI Data Platform
- AI Language
- AI Speech
- AI Vision
- Analytics Cloud
- Announcements
- API Gateway
- Application Dependency Management
- Application Performance Monitoring
- Audit
- Autonomous Recovery
- Autoscaling (Compute)
- Bastion
- Batch
- Big Data Service
- Blockchain Platform
- Budgets
- Build
- OCI Cache
- Certificates
- Cloud Bridge
- Cloud Guard
- Cloud Migrations
- Cluster Health
- Cluster Placement Groups
- Compute Cloud@Customer
- Compute Instance Agent (Oracle Cloud Agent)
- Connector Hub
- Kubernetes Engine
- Container Instances
- Content Management
- Core Services (Networking, Compute, Block Volume)
- Cost Anomaly Detection
- Data Connectivity Management
- Database Lifecycle Management
- Database Migration
- Data Catalog
- Data Flow
- Data Labeling
- Data Integration
- Data Labeling
- Data Safe
- Data Science
- Database
- Database Management
- Database Tools
- Database Tools Runtime
- Delegate Access Control
- Demand Signal
- DevOps
- Digital Assistant
- Digital Media
- Disaster Recovery
- DNS
- Document Understanding
- Email Delivery
- Enterprise Manager Warehouse
- Events
- Exadata Fleet Update
- File Storage
- File Storage with Lustre
- Fleet Application Management
- Functions
- Fusion Apps as a Service
- Generative AI
- Generative AI Agent
- Generative AI Inference
- Generic Artifacts
- Globally Distributed AI Database
- Golden Gate
- Governance Rules
- Health Checks
- IAM
- Identity Domains
- Integration
- Internet of Things
- Java Management
- Java Management Service Downloads
- Key Management (for the Vault service)
- License Manager
- Limits
- Load Balancer
- Logging
- Log Analytics
- Logging Search
- Logging Ingestion
- Managed Access
- Managed Services for Mac
- Management Agent Cloud
- Management Dashboard
- Marketplace
- Marketplace Private Offer
- Monitoring
- Multicloud
- MySQL HeatWave
- Network Firewall
- Network Load Balancing
- Network Monitoring
- Networking Topology
- NoSQL Database Cloud
- Notifications
- Object Storage
- OCI Control Center
- OCI Registry
- OCI Secure Desktops
- OneSubscription
- Operations Insights
- Operator Access Control
- Optimizer
- Organizations
- OS Management
- OS Management Hub
- PostgreSQL
- Process Automation
- Publisher
- Queue Service
- Quotas
- Resource Analytics
- Resource Manager
- Resource Scheduler
- Search
- Secret Management (for the Vault service)
- Secret Retrieval (for the Vault service)
- Secure Desktops
- Service Catalog
- Service Mesh
- Source Code Management
- Stack Monitoring
- Streaming
- Support Management
- Threat Intelligence
- Usage
- Visual Builder
- VMWare Solution
- Web Application Acceleration and Security
- WebLogic Management
- Work Requests (Compute, Database)
- WebLogic Management

## Contact Us

### Contributions

Got a fix for a bug or a new feature you'd like to contribute? The SDK is open source and[accepting pull requests](https://github.com/oracle/oci-cli/blob/master/CONTRIBUTING.md)on[GitHub](https://github.com/oracle/oci-cli).

### Notifications

To be notified when a new version of the CLI is released, subscribe to the[Atom feed](https://github.com/oracle/oci-cli/releases.atom).

### Questions or Feedback
- [GitHub Issues](https://github.com/oracle/oci-cli/issues): To file bugs and feature requests only
- [Developer Tools section](https://cloudcustomerconnect.oracle.com/resources/9c8fa8f96f/search/posts?find=&daysBack=0&userName=&tagName=Developer+Tools&type=)of the Oracle Cloud forums
- [My Oracle Support](https://support.oracle.com)
