# Scanning Images for Vulnerabilities
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm
- Fetched: 2026-09-05 02:54 CDT

# Scanning Images for Vulnerabilities

Find out how to scan images in a repository for security vulnerabilities with Container Registry.

It is not uncommon for the operating system packages included in images to have vulnerabilities. Managing these vulnerabilities enables you to strengthen the security posture of your system, and respond quickly when new vulnerabilities are discovered.

You can set up Oracle Cloud Infrastructure Registry (also known as Container Registry) to scan images in a repository for security vulnerabilities published in the publicly available Common Vulnerabilities and Exposures (CVE) database.

You enable image scanning by adding an image scanner to a repository. From then on, any images pushed to the repository are scanned for vulnerabilities by the image scanner. If the repository already contains images, the four most recently pushed images are immediately scanned for vulnerabilities.

Whenever new vulnerabilities are added to the CVE database, Container Registry automatically re-scans images in repositories that have scanning enabled.

For every scanned image, you can view:
- A summary of each scan of the image for the last 13 months, showing the number of vulnerabilities found in each scan, and a single overall risk level for each scan. Image scan results are retained for 13 months to enable you to compare the scan results over time.
- Detailed results of each image scan, to see a description of each vulnerability, along with its risk level, and (where available) a link to the CVE database for more information.

You can disable image scanning on a particular repository by removing the image scanner.

To perform image scanning, Container Registry makes use of the Oracle Cloud Infrastructure Vulnerability Scanning service and Vulnerability Scanning REST API. For more information about the Vulnerability Scanning service, see[Scanning Overview](https://docs.oracle.com/iaas/Content/scanning/using/overview.htm)and[Container Image Targets](https://docs.oracle.com/iaas/Content/scanning/using/managing-image-targets.htm).

You can integrate image scanning into your existing software development and deployment lifecycle. Having built an image, your CI/CD tool can use the regular`docker push`command to push the image to a repository in Container Registry that has image scanning enabled. Your CI/CD tool can obtain the results of the image scan using the Vulnerability Scanning REST API. Based on the results of the image scan, your CI/CD tool can then determine whether to move the image to the next stage in the lifecycle.

## Required IAM Policy for Scanning Images for Vulnerabilities

If you enable repositories for image scanning, you must give the Vulnerability Scanning service permission to pull images from Container Registry.
To grant this permission for all images in the entire tenancy:
```

```

To grant this permission for all images in a specific compartment:
```

```

## Using the Console to Enable and Disable Image Scanning

When you create a new repository, image scanning is disabled by default. You can use the Console to enable image scanning for a repository by creating a new image scanner. If image scanning has already been enabled, you can use the Console to disable it.

To enable image scanning for a repository:
- 

On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- 

Select Add scanner from the Actions menu and either accept the default settings (usually sufficient) or specify:
- 

Target name : Optionally, a name for the new image scanner.
- 

Create in compartment : The compartment in which to create the image scanner. The compartment to which the repository belongs is selected by default, but you can select an alternative compartment.
- 

Description : Optionally, a description of the scanner.
- 

Select the scan configuration to use.

A scan configuration identifies the images to scan, by designating the compartments to which images belong. You will typically select an existing scan configuration, or create a new scan configuration, that designates the compartment to which the repository itself belongs.
- 

Create new scan configuration : Scan images belonging to the compartment to which the repository itself belongs, by creating a new scan configuration. Enter a name for the new scan configuration, and select the compartment in which to create the new scan configuration. All the images in the repository will be scanned.
- 

Select existing scan configuration : Scan images belonging to the compartment(s) specified in an existing scan configuration. By default, you can see and select scan configurations belonging to the same compartment as the repository, but you can select scan configurations belonging to other compartments. All the images in the repository will be scanned, provided the repository belongs to one of the designated compartments in the existing scan configuration you select.
- 

Select Add scanner to create the new image scanner with the scan configuration you specified.

From now on, any images pushed to the repository are scanned for vulnerabilities by the image scanner. If the repository already contains images, the four most recently pushed images are immediately scanned for vulnerabilities.

To disable image scanning for a repository:
- 

On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- 

Select Remove scanner from the Actions menu.

## Using the Console to View Results of Image Scans

To view the results of image scans:
- 

On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- 

To see vulnerabilities detected in a particular image in the repository:
- 

On the details page, select the Image versions tab.

All images in the repository, including their version identifiers, are displayed in a table.
- 

Select the image.

The details page for the image opens.
- 

Select the Scan results tab to see a summary of each scan of the image for the last 13 months, showing:
- 

Risk level : The risk level posed by the image, derived by aggregating the risk levels of individual vulnerabilities found in the scan into a single overall risk level.
- 

Issues found : The number of vulnerabilities found in the scan.
- 

Scan started : and Scan completed : When the scan was run.
- 

(Optional) To see more information about the vulnerabilities found in a particular scan, select View details from the Action menu beside the scan on the Scan results tab to open the Scan details dialog showing:
- 

Issue : The name given to the vulnerability in the CVE database. Select the link to find out more information about it.
- 

Risk level : The severity level of the vulnerability. Critical is the highest level (for the most serious issues that should be your highest priority to resolve), followed by High , then Medium , then Low , and finally Minor (indicating the least serious issues that you still need to resolve, but which can be your lowest priority).
- 

Description : A description of the vulnerability.
- 

Select Close .

## Using the CLI

Use the Vulnerability Scanning CLI commands to scan images for vulnerabilities (see[Container Image Targets](https://docs.oracle.com/iaas/Content/scanning/using/managing-image-targets.htm)).

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the Vulnerability Scanning API to scan images for vulnerabilities (see[Container Image Targets](https://docs.oracle.com/iaas/Content/scanning/using/managing-image-targets.htm)
