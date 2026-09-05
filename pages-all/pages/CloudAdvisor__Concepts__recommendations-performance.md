# Performance Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-performance.htm
- Fetched: 2026-09-05 01:47 CDT

# Performance Recommendations

This section of Recommendations describes the recommendations that help you optimize the performance of your resources.

Performance recommendations find overutilized resources and recommend adjustments. For example, performance recommendations show you how to improve performance by rightsizing overutilized compute instances, load balancers, and databases. They show you how to optimize performance settings by finding block volumes and boot volumes that aren't using the detached volume auto-tune feature.

## Rightsize Exadata Cloud VM Clusters

The Rightsize Exadata Cloud VM (ExaDB-D) clusters recommendation finds ExaDB-D clusters that are considered overutilized and may degrade performance. To improve performance, increase the number of enabled CPU cores for the cluster.

### Recommendation generation logic

- Cloud Advisor gathers telemetry data about the CPU utilization for every database server node of the system. Then it determines the algorithm from a user-configured profile setting similar to rightsize compute recommendation, according to the following profiles (thresholds):
- Conservative - If the CPU utilization is more than 95%, OCI recommends rightsizing the enabled CPU cores to a value that helps achieve an average CPU utilization of 85% .
- Standard - If the CPU utilization is more than 80%, OCI recommends rightsizing the enabled CPU cores to a value that helps achieve an average CPU utilization of 70% .
- Aggressive - If the CPU utilization is more than 60%, OCI recommends rightsizing the enabled CPU cores to a value that helps achieve an average CPU utilization of 50% .
- Cloud Advisor uses your configured profile settings and threshold (default is 80% for CPU) to determine if the average of all of the database server nodes average the CPU utilizations during the last seven days (the number of days is customizable) is above the threshold. If it is, Cloud Advisor identifies the ExaCS cluster as overutilized.

For example, if a customer is running an ExaCS X8 cluster on full rack with 24 enabled cores and Cloud Advisor determines that the infrastructure is overutilized, Cloud Advisor recommends rightsizing the enabled core count for the infrastructure to a value of 32 or higher. The node count remains the same.

### Implementing the recommendation

Cloud Advisor does not support a fix-it operation for this recommendation. The only implementation method available for this recommendation is to do it manually. To manually adjust the number of enabled CPU cores, see[To scale CPU cores in an Exadata Cloud Infrastructure cloud VM cluster or DB system](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-manage-infrastructure.html#GUID-4EEDDECE-6622-4BB4-B3EE-39C23097D779).

### Status changes

After you implement the recommendation manually, the status changes to Implemented after the next Cloud Advisor scan (typically within 24 to 48 hours).

## Rightsize Base Database System

The Rightsize Base Database (BaseDB) System recommendation indicates that a BaseDB system is overutilized, which may degrade its performance. To improve the system performance, cloud advisor recommends scaling up the shape of the BaseDB system.

### Recommendation generation logic

- Cloud Advisor gathers telemetry data about the CPU utilization for every database server node of the system. Then it determines the algorithm from a user-configured profile setting similar to rightsize compute recommendation, according to the following profiles (thresholds):
- Conservative - If the CPU utilization is more than 95%, OCI recommends rightsizing to the next available higher shape.
- Standard - If the CPU utilization is more than 80%, OCI recommends rightsizing to the next available higher shape.
- Aggressive - If the CPU utilization is more than 60%, OCI recommends rightsizing to the next available higher shape.
- Cloud Advisor uses your configured profile settings and threshold (default is 80% for CPU) to determine if the average of all of the database server nodes average the CPU utilizations during the last seven days (the number of days is customizable) is above the threshold. If it is, Cloud Advisor identifies the BaseDB system as overutilized. For example if a customer is running a BaseDB system on database server nodes having shape VM.Standard2.16 instance and Cloud Advisor determines that the BaseDB system is overutilized, it recommends downsizing the BaseDB system to a higher shape such as VM.Standard2.24 (or higher configuration) based on the current utilization. The node count remains the same.

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

### Implementing the recommendation

To implement the recommendation, do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- Manually adjust the system CPUs. See +[Change the Shape of a DB System](https://docs.oracle.com/en/cloud/paas/base-database/shape-dbs/index.html).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual shape adjustment), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Rightsize Compute Instances

The`Rightsize Compute Instances`recommendation indicates that a compute instance doesn't have the shape needed for optimal performance. Implementing this recommendation improves compute instance performance.

### Recommendation generation logic

Cloud Advisor gathers the CPU and Memory utilization over the selected interval (default seven days) to see if the usage is above the thresholds as specified by the[recommendation profile](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/cloudadvisor-customizing-profiles.htm#upsize-compute-profile). Based on the methodology of the recommendation profile, Cloud Advisor either uses the Average or P95 statistic for the CPU utilization during evaluation.

For the identified instances, Cloud Advisor suggests new shapes with higher configurations.

To customize the logic for this recommendation, see[Editing a Global Recommendation Override](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/customizing-overrides-console-edit-global.htm).

### Supported shapesCloud Advisor scans support the following shapes using`Rightsize Compute Instances`:

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

### Implementing the recommendation
Note  
  
Before rightsizing compute instances, confirm sufficient[service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). If needed, request a service limit increase.

To implement the recommendation, do one of the following:
- 

Select the resource, select Implement selected, and then follow the fix-it flow. See[Implementing Cloud Advisor recommendations](https://docs.oracle.com/iaas/Content/CloudAdvisor/Tasks/implementing_cloud_advisor_recommendations.htm). New shapes are suggested.
- 
To manually adjust compute instances, do one of the following:
- Use[Autoscaling](https://docs.oracle.com/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)to automatically adjust the number of compute instances in an instance pool.
- To increase the number of OCPUs and amount of memory assigned to the instance, select a new shape. See[Changing the Shape of an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual adjustment), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Rightsize Load Balancers

The Rightsize Load Balancers recommendation indicates that a load balancer doesn't have the bandwidth or shape needed for optimal performance. Implementing this recommendation improves load balancer performance.

### Recommendation generation logic

Cloud Advisor detects if the average of the maximum values for peak bandwidth usage over the evaluation period is more than the threshold percent of maximum bandwidth as specified by the[recommendation profile](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/cloudadvisor-customizing-profiles.htm#upsize-lb-profile). For the identified load balancers, Cloud Advisor suggests increasing the maximum bandwidth value by 25%. The minimum bandwidth value remains the same.

For dynamic shapes, we recommend converting to flexible shape where the current bandwidth of dynamic shape is selected as the minimum bandwidth value. The maximum bandwidth is set to be 25% higher than the current bandwidth of the dynamic shape.

To customize the logic for this recommendation, see[Editing a Global Recommendation Override](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/customizing-overrides-console-edit-global.htm).

### Implementing the recommendation
Note  
  
Before rightsizing load balancers, confirm sufficient[service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). If needed, request a service limit increase.

To implement the recommendation, do one of the following:
- Select the resource, select Implement selected, and then follow the fix-it flow. See[Implementing Cloud Advisor recommendations](https://docs.oracle.com/iaas/Content/CloudAdvisor/Tasks/implementing_cloud_advisor_recommendations.htm).
Important  
  
If the load balancer uses a dynamic shape, this recommendation switches it to a flexible shape. After you switch to a flexible shape, you can't revert the load balancer to a dynamic shape.

This recommendation changes the maximum bandwidth only. The minimum bandwidth remains unchanged.
- 

Manually increase the load balancer's maximum bandwidth or convert the load balancer to a suggested shape. See[Changing a Load Balancer's Bandwidth Shape](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manual adjustment, either from dynamic to flexible shape or adjustment of existing flexible shape), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Enable Performance Auto-tuning for Detached Block Volumes

The Enable performance auto-tuning for detached block volumes recommendation indicates that a block volume is using suboptimal performance settings. Implementing this recommendation adjusts the performance level to lower costs (0 VPUs/GB) when the volume is detached. When the volume is reattached, the performance is adjusted back to the performance level specified by the default VPUs/GB setting. With the detached volume auto-tune feature enabled, you don't need to continually manage volume resources.

For more information about the auto-tune feature, see[Detached Volume Performance Autotuning](https://docs.oracle.com/iaas/Content/Block/Tasks/detached-perf.htm).

### Recommendation generation logic

Cloud Advisor identifies block volumes that don't have the detached volume auto-tune feature enabled.

### Implementing the recommendation
To implement the recommendation, do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- Manually enable auto-tuning. See[Detached Volume Performance Autotuning](https://docs.oracle.com/iaas/Content/Block/Tasks/detached-perf.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manually enabling auto-tuning), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
- Manual implementation: The status changes after the next Cloud Advisor scan for your tenancy (typically within 24 to 48 hours).

## Enable Performance Auto-tuning for Detached Boot Volumes

The Enable Performance Auto-tuning for Detached Boot Volumes recommendation indicates that a boot volume is using suboptimal performance settings. Implementing this recommendation adjusts the performance level to lower costs (0 VPUs/GB) when the volume is detached. When the volume is reattached, the performance is adjusted back to the performance level specified by the default VPUs/GB setting. With the detached volume auto-tune feature enabled, you don't need to continually manage volume resources.

For more information about the auto-tune feature, see[Detached Volume Performance Autotuning](https://docs.oracle.com/iaas/Content/Block/Tasks/detached-perf.htm).

### Recommendation generation logic

Cloud Advisor identifies boot volumes that don't have the detached volume auto-tune feature enabled.

### Implementing the recommendation
To implement the recommendation, do one of the following:
- Select the resource, then select Implement selected , and then follow the fix-it flow. See[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).
- Manually enable auto-tuning. See[Detached Volume Performance Autotuning](https://docs.oracle.com/iaas/Content/Block/Tasks/detached-perf.htm).

### Status changes

When you implement the recommendation (Cloud Advisor fix-it flow or manually enabling auto-tuning), its status changes from Pending to Implemented . The time needed to reflect this status change depends on the method used to implement the recommendation.
- Cloud Advisor fix-it flow: The status changes when the work request completes.
-
