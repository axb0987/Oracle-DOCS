# Signing Function Images and Enforcing the Use of Signed Images from Registry
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm
- Fetched: 2026-09-05 02:08 CDT

# Signing Function Images and Enforcing the Use of Signed Images from Registry

Find out how to sign function images, and how to enforce the use of signed images from Oracle Cloud Infrastructure Registry when deploying when deploying and invoking functions using OCI Functions.

For compliance and security reasons, system administrators often want to deploy software into a production system only when they are satisfied that:
- the software comes from a trusted source
- the software has not been modified since it was published, compromising its integrity

To meet these requirements, you can sign images stored in Oracle Cloud Infrastructure Registry. Signed images provide a way to verify both the source of an image and its integrity. Oracle Cloud Infrastructure Registry enables users or systems to push images to the registry and then sign them creating an image signature. An image signature associates an image with a master encryption key obtained from Oracle Cloud Infrastructure Vault.

Users or systems pulling a signed image from Oracle Cloud Infrastructure Registry can be confident both that the source of the image is trusted, and that the image's integrity has not been compromised. For more information, see[Signing Images for Security](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm).

To further enhance security, you can configure OCI Functions applications to only allow the creation, updating, deployment, and invocation of functions based on images in Oracle Cloud Infrastructure Registry that have been signed by particular master encryption keys. At a high level, these are the steps to follow:
- Obtain the master encryption keys from Oracle Cloud Infrastructure Vault to use to sign the images that are pushed to, and pulled from, Oracle Cloud Infrastructure Registry when creating, updating, deploying, and invoking functions.
- Create an image signature verification policy for the application. The signature verification policy defines the master encryption key that must be used to sign images that are pushed to, and pulled from, Oracle Cloud Infrastructure Registry when creating, updating, deploying, and invoking functions in the application.
- When using the`fn deploy`command to deploy functions in an application that has a signature verification policy, specify the master encryption key from the signature verification policy in the function's func.yaml file. When pushing the function's image to Oracle Cloud Infrastructure Registry using the Fn Project CLI, the Fn Project CLI signs the image with the master encryption key. See[Using the Fn Project CLI to Sign a Function Image for Deployment in an Application With a Signature Verification Policy](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm#functionsenforcingsignedimagesfromocir_topic_Deploy_Function_with_Signature_Verification_Policy_Fn_CLI).
- When using the Console or the`fn create function`command to create a new function in an application with a signature verification policy, base the function on an existing Docker image that has been signed by a master encryption key in the policy. See[Creating Functions from Existing Docker Images](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm). Similarly, when updating a function, always base the function on an existing image that has been signed by a master encryption key in the policy (see[Updating a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions.htm)). To find out how to sign images in Oracle Cloud Infrastructure Registry, see[Signing Images for Security](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm).

You invoke a function in an application that has a signature verification policy in exactly the same ways as functions in other applications. When the function is invoked, OCI Functions first verifies that the function's image in Oracle Cloud Infrastructure Registry has been signed with the encryption key specified in the application's signature verification policy. If encryption key verification is successful, OCI Functions pulls the image from Oracle Cloud Infrastructure Registry and invokes the function. If encryption key verification is unsuccessful, the error code and message (`status 502: message: FunctionImageVerificationFail: Image cannot be verified or no valid signature found`) are:
- returned to the caller
- shown in the Function Errors chart on the Metrics page in the Console
- shown in the default invocation span on the Traces page in the Console (when function tracing is enabled)

Note the following:
- You can include up to five functions in an application for which you define a signature verification policy. You cannot add a sixth function to such an application. Also note that you cannot define a signature verification policy for an existing application that already contains six or more functions.
- Before creating a signature verification policy for an existing application, make sure that any existing functions in the application are based on images that have already been signed by the master encryption key that you intend to specify in the policy. Otherwise, you will not be able to create the signature verification policy.
- An image in Oracle Cloud Infrastructure Registry can be signed using multiple signatures, each associated with a different master encryption key. Provided an application's signature verification policy includes one of the master encryption keys, the application allows the image to be pulled from Oracle Cloud Infrastructure Registry.
- If you enable an application to use its signature verification policy but OCI Functions cannot connect to Oracle Cloud Infrastructure Registry, no images can be pulled from Oracle Cloud Infrastructure Registry.

## Required IAM Policies for Enforcing the Use of Signed Images

To enforce a signature verification policy, OCI Functions must have been granted:
- Access to verify master encryption keys in Oracle Cloud Infrastructure Vault with a policy like:

```

```

If functions and encryption keys are in different tenancies:
- 
Use the following policies in the functions' tenancy:
```

```

- 
Use the following policies in the encryption keys' tenancy:
```

```

- Access to images in Oracle Cloud Infrastructure Registry.

If functions and images are in different tenancies:
- 
Use the following policies in the functions' tenancy:
```

```

- 
Use the following policies in the images' tenancy:
```

```

To create a signature verification policy, you must have been granted:
- access to master encryption keys in Oracle Cloud Infrastructure Vault with a policy like:

```

```

```

```

- access to images in Oracle Cloud Infrastructure Registry with a policy like:

```

```

You can restrict the master encryption keys that can be used for function image signing, and signature verification by using more restrictive policies (for examples, see[Policy Statements to Give the OCI Functions Service and OCI Functions Users Access to Oracle Vault Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#functionscreatingpolicies_topic_Create_a_Policy_to_Give_Oracle_Functions_Users_Access_to_Encryption_Key_Resources)).

## Obtaining Encryption Keys with which to Sign Function Images (if they don't exist already)

To obtain the master encryption key to include in an application's signature verification policy, and to specify when deploying a function in the application:
- 

If you don't already have access to an RSA or ECDSA asymmetric key in Oracle Cloud Infrastructure Vault, either obtain access to an existing RSA or ECDSA asymmetric key or create a new master encryption key as an RSA or ECDSA asymmetric key (see[Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm)).

Note that the use of AES symmetric keys to sign images is not supported. For more information about different key types, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- 

Make a note of both the OCID of the master encryption key and the OCID of the key version stored in Oracle Cloud Infrastructure Vault. See[Listing Master Encryption Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm).

You use these OCIDs when deploying the function.

## Creating a Signature Verification Policy for an Application

To define a signature verification policy for an application and specify a master encryption key that can be used to sign images:
- On the Applications list page, select the application for which you want to define a signature verification policy. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- Select the Configuration tab.
- Select Manage Signature Verification .
- Select Enable signature verification policies for this application to enable the application to use the signature verification policy you define.

If a policy to grant OCI Functions access to Oracle Cloud Infrastructure Registry does not already exist, you are prompted to create such a policy. If you're an administrator, create the policy. Otherwise, ask your administrator to create the policy for you. See[Required IAM Policies for Enforcing the Use of Signed Images](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm#functionsenforcingsignedimagesfromocir_topic_Required_IAM_policies).
- 

Select a master encryption key in Oracle Cloud Infrastructure Vault that must have been used to sign images.

If policies to grant OCI Functions access to the master encryption key in Oracle Cloud Infrastructure Vault do not already exist, you are prompted to create such policies. If you're an administrator, create the policies. Otherwise, ask your administrator to create the policies for you. See[Required IAM Policies for Enforcing the Use of Signed Images](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm#functionsenforcingsignedimagesfromocir_topic_Required_IAM_policies).

Note that any existing functions in the application must be based on images that have already been signed by the master encryption key that you select. Otherwise, you will not be able to create the signature verification policy.
- 

Select Save Changes .

From now on:
- When you deploy a function in this application (for example, using the`fn deploy`command), you have to set image signing options. These options identify the master encryption key in the application's signature verification policy, including the OCID of the master encryption key. Assuming you specify a valid master encryption key, the image is pushed to Oracle Cloud Infrastructure Registry and signed with the encryption key.
- When you create a new function (or update an existing function) in this application using the Console or the Fn Project CLI, you have to specify an existing image that has been signed using the master encryption key in the application's signature verification policy.
- When a function in this application is invoked, OCI Functions first verifies the image in Oracle Cloud Infrastructure Registry. OCI Functions only pulls the image from Oracle Cloud Infrastructure Registry and invokes the function if encryption key verification is successful.

## Using the Fn Project CLI to Sign a Function Image for Deployment in an Application With a Signature Verification Policy

You can use the Fn Project CLI command`fn deploy`command to deploy a function in an application that has a signature verification policy, by specifying the master encryption key from the signature verification policy in the function's func.yaml file. The function image is then signed during deployment.

To use the Fn Project CLI to deploy a function based on a signed function image in an application that has an enabled signature verification policy:
- 

Follow the steps in[Creating and Deploying Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm)to create a function using the`fn init`command, but do not immediately use the`fn -v deploy`command. Instead, follow the instructions below to first add image signing details to the function's func.yaml file, and then use the`fn -v deploy`command.
- Having used the`fn init`command to initialize the function, change directory to the newly created directory containing the function's func.yaml file.
- Edit the function's func.yaml file and add the following section:
```

```

where:
- `image_compartment_id: <root-compartment-ocid>`is the OCID of the tenancy's root compartment that owns the repository in Oracle Cloud Infrastructure Registry to which you are going to push the function image. For example,`image_compartment_id: ocid1.tenancy.oc1..aaaaaaaa___ta`.
- `kms-key-id: <key-ocid>`is the OCID of the master encryption key to use to sign the image. Since you will be deploying a function based on this image in an application with an enabled signature verification policy, you must specify the OCID of a master encryption key that is included in the signature verification policy (see[Creating a Signature Verification Policy for an Application](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm#functionsenforcingsignedimagesfromocir_topic_Create_Signature_Verification_Policy)). For example,`kms-key-id: ocid1.key.oc1.phx.bbqehaq3aadfa.abyh______qlj`
- `kms-key-version-id: <key-version-ocid>`is the OCID of the key version to use to sign the image. For example,`kms-key-version-id: ocid1.keyversion.oc1.phx.0.bbqehaq3aadfa.acy6______mbb`
- 

`signing-algorithm: <signing-algorithm>`is one of the following algorithms to use to sign the image:
- `SHA_224_RSA_PKCS_PSS`
- `SHA_256_RSA_PKCS_PSS`
- `SHA_384_RSA_PKCS_PSS`
- `SHA_512_RSA_PKCS_PSS`
- `SHA_224_RSA_PKCS1_V1_5`
- `SHA_256_RSA_PKCS1_V1_5`
- `SHA_384_RSA_PKCS1_V1_5`
- `SHA_512_RSA_PKCS1_V1_5`
- `ECDSA_SHA_256`
- `ECDSA_SHA_384`
- `ECDSA_SHA_512`

The algorithm to choose depends on the type of the master encryption key. For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with different hashing algorithms. For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms. For the latest list of supported algorithms, see[Sign](https://docs.oracle.com/iaas/api/#/en/key/release/SignedData/Sign)and the SignDataDetails resource in the Vault API documentation.

For example,`signing-algorithm: SHA_224_RSA_PKCS_PSS`

For example:
```

```

- In the directory containing the function's func.yaml file, enter the following single Fn Project command to build and deploy the function and its dependencies as a signed Docker image:
```

```

where`<app-name>`is the name of an application with an enabled image verification policy.

The image is built, pushed to the specified Docker registry, and signed with the master encryption key and key version specified in the func.yaml file. The function based on the signed image is successfully deployed to OCI Functions in the application with the enabled image verification policy that you specified in the command.

## Using the OCI CLI to Sign a Function Image for Deployment in an Application With a Signature Verification Policy

You can use the OCI CLI command`oci artifacts container image-signature sign-upload`to sign a function image after you have used the Fn Project CLI command`fn push`to push the image to Oracle Cloud Infrastructure Registry. You can then use the OCI CLI commands`oci fn function create`and`oci fn function update`to deploy a function based on the signed image in an application that has a signature verification policy.

To use the OCI CLI to deploy a function based on a signed function image in an application that has an enabled signature verification policy:
- 

Follow the steps in[Creating and Deploying Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm)to create a function, but do not use the`fn -v deploy`command. Instead of using`fn -v deploy`, follow the numbered steps below to:
- use the`fn -v build`command to build the function and its dependencies as a Docker image
- use the`fn -v push`command to tag and push the image to Container Registry
- use the`oci artifacts container image-signature sign-upload`command to sign the image
- use the`oci fn function create`command to create a function based on the signed image (or use the`oci fn function update`command to base an existing function on the signed image)
- Build the function and its dependencies as a Docker image using the`fn -v build`command. For example:
```

```

- 

Make a note of the image name shown in the output from the previous command.

For example, the image name might be`phx.ocir.io/ansh81vru1zp/helloworld/helloworld-func:0.0.1`
- Push the image to Container Registry using the`fn -v push`command. For example:
```

```

- Obtain the OCID of the image, either using the Console (see[Viewing Images and Image Details](https://docs.oracle.com/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm)), or using the CLI (use the`oci artifacts container image list --compartment-id <compartment-ocid> --repository-name <repository-name>`command).
- Sign the image you pushed to Container Registry using the master key and key version in the Vault service, creating an image signature, by entering:

```

```

where:
- `--compartment-id <compartment-ocid>`is the OCID of the compartment to which the image's repository belongs. For example,`--compartment-id ocid1.compartment.oc1..aaaaaaaa23______smwa`
- `--kms-key-id <key-ocid>`is the OCID of the master encryption key to use to sign the image. Since you will be creating a function based on this image in an application with an enabled signature verification policy, you must specify the OCID of a master encryption key that is included in the signature verification policy (see[Creating a Signature Verification Policy for an Application](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm#functionsenforcingsignedimagesfromocir_topic_Create_Signature_Verification_Policy)). For example,`--kms-key-id ocid1.key.oc1.phx.bbqehaq3aadfa.abyh______qlj`
- `--kms-key-version-id <key-version-ocid>`is the OCID of the key version to use to sign the image. For example,`--kms-key-version-id ocid1.keyversion.oc1.phx.0.bbqehaq3aadfa.acy6______mbb`
- 

`--signing-algorithm <signing-algorithm>`is one of the following algorithms to use to sign the image:
- `SHA_224_RSA_PKCS_PSS`
- `SHA_256_RSA_PKCS_PSS`
- `SHA_384_RSA_PKCS_PSS`
- `SHA_512_RSA_PKCS_PSS`
- `SHA_224_RSA_PKCS1_V1_5`
- `SHA_256_RSA_PKCS1_V1_5`
- `SHA_384_RSA_PKCS1_V1_5`
- `SHA_512_RSA_PKCS1_V1_5`
- `ECDSA_SHA_256`
- `ECDSA_SHA_384`
- `ECDSA_SHA_512`

The algorithm to choose depends on the type of the master encryption key. For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with different hashing algorithms. For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms. For the latest list of supported algorithms, see[Sign](https://docs.oracle.com/iaas/api/#/en/key/release/SignedData/Sign)and the SignDataDetails resource in the Vault API documentation.

For example,`--signing-algorithm SHA_224_RSA_PKCS_PSS`
- `--image-id <image-ocid>`is the OCID of the image to sign . For example,`--image-id ocid1.containerimage.oc1.phx.0.ansh81vru1zp.aaaaaaaalqzj______yks`
- `--description <signature-description>`is optional text of your choice to describe the image. The description is included as part of the signature, and is shown in the Console. For example,`--description "Image for UAT testing"`

For example:

```

```

The function image is now signed with the same master encryption key that is specified in the application's signature verification policy.
- 

If you want to create a new function based on the signed image, enter:

```

```

where:
- `<app-ocid>`is the OCID of the application with the enabled signature verification policy, in which to create the new function.
- `<function-name>`is the name of the new function you want to create. Avoid entering confidential information.
- `<image-name>`is the name of the signed image in the Docker registry on which to base the new function.
- `<memory>`is the maximum usable memory for the new function

For example:

```

```

A new function is successfully created in the application that has the signature verification policy. The function is based on the signed image and with the name you specified.
- 

If you want to update an existing function so that the function is based on the signed image, update the existing function by entering:

```

```

where:
- `<function-id>`is the OCID of the existing function you want to update.
- `<image-name>`is the name of the signed image in the Docker registry on which to base the function.

For example:

```

```
