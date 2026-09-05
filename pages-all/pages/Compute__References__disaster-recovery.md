# Disaster Recovery
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/disaster-recovery.htm
- Fetched: 2026-09-05 01:49 CDT

# Disaster Recovery

Disaster recovery for OCI Compute instances is accomplished using OCI Full Stack Disaster Recovery service. Full Stack Disaster Recovery is a robust OCI cloud native service that is tightly integrated with many OCI services including OCI Compute. Full Stack DR can orchestrate recovery for virtual machines alone but is intended to handle recovery for entire application stacks that include much more than OCI Compute.

## Overview

OCI Full Stack Disaster Recovery service provides a simple, low code means of creating and maintaining robust disaster recovery plans (DR Plans) that orchestrate recovery for entire application stacks. DR plans can be customized to include user-defined steps to stop and restart other OCI platform services and applications as part of a fully automated recovery plan. The disaster recovery service includes OCI native support for the following OCI resource types and assumes the supported resources are already provisioned for disaster recovery across OCI regions or availability domains.
- OCI Compute virtual machines
- Load balancers and network load balancers
- Oracle databases
- Autonomous AI Database
- Base Database
- Exadata Database
- Oracle Kubernetes Engine
- Storage
- Block volume groups
- File systems
- Object storage buckets

## How to configure DR for OCI Compute instances

There are two approaches for adding one or more virtual machines to disaster recovery using Full Stack DR.

QuickDR

Configure disaster recovery for individual OCI Compute virtual machines from the instance details page of any Compute instance. QuickDR provides a fast and efficient method for provisioning DR for your virtual machines. QuickDR is can either create a new, dedicated, Full Stack DR configuration for your Compute instance, or you can add your Compute instance to an existing configuration. Use this approach if you have a basic knowledge of disaster recovery but little, to no experience with OCI networking, OCI storage or the full featured Full Stack Disaster Recovery service.[Learn more about QuickDR](https://docs.oracle.com/iaas/disaster-recovery/doc/quickdr.html).

Full Service

Configure disaster recovery for individual OCI Compute virtual machines plus many other OCI resources using the Full Stack DR full featured service. Use this approach if you are experienced with disaster recovery, have a fundamental understanding of OCI Full Stack DR and need to create fully automated recovery for an entire application stack including virtual machines, storage, databases, load balancers, Oracle, or nonOracle applications and other OCI services.[Learn more about Full Stack Disaster Recovery](https://docs.oracle.com/iaas/disaster-recovery/doc/overview-disaster-recovery.html)
