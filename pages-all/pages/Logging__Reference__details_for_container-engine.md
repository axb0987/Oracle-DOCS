# Details for Kubernetes Engine
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_container-engine.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Kubernetes Engine

Logging details for Kubernetes Engine.

The following Kubernetes control plane process logs are available for Kubernetes Engine as service logs:
- The kube-scheduler log, containing errors and events within the kube-scheduler process (such as scheduler decisions).
- The kube-controller-manager log, containing errors and events within the kube-controller-manager process (such as reconciling the deployment).
- The cloud-controller-manager log, containing errors and events within the cloud-controller-manager process (such as provisioning the load balancer).
- The kube-apiserver log, containing errors and events within the kube-apiserver process (for every request sent to the Kubernetes API server).

The service logs are configured at the default Kubernetes log level verbosity (`v=2`). At this level, the service logs contain useful steady state information about the service, and important log messages that might correlate to significant changes in the system.

See[Viewing Kubernetes Engine (OKE) Service Logs](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengviewingservicelogs.htm)
