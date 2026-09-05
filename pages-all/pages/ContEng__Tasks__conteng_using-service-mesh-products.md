# Using Service Mesh Products on Clusters Created with Kubernetes Engine (OKE)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng_using-service-mesh-products.htm
- Fetched: 2026-09-05 01:54 CDT

# Using Service Mesh Products on Clusters Created with Kubernetes Engine (OKE)

Find out about using service mesh products on clusters you've created with Kubernetes Engine (OKE).

You can use Kubernetes service mesh products (such as Istio) with clusters you have created with Kubernetes Engine.

Service mesh products manage network communication between services in a Kubernetes cluster, by adding a dedicated infrastructure layer (a "service mesh") to applications running on the cluster. Service mesh products typically use sidecar proxies, a control plane, and a data plane to provide observability, security, and traffic management capabilities. These capabilities are provided transparently, without modifying the code of applications running on the cluster.

Note that service mesh products (such as Istio) are supported regardless of the CNI plugin you are using for pod networking (either the OCI VCN-Native Pod Networking CNI plugin or the flannel CNI plugin). Worker nodes must be running Kubernetes 1.26 (or later).

For more information and examples, see:
- [Using Istio on Clusters Created with Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-using-istio.htm)
- [Using OCI Service Mesh on Clusters created with Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengservice-mesh-intro-topic.htm)
