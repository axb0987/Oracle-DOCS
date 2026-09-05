# Overview of Kubernetes Engine (OKE)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm
- Fetched: 2026-09-05 01:53 CDT

# Overview of Kubernetes Engine (OKE)

Find out about Kubernetes Engine (OKE), which enables you to deploy, manage, and scale containerized applications on Oracle Cloud Infrastructure with flexible node choices, automation, and integrated security.

Oracle Cloud Infrastructure Kubernetes Engine (OKE) is a fully-managed, scalable, and highly available service for deploying containerized applications to the cloud. With OKE, you can build, deploy, and manage cloud-native applications using open source[Kubernetes](https://www.oracle.com/cloud-native/container-engine-kubernetes/what-is-kubernetes)that is certified as conformant by the Cloud Native Computing Foundation (CNCF).

OKE supports a range of deployment options. You can choose to run applications on virtual nodes for serverless operation, on managed nodes for shared responsibility between you and Oracle, or on self-managed nodes when you require advanced customization or specific compute resources, such as GPU or high-performance networking. OKE supports multiple compute shapes, including bare metal and virtual machine types, and enables you to select the configuration that best fits your cost, performance, or hardware needs.

For virtual nodes only, OKE automates critical cluster operations, including scaling, patching, and control plane upgrades. For other node types, OKE provides features for node lifecycle management, add-on software management, safe deletion and replacement of worker nodes, and automatic cluster healing when failures are detected. You can scale pods and clusters vertically and horizontally, and configure clusters to span multiple availability domains or operate in a dedicated region. OKE also supports job scheduling for efficient resource utilization.

You manage clusters through the OCI Console, REST API, and CLI, and you can access Kubernetes clusters using standard Kubernetes tools such as kubectl, the Kubernetes Dashboard, and the Kubernetes API. OKE integrates with other OCI services, including Identity and Access Management (IAM), Container Registry , Storage, and Networking services, as well as CI/CD tools, supporting the creation of complete DevOps pipelines in the cloud.

OKE includes built-in security and compliance features such as data encryption at rest, support for network security groups, private Kubernetes clusters, pod-level isolation, and RBAC integration with OCI IAM. You can use container image scanning and signing, workload identity, and OCI audit services to monitor and protect applications and data.

OKE supports a variety of workloads, including resource-intensive tasks such as artificial intelligence (AI) and machine learning. You can provision and manage large fleets of GPU and CPU nodes, use high-performance cluster networking, and apply Kubernetes autoscaling to adjust to dynamic workloads.

For more information about deploying and managing Kubernetes clusters, along with tutorials and integration guidance, see the related topics in this documentation, and a number of[Developer Tutorials](https://docs.oracle.com/iaas/Content/developer/home.htm#home__kubernetes)that are available.

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

For general information about using the API, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).

## Creating Automation with Events

You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

See[Kubernetes Engine](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#contengevents)for details about OKE resources that emit events.

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

Note that to perform certain operations on clusters created by OKE, you might require additional permissions granted via a Kubernetes RBAC role or clusterrole. See[About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm).

## OKE Capabilities and Limits

Your account type (Monthly Universal Credits, Pay-as-You-Go, Promo) determines the number of clusters you can create in each region that is enabled for your tenancy, and the maximum number of nodes in each cluster. You can[contact us](https://support.oracle.com/)to request an increase to the number of enhanced clusters (but not to the number of basic clusters) that you can create in each region. See[Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Container_Engine_for_Kubernetes_Limits).

You can specify up to 256 pods to run on a single managed node in a node pool in a cluster.

To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

For more details about policies for OKE, see:
- [Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm)
- [Details for Kubernetes Engine](https://docs.oracle.com/iaas/Content/Identity/policyreference/contengpolicyreference.htm)
