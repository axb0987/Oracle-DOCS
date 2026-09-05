# Working with the OCI Native Ingress Controller as a Cluster Add-on
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-cluster-addon-top-level.htm
- Fetched: 2026-09-05 01:56 CDT

# Working with the OCI Native Ingress Controller as a Cluster Add-on

Find out how to set up the OCI native ingress controller as a cluster add-on, to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster.

Using the OCI native ingress controller as a cluster add-on rather than as a standalone program gives simplifies configuration and ongoing maintenance. You can more simply:
- Enable or disable the OCI native ingress controller.
- Opt into, and out of, automatic updates by Oracle.
- Select OCI native ingress controller add-on versions.
- Manage add-on specific customizations using approved key/value pair configuration arguments.

Note that if the OCI native ingress controller has already been deployed on the cluster as a standalone program, do not deploy the OCI native ingress controller cluster add-on on the cluster .

The sections below describe how to set up the OCI native ingress controller as a cluster add-on to load balance and route incoming traffic to service pods running on worker nodes in a cluster:
- [High Level Steps to Set Up the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-highlevelsteps.htm)
- [Prerequisites for deploying the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm)
- [Installing the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm)
- [Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm)
- [Configuring the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm)
- [Troubleshooting the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-troubleshooting.htm)
