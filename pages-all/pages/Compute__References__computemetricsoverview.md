# Compute Metrics and Monitoring
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetricsoverview.htm
- Fetched: 2026-09-05 01:49 CDT

# Compute Metrics and Monitoring

You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

For details about enabling monitoring for compute instances, see[Compute Health Monitoring for Bare Metal Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)and[Enabling Monitoring for Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/enablingmonitoring.htm).

There are multiple Monitoring service metric namespaces related to compute resources:
- oci_computeagent: Metrics related to the activity level and throughput of compute instances, as emitted by the Compute Instance Monitoring plugin. See[Compute Instance Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm). To enable monitoring for compute instance metrics, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/enablingmonitoring.htm).
- oci_instancepools: Metrics related to the lifecycle state of instances in instance pools. See[Instance Pool Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/instancepoolmetrics.htm).
- oci_compute_instance_health: Metrics related to the accessibility and health of instances. See[Compute Instance Health Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm).
- oci_compute_infrastructure_health: Metrics related to the up/down status, health, and maintenance status of instances. This namespace focuses specifically on the underlying infrastructure for instances. See[Infrastructure Health Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm).
- oci_compute: Metrics related to the instance metadata service (IMDS) that provides information about running compute instances. See[Compute Management Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-management-metrics.htm).
- oci_vmi_resource_utilization: Agentless compute metrics helps you monitor the status of compute instances without the use of Oracle Cloud Agent. See[Agentless Compute Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics-topic-available-metrics-oci-vmi-resource-utilization.htm)
