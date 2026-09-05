# Managing Ingress Controllers
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmanagingresscontrollers.htm
- Fetched: 2026-09-05 01:55 CDT

# Managing Ingress Controllers

Find out about the Kubernetes ingress controllers you can set up in clusters you create using Kubernetes Engine (OKE).

A Kubernetes ingress controller implements the rules and configuration options defined in a Kubernetes ingress to load balance and route incoming traffic to service pods running on worker nodes in a cluster.

A Kubernetes ingress is a kind of Kubernetes resource that comprises a collection of routing rules and configuration options to handle HTTP and HTTPS traffic originating from outside the cluster. You can use a single ingress resource to consolidate routing rules for multiple services, thereby avoiding the need for a Kubernetes service of type LoadBalancer (and associated OCI load balancer) to be created for each service that is to receive traffic from the internet or from a private network.

When you create clusters using Kubernetes Engine, you can set up:
- The OCI native ingress controller. The OCI native ingress controller creates an OCI flexible load balancer to handle requests and route them according to the rules defined for the ingress resource. The OCI native ingress controller also updates the load balancer configuration if the routing rules change. See[Setting Up the OCI Native Ingress Controller on a Kubernetes Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller.htm).
- A third-party ingress controller, such as the Nginx ingress controller. You are responsible for explicitly installing and upgrading the third-party ingress controller separately from the cluster. When running as a pod on worker nodes, third-party ingress controllers perform a load balancing role and act as routers. As such, third-party ingress controllers potentially consume a significant amount of compute resource if the ingress controller has a lot of HTTPS traffic to encrypt and decrypt. See[Example: Setting Up an Nginx Ingress Controller on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupingresscontroller.htm)
