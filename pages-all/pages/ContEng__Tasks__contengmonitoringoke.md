# Viewing Kubernetes API Server Audit Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringoke.htm
- Fetched: 2026-09-05 01:55 CDT

# Viewing Kubernetes API Server Audit Logs

Find out how to view operations of both Kubernetes Engine (OKE) and the Kubernetes API server as log events in the Oracle Cloud Infrastructure Audit.

It's often useful to understand the context behind activities happening in a cluster. For example, to perform compliance checks, to identify security anomalies, and to troubleshoot errors by identifying who did what and when.

You can use the Oracle Cloud Infrastructure Audit service to view all operations performed by:
- Kubernetes Engine, which emits audit events whenever you perform actions on a cluster, such as create and delete.
- The Kubernetes API server, which emits audit events whenever you use tools like kubectl to make administrative changes to a cluster, such as creating a service. Kubernetes API server audit events are shown in the Oracle Cloud Infrastructure Audit service for clusters running Kubernetes version 1.13.x (or later). Note that events are only shown from 15 July, 2020 onward.

Note that in addition to viewing operations as described in this topic, you can also:
- Monitor the overall status of the cluster itself, node pools, and nodes. See[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).
- View and search the logs of Kubernetes processes (such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver) running in the cluster's control plane. See[Viewing Kubernetes Engine (OKE) Service Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingservicelogs.htm).
- Monitor the health, capacity, and performance of clusters, node pools, and nodes at a more granular level using metrics , alarms , and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). See[Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengmetrics.htm).

## Using the Console

To view operations performed by Kubernetes Engine and the Kubernetes API server as log events in the Oracle Cloud Infrastructure Audit service:
- Open the navigation menu , select Observability &amp; Management , and then from Logging select Audit .
- Choose a Compartment you have permission to work in.
- 

Search and filter to show the operations you're interested in:
- To view operations performed by Kubernetes Engine, enter`ClustersAPI`in the Keywords field and select Search .
- To view operations performed by the Kubernetes API server, enter`OKE API Server Admin Access`in the Keywords field and select Search .

For more information about using the Oracle Cloud Infrastructure Audit service, see[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following operation to list audit log events:
- [ListEvents](https://docs.oracle.com/iaas/api/#/en/audit/latest/AuditEvent/ListEvents)
