# High Availability Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-highavailability.htm
- Fetched: 2026-09-05 01:47 CDT

# High Availability Recommendations

This section of Recommendations describes the recommendations that help you ensure that your resources are available all the time.

High availability recommendations provide hardware failure best practices to ensure the resilience of your solution and show you how to improve system resilience. For example, High availability recommendations might suggest increasing the availability of applications running on Oracle Cloud Infrastructure by using redundant compute nodes in different availability domains to support failover capability and correctly leverage fault domains.

## Improve Fault Tolerance

The Improve Fault Tolerance recommendation indicates that all virtual machine (VM) instances in the indicated compartment are clustered in a single fault domain. Implementing this recommendation improves availability of your VMs across fault domains.

### Recommendation generation logic

Cloud Advisor generates this recommendation when all of a compartment's VMs are in a single[fault domain](https://docs.oracle.com/iaas/Content/Compute/References/bestpracticescompute.htm#Fault).

### Implementing the recommendation

Manually move instances to spread them across multiple fault domains (this recommendation cannot be implemented using Cloud Advisor). For best practices, see[Fault Domains](https://docs.oracle.com/iaas/Content/Compute/References/bestpracticescompute.htm#Fault). For instructions, see[Editing the Fault Domain for an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/edit-fault-domain.htm).

### Status changes

When you implement the recommendation (manually moving instances), its status changes from Pending to Implemented . The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Enable Object Versioning

Object versioning provides data protection against accidental or malicious object updating, overwriting, or deletion. Enabled at the bucket level, versioning directs Object Storage to automatically create an object version each time a new object is uploaded, an existing object is overwritten, or when an object is deleted. The Enable Object Versioning recommendation indicates that object versioning is not implemented for an Object Storage bucket in your tenancy.
Note  
  
Object versioning increases your[storage costs](https://www.oracle.com/cloud/storage/pricing/)because the resource includes multiple versions of the same object. Consider using object versioning to help manage object lifecycle management automatically. For more information, see[Using Object Versioning](https://docs.oracle.com/iaas/Content/Object/Tasks/usingversioning.htm).

### Recommendation generation logic

Enabling object versioning automatically creates an object version each time a new object is uploaded, when an existing object is overwritten, or when an object is deleted. If Object Versioning is not enabled for the bucket, Cloud Advisor recommends that you enable it.

### Implementing the recommendation

To implement the recommendation, do one of the following:
- Select the resource, select Implement selected , and then follow the fix-it flow. See[Using the Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/bulk-apply-recommendations.htm#bulk-apply-recommendations-console)
- Manually create an IAM policy and then enable object versioning. See[Using Object Versioning](https://docs.oracle.com/iaas/Content/Object/Tasks/usingversioning.htm).

### Status changes

When you implement the Enable Object Versioning recommendation using the Cloud Advisor fix-it flow, the status of the recommendation changes from Pending to Implemented. The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes at the next scan of your tenancy (usually within 24 to 48 hours).

## Enable Object Replication

Object replication provides protection from regional outages, aids in disaster recovery efforts, and addresses data redundancy compliance requirements. Maintaining multiple copies of data in regional locations closer to user access can also reduce latency. The Enable Object Replication recommendation indicates that object replication is not implemented for an Object Storage bucket in your tenancy.
Note  
  
Object replication increases your storage costs because the resource includes multiple copies of the same object.
Note  
  
Replication overwrites objects in the destination bucket that have the same names as objects in the source bucket. Objects uploaded to a source bucket before the policy is created are not replicated.

### Recommendation generation logic

Cloud Advisor scans your buckets in Object Storage and if[Object Storage Replication](https://docs.oracle.com/iaas/Content/Object/Tasks/usingreplication.htm)is not enabled for the bucket, Cloud Advisor recommends that you enable it.

### Implementing the recommendation

To implement the recommendation, do one of the following:
- Select the resource, select Implement selected , and then follow the fix-it flow. See[Using the Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/bulk-apply-recommendations.htm#bulk-apply-recommendations-console)
- Manually create replication policy rules. See[Using Replication.](https://docs.oracle.com/iaas/Content/Object/Tasks/usingreplication.htm)

### Status changes

When you implement the enable Object Replication recommendation using Cloud Advisor fix-it flow, the status of the recommendation changes from Pending to Implemented . The time needed to change this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
-
