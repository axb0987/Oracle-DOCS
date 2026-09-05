# IAM Security Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-IAM_Security_Policies.htm
- Fetched: 2026-09-05 03:04 CDT

# IAM Security Policies

IAM security policies are used to govern the access of IAM groups to resources in compartments and in the tenancy.

Oracle recommends that you assign least privilege access to IAM groups for accessing resources. The common format for IAM policies is shown in the following example.
```

```

IAM policies allow four predefined verbs: inspect, read, use and manage. Inspect allows least privilege and manage allows the maximum. The four verbs are shown in increasing order of privilege in the following table.

IAM policy verbs
Verb Access Type Example User
`inspect`Should only show metadata. This usually results in ability to list resources only third-party auditor
`read`inspect plus ability to read resource and user metadata. This is the permission most users need to get work done. internal auditors
`use`read plus ability to work with resources (the actions vary by resource type). Excludes ability to create or delete resource regular users (software developers, system engineers, dev managers, etc) setting up and configuring tenancy resources, and applications running on them
`manage`All the permissions for all the resources administrators, executives (for break-glass scenarios)

The resource types of Oracle Cloud Infrastructure resources are shown in the following table.

IAM resource families, descriptions, and resource types
Resource Type Family Description Resource Types
`all-resources`All resource types
No name by design Resource types in IAM service`compartments`,`users`,`groups`,`dynamic-groups`,`policies`,`identity-providers`,`tenancy tag-namespaces`,`tag-definitions`
`instance-family`Resource types in compute service`console-histories`,`instance-console-connection`,`instance-images`,`instances`,`volume-attachments``app-catalog-listing`
`volume-family`Resource types in block storage service`volumes`,`volume-attachments`,`volume-backups`
`virtual-network-family`Resource types in virtual networking service`vcns`,`subnets`,`route-tables`,`security-lists`,`dhcp-options`,`private-ips`,`public-ips`,`internet-gateways`,`local-peering-gatewaysdrgs`,`deg-attachments`,`cpes`,`ipsec-connections`,`cross-connects`,`cross-connect-groups`,`virtual-circuits`,`vnics`,`vnic-attachments`
`object-family`Resource types in object storage service`buckets`,`objects`
`database-family`Resource types in DbaaS service`db-systems`,`db-nodes`,`db-homes`,`databases`,`backups`
`load-balancers`Resources in Load Balancer service`load-balancers`
`file-family`Resources in file storage service`file-systems`,`mount-targets`,`export-sets`
`dns`Resources in DNS service`dns-zones`,`dns-records`,`dns-traffic`
`email-family`Resources in email delivery service`approved-senders`,`suppressions`

For more information about IAM verbs and resource type permission mappings, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

IAM security policies can be made fine-grained through conditions. Access specified in the policy is allowed only if the condition statements evaluate to true. Conditions are specified using predefined variables. The variables use the key words`request`or`target`, depending on whether the variable is relevant to the request or the resource being acted on, respectively. For information about supported predefined variables, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm).
