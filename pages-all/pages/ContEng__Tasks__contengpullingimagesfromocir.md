# Pulling Images from Registry during Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengpullingimagesfromocir.htm
- Fetched: 2026-09-05 01:55 CDT

# Pulling Images from Registry during Deployment

Find out how to create a Docker registry secret, and how to specify the image to pull from Oracle Cloud Infrastructure Registry (along with the Docker secret to use) during deployment of an application to a cluster you've created using Kubernetes Engine (OKE).

During the deployment of an application to a Kubernetes cluster, you'll typically want one or more images to be pulled from a Docker registry. In the application's manifest file you specify the images to pull, the registry to pull them from, and the credentials to use when pulling the images. The manifest file is commonly also referred to as a pod spec, or as a deployment.yaml file (although other filenames are allowed).

If you want the application to pull images that reside in Oracle Cloud Infrastructure Registry, you have to perform two steps:
- You have to use kubectl to create a Docker registry secret. The secret contains the Oracle Cloud Infrastructure credentials to use when pulling the image. When creating secrets, Oracle strongly recommends you use the latest version of kubectl (see the[kubectl documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)).
- You have to specify the image to pull from Oracle Cloud Infrastructure Registry, including the repository location and the Docker registry secret to use, in the application's manifest file.

Note that you can configure clusters to only allow images to be pulled from Oracle Cloud Infrastructure Registry that have been signed by particular master encryption keys included in an image verification policy (see[Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengenforcingsignedimagesfromocir.htm)).

To create a Docker registry secret:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- 

In a terminal window, enter:

```

```

where:
- `<secret-name>`is a name of your choice, that you will use in the manifest file to refer to the secret . For example,`ocirsecret`
- `<region-key>`is the key for the Oracle Cloud Infrastructure Registry region you're using. For example,`iad`. See[Availability by Region](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability).
- `ocir.io`is the Oracle Cloud Infrastructure Registry name.
- `<tenancy-namespace>`is the auto-generated Object Storage namespace string of the tenancy containing the repository from which the application is to pull the image (as shown on the Tenancy Information page). For example, the namespace of the acme-dev tenancy might be`ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example,`acme-dev`).
- `<oci-username>`is the username to use when pulling the image. The username must have access to the tenancy specified by`<tenancy-name>`. For example,`jdoe@acme.com`

If your tenancy is federated with Oracle Identity Cloud Service, use the format`<domain-name>/<oci-username>`. For federated users, the`<domain-name>/<oci-username>`is displayed in the Profile menu in the Console. For example, if your tenancy is federated with Oracle Identity Cloud Service, and your username is`jdoe@acme.com`, then enter`oracleidentitycloudservice/jdoe@acme.com`
- `'<oci-auth-token>'`is the auth token of the user specified by`<oci-username>`. For example,`k]j64r{1sJSSF-;)K8`. If the auth token contains some special characters (such as the parenthesis in this example), which is often the case, surround the auth token with single quotes. Otherwise, single quotes are not required.
- `<email-address>`is an email address. An email address is required, but it doesn't matter what you specify. For example,`jdoe@acme.com`

Note that strings containing some special characters (such as parentheses) must be surrounded by single quotes.

For example, combining the previous examples, you might enter:

```

```

Having created the Docker secret, you can now refer to it in the application manifest file.

To specify the image to pull from Oracle Cloud Infrastructure Registry, along with the Docker secret to use, during deployment of an application to a cluster:
- Open the application's manifest file in a text editor.
- 

Add the following sections to the manifest file:
- Add a`containers`section that specifies the name and location of the container you want to pull from Oracle Cloud Infrastructure Registry, along with other deployment details.
- Add an`imagePullSecrets`section to the manifest file that specifies the name of the Docker secret you created to access the Oracle Cloud Infrastructure Registry.

Here's an example of what the manifest might look like when you've added the`containers`and`imagePullSecrets`sections:

```

```

-
