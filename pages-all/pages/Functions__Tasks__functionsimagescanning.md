# Scanning Function Images for Vulnerabilities
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsimagescanning.htm
- Fetched: 2026-09-05 02:08 CDT

# Scanning Function Images for Vulnerabilities

Find out how to enable and disable scans of function images pushed to Container Registry using OCI Functions, and how to check scan results for vulnerabilities found in those function images.

In OCI Functions, a function's definition specifies the Docker image to push to, and pull from, a repository in Oracle Cloud Infrastructure Registry.

You can set up Oracle Cloud Infrastructure Registry (also known as Container Registry) to scan function images when they are pushed to a function's repository. The function images are scanned for security vulnerabilities published in the publicly available Common Vulnerabilities and Exposures (CVE) database. See[Scanning Images for Vulnerabilities](https://docs.oracle.com/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm).

To perform function image scanning, Container Registry makes use of the Oracle Cloud Infrastructure Vulnerability Scanning service and Vulnerability Scanning REST API (see[Container Image Targets](https://docs.oracle.com/iaas/Content/scanning/using/managing-image-targets.htm)in the Vulnerability Scanning service documentation). Note that you must give the Vulnerability Scanning service permission to pull images from Container Registry (see[Required IAM Policy for Scanning Function Images for Vulnerabilities](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsimagescanning.htm#functionsimagescanning_permissions)).

You enable function image scanning by adding an image scanner to the function's repository. From then on, any images pushed to that repository are scanned for vulnerabilities by the image scanner. If the repository already contains images, the four most recently pushed images are immediately scanned for vulnerabilities. You can disable image scanning on a particular repository by removing the image scanner. See[Using the Console to Enable and Disable Image Scanning](https://docs.oracle.com/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm#console3).

Whenever new vulnerabilities are added to the CVE database, Container Registry automatically re-scans images in repositories that have scanning enabled.

You can view the results of image scans in the Console (see[Using the Console to View Results of Image Scans](https://docs.oracle.com/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm#unique_1256655158)). For every scanned function image, you can view:
- A summary of each scan of the image for the last 13 months, showing the number of vulnerabilities found in each scan, and a single overall risk level for each scan. Image scan results are retained for 13 months to enable you to compare the scan results over time.
- Detailed results of each image scan, to see a description of each vulnerability, along with its risk level, and (where available) a link to the CVE database for more information.

Always use the latest FDK build-time and runtime base images to reduce the number of known vulnerabilities included in an image and reported in the scan results. See[How to upgrade an existing function to use the latest FDK build-time and runtime base image version for a supported language](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssupportedlanguageversions.htm#functionssupportedlanguageversions_topic_How_to_upgrade_a_function).

## Required IAM Policy for Scanning Function Images for Vulnerabilities

If you enable repositories for image scanning, you must give the Vulnerability Scanning service permission to pull images from Container Registry.
To grant this permission for all images in the entire tenancy:
```

```
