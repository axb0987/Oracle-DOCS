# Working with the OCI Native Ingress Controller as a Standalone Program
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-standalone-top-level.htm
- Fetched: 2026-09-05 01:56 CDT

# Working with the OCI Native Ingress Controller as a Standalone Program

Find out how to set up the OCI native ingress controller as a standalone program, to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster.

Using the OCI native ingress controller as a standalone program rather than as a cluster add-on gives you complete control and responsibility for configuration and ongoing maintenance, including:
- Installing a version of the OCI native ingress controller that is compatible with the version of Kubernetes running on the cluster.
- Specifying configuration arguments correctly.
- Manually upgrading the OCI native ingress controller when you upgrade a cluster to a new version of Kubernetes, to ensure the OCI native ingress controller is compatible with the cluster's new Kubernetes version.

The sections below describe how to set up the OCI native ingress controller as a standalone program to load balance and route incoming traffic to service pods running on worker nodes in a cluster:
- [High Level Steps to Set Up the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-highlevelsteps.htm)
- [Prerequisites for deploying the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm)
- [Installing the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-installing-creating-resources.htm)
- [Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm)
- [Configuring the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm)
- [Troubleshooting the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-troubleshooting.htm)
