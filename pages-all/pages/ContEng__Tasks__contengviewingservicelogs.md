# Viewing Kubernetes Engine (OKE) Service Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingservicelogs.htm
- Fetched: 2026-09-05 01:57 CDT

# Viewing Kubernetes Engine (OKE) Service Logs

Find out how to view the logs of Kubernetes processes (such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver) running on the control plane of clusters you've created using Kubernetes Engine (OKE).

Having created a cluster using Kubernetes Engine, you can use Oracle Cloud Infrastructure Logging to view and search the logs of Kubernetes processes running on the cluster's control plane. The Kubernetes control plane process logs are available in Oracle Cloud Infrastructure Logging as logs for the Kubernetes Engine service, where they are referred to as service logs.

The following Kubernetes control plane process logs are available for Kubernetes Engine as service logs:
- The kube-scheduler log, containing errors and events within the kube-scheduler process (such as scheduler decisions).
- The kube-controller-manager log, containing errors and events within the kube-controller-manager process (such as reconciling the deployment).
- The cloud-controller-manager log, containing errors and events within the cloud-controller-manager process (such as provisioning the load balancer).
- The kube-apiserver log, containing errors and events within the kube-apiserver process (for every request sent to the Kubernetes API server).

The service logs are configured at the default Kubernetes log level verbosity (`v=2`). At this level, the service logs contain useful steady state information about the service, and important log messages that might correlate to significant changes in the system.

You'll find the service logs useful when troubleshooting cluster issues such as:
- Cluster control plane virtual machine(s) shutdowns.
- Network partitioning issues within a cluster, or between the cluster and users.
- Kubernetes software crashes.
- Data loss or unavailability of persistent storage.
- Operator errors, such as misconfigured Kubernetes or application software.

Having enabled and configured service logs, you can subsequently view the service logs.

For more information about service logs, see[Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm).

Note that in addition to viewing the Kubernetes Engine service logs, you can also:
- Monitor the overall status of the cluster itself, node pools, and nodes. See[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).
- View log events in the Oracle Cloud Infrastructure Audit. See[Viewing Kubernetes API Server Audit Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringoke.htm).
- View application logs on managed node compute instances. See[Viewing Application Logs on Managed Nodes and Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm).
- Monitor the health, capacity, and performance of clusters, node pools, and nodes at a more granular level using metrics , alarms , and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). See[Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengmetrics.htm).

## Using the Console

To create a new service log object to enable you to view and search the logs of Kubernetes processes running on a cluster's control plane:
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Logs .
- Choose a Compartment you have permission to work in.
- Select Enable service log from the Actions menu to create a new service log.
- 

In the Enable Resource Log dialog:
- Identify the cluster, by specifying:
- Resource Compartment: Select the compartment to which the cluster belongs.
- Service: Select Container Engine for Kubernetes (Kubernetes Engine, OKE).
- Resource: Select the cluster for which you want to enable service logs.
- Configure the service log you want to view, by specifying:
- Log Category: Select the Kubernetes process for which you want to view the service log (for example, kube-controller-manager ), or select All log sources .
- Log Name: A name of your choosing for the new service log. Avoid entering confidential information.
- Optionally, select Advanced Options and specify:
- Log Location: The compartment in which to create the service log.
- Log group: The log group in which to place the service log. Optionally, select Create New Group to create a new log group (see[Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm)).
- Log retention: The length of time (in months) to retain the service log.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

A new service log is created, and the Log Details page is displayed.

To view and search the contents of a service log:
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Logs .
- Select the name of the service log that you want to view.
- (Optional) Select the Explore log tab to see log entries. You can sort log entries by age, and filter by time.
-
