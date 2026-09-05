# NVIDIA AI Enterprise on OCI Compute
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/nvidia-ai-enterprise.htm
- Fetched: 2026-09-05 01:52 CDT

# NVIDIA AI Enterprise on OCI Compute

NVIDIA AI Enterprise (NVAIE) on OCI Compute offers a seamless enterprise-grade AI experience that minimizes deployment friction, accelerates adoption, and simplifies licensing and billing.

NVAIE artifacts require a specific set of NVIDIA GPU drivers and CUDA libraries. For Oracle Linux, platform images include NVAIE specific drivers. For Ubuntu, follow installation steps provided in documentation for OCI Ubuntu images. In addition, OCI provides a curated set of approximately 90 high-priority NVIDIA containers and Helm charts for Oracle environments. These artifacts include open-source models, NVIDIA NeMo containers for RAG and agentic workloads, and BioNeMo models for healthcare. You can request additional artifacts if your use cases are not in the current set of options. OCI ensures full version parity though regular syncs with NVIDIA’s NGC (NVIDIA’s container and artifact repository), including all metadata, scan results, and artifact details.

## Using NVAIE Images

NVIDIA AI Enterprise requires a specific set of GPU drivers to run its containers. OCI supports Ubuntu and Oracle Linux GPU operating systems. NVAIE-specific drivers included in the base images for Oracle Linux .

NVAIE Driver Requirements
- [NVIDIA Driver](http://www.nvidia.com/Download/index.aspx?lang=en-us)release 560 or later.

If you are running on a data center GPU, for example an NVidia A100, you can use NVIDIA driver release 470.57 or later, 535.86 or later, or 550.54 or later.
- NVIDIA Docker 23.0.1 or later.
- [CUDA 12.6.1 or later](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html).

## Creating an NVAIE Instance

To create an instance, follow the steps as described in[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).

When you reach the Image and Shape section, follow these steps.
- Select Change image .
- Select an Oracle Linux or Ubuntu image. Choose Select image .
- Under Shape select Change shape .
- For Instance type , select Bare metal machine .

All the available NVidia GPU shapes are displayed
- Select any available NVidia shape based on your deployment needs. Choose Select shape .
- To enable NVidia AI Enterprise for that instance, select Enable NVIDIA AI Enterprise .
- Select Next .
- Continue to complete the steps listed for[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).
- Select Create to create the instance.

## Creating an NVAIE Instance Configuration

Create an instance configuration to define an instance template you can use to create more instances. An instance configuration is required to create an Instance Pool.

To create an instance configuration, follow the steps as described in[Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm).

When you reach the Image and Shape section, follow these steps.
- Select Change image .
- Select an Oracle Linux or Ubuntu image. Choose Select image .
- Under Shape select Change shape .
- For Instance type , select Bare metal machine .

All the available NVidia GPU shapes are displayed
- Select any available NVidia shape based on your deployment needs. Choose Select shape .
- To enable NVidia AI Enterprise for that instance, select Enable NVIDIA AI Enterprise .
- Select Next .
- Continue to complete the steps listed for[Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm).
- Select Create to create the instance configuration.

## Creating an NVAIE Instance Pool

To create an instance pool, follow the steps as described in[Creating Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm).

In the basic details section, select the instance configuration you created using an NVidia shape.

Continue following the steps in[Creating Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm)until the instance pool is created.

## Using NVAIE Components from Marketplace

You can import NVAIE containers and Helm charts from Marketplace. Follow these steps to navigate to marketplace.
- From the main menu, select Marketplace .
- Under Marketplace select All applications . The main Marketplace page is displayed.
- Use the Type filter to select container images or Helm charts.
- For example, to identify NVAIE Helm charts you might type a string like`Llama-3.1-8B-Instruct-NIM-microservice`to display Llama 3 charts.

## Adding NVAIE Components to OCIR

Oracle Cloud Infrastructure Registry (OCIR), also known as Container Registry, is an Oracle-managed registry that makes it easy for you to store, share, and manage container images (such as Docker images). To add a NVAIE marketplace container to your OCIR, follow these steps.
- From the main menu, select Marketplace .
- Under Marketplace select All applications . The main Marketplace page is displayed.
- Use the Type filter to select Container images.
- Select a container.
- Select Export Package .
- Fill out the following information:
- Compartment: Select a compartment.
- OCI Registry: Select an existing registry or create a new one. The following steps are for creating a new registry.
- Registry name: Enter a name for your registry.
- Access: Select Private or Public .
- Accept terms and conditions for the container.
- Select Export . The OCIR instance is created and the selected NVAIE component is copied.

## Deploying an NVAIE Image to Docker

After you have created an NVAIE container image, you can deploy it to an instance. The following steps provide an example.
- Pull the container image from OCIR:

```

```

- Create a local cache.
Note  
  
This is an optional step, but the result keeps large weights off the writable layer.

```

```

- Run the container.

```

```

- Run a quick smoke test.

```

```

## Accessing NVidia AI Models From Regional S3 Buckets

During execution, the Multi-NIM container requires a model for its rendering initialization. At OCI, these models are stored in every region in OC1 (the commercial realm) in S3 buckets. The container consumes the following environment variables:

```

```

### Authorization

To access the NVIDIA AI bucket in each region you must be authorized with an access key ID and a secret access key. These keys need to be set up in your tenancy following this guide:[Creating a customer secret key.](https://docs.oracle.com/iaas/Content/Identity/access/to_create_a_Customer_Secret_key.htm)Store the keys and secrets in a secure Vault or secret service. Retrieve the keys when needed.

### Region

Home regions vary based on tenancy. For performance reasons, as a best practice pull models from the same region that the NVIDIA AI container runs in. To do this, identify the region identifier and set it in the environment parameters. The following guide outlines the various regions and associated region identifiers:[OCI Regions and identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

### Endpoint URL

After identifying your authorization and region, derive the endpoint URL (`AWS_ENDPOINT_URL`). Follow this guide:[Object Storage Dedicated Endpoints](https://docs.oracle.com/iaas/Content/Object/Concepts/dedicatedendpoints.htm).

S3 URLs follow this pattern for S3 compatibility:`<$namespace> .compat.objectstorage. <$region> .oraclecloud.com`.
- The &lt;$namespace&gt; value for Nvidia AI models is always`bmcinfraorch`.
- The &lt;$region&gt; value is the region identifier.

To access the bucket in Ashburn with identifier`us-ashburn-1`the endpoint URL is:`https://bmcinfraorch.compat.objectstorage.us-ashburn-1.oraclecloud.com/`

As a best practice, create a region variable similar to the following example:`https://bmcinfraorch.compat.objectstorage. ${region} .oraclecloud.com/`"

### Model Names

Models are accessible in each region via s3 buckets. Each model is organized under a root folder labeled`nvaie`.

For example:`s3repo://nvaie/`
To load Meta's Llama instruct LLM, the environment variable is set as follows:

```

```

### Wrapping Up

The following example docker script loads the Multi-Nim container version 1.14.0 and injects Meta's Llama instruct LLM in the Ashburn region.

```

```
