# Overview of Tagging
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/taggingoverview.htm
- Fetched: 2026-09-05 03:06 CDT

# Overview of Tagging

Oracle Cloud Infrastructure Tagging allows you to add metadata to resources, which enables you to define keys and values and associate them with resources. You can use the tags to organize and list resources based on your business needs.

Tagging is part of the Identity and Access Management service. The Tagging service has two parts:
- Handling the creation and management of new tag namespaces and tag key definitions. For these operations, use the Identity and Access Management Service base URL.
- Applying tags to specific resources by including the tag namespace, key, and value information in requests sent to each supporting service.

For more information about adding tags to your resources (for example, instances, VCNs, load balancers, and block volumes), see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

Caution  
  
Avoid entering confidential information when assigning descriptions, tags, or friendly names to cloud resources through the Oracle Cloud Infrastructure Console, API, or CLI.

## How Tagging Works

The Tagging service provides two ways for you to add tags to resources.

Each approach offers a different type of tag for you to work with:
- Defined tags - tag administrators manage resource metadata.
- Free-form tags - unmanaged metadata applied to resources by users.

One approach involves a tag administrator creating and managing all the tags that users apply to resources. Use IAM policy to select tag administrators, who can create tags. Grant all others in the tenancy only the ability to apply tags. The benefit to this approach is that you can create and manage the keys and values used to tag resources. You can then avoid typos that weaken automation based on tags and provide better reporting based on tags.

The other approach is to allow users to add tags to resources. Each tag is edited or applied at the resource by you or a user creating or modifying a resource. You can use both types of tags throughout your tenancy.

Most of the Tagging features require defined tags. "Tag" is used generically to refer to defined tags. To create metadata that you can trust to manage resources and collect data, use defined tags. With defined tags, the following scenarios become possible:
- Create default tags that are applied to all resources in compartments. See[Managing Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagdefaults.htm).
- Specify that users must apply tags to resources to successfully create resources in compartments.
- If you make a typo using defined tags, correct it by editing or even deleting the tag. When you delete a defined tag, Oracle removes the key and any value for that tag from all resources. See[Deleting Tag Key Definitions and Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagsandtagnamespaces.htm#deletingtags).
- Associate a list of predefined values for a defined tag. See[Using Predefined Values](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/usingpredefinedvalues.htm).
- Use system variables to generate values for defined tags or tag defaults automatically. See[Using Tag Variables](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/usingtagvariables.htm).
- Track costs based on tags. Use of defined tags is recommended for this use case.
Note  
  
Tagging is only supported with resources that have OCIDs.

## Tagging Concepts

Describes the basic tagging concepts.

Here's a list of the basic tagging concepts: TAG NAMESPACE You can think of a tag namespace as a container for your tag keys. It consists of a name and zero or more tag key definitions. Tag namespaces are not case sensitive and must be unique across the tenancy. The namespace is also a natural grouping to which administrators can apply policy. One policy on the tag namespace applies to all the tag definitions contained within that namespace.

Note  
  

- You cannot use OCID to name the tag namespace as OCIDs do not follow the required format for naming tag namespaces.
- You cannot change the name of your tag namespace. However, you can retire it. TAG KEY The name you use to refer to the tag. Tag keys are case insensitive. For example,`mytagkey`duplicates`MyTagKey`. You must create tag keys for defined tags in a namespace. Each tag key must be unique within a namespace. TAG VALUE TYPE The tag value type specifies the data type allowed for the value. Currently two data types are supported: string and a list of strings. KEY DEFINITION A key definition defines the schema of a tag and includes a namespace, tag key, and tag value type.

Note  
  
You cannot change the name of your tag key definition. However, you can retire it TAG VALUE The tag value is the value that the user applying the tag adds to the tag key. Tag values support two data types: strings and lists of strings. You can define a list of values for the user to select from when you define the tag key, or you can allow the user to enter any value when the tag is applied to the resource. If you select a string tag value when you create the key, the user can leave the value blank when they apply the key. In the example: Operations.CostCenter="42" Operations is the namespace, CostCenter is the tag key, and 42 is the tag value. TAG (OR DEFINED TAG) A tag is the instance of a key definition that is applied to a resource. It consists of a namespace, a key, and a value. "Tag" is used generically to refer to defined tags. FREE-FORM TAG A basic metadata association that consists of a key and a value only. Free-form tags have limited functionality. See[Understanding Free-form Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm). COST TRACKING

Use any tag for cost tracking purposes.

You don't have to designate a tag as cost-tracking, in order for it to be exposed in[Cost Analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm)or[Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm). TAG DEFAULT Tag defaults let you specify tags that are applied automatically to all resources in a specific compartment at the time of creation, regardless of the permissions of the user who creates the resource. See[Managing Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagdefaults.htm). RETIRE You can retire a tag key definition or a tag namespace. Retired tag namespaces and key definitions can no longer be applied to resources. However, retired tags are not removed from the resources to which they have already been applied. You can still specify retired tags when searching, filtering, reporting, and so on. REACTIVATE You can reactivate a tag namespace or tag key definition that has been retired to reinstate its usage in your tenancy. TAG VARIABLE You can use a variable to set the value of a tag. When you add or update a tag on a resource, the variable resolves to the data it represents. See[Using Tag Variables](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/usingtagvariables.htm). PREDEFINED VALUES You can use a variable to set the value of a tag. When you add or update a tag on a resource, the variable resolves to the data it represents. See[Using Predefined Values](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/usingpredefinedvalues.htm). TAG EXAMPLE
```

```

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

For administrators: Use the following topics to find example of IAM policy for Tagging:
- [Required Permissions for Working with Defined Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagsandtagnamespaces.htm#Who)
- [Required Permissions for Working with Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/../Tasks/managingtagdefaults.htm#requriedIAM)
- [Required Permissions for Working with Free-form Tags](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm#IAM-free-form)
Note  
  

If you don't have`use`or`manage`permissions for`tag-namespaces`, you might receive an error message when trying to create resources in the Console similar to the following: "The following tag namespaces / keys are not authorized or not found: 'oracle-tags'."

See[Understanding Automatic Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/understandingautomaticdefaulttags.htm)for information about the 'oracle-tags' namespace and the two automatic tags applied when creating resources.

## Region Availability

Tagging is currently available in all regions.

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

## Limits on Tags

Learn about per-resource limits on tags, and what characters are supported in tag strings.
- Tags per tenancy: unlimited
- Tags per resource: 10 free-form tags and 64 defined tags
- Total tag data size: 5 K (JSON). The total tag data size includes all tag data for a single resource (all applied tags and tag values). Sizing is per UTF-8.
- Number of pre-defined values for a tag key: 100 per list

Resource Supported Characters Max Length
Tag namespace Printable ASCII, excluding periods (.) and spaces 100 characters

Tag key name

(free-form and defined) Printable ASCII, excluding periods (.) and spaces 100 characters

Tag value

(free-form and defined) Unicode characters 256 characters

## Resources That Can Be Tagged

Provides the list of resources supported by tagging.

The following table lists resources that support tagging. This table will be updated as tagging support is added for more resources.

Service Taggable Resource Types
Analytics Cloud analytics-instances
API Gateway

api-deployments

api-gateways
Application Performance Monitoring

apm-domains

scripts

monitors
Artifact Registry

artifact-repositories

generic-artifacts
Audit audit-events
Autonomous Recovery Service

recovery-service-protected-database

recovery-service-subnet

recovery-service-policy
Bastion bastions
Big Data Service bds-instances
Block Volume

backup-policies

boot-volumes

boot-volume-backups

volumes

volume-backups

volume-groups

volume-group-backups
Blockchain Platform blockchain-platforms
Budgets usage-budgets
Cloud Guard

managed-lists

targets
Cluster Placement Groups

cluster-placement-groups
Compute

auto-scaling-configurations

cluster-networks

instance

instance-configurations

instance-image

instance-pools

instanceconsoleconnections
Compute Cloud@Customer

ccc-infrastructures

ccc-upgrade-schedules
Connector Hub service-connectors
Container Instances

compute-container

compute-container-instances
Content Management oce-instances
Console Dashboards

dashboards

dashboard-groups
Data Catalog

data-catalogs

data-catalog-data-assets

data-catalog-glossaries
Data Flow

dataflow-applications

dataflow-runs
Data Integration workspaces
Data Labeling dataset
Data Safe data-safe
Data Science

data-science-models

data-science-notebook-sessions

data-science-projects
Database

autonomous-databases

db-systems

databases
Database Management

dbmgmt-external-dbsystem-discoveries

dbmgmt-external-dbsystems

dbmgmt-external-exadata

dbmgmt-jobs

dbmgmt-managed-database-groups

dbmgmt-managed-databases

dbmgmt-named-credentials

dbmgmt-private-endpoints
Database Migration

connections

jobs

migrations
OCI Database with PostgreSQL

postgresqlbackup

postgresqlconfiguration

postgresqldbsystem
DevOps

DevOps projects

environments

artifacts

deployment pipelines
Digital Assistant

oda-instances
DNS

dns-steering-policies

dns-tsig-keys

dns-zones
Email Delivery approved-senders
Events cloudevents-rules
File Storage

file-systems

mount-targets

snapshots
File Storage with Lustre lustrefilesystem
Fleet Application Management

fams-fleets

fams-maintenance-windows

fams-schedules

fams-catalog-items

fams-provisions

fams-runbooks
Full Stack Disaster Recovery

DrProtectionGroup

DrPlan

DrPlanExecution
Functions

fn-app

fn-function
Globally Distributed Autonomous AI Database

sharded-database

sharded-database-private-endpoint
Globally Distributed Exadata Database on Exascale Infrastructure

osddistributeddb

osddistributeddbprivateendpoint
GoldenGate

deployments

registered-databases
Health Checks health-check-monitor
IAM

compartments

dynamic-groups

groups

identity-providers

network-sources

policies

tenancy (root compartment)

users
Integration integration-instances
Java Management fleet
Load Balancer load-balancers
Log Analytics

loganalytics-entity

loganalytics-log-group
Management Agent management-agents
Management Dashboards

management-dashboard

management-saved-search
Media Services (Media Flow)

media-workflow

media-workflow-configuration

media-workflow-job
Media Services (Media Streams)

media-stream-distribution-channel

media-stream-packaging-config

media-stream-cdn-config
Monitoring alarms
MySQL HeatWave

mysql-configurations

mysql-instances

mysql-backups
Networking, FastConnect

cpes

cross-connects

cross-connect-groups

dhcp-options

drgs

internet-gateways

ipsec-connections

ipv6s

ipsec-connections

local-peering-gateways

nat-gateways

network-security-groups

private-ips

public-ips

remote-peering-connections

route-tables

security-lists

service-gateways

subnets

vcns

virtual-circuits

vnics

vnic-attachments
Network Firewall

network-firewalls

network-firewall-policies
NoSQL Database Cloud

nosqltable
Notifications

ons-subscriptions

ons-topics
Object Storage and Archive Storage

buckets
Oracle Cloud Migrations

Remote connections agents

Agent dependencies

Asset sources

Discovery schedules

Inventory assets

Migration projects

Migration plans

Replication schedule
OS Management

osms-managed-instances

osms-managed-instance-groups

osms-software-sources

osms-scheduled-jobs
OS Management Hub

osmh-lifecycle-environments

osmh-lifecycle-stages

osmh-managed-instance-group

osmh-management-station

osmh-profiles

osmh-scheduled-jobs

osmh-software-sources
Process Automation

process-automation-instances
Queue queues
Quotas Service quota
Resource Manager

orm-config-source-provider

orm-jobs

orm-private-endpoints

orm-stacks

orm-template
Search resourcesummary
Secret Management Service secrets
Secure Desktops desktop-pool
Streaming

connect-harnesses

streams

streampools
Tagging

tag-namespaces

tag-definitions (API only)
Vault

keys

vaults

key-delegate
Visual Builder visualbuilder-instances
Visual Builder Studio vbs-instances
Vulnerability Scanning

host-scan-recipes

host-scan-targets
WAF

http-redirects

waas-address-list

waas-certificate

waas-custom-protection-rule

waas-policy
