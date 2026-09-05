# Adding OCI Service Operator for Kubernetes to Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingosok.htm
- Fetched: 2026-09-05 01:54 CDT

# Adding OCI Service Operator for Kubernetes to Clusters

Find out how to add OCI Service Operator for Kubernetes to clusters you've created with Kubernetes Engine (OKE).

The OCI Service Operator for Kubernetes is an open source Kubernetes add-on that enables you to create, manage, and connect to Oracle Cloud Infrastructure resources (such as the[Autonomous AI Database service](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and the[MySQL HeatWave](https://docs.oracle.com/iaas/mysql-database/home.htm)service) using the Kubernetes API and Kubernetes tooling. Having installed the OCI Service Operator for Kubernetes, you can perform actions on Oracle Cloud Infrastructure resources using the Kubernetes API, without having to use the Oracle Cloud Infrastructure Console, CLI, or other developer tools. As a result, you can manage Oracle Cloud Infrastructure resources the same way you manage Kubernetes applications, reducing complexity and management overhead.

OCI Service Operator for Kubernetes is built using the open source[Operator Framework](https://operatorframework.io/)toolkit. The Operator Framework manages 'Kubernetes native applications' called Operators, in an effective, automated, and scalable way. An Operator implements and automates common activities in a piece of software running inside a Kubernetes cluster, by integrating natively with Kubernetes concepts and APIs. Operator Framework components include:
- The[Operator SDK](https://sdk.operatorframework.io/), which uses the[Kubernetes controller-runtime library](https://github.com/kubernetes-sigs/controller-runtime)to provide high-level APIs and abstractions to write operational logic, and tools for scaffolding and code generation.
- The[Operator Lifecycle Manager (OLM)](https://olm.operatorframework.io/), which extends Kubernetes to provide a declarative way to install, manage, and upgrade Operators on a cluster.

OCI Service Operator for Kubernetes enables you to provision and integrate with several Oracle Cloud Infrastructure services. For the full list of supported services, see[Supported Resources](https://github.com/oracle/oci-service-operator/blob/main/docs/reference/index.md)in the[OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator).

You can add OCI Service Operator for Kubernetes to clusters you've created with Oracle Cloud Infrastructure Kubernetes Engine to interact with the Oracle Cloud Infrastructure services listed above. Having added OCI Service Operator for Kubernetes to a cluster, you don't have to manually provision and de-provision the services each time you deploy or un-deploy an application on the cluster. Instead, you interact with the services by using kubectl to call the Operator Framework APIs implemented by OCI Service Operator for Kubernetes.

OCI Service Operator for Kubernetes is packaged as an Operator Lifecycle Manager (OLM) bundle to make it easy to install on Kubernetes clusters. The bundle contains all the required objects and definitions to install OCI Service Operator for Kubernetes on a cluster (such as CRDs, RBACs, configmaps, and deployments).

For more information about OCI Service Operator for Kubernetes, see the[OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator).

## Adding OCI Service Operator for Kubernetes to a Cluster

To add OCI Service Operator for Kubernetes to a cluster, follow the detailed instructions in the[OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator).

For convenience, here's a high-level summary of the steps involved:
- Install OCI Service Operator for Kubernetes. During this step, you will typically:
- Install the[Operator SDK](https://sdk.operatorframework.io/).
- Install the[Operator Lifecycle Manager (OLM)](https://olm.operatorframework.io/)
- Deploy OCI Service Operator for Kubernetes.

For more information, see the[OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator).
- Secure OCI Service Operator for Kubernetes. During this step, you will typically:
- Set up an Oracle Cloud Infrastructure user for use by OCI Service Operator for Kubernetes.
- Set up appropriate policies to control access to resources (according to the Oracle Cloud Infrastructure services to be used).
- Protect sensitive values by creating secrets.

The security configuration to choose will depend on your particular requirements. For more information, see the[OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator).
- Provision and bind to the required Oracle Cloud Infrastructure services. During this step, you will typically:
- Provide service provision request parameters.
- Provide service binding request parameters.
- Provide service binding response credentials.

The security configuration to choose will depend on your particular requirements. For more information, see the[OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator)
