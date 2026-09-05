# Signing Images for Security
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm
- Fetched: 2026-09-05 02:54 CDT

# Signing Images for Security

Find out how to sign images stored in Container Registry.

For compliance and security reasons, system administrators often want to deploy software into a production system only when they're satisfied that:
- 

The software comes from a trusted source.
- 

The software hasn't been modified since it was published, compromising its integrity.

To meet these requirements, you can sign images stored in Oracle Cloud Infrastructure Registry (also known as Container Registry). Signed images provide a way to verify both the source of an image and its integrity.

Container Registry enables users or systems to push images to the registry and then sign them using a master encryption key obtained from Oracle Cloud Infrastructure Vault, creating an image signature. An image signature associates a signed image with a particular master encryption key used to sign the image. An image can have multiple signatures, each created using a different master encryption key.

Users or systems pulling a signed image from Container Registry can be confident both that the source of the image is trusted, and that the image's integrity hasn't been compromised. To further enhance compliance and security, clients can be configured to only pull signed images from the registry.

At a high level, these are the steps to follow to store signed images in Container Registry:
- 

Build the image on your own machine or in your CI/CD system.
- 

Tag and push the image to Container Registry.
- 

If you don't have access to a master encryption key in Oracle Cloud Infrastructure Vault, either obtain access to an existing key or create a new key.
- 

Sign the image using the Container Registry CLI, creating an image signature that associates the image with the master encryption key and key version in the Vault service.

## Signing an Image and Creating an Image Signature

Having built an image and pushed it to Container Registry, you can sign the image using a master encryption key obtained from Oracle Cloud Infrastructure Vault, creating an image signature. Note that an image signature is associated with an image's OCID, making it specific to a particular push of the image.

To sign an image and create an image signature:
- 

Build an image on your own machine or in your CI/CD system (for example, using the`docker build`command).
- 

Push the image to Container Registry. Follow the instructions in[Pushing Images Using the Docker CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrypushingimagesusingthedockercli.htm)to:
- 

Log in to Container Registry using the`docker login`command.
- 

Tag the image you want to push using the`docker tag`command. For example:

```

```

- 

Push the image to Container Registry using the`docker push`command. For example:

```

```

- 

Obtain the OCID of the image, either using the Console (see[Getting an Image's Details](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm)), or using the CLI (use the`oci artifacts container image list --compartment-id <compartment_ocid> --repository-name <repository-name>`command).
- 

If you don't already have access to an RSA asymmetric key in Oracle Cloud Infrastructure Vault, either obtain access to an existing RSA asymmetric key or create a new master encryption key as an RSA asymmetric key (see[Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm)).

Note that the use of AES symmetric keys to sign images is not supported. For more information about different key types, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- 

Make a note of both the OCID of the master encryption key and the OCID of the key version stored in Oracle Cloud Infrastructure Vault. See[Listing Master Encryption Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm).
- 

Sign the image you pushed to Container Registry using the master key and key version in the Vault service, creating an image signature, by entering:

```

```

where:
- 

`--compartment-id <compartment-ocid>`is the OCID of the compartment to which the image's repository belongs. For example,`--compartment-id ocid1.compartment.oc1..aaaaaaaa23______smwa`
- 

`--kms-key-id <key-ocid>`is the OCID of the master encryption key to use to sign the image. For example,`--kms-key-id ocid1.key.oc1.phx.bbqehaq3aadfa.abyh______qlj`
- 

`--kms-key-version-id <key-version-ocid>`is the OCID of the key version to use to sign the image. For example,`--kms-key-version-id ocid1.keyversion.oc1.phx.0.bbqehaq3aadfa.acy6______mbb`
- 

`--signing-algorithm <signing-algorithm>`is one of the following algorithms to use to sign the image:
- 

`SHA_224_RSA_PKCS_PSS`
- 

`SHA_256_RSA_PKCS_PSS`
- 

`SHA_384_RSA_PKCS_PSS`
- 

`SHA_512_RSA_PKCS_PSS`

The algorithm to choose depends on the type of the master encryption key.

For example,`--signing-algorithm SHA_224_RSA_PKCS_PSS`
- 

`--image-id <image-ocid>`is the OCID of the image to sign . For example,`--image-id ocid1.containerimage.oc1.phx.0.ansh81vru1zp.aaaaaaaalqzj______yks`
- 

`--description <signature-description>`is optional text of your choice to describe the image. The description is included as part of the signature, and is shown in the Console. For example,`--description "Image for UAT testing"`
- 

`--metadata <image-metadata-json>`is optional information of your choice about the image, in a valid JSON format (alphanumeric characters only, with no whitespace or escape characters). For example,`--metadata {"buildnumber":"8447"}`

For example:

```

```

The image you specified is now signed. When you view the list of images in a repository in the Console, the image is shown as signed.

## Viewing Signed Images

You can use the Console to view the signed images in a repository.

To view signed images:
- 

On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).

The repository's details page opens.
- On the details page, select the Image versions tab.

All images in the repository, including their version identifiers, are displayed in a table.

The Signed column indicates which images have been signed.
- 

(Optional) From the list, select a signed image, and select the Signatures tab to view the signatures created when the image was signed.

## Working with Image Signatures

An image signature associates an image with the master key (obtained from the Vault service) that was used to sign the image. An image can have several signatures, each created using a different master encryption key.

Having signed an image in Container Registry and created an image signature, you can:
- 

View details of the signature.
- 

Verify the signature with the Vault service to confirm that the master encryption key used to sign the image is still valid and available.
- 

Add free-form tags and defined tags to the signature.
- 

Delete the signature to indicate that the image is no longer to be considered as trusted.

To view, verify, tag, or delete the signature(s) that was created when an image was signed:
- 

On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).

The repository's details page opens.
- 

On the details page, select the Image versions tab.

All images in the repository, including their version identifiers, are displayed in a table.

The Signed column indicates which images have been signed.
- 

From the list, select a signed image, and select the Signatures tab to view details of the signatures created when the image was signed:
- 

Description : A description of the signature that was specified when the image was signed.
- 

Verification response : The result of the last attempt to verify the image signature with the Vault service.
- 

Tag : The number of free-form or defined tags applied to the image signature.
- 

Date : When the image was signed and the image signature created.
- 

(Optional) To see the master key, key version, and signing algorithm for a particular signature, select View key details from the Actions menu for the signature.
- 

(Optional) To verify a particular signature with the Vault service, select Verify signature from the Actions menu for the signature.

The Vault service checks that the source of the image had access to a valid private key when they pushed the image, and that the image hasn't been modified since it was pushed. If both conditions are met, the signature is shown with a Verified status. Users or systems pulling the image from the registry can be confident both that the source of the image is trusted, and that the image's integrity hasn't been compromised.

If image verification fails, check that you have access to the master key, and that it hasn't been deleted.
- 

(Optional) To add a free-form tag or a defined tag to a signature to which no tags have been applied yet, select Add tags from the Actions menu for the signature.

If one or more tags have already been applied to the signature, select View tags from the Actions menu for the signature and then select Add tags in the View tags dialog. For more information, see[Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm).
- 

(Optional) To delete a particular signature, select Delete signature from the Actions menu for the signature.

The signature is deleted and no longer shown on the Signatures tab. If the image has no other signatures, the Signed column beside the image name in the list of images in the repository indicates the image has not been signed.

## Using the CLI

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).

### To sign an image and create an image signature

Use the[oci artifacts container image-signature sign-upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image-signature/sign-upload.html)command and required parameters to sign an image and create an image signature:

```

```

For example:

```

```

### To verify a signed image using an image signature

Use the[oci artifacts container image-signature get-verify](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image-signature/get-verify.html)command and required parameters to verify a signed image using an image signature:

```

```

For example:

```

```

## Using the API

Run the[CreateContainerImageSignature](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImageSignature/CreateContainerImageSignature)operation to sign an image and create an image signature.

Run the[GetContainerImageSignature](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImageSignature/GetContainerImageSignature)operation to fetch an image signature, and the[Verify](https://docs.oracle.com/iaas/api/#/en/key/latest/VerifiedData/Verify)
