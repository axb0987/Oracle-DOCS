# Creating Functions Using Pre-Built Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_creating_prebuilt.htm
- Fetched: 2026-09-05 02:07 CDT

# Creating Functions Using Pre-Built Functions

Find out how to create functions and applications with OCI Functions using pre-built functions.

## Overview

Pre-built Functions (PBFs) provide you with a catalog of ready-to-use tasks or actions implemented using Oracle Cloud Infrastructure Functions. You don't need to write, build, package, and maintain function code. Pre-built functions can leverage the existing integration between OCI Functions and other OCI services (such as Event Rules, and Connector Hub) to offer a seamless integration experience.

Examples of pre-built function tasks include:
- Automatically rotate the database secrets and generate newer versions in Vault.
- Send logs or metrics from Oracle Cloud Infrastructure Monitoring to external systems like Splunk using OCI Functions and Connector Hub.
- Clean up orphaned resources in a tenancy given a certain age in days.
- Read a zipped file from Object Store, unzip it, and push it to an Object Store.
- Zip files in an object storage bucket and store the zipped file in a destination bucket.

## Navigating to a Pre-Built Function

To navigate to pre-built functions from the OCI menu, perform the following steps:
- Sign in to the Console as a functions developer.
- Open the navigation menu and select Developer Services . Under Functions , select Pre-Built Functions .

The console displays the Pre-Built Functions page, showing a list of the pre-built functions you can select.

## Select Pre-Built Function

After navigating to the Pre-Built Functions page, select the function to create. The following pre-built function catalog pages provide details about each function:
- [APM Log Sender Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_apm_log_sender.htm)
- [Cost Reports FOCUS Converter Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_cost_reports_focus_converter.htm)
- [Database Secret Rotation with Wallet Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_database_secret_rotation_with_wallet.htm)
- [Database Secret Rotation without Wallet Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_database_secret_rotation_without_wallet.htm)
- [Document Generator Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_document_generator.htm)
- [Media Workflow Job Spawner Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_media_workflow_job.htm)
- [Object Storage File Extractor Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_object_storage_extractor.htm)
- [Object Storage File Zip Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_object_storage_file_zip.htm)
- [Zero Quota Policy Creator Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_zero_quota_policy_creator.htm)
