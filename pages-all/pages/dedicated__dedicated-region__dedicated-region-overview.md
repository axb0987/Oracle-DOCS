# Dedicated Region Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-overview.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-overview.htm#dcoc-content-body)

# Dedicated Region Overview

OCI Dedicated Region is an Oracle-operated OCI cloud region that is deployed in a customer-selected data center. Dedicated Region provides OCI public cloud services, operational practices, APIs, and cloud economics in a customer-controlled location.

Oracle installs, operates, patches, monitors, and maintains the environment. Organizations can use OCI services, APIs, pricing, and enterprise support while keeping data and workloads in the required location.

Dedicated Region helps organizations meet data residency, sovereignty, latency, AI, and operational requirements that make workload relocation impractical. Customers retain control of sensitive data, regulated workloads, and mission-critical applications.

Cloud placement now involves boards, regulators, legal teams, procurement teams, and lines of business. Dedicated Region addresses these requirements by providing a full OCI region in the customer environment instead of a reduced subset of cloud capabilities.

## Critical Implementation Data

Use the following table as the first-pass checklist for design decisions and executive alignment.

Planning Area Important Data for Architects
Operating model Oracle operates and monitors the Dedicated Region 24x7x365 and delivers updates with OCI cloud operations processes.
Location and control The region runs in the customer-selected data center. The customer retains control of the facility, physical access program, and environmental services.
Footprint and growth Deployments can start with Dedicated Region25 (DR25) with a base footprint of 3 racks and expand through additional capacity and network expansion racks as consumption grows.
Services and APIs Oracle describes Dedicated Region as access to more than 200 OCI services through the OCI Console, SDKs, CLIs, Terraform providers, and service APIs. Confirm service availability for the specific Dedicated Region.
Availability and recovery Fault domains provide high availability within a region. Implement DR across a pair of Dedicated Regions in separate geographies.
Support and change Oracle provides standard OCI support processes, including 24x7 support channels, a 15-minute response objective for Severity 1 service requests (SRs), and 15-day advance notice for known disruptive changes.
Multitenancy decision When multitenancy is required, determine the model during contracting and architecture approval. A Dedicated Region is planned as single-tenancy or multitenancy. The model is not treated as an in-place conversion later.

## Dedicated Region Deployment Types

This section describes the main deployment patterns used to place, operate, and scale OCI Dedicated Region for an enterprise environment.

A Dedicated Region is deployed as a complete OCI region in the customer data center and is operated by Oracle. Architects must select the deployment pattern based on tenancy isolation, organizational ownership, latency requirements, data residency requirements, expected growth, and internal support responsibilities.

Deployment Pattern When to Use It Design Considerations
Single enterprise region Use this pattern when one organization needs a full OCI region in its own facility for regulated, latency-sensitive, or mission-critical workloads. Plan the realm, region identifier, IAM model, network connectivity, capacity growth, operational access, and compliance evidence before onboarding workloads.
Enterprise multitenancy Use this pattern when a central enterprise team must onboard multiple internal departments or business units while keeping their cloud resources isolated. Each top-level tenancy can have independent administrators, resources, policies, and users. Central teams must define tenancy lifecycle, escalation, quota, tagging, and chargeback models.
Scalable footprint Use this pattern when the initial capacity requirement is smaller than the long-term target or when growth is expected to occur in waves. Plan floor space, power, cooling, cabling, and network expansion paths early. Oracle design materials describe high-density and low-density racks, noncontiguous placement options, and expansion through capacity racks.
AI and specialized capacity Use this pattern when workloads require GPU, high-performance computing (HPC), database, VMware, bare metal, or other specialized shapes close to sensitive data or existing systems. Validate shape availability, power and cooling density, cluster networking needs, storage throughput, and expansion schedule with Oracle during solution design.

Document tenancy ownership, region naming, administrator responsibilities, identity federation, capacity trigger points, and the service activation sequence before production onboarding.

- [Dedicated Region Overview](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-overview.htm#dedicated-region-overview)
- [Critical Implementation Data](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-overview.htm#critical-implementation-data)
- [Dedicated Region Deployment Types](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-overview.htm#dedicated-region-deployment-types)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
