# Cost Management Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm
- Fetched: 2026-09-05 01:47 CDT

# Cost Management Recommendations

This section of Recommendations describes the recommendations that help you reduce the costs of your resources.

Cost management recommendations identify underutilized resources and help you reduce costs by finding and adjusting resources that are underutilized. For example, cost management recommendations help you find underutilized Compute instances, overprovisioned Autonomous AI Lakehouse instances, detached block volumes, detached boot volumes, Object Storage buckets without lifecycle policy rules, and continuous consumption discounts (CCDs). Except for CCDs, cost management recommendations show you the resource utilization and its cost, the recommended utilization, the cost savings per month, and the number of cost management recommendations available for your tenancy at the time that the last scan was made. A CCD advises customers to create a CCD commitment when it is financially beneficial for them.

## How Cost Savings Estimates Are Calculated

Cloud Advisor estimates cost savings for applicable recommendations. Each cost savings estimate indicates how much lower your costs are after you implement the recommendation.

Cloud Advisor also provides a percentage cost savings of the expected monthly bill for the tenancy. The expected bill is based on data from current usage and the previous month. If less than a full month of data is available, then Cloud Advisor estimates the cost savings using data starting on the first day of the current month.

New resources have less than a full month of data when they are created:
- After the start of the current billing month and the time is less than a full month to the current date.
- In the previous billing month, and the time is less than a month to the current date.

There are typically two reasons that cost information is not available:
- The recommendation itself doesn't make sense to have cost saving estimate. For example, Enable Compute Monitoring and Enable Database
- Cloud Advisor does not have enough data to calculate the savings.

## Enable Database Management

The Enable Database Management recommendation applies to all databases belonging to the Base Database (BaseDB) System and Exadata Cloud VM clusters (ExaDB-D) families. Cloud Advisor checks to see if database management is enabled on all database instances. If database management is not enabled on a database instance, Cloud Advisor generates a recommendation to enable database management. The recommendation is made on a per database level instead of the underlying database infrastructure. Enabling database management generates metrics that provide insights for your database performance.
Note  
  
Enabling basic management does not add any extra cost. Enabling full management adds extra cost. For more information, see[About Management Options.](https://docs.oracle.com/iaas/database-management/doc/enable-database-management-oracle-cloud-databases.html#GUID-82E59C37-A1EA-4355-8216-769D22F8EFDD)

### Recommendation generation logic

Cloud Advisor determines whether the monitoring was enabled on a database instance, and then provides a recommendation accordingly..

### Implementing the recommendation

Manually enable database management (this recommendation cannot be implemented using Cloud Advisor). For detailed instructions, see[Perform Database Management Prerequisite Tasks](https://docs.oracle.com/iaas/database-management/doc/perform-database-management-prerequisite-tasks.html).

### Status changes

When you implement the recommendation (manually enabling database management), its status changes from Pending to Implemented . The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours). If the database instance stops running or is deleted, the recommendation is deleted.

## Enable Monitoring on Compute Instances

The Enable Monitoring on Compute Instances recommendation indicates that metrics for some running Compute instances aren't visible to Cloud Advisor. For example, CPU utilization data can't be tracked. When you implement this recommendation, Cloud Advisor can read the Compute instance metrics and then provide you with recommendations.

### Recommendation generation logic
Cloud Advisor identifies Compute instances that don't have Monitoring enabled.
Note  
  
Although this recommendation is a cost management recommendation, it does not by itself show a cost saving for your tenancy. The estimated cost saving is set to 0.

### Implementing the recommendation

Manually enable monitoring (this recommendation cannot be implemented using Cloud Advisor). To determine what needs to be changed to enable monitoring, examine the instance. For detailed instructions, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm).
Note  
  
Possible reasons why a Compute instance does not have Monitoring enabled:
- The instance's image does not support monitoring.
- The instance's image supports monitoring, but the Oracle Cloud Agent is either disabled or not installed. For manual installation instructions, see[Cloud Advisor Categories and Recommendations](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent).
- A service gateway does not exist for that virtual cloud network (VCN).

### Status changes

When you implement the recommendation (manually enabling monitoring), its status changes from Pending to Implemented . The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours). If the instance stops running or is deleted, then the recommendation is deleted.

## Enable Object Lifecycle Management

The Enable Object Lifecycle Management recommendation indicates that no lifecycle policy rules exist for an Object Storage bucket in your tenancy. Consider using Object Lifecycle Management to help manage object versions automatically.

### Object Lifecycle Policies

Enabling object lifecycle management depends on the existing object lifecycle policies.
- When an object does not have Object Versioning enabled, Object Storage lets you create multiple lifecycle policy rules such as moving objects to infrequent access or deleting abandoned multipart uploads for cost savings.
- When an object has Object Versioning enabled, Object Storage lets you create lifecycle policy rules such as automatically archiving or deleting object versions, moving objects to infrequent access, or managing abandoned multipart uploads.
- When it is possible to move Object Storage data, you can define a lifecycle policy rule that automatically moves it to lower tiers.

For more information, see[Using Object Lifecycle Management](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm)

### Recommendation generation logic

Cloud Advisor queries the latest`EnabledOLM`metric to determine whether Object Lifecycle Management is enabled for buckets in your tenancy. For more information, see[Object Storage Metrics](https://docs.oracle.com/iaas/Content/Object/Reference/objectstoragemetrics.htm). If there are no policy rules enabled under Object Lifecycle Management for the bucket, Cloud Advisor recommends that you enable it.

### Calculating Savings
- For each Object Storage bucket, Cloud Advisor multiplies the billed usage by the unit price and then takes 45 percent of that value. Cloud Advisor uses 45 percent because of overall customer trends. These trends indicate that over time, buckets with lifecycle management enabled trend toward a balance of 50 percent Archive Storage and 50 percent standard storage. Therefore, Cloud Advisor estimates that over time, the current standard storage for a bucket converts to a balance of 50 percent Archive Storage and 50 percent standard storage.
- The actual ratio varies based on the bucket's purpose. Although Cloud Advisor estimates a 45 percent savings, the savings could be higher or lower.

### Implementing the recommendation

Note  
  
In addition to implementing this recommendation, archiving or deleting old versions can reduce system usage, and can help to reduce costs.
Note  
  
After you move objects to Archive Storage, you must restore them before you can access them.
- To use Object Lifecycle Management, you must first authorize the Object Storage service to archive and delete objects on your behalf. See[Required IAM Policies](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#permissions)for more information.
- After objects are moved to Archive Storage, you must first[restore](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)objects to access them.
- You can also use Object Lifecycle Management to:
- delete all objects in a bucket or objects that match the names filters that you specify, or
- delete uncommitted or failed multipart uploads.
- Cloud Advisor does not provide cost savings estimates for these deletions. To implement the recommendation, do one of the following:

- Select the resource, select Implement selected , and then follow the fix-it flow. See[Using the Console](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/bulk-apply-recommendations.htm#bulk-apply-recommendations-console).
- 

Manually create lifecycle policy rules. You can define lifecycle policy rules that automatically archive or delete resources within a specific Object Storage bucket. Learn about how[Object Lifecycle Management](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm)works.

### Status changes

When you implement the recommendation, either by Cloud Advisor fix-it flow or manual creation, its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes at the next scan of your tenancy (typically within 24 hours), assuming that the metric is displayed.

## Downsize Underutilized Base Database system

The Downsize underutilized Base Database (BaseDB) system recommendation indicates that more CPU cores are allocated to a BaseDB system than are needed. Reducing the number of CPUs allocated to the BaseDB system saves you money.

### Recommendation generation logic

- Cloud Advisor gathers telemetry data about the CPU utilization for every database server node of the system. Then it determines the algorithm from a user-configured profile setting similar to downsize Compute recommendation, according to the following profiles (thresholds):
- Conservative - If the CPU utilization is less than 5%, OCI recommends downsizing to a shape that reaches utilization of 10% .
- Standard - If the CPU utilization is less than 10%, OCI recommends downsizing to a shape that reaches an average utilization of 20% .
- Aggressive - If the CPU utilization is less than 15%, OCI recommends downsizing to a shape that reaches an average utilization of 30%.
- Cloud Advisor uses your configured profile settings and threshold (default is 10% for CPU) to determine if the maximum of all of the database server nodes average the CPU utilizations during the last seven days (the number of days is customizable) is below the threshold. If it is, Cloud Advisor identifies the BaseDB system as underutilized. For example if a customer is running a BaseDB system on database server nodes having shape VM.Standard2.24 instance and Cloud Advisor determines that the BaseDB system is underutilized, it recommends downsizing the BaseDB system to a lower shape such as VM.Standard2.16 (or lower configuration) based on the current utilization. The node count remains the same.

### Supported shapes

Cloud Advisor scans support the following shapes using Downsize BaseDB system:

Standard Shapes
- VM.Standard1.1
- VM.Standard1.2
- VM.Standard1.4
- VM.Standard1.8
- VM.Standard1.16
- VM.Standard2.1
- VM.Standard2.2
- VM.Standard2.4
- VM.Standard2.16
- VM.Standard.2.24

### Calculating Savings

For the virtual machine DB system that the recommendation applies to, Cloud Advisor subtracts the recommended core count from the current core count and then divides this value by the current core count to get the core difference ratio. It then multiplies the result by the billed usage and the unit price.

### Implementing the recommendation

To implement the recommendation, do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- 

Manually adjust the system CPUs. See[Change the Shape of a DB System](https://docs.oracle.com/en/cloud/paas/base-database/shape-dbs/index.html).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual shape adjustment), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Downsize Underutilized Exadata Cloud VM clusters

The Downsize underutilized Exadata Cloud VM (ExaDB-D) cluster recommendation indicates that more CPUs are allocated to an ExaDB-D cluster than needed. Reducing the number of CPUs allocated to a cluster saves you money. The recommendation is currently made for only X6, X7 or X8 Exadata Cloud VM clusters.

### Recommendation generation logic

- Cloud Advisor gathers telemetry data about the CPU utilization for every database server node of the system. Then it determines the algorithm from a user-configured profile setting similar to the downsize compute recommendation, according to the following profiles (thresholds):
- Conservative - If the CPU utilization is less than 5%, OCI recommends downsizing the enabled CPU cores to help achieve an average utilization of 10% .
- Standard - If the CPU utilization is less than 10%, OCI recommends downsizing the enabled CPU cores to help achieve an average utilization of 20% .
- Aggressive - If the CPU utilization is less than 15%, OCI recommends downsizing the enabled CPU cores to help achieve an average utilization of 30%.
- Cloud Advisor uses your configured profile settings and threshold (default is 10% for CPU) to determine if the maximum of all of the database server nodes average the CPU utilizations during the last seven days (the number of days is customizable) is below the threshold. If it is, Cloud Advisor identifies the ExaDB-D system as underutilized.

For example, a customer is running a Exadata Cloud VM X8 cluster on full rack with 24 enabled cores and Cloud Advisor determines that the infrastructure is underutilized, Cloud Advisor would recommend downsizing the enabled core count for the infrastructure to a value of 16 (or lower). The node count of the infrastructure remains the same.

### Calculating Savings

To obtain the resource's compute costs,:
- Cloud Advisor checks the usage store and multiplies the recommended OCPU count with the price per OCPU to determine the new price. Then it calculates the existing price by multiplying the current OCPU count with the price per OCPU. This is the current cost of the system.
- Then Cloud Advisor determines the cost of the base system by looking at the cost in the usage store.
- Finally, Cloud Advisor calculates the difference between the base system and the existing system to show the cost savings.

### Implementing the recommendation

Cloud Advisor does not support a fix-it operation for this recommendation. The only implementation method available for this recommendation is to do it manually. To manually adjust the number of enabled CPU cores, see[To scale CPU cores in an Exadata Cloud Infrastructure cloud VM cluster or DB system.](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-manage-infrastructure.html#GUID-4EEDDECE-6622-4BB4-B3EE-39C23097D779)

### Status changes

After you implement the recommendation manually, the status changes to Implemented after the next Cloud Advisor scan (typically within 24 to 48 hours).

## Downsize Underutilized Compute Instances

The Downsize Underutilized Compute Instances recommendation indicates that some compute instances are bigger than needed. Implementing this recommendation saves you money without degrading performance.

### Recommendation generation logic

Cloud Advisor gathers the CPU, Memory, and Network utilization over the selected interval (default seven days) to see if the usage is below the thresholds as specified by the[recommendation profile](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/cloudadvisor-customizing-profiles.htm#downsize-compute-profile). Based on the methodology of the recommendation profile, Cloud Advisor either uses the Average or P95 statistic for the CPU utilization during evaluation. The network utilization value is computed based on the max of the network bytes in-rate and network bytes out-rate over the network bandwidth in Gbps.

The recommendation is generated only if a smaller instance is available to support the number of VNICs in use.

To customize the logic for this recommendation, see[Editing a Global Recommendation Override](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/customizing-overrides-console-edit-global.htm).

### Supported shapes

Cloud Advisor scans support the following shapes using Downsize Underutilized Compute Instances :

Standard VM Shapes
- VM.Standard1.1
- VM.Standard1.16
- VM.Standard1.2
- VM.Standard1.4
- VM.Standard1.8
- VM.Standard2.1
- VM.Standard2.16
- VM.Standard2.2
- VM.Standard2.24
- VM.Standard2.4
- VM.Standard2.8
- VM.Standard3.Flex
- VM.Standard.A1.Flex
- VM.Standard.B1.1
- VM.Standard.B1.16
- VM.Standard.B1.2
- VM.Standard.B1.4
- VM.Standard.B1.8
- VM.Standard.E2.1
- VM.Standard.E2.2
- VM.Standard.E2.4
- VM.Standard.E2.8
- VM.Standard.E3.Flex
- VM.Standard.E4.Flex

Optimized VM shapes
- VM.Optimized3.Flex

### Calculating Savings
For the resource that the recommendation applies to, Cloud Advisor subtracts the recommended OCPU from the current OCPU. It then multiplies the result by the billed usage and by the unit price. That value is divided by the current OCPU.
Note  
  
Cloud Advisor uses the saving calculation formulas listed in this manual to generate estimated cost savings. However, these formulas use cost information to calculate the savings. If the cost information is not available and you are using the API, Cloud Advisor sets the Return value of the estimated cost savings to minus 1`( -1)`. If you are using the Console, Cloud Advisor displays a message that says "Not Available" or "–".

See[How Cost Savings Estimates Are Calculated](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#cost-calc)for more information.

### Implementing the recommendation
Note  
  

- Select a good time for updating the instances. Because instances require reboots after resizing, we recommend that you resize the instances at a time that does not disrupt your users. It usually takes less than five minutes to reboot an instance, and you can track the progress for each instance by monitoring the associated work request.
- Downsizing an instance reduces the number of OCPUs, the amount of memory, the network bandwidth, and the maximum number of VNICs for the instance. The instance's public and private IP addresses, volume attachments, and VNIC attachments do not change.

To implement the recommendation, do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- 

Manually adjust compute instances. See[Changing the Shape of an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual instance adjustment), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Downsize Underutilized Load Balancers

The Downsize Underutilized Load Balancers recommendation indicates that some load balancers are configured with later minimum bandwidth than needed. Implementing this recommendation saves you money without degrading performance as the minimum bandwidth assigned decide the minimum amount that would be charged for the Load Balancer.

### Recommendation generation logic

Cloud Advisor detects if the average of the maximum values for peak bandwidth usage over the evaluation period is less than the threshold percentage of minimum bandwidth as specified by the[recommendation profile](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/cloudadvisor-customizing-profiles.htm#downsize-lb-profile). For the identified load balancers, Cloud Advisor suggests decreasing the minimum bandwidth to the current peak bandwidth usage value. The maximum bandwidth value remains the same.

For dynamic shapes, we recommend converting to flexible shape where the current bandwidth of dynamic shape is selected as the maximum bandwidth value. The minimum bandwidth is set to the peak bandwidth usage value as before mentioned.

To customize the logic for this recommendation, see[Editing a Global Recommendation Override](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/customizing-overrides-console-edit-global.htm).

### Calculating Savings
- If a Load Balancer with a dynamic shape is recommended to be converted to a flexible shape, Cloud Advisor subtracts the recommended minimum bandwidth from the current minimum bandwidth. It then multiplies the result by the billed usage and by the unit price per bandwidth of the current dynamic shape. If the recommended minimum bandwidth is less than or equal to 100 Mbps, that number is multiplied by 0.35 to offset the cost difference between dynamic and flexible shapes.
- If the recommendation is generated for a Load Balancer with a flexible shape, Cloud Advisor subtracts the recommended minimum bandwidth from the current minimum bandwidth. It then multiplies the result by the billed usage and unit price of a single flex bandwidth. The billed usage of a single flex bandwidth is calculated by dividing billed usage by the current minimum bandwidth.

### Implementing the recommendation
Note  
  

- This recommendation changes the Load Balancer's minimum bandwidth only. The maximum bandwidth remains unchanged.
- Changing the bandwidth size of the Load Balancer requires resetting all existing sessions of the Load Balancer. If you switch to a flexible shape, you can't revert to a dynamic shape. If the fixed shape is billed at a discounted rate, the estimated savings values might overstate potential savings. Before making changes, work with sales representative to understand billing and discount options.

To implement the recommendation, do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- 

Manually adjust load balancers. See[Changing a Load Balancer's Bandwidth Shape](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual change, either from dynamic to flexible shape or change of existing flexible shape), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Downsize Underutilized ADW and ATP Databases

The Downsize Underutilized ADW and ATP Databases recommendation indicates that more CPUs are allocated to autonomous databases than you need. Reducing the number of CPUs allocated to your databases saves you money.

### Recommendation generation logic

Cloud Advisor identifies low average CPU utilization the last seven days for Autonomous AI Lakehouse and Autonomous AI Transaction Processing databases. A low average CPU utilization indicates the utilization to be less than 30% of the allocated CPUs.

### Calculating Savings

For the resource's compute costs, Cloud Advisor multiplies the billed usage for ADB Compute by the unit price, and then divides that value in half.

### Implementing the recommendation

To implement the recommendation, do one of the following:
- Cloud Advisor suggests the number of OCPUs to allocate to these databases. For more information, see[Manage the Service](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/manage-service.html).
Note  
  
When you use Cloud Advisor to implement the recommendation, the cores are reduced by 20 percent.
- Manually adjust database CPUs. See[Add CPU or Storage Resources or Enable Auto Scaling](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-add-resources.html)and[Remove CPU or Storage Resources or Disable Auto Scaling.](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-remove-resources.html)

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual CPU adjustment), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Delete Idle Compute Instances

The Delete Idle Compute Instances recommendation indicates that some compute instances are unused. When you delete unused compute instances, you save money by not having to pay for them. Boot volumes are retained when you delete the compute instances.

### Recommendation generation logic

This recommendation analyzes the past seven days of data and generates recommendations with logic that depends on the shape of the compute instance.

For supported VM shapes:
- CPU Utilization P95 over all days is &lt; 3%
- Memory utilization max over all days is &lt; 8%
- Network utilization max over all days is &lt; 3%

For supported BM shapes:
- CPU Utilization P95 &lt; 2%
- Memory utilization max &lt; 5%
- Network utilization max &lt; 3%

### Supported shapes

When using Delete idle compute instances, Cloud Advisor supports the following shapes:

VM shapes:
- VM.Standard1.1
- VM.Standard2.1
- VM.Standard3.Flex
- VM.Optimized3.Flex
- VM.Standard.A1.Flex
- VM.Standard.B1.1
- VM.Standard.E2.1
- VM.Standard.E2.1.Micro
- VM.Standard.E3.Flex
- VM.Standard.E4.Flex

BM shapes:
- BM.Standard1.36
- BM.Standard2.52
- BM.Standard.A1.160
- BM.Standard.B1.44
- BM.Standard.E2.64
- BM.Standard.E3.128
- BM.Standard.E4.128
- BM.DenseIO1.36
- BM.DenseIO2.52

### Calculating Savings

For each compute instance, Cloud Advisor multiplies the billed usage by the unit price.

### Implementing the recommendation
To implement the recommendation, do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- Manually create lifecycle policy rules. You can define lifecycle policy rules that automatically archive or delete resources within a specific Object Storage bucket. Learn about how[Object Lifecycle Management](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm)works.

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual deletion), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Delete Unattached Block Volumes

The Delete Unattached Block Volumes recommendation indicates that unattached block volumes exist in your tenancy. Attaching or deleting unattached block volumes reduces costs.

### Recommendation generation logic

Cloud Advisor scans the tenancy once a day for block volumes that are not attached to any compute resource. If the volume is unattached for fourteen consecutive days, Cloud Advisor recommends that you delete it.

### Calculating Savings

Cloud Advisor estimates how much money would be saved by deleting the unattached block volume. For the resource that the recommendation applies to, Cloud Advisor uses the billed usage for performance units and storage.

### Implementing the recommendation

To implement the recommendation, do one of the following:
- 
Delete the volumes. Do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- Manually delete the volumes. See[Deleting a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/deletingavolume.htm).
- 

Manually attach the volumes. See[Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow, manual deletion, or manual attachment), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Delete Unattached Boot Volumes

The Delete Unattached Boot Volumes recommendation indicates that unattached boot volumes exist in your tenancy. Attaching or deleting unattached boot volumes reduces costs.

### Recommendation generation logic

Cloud Advisor scans the tenancy once a day for boot volumes that are not attached to any compute resource. If the volume is detached for fourteen consecutive days, Cloud Advisor recommends that you delete it.

### Calculating Savings

Cloud Advisor estimates how much money would be saved by deleting the detached boot volume. For the resource that the recommendation applies to, Cloud Advisor uses the billed usage for performance units and storage.

### Implementing the recommendation

To implement the recommendation, do one of the following:
- 
Delete the volumes. Do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- Manually delete the volumes. See[Deleting a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/delete-bv-boot-volume.htm).
- 

Manually attach the volumes. See[Attaching a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow, manual deletion, or manual attachment), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Change Compute Instances to Burstable

The Change Compute Instances to Burstable recommendation indicates bursty traffic in VM.Standard3.Flex, VM.Standard.E3.Flex, and VM.Standard.E4.Flex compute instances. Bursty traffic occurs when compute instances have low usage with only occasional spikes of high usage.

A burstable instance is a virtual machine (VM) instance that provides a baseline level of CPU performance with the ability to burst to a higher level to support occasional spikes in usage. When customers create a burstable instance, they can specify the total OCPU count (or CPU cores) and the baseline CPU utilization. The baseline utilization, which is always allocated to the instance, is a fraction of each CPU core, either 12.5% or 50%.

The advantage of changing a compute instance to a burstable instance is that burstable instances can sustain low workloads running with a fraction of normal number of CPUs most of the time, but can burst up to use the full number of available CPUs for a limited amount of time when needed to handle high workloads. Adjusting instances to the suggested burstable configuration saves you money when workloads are low, without degrading performance when the workload increases. For more information, see[Changing the shape of an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm#Changing_the_Shape_of_an_Instance)in the Compute Service manual.

### Recommendation generation logic

Cloud Advisor detects bursty VM.Standard3.Flex, VM.Standard.E3.Flex, and VM.Standard.E4.Flex instances using CPU utilization metrics (Max and P95 statistics). In a 24-hour period, Cloud Advisor reviews 48 data points for CPU utilization per instance, generating this recommendation when only a few data points (5 or fewer) have Max CPU utilization greater than a threshold (50% or 12.5%). When all other conditions are met, Cloud Advisor checks the instance memory-core ratio and generates the recommendation only when the memory-core ratio is less than 12GB/OCPU core. The P95 CPU utilization value in this duration should be less than 40% (for 50% threshold) and 10% (for 12.5% threshold) to ensure that the usage is low (non spiky) for most part of the duration. This recommendation suggests adjusting the instance to burstable at the percentage indicated by the exceeded threshold. Oracle recommends that you set burstable 50% for the 50% threshold and set burstable 12.5% for the 12.5% threshold.

To customize the logic for this recommendation, see[Editing a Global Recommendation Override](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/customizing-overrides-console-edit-global.htm).

### Calculating Savings

Cloud Advisor calculates cost savings for an instance as the difference between the suggested[burstable configuration](https://docs.oracle.com/iaas/Content/Compute/References/burstable-instances.htm)and the standard configuration. For example, if the suggested burstable configuration is 12.5%, then the new cost would be 12.5% of the standard configuration.

### Implementing the recommendation

To implement the recommendation, do one of the following:
- 

When implemented using the fix-it flow, the instance's[networking type](https://docs.oracle.com/iaas/Content/Compute/Tasks/recommended-networking-launch-types.htm)is updated to Paravirtualized networking
- 

Manually set up a burstable configuration. See[Burstable Instances](https://docs.oracle.com/iaas/Content/Compute/References/burstable-instances.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual steps to change the instance to a burstable configuration), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Continuous Consumption Discounts

Cloud Advisor creates recommendations for OCI customers to create a Continuous Consumption Discounts (CCD) commitment when it's financially beneficial for the customer.

A Create CCD Commitment Recommendation is determined by a clear resource consumption pattern over an evaluation period of 60 days. Cloud Advisor measures the consumption of resources that are billed to subscriptions owned by the tenancy you're signed in to, over the evaluation period (the last 60 days).

Using the calculation methods explained below, Cloud Advisor decides whether using a CCD can save you money based on the measured resource consumption trends. If you can save money with a CCD, Cloud Advisor creates a Continuous Consumption Discounts recommendation and displays it in the Cost Management section of the[Recommendations page](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations.htm), and in the Cost savings opportunities section on the OCI home page.

On the CCD details page, Cloud Advisor shows the recommended commit value and estimated savings. Using the CCD recommendation, you can select and activate any or all available CCD offers that are listed on the CCD details page. When activated, CCD rates are used for cost calculation, you're accountable for maintaining the commitment and you're billed for the minimum committed usage.

### Recommendation generation logic

Cloud Advisor identifies resources that meet the CCD settings by comparing the list of active CCD offerings and the CCD discount percentages with the contracted rate and the list price for the SKU.
Cloud Advisor generates a maximum of one recommendation to create a new CCD commitment for every SKU for each subscription owned by this tenancy using the best applicable CCD offer, that is, the offer which yields the highest estimated savings
Note  
  
There might be alternate offers for the same SKU-subscription combination.
- If the CCD rate is lower than the contracted rate, Cloud Advisor lists the CCD recommendation on the recommendations page and cost saving widget on the OCI home page, and displays the information on the Cloud Advisor home page.
- If the rate is equal to or higher than the contracted rate, Cloud Advisor doesn't display a CCD recommendation.

### Calculating the commit value

Cloud Advisor provides four commitment choices using common aggregation methods based on percentile calculations. The recommendation can be P30, Median, and P70. By default the aggregations are weighted, with higher weights toward the latest 7-day usage. The following table shows the commit time and assigned weights. The commitment choices are provided in the following table.
Depending on your resource usage, Cloud Advisor displays a set of four easy-to-understand options that help you select the best option for your tenancy.
Note  
  
Your tenancy has limits on the maximum number of resources that you can use. You can use quotas to allocate resource to compartments. If you're an administrator of an eligible account, you can request a service limit increase.

Commitment choices
Latest Resource usage Commitment choices
Declining
- P10
- P30
- Median
- Average
Increasing
- Median
- Average
- P70
- P90
Not changing
- Median
- Average
- P30
- P70

### Calculating Savings

To determine whether a CCD can save you money, Cloud Advisor calculates the commitment value and the estimated savings for the previous 60 days using these values:
- Cost of commit usage = (Recommended Commit Value) * (SKU list price - CCD discount)
- Cost of usage preceding commit value * non CCD rate
- Cost savings = Cost of usage preceding commit minus the cost of new commit usage

### Implementing the recommendation
- Open the navigation menu and select Governance &amp; Administration . Under Cloud Advisor , select Recommendations .
- Under Recommendation type, select the Continuous consumption discounts recommendation, then select Resource recommendations .

A list of CCD offers is displayed.
Note  
  
Active CCDs (CCDS that were implemented in a previous Cloud Advisor session) aren't displayed on this page. They're listed in the Cost Management category. On the Recommendations page, from the Search and Filter box above the list table, select Category &gt; Cost management &gt; Apply filter . Then, from the Search and Filter box, select Service &gt; Subscriptions &gt; Apply filter .
Caution  
  
Before implementing a CCD, check the list of existing CCDs to ensure that you're not adding a time commitment and extra cost to an existing CCD.
- Select the CCD offers that you want to implement and select Implement selected .

The Alternate Options page opens, showing a set of subscription options that you can select to use when implementing the offer.
- Select a subscription offer and then select Preview .

The Preview page for the subscription option opens. This page includes a graphical diagram that shows the time period when the discount is effective, the recommended value, and the estimated savings.
- Select Close .

The Preview page closes and returns to the Alternate Options page.
- To implement the selected CCD options, select Continue .

The Create CCD commitment panel opens.
- Enter the following information:
- A name for the CCD commitment.
- The date when you want the CCD commitment to start. Use the calendar icon to select the date.
- The product ID. Example : B93113 - Compute - Standard - 64 - OCPU
- The number of Commitment OCPUs per hour. Example : 400
- Review the commitment details at the bottom of the page. If you agree with them, select Create commitment .

The Create CCD commitment confirmation dialog box opens. It shows all the details of the CCD commitment that you're creating. Review the information and if it's correct, select Create commitment . The dialog box closes and returns to the CCD commitments details page.

### Status changes
