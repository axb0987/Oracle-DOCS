# Profile Descriptions
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-customizing-profiles.htm
- Fetched: 2026-09-05 01:47 CDT

# Profile Descriptions

You can change the parameters in the profiles of some recommendations to tailor the operation of the recommendations to meet your requirements.

## Downsize Underutilized Compute Instances Profiles

The following profiles are available for the Downsize Underutilized Compute Instances recommendation type.

### Average Method Profile Descriptions

If you choose the average method, the mean CPU utilization is used when evaluating compute instances. The profile options with the average method are:
- 

Conservative (Average): The conservative profile identifies all compute instances that have had the following:
- an average CPU utilization less than 5%
- a maximum memory utilization less than 10%
- a maximum network utilization less than 3%

Supported VNICs are also considered. If a resize is recommended, the recommended core count has a projected average CPU utilization less than 10%.
- 

Standard (Average): The standard profile identifies all compute instances that have had the following:
- an average CPU utilization less than 10%
- a maximum memory utilization less than 10%
- a maximum network utilization less than 3%

Supported VNICs are also considered. If a resize is recommended, the recommended core count has a projected average CPU utilization less than 20%.
- 

Aggressive (Average): The Aggressive profile identifies all compute instances that have had the following:
- an average CPU utilization less than 15%
- a maximum memory utilization less than 10%.
- a maximum network utilization less than 3%

Supported VNICs are also considered. If a resize is recommended, the recommended core count has a projected average CPU utilization less than 30%.

### P95 Method Profile Descriptions
- 

If you choose the P95 method, a p-value of 95 is used to evaluate the CPU utilization threshold. The profile options with the P95 method are:
- 

Conservative (P95): The conservative profile identifies all compute instances that have had the following:
- a P95 CPU utilization less than 5%
- a maximum memory utilization less than 10%
- a maximum network utilization less than 3%

Supported VNICs are also considered. If a resize is recommended, the recommended core count has a projected P95 CPU utilization less than 10%.
- 

Standard (P95): The standard profile identifies all compute instances that have had the following:
- a P95 CPU utilization less than 10%
- a maximum memory utilization less than 10%
- a maximum network utilization less than 3%

Network throughput and supported VNICs are also considered. If a resize is recommended, the recommended core count has a projected P95 CPU utilization less than 20%.
- 

Aggressive (P95): The aggressive profile identifies all compute instances that have had the following:
- a P95 CPU utilization of less than 15%
- a maximum memory utilization of less than 10%
- a maximum network utilization less than 3%
- 

Network throughput and supported VNICs are also considered. If a resize is recommended, the recommended core count has a projected P95 CPU utilization less than 30%.

## Downsize Underutilized Load Balancers Profiles

The following profiles are available for the Downsize Underutilized Load Balancers recommendation type. All profile options use the average methodology.

### Profile Descriptions

For these profiles, the`PeakBandwidth`metric is used. Peak bandwidth measures the maximum bandwidth per second used during the specified interval. For more details, see[Load Balancer Metrics](https://docs.oracle.com/iaas/Content/Balance/Reference/loadbalancermetrics.htm#Load_Balancing_Metrics). Cloud Advisor pulls the metric every three hours and averages the values over the specified evaluation period.
- 

Conservative: The conservative profile identifies all load balancers for which the average of the maximum values for peak bandwidth usage over the evaluation period is less than 85% of the minimum network bandwidth.
- 

Standard: The standard profile identifies all load balancers for which the average of the maximum values for peak bandwidth usage over the evaluation period is less than 90% of the minimum network bandwidth.
- 

Aggressive: The aggressive profile identifies all load balancers for which the average of the maximum values for peak bandwidth usage over the evaluation period is less than 95% of the minimum network bandwidth.

## Rightsize Compute Instances Profiles

The following profiles are available for the Rightsize Compute Instances recommendation type.

### Average Methodology Profile Descriptions

If you choose the average methodology, the mean CPU utilization is used when evaluating compute instances. The profile options with the average methodology are:
- 

Conservative (Average): The conservative profile identifies all compute instances that have had both:
- an average CPU utilization greater than 95% and
- a maximum memory utilization greater than 95%
- 

Standard (Average): The standard profile identifies all compute instances that have had both:
- an average CPU utilization greater than 80% and
- a maximum memory utilization greater than 80%
- 

Aggressive (Average): The Aggressive profile identifies all compute instances that have had both:
- an average CPU utilization greater than 60% and
- a maximum memory utilization greater than 60%

### P95 Methodology Profile Descriptions

If you choose the P95 methodology, a p-value of 95 is used to evaluate the CPU utilization threshold. The profile options with the P95 methodology are:
- 

Conservative (P95): The conservative profile identifies all compute instances that have had both:
- a P95 CPU utilization greater than 95% and
- a maximum memory utilization greater than 95%
- 

Standard (P95): The standard profile identifies all compute instances that have had both:
- a P95 CPU utilization greater than 80% and
- a maximum memory utilization greater than 80%
- 

Aggressive (P95): The aggressive profile identifies all compute instances that have had both:
- a P95 CPU utilization greater than 60% and
- a maximum memory utilization greater than 60%

## Rightsize Load Balancers Profiles

The following profiles are available for the Rightsize Load Balancers recommendation type. All profile options use the average methodology.

### Profile Descriptions

For these profiles, the`PeakBandwidth`metric is used. Peak bandwidth measures the maximum bandwidth per second used during the specified interval. For more details, see[Load Balancer Metrics](https://docs.oracle.com/iaas/Content/Balance/Reference/loadbalancermetrics.htm). Cloud Advisor pulls the metric every three hours and averages the values over the specified evaluation period.
- 

Conservative: The conservative profile identifies all load balancers for which the average of the maximum values for peak bandwidth usage over the evaluation period is more than 95% of the maximum network bandwidth.
- 

Standard: The standard profile identifies all load balancers for which the average of the maximum values for peak bandwidth usage over the evaluation period is more than 85% of the maximum network bandwidth.
-
