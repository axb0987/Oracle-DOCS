# Installing the OCI Native Ingress Controller as a Standalone Program
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-installing-creating-resources.htm
- Fetched: 2026-09-05 01:56 CDT

# Installing the OCI Native Ingress Controller as a Standalone Program

Find out how to install the OCI native ingress controller as a standalone program.

When you have completed the prerequisites, you can deploy the OCI native ingress controller as a standalone program. See[Installing the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-installing-creating-resources.htm#contengsettingupnativeingresscontroller-deployment).

Note that having installed the OCI native ingress controller cluster add-on as a standalone program, before you can use it you also have to create the necessary Kubernetes ingress-related resources. See[Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm).

## Installing the OCI Native Ingress Controller

You can use the Helm CLI in two ways to install the OCI native ingress controller and deploy the required resources:
- Use Helm to install the OCI native ingress controller. With this approach, you use the`helm install`command. Helm manages OCI native ingress controller releases for initial installation and subsequent upgrades. During installation, the required resources are deployed on the cluster using parameter values obtained from the values.yaml file where available.
- Use Helm to generate .yaml manifest files. With this approach, you use the Helm CLI to generate a list of manifest .yaml files to hold all Kubernetes resources required for the OCI native ingress controller installation. You can use these .yaml files with any API server client, such as kubectl. The manifest .yaml files are populated with parameter values obtained from the values.yaml file where available. This method of installation enables you to subsequently customize the manifest .yaml files and override parameter values obtained from the values.yaml file.

### Installing the OCI native ingress controller using the helm install command

To install the OCI native ingress controller using the`helm install`command:
- In the local Git repository, navigate to the`oci-native-ingress-controller`directory.
- Install the OCI native ingress controller using Helm by entering:

```

```

During installation, the required Kubernetes resources are deployed on the cluster using parameter values obtained from the values.yaml file where available.
- Confirm that you have successfully installed the OCI native ingress controller by entering:

```

```

Example output:
```

```

### Installing the OCI native ingress controller using generated manifest files

To install the OCI native ingress controller using generated manifest files:
- In the local Git repository, navigate to the`oci-native-ingress-controller`directory.
- Generate the manifest .yaml files for the required resources into a`/manifests`directory, by entering:

```

```

The manifest .yaml files are created for the required resources, populated with parameter values obtained from the values.yaml file where available.

If necessary, you can customize the manifest .yaml files before deploying the required resources.
- Deploy the required resources using the manifest .yaml files:
- Deploy the required resources defined in the crd .yaml files by entering:

```

```

- Deploy the required resources defined in the template .yaml files by entering:

```

```

- Confirm that you have successfully installed the OCI native ingress controller by entering:

```

```

Example output:
```

```
