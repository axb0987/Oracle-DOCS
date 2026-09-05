# Categories and Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations.htm
- Fetched: 2026-09-05 01:47 CDT

# Categories and Recommendations

Cloud Advisor recommendations are divided into three categories: cost management, performance, and high availability. These categories and the recommendations they include are described in this section.
Note  
  
When listing recommendations, you might not see every recommendation listed on this page, depending on how your tenancy or compartment is set up and what you have selected in the Category, Service, and Status boxes. For example, the default Status setting is Active. To see recommendations that have other statuses, select the Status box to add Dismissed and Postponed as needed.
Note  
  
Cloud Advisor supports a dedicated IAM policy that improves data security and safeguards resource metadata. See the explanation about the[additonal required permissions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/additional_required_permissions.htm)needed to view all the recommendation and resource metadata.

Cloud Advisor categories and their recommendations are:
- [Cost management](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm). These recommendations help you save money by downsizing underutilized databases to match the size of the data:
- [Enable Database Management](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#rec-enable-database-management)
- [Enable Monitoring on Compute Instances](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#enable-monitoring)
- [Enable Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#enable-object)
- [Downsize Underutilized Exadata Cloud VM clusters](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#rec-downsize-underutilized-exadata-cloud-clusters)
- [Downsize Underutilized Base Database system](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#rec-downsize-base-database-system)
- [Downsize Underutilized Load Balancers](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#downsize-loadbalancers)
- [Downsize Underutilized ADW and ATP Databases](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#downsize-adw-atp)
- [Downsize Underutilized Compute Instances](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#downsize-compute)
- [Delete Idle Compute Instances](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#delete-idle)
- [Delete Unattached Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#delete-boot)
- [Delete Unattached Block Volumes](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#delete-block)
- [Change Compute Instances to Burstable](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#burstable)
- [Continuous Consumption Discounts](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#consumption-discount)
- [Performance](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm). These recommendations help you to increase performance by rightsizing overutilized databases to make them large enough to contain the data.
- [Rightsize Exadata Cloud VM Clusters](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm#rec-rightsize-underutilized-exadata-cloud-clusters)
- [Rightsize Base Database System](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm#rec-rightsize-base-database)
- [Rightsize Compute Instances](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm#rightsize-compute)
- [Rightsize Load Balancers](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm#rightsize-loadbalancers)
- [Enable Performance Auto-tuning for Detached Block Volumes](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm#enable-autotune-block)
- [Enable Performance Auto-tuning for Detached Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm#enable-autotune-boot)
- [High availability](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-highavailability.htm). These recommendations provide hardware failure best practices to ensure system resilience.
- [Improve fault tolerance](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-highavailability.htm#improve-fault-tol)
- [Enable object versioning](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-highavailability.htm#rec-enable_object_versioning)
- [Enable object replication](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-highavailability.htm#rec-enable_object_replication)

Service Types

Cloud Advisor provides recommendations for the following service types:
- Block Storage
- Compute
- Database
- Load balancing
- Object Storage
-
