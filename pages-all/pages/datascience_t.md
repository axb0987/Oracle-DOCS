# Data Science Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#dcoc-content-body)

## Data Science Common Types

### DBMS_CLOUD_OCI_DATASCIENCE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_EXPORT_DETAILS_T Type

Details of Artifact source

Syntax
```

```

Fields

Field Description

`artifact_source_type`

(required) Source type where actually artifact is being stored

Allowed values are: 'ORACLE_OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_EXPORT_DETAILS_OBJECT_STORAGE_T Type

Model artifact source details for exporting artifact to service bucket

Syntax
```

```

`dbms_cloud_oci_datascience_artifact_export_details_object_storage_t`is a subtype of the`dbms_cloud_oci_datascience_artifact_export_details_t`type.

Fields

Field Description

`namespace`

(optional) The Object Storage namespace used for the request.

`source_bucket`

(optional) The name of the bucket. Avoid entering confidential information.

`source_object_name`

(optional) The name of the object resulting from the copy operation.

`source_region`

(optional) Region in which OSS bucket is present

### DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_IMPORT_DETAILS_T Type

Details of Artifact source

Syntax
```

```

Fields

Field Description

`artifact_source_type`

(required) Source type where actually artifact is being stored

Allowed values are: 'ORACLE_OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_IMPORT_DETAILS_OBJECT_STORAGE_T Type

Artifact destination details for importing to destination bucket

Syntax
```

```

`dbms_cloud_oci_datascience_artifact_import_details_object_storage_t`is a subtype of the`dbms_cloud_oci_datascience_artifact_import_details_t`type.

Fields

Field Description

`namespace`

(optional) The Object Storage namespace used for the request.

`destination_bucket`

(optional) The name of the bucket. Avoid entering confidential information.

`destination_object_name`

(optional) The name of the object resulting from the copy operation.

`destination_region`

(optional) Region in which OSS bucket is present

### DBMS_CLOUD_OCI_DATASCIENCE_LOG_DETAILS_T Type

The log details.

Syntax
```

```

Fields

Field Description

`log_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a log to work with.

`log_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a log group to work with.

### DBMS_CLOUD_OCI_DATASCIENCE_CATEGORY_LOG_DETAILS_T Type

The log details for each category.

Syntax
```

```

Fields

Field Description

`l_access`

(optional)

`predict`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_DATA_SCIENCE_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

The details required to change a private endpoint compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create private endpoint.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_JOB_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a job.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_JOB_RUN_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a job run.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a model.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_MODEL_DEPLOYMENT_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a model deployment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_MODEL_VERSION_SET_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a model version set.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved to.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_NOTEBOOK_SESSION_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a notebook session.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_PIPELINE_COMPARTMENT_DETAILS_T Type

Details for which compartment to move the resource to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_PIPELINE_RUN_COMPARTMENT_DETAILS_T Type

Details for which compartment to move the resource to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a project.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_DATA_SCIENCE_PRIVATE_ENDPOINT_DETAILS_T Type

The details required to create a Data Science private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the private endpoint.

`description`

(optional) A user friendly description. Avoid entering confidential information.

`display_name`

(optional) A user friendly name. It doesn't have to be unique. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`nsg_ids`

(optional) An array of network security group OCIDs.

`subnet_id`

(required) The OCID of the subnet.

`sub_domain`

(optional) Subdomain for a private endpoint FQDN.

`data_science_resource_type`

(required) Data Science resource type.

Allowed values are: 'NOTEBOOK_SESSION'

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_CONFIGURATION_DETAILS_T Type

The job configuration details

Syntax
```

```

Fields

Field Description

`job_type`

(required) The type of job.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type

The job infrastructure configuration details (shape, block storage, etc.)

Syntax
```

```

Fields

Field Description

`job_infrastructure_type`

(required) The infrastructure type used for job run.

Allowed values are: 'STANDALONE', 'ME_STANDALONE'

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_LOG_CONFIGURATION_DETAILS_T Type

Logging configuration for resource.

Syntax
```

```

Fields

Field Description

`enable_logging`

(optional) If customer logging is enabled for job runs.

`enable_auto_log_creation`

(optional) If automatic on-behalf-of log object creation is enabled for job runs.

`log_group_id`

(optional) The log group id for where log objects are for job runs.

`log_id`

(optional) The log id the job run will push logs too.

### DBMS_CLOUD_OCI_DATASCIENCE_STORAGE_MOUNT_CONFIGURATION_DETAILS_T Type

The storage mount configuration details

Syntax
```

```

Fields

Field Description

`storage_type`

(required) The type of storage.

Allowed values are: 'FILE_STORAGE', 'OBJECT_STORAGE'

`destination_directory_name`

(required) The local directory name to be mounted

`destination_path`

(optional) The local path of the mounted directory, excluding directory name.

### DBMS_CLOUD_OCI_DATASCIENCE_STORAGE_MOUNT_CONFIGURATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_datascience_storage_mount_configuration_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_JOB_DETAILS_T Type

Parameters needed to create a new job.

Syntax
```

```

Fields

Field Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the job with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`display_name`

(optional) A user-friendly display name for the resource.

`description`

(optional) A short description of the job.

`job_configuration_details`

(required)

`job_infrastructure_configuration_details`

(required)

`job_log_configuration_details`

(optional)

`job_storage_mount_configuration_details_list`

(optional) Collection of JobStorageMountConfigurationDetails.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_JOB_RUN_DETAILS_T Type

Parameters needed to create a new job run.

Syntax
```

```

Fields

Field Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the job with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`display_name`

(optional) A user-friendly display name for the resource.

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job to create a run for.

`job_configuration_override_details`

(optional)

`job_log_configuration_override_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type

The model deployment configuration details.

Syntax
```

```

Fields

Field Description

`deployment_type`

(required) The type of the model deployment.

Allowed values are: 'SINGLE_MODEL'

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_DEPLOYMENT_DETAILS_T Type

Parameters needed to create a new model deployment. Model deployments are used by data scientists to perform predictions from the model hosted on an HTTP server.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`

`description`

(optional) A short description of the model deployment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the model deployment.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the model deployment.

`model_deployment_configuration_details`

(required)

`category_log_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_METADATA_T Type

Defines properties of each model metadata.

Syntax
```

```

Fields

Field Description

`key`

(optional) Key of the model Metadata. The key can either be user defined or OCI defined. List of OCI defined keys: * useCaseType * libraryName * libraryVersion * estimatorClass * hyperParameters * testartifactresults

`value`

(optional) Allowed values for useCaseType: binary_classification, regression, multinomial_classification, clustering, recommender, dimensionality_reduction/representation, time_series_forecasting, anomaly_detection, topic_modeling, ner, sentiment_analysis, image_classification, object_localization, other Allowed values for libraryName: scikit-learn, xgboost, tensorflow, pytorch, mxnet, keras, lightGBM, pymc3, pyOD, spacy, prophet, sktime, statsmodels, cuml, oracle_automl, h2o, transformers, nltk, emcee, pystan, bert, gensim, flair, word2vec, ensemble, other

`description`

(optional) Description of model metadata

`category`

(optional) Category of model metadata which should be null for defined metadata.For custom metadata is should be one of the following values \"Performance,Training Profile,Training and Validation Datasets,Training Environment,other\".

### DBMS_CLOUD_OCI_DATASCIENCE_METADATA_TBL Type

Nested table type of dbms_cloud_oci_datascience_metadata_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_DETAILS_T Type

Parameters needed to create a new model. Models are mathematical representations of the relationships between data. Models are represented by their associated metadata and artifact.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to create the model in.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the model.

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My Model`

`description`

(optional) A short description of the model.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`custom_metadata_list`

(optional) An array of custom metadata details for the model.

`defined_metadata_list`

(optional) An array of defined metadata details for the model.

`input_schema`

(optional) Input schema file content in String format

`output_schema`

(optional) Output schema file content in String format

`model_version_set_id`

(optional) The OCID of the model version set that the model is associated to.

`version_label`

(optional) The version label can add an additional description of the lifecycle state of the model or the application using/training the model.

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_PROVENANCE_DETAILS_T Type

Model provenance gives data scientists information about the origin of their model. This information allows data scientists to reproduce the development environment in which the model was trained.

Syntax
```

```

Fields

Field Description

`repository_url`

(optional) For model reproducibility purposes. URL of the git repository associated with model training.

`git_branch`

(optional) For model reproducibility purposes. Branch of the git repository associated with model training.

`git_commit`

(optional) For model reproducibility purposes. Commit ID of the git repository associated with model training.

`script_dir`

(optional) For model reproducibility purposes. Path to model artifacts.

`training_script`

(optional) For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\"

`training_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a training session(Job or NotebookSession) in which the model was trained. It is used for model reproducibility purposes.

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_VERSION_SET_DETAILS_T Type

Parameters that are required to create a new model version set.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to create the model version set in.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the model version set.

`name`

(required) A user-friendly name for the resource. It must be unique and can't be modified. Avoid entering confidential information. Example: `My model version set`

`description`

(optional) A short description of the model version set.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_SHAPE_CONFIG_DETAILS_T Type

Details for the notebook session shape configuration.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the notebook session instance.

`memory_in_g_bs`

(optional) The total amount of memory available to the notebook session instance, in gigabytes.

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_CONFIGURATION_DETAILS_T Type

Details for the notebook session configuration.

Syntax
```

```

Fields

Field Description

`shape`

(required) The shape used to launch the notebook session compute instance. The list of available shapes in a given compartment can be retrieved using the `ListNotebookSessionShapes` endpoint.

`block_storage_size_in_g_bs`

(optional) A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.

`subnet_id`

(required) A notebook session instance is provided with a VNIC for network access. This specifies the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet to create a VNIC in. The subnet should be in a VCN with a NAT gateway for egress to the internet.

`private_endpoint_id`

(optional) The OCID of a Data Science private endpoint.

`notebook_session_shape_config_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_CONFIG_DETAILS_T Type

Details for the notebook session configuration.

Syntax
```

```

Fields

Field Description

`shape`

(required) The shape used to launch the notebook session compute instance. The list of available shapes in a given compartment can be retrieved using the `ListNotebookSessionShapes` endpoint.

`block_storage_size_in_g_bs`

(optional) A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.

`subnet_id`

(optional) A notebook session instance is provided with a VNIC for network access. This specifies the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet to create a VNIC in. The subnet should be in a VCN with a NAT gateway for egress to the internet.

`private_endpoint_id`

(optional) The OCID of a Data Science private endpoint.

`notebook_session_shape_config_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_GIT_REPO_CONFIG_DETAILS_T Type

Git repository configurations.

Syntax
```

```

Fields

Field Description

`url`

(required) The repository URL

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_GIT_REPO_CONFIG_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_datascience_notebook_session_git_repo_config_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_GIT_CONFIG_DETAILS_T Type

Git configuration Details.

Syntax
```

```

Fields

Field Description

`notebook_session_git_repo_config_collection`

(optional) A collection of Git repository configurations.

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_RUNTIME_CONFIG_DETAILS_T Type

Notebook Session runtime configuration details.

Syntax
```

```

Fields

Field Description

`custom_environment_variables`

(optional) Custom environment variables for Notebook Session. These key-value pairs will be available for customers in Notebook Sessions.

`notebook_session_git_config_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_NOTEBOOK_SESSION_DETAILS_T Type

Parameters needed to create a new notebook session. Notebook sessions are interactive coding environments for data scientists.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My NotebookSession`

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate with the notebook session.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the notebook session.

`notebook_session_configuration_details`

(optional)

`notebook_session_config_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`notebook_session_runtime_config_details`

(optional)

`notebook_session_storage_mount_configuration_details_list`

(optional) Collection of NotebookSessionStorageMountConfigurationDetails.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CONFIGURATION_DETAILS_T Type

The configuration details of a pipeline.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of pipeline.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_LOG_CONFIGURATION_DETAILS_T Type

The pipeline log configuration details.

Syntax
```

```

Fields

Field Description

`enable_logging`

(optional) If customer logging is enabled for pipeline.

`enable_auto_log_creation`

(optional) If automatic on-behalf-of log object creation is enabled for pipeline runs.

`log_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log group.

`log_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_SHAPE_CONFIG_DETAILS_T Type

Details for the pipeline step run shape configuration. Specify only when a flex shape is selected.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) A pipeline step run instance of type VM.Standard.E3.Flex allows the ocpu count to be specified.

`memory_in_g_bs`

(optional) A pipeline step run instance of type VM.Standard.E3.Flex allows memory to be specified. This specifies the size of the memory in GBs.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type

The infrastructure configuration details of a pipeline or a step.

Syntax
```

```

Fields

Field Description

`shape_name`

(required) The shape used to launch the instance for all step runs in the pipeline.

`block_storage_size_in_g_bs`

(required) The size of the block storage volume to attach to the instance.

`shape_config_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_CONFIGURATION_DETAILS_T Type

The configuration details of a step.

Syntax
```

```

Fields

Field Description

`maximum_runtime_in_minutes`

(optional) A time bound for the execution of the step.

`environment_variables`

(optional) Environment variables to set for step.

`command_line_arguments`

(optional) The command line arguments to set for step.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_DETAILS_T Type

A step in the pipeline.

Syntax
```

```

Fields

Field Description

`step_type`

(required) The type of step.

Allowed values are: 'ML_JOB', 'CUSTOM_SCRIPT'

`step_name`

(required) The name of the step. It must be unique within the pipeline. This is used to create the pipeline DAG.

`description`

(optional) A short description of the step.

`depends_on`

(optional) The list of step names this current step depends on for execution.

`step_configuration_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_datascience_pipeline_step_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_PIPELINE_DETAILS_T Type

The information about new Pipeline.

Syntax
```

```

Fields

Field Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the pipeline with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the pipeline.

`display_name`

(optional) A user-friendly display name for the resource.

`description`

(optional) A short description of the pipeline.

`configuration_details`

(optional)

`log_configuration_details`

(optional)

`infrastructure_configuration_details`

(optional)

`step_details`

(required) Array of step details for each step.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_OVERRIDE_DETAILS_T Type

Override details of the step. Only Step Configuration is allowed to be overridden.

Syntax
```

```

Fields

Field Description

`step_name`

(required) The name of the step.

`step_configuration_details`

(required)

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_OVERRIDE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_datascience_pipeline_step_override_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_PIPELINE_RUN_DETAILS_T Type

The information about new PipelineRun.

Syntax
```

```

Fields

Field Description

`project_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the pipeline run with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the pipeline run.

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline for which pipeline run is created.

`display_name`

(optional) A user-friendly display name for the resource.

`configuration_override_details`

(optional)

`log_configuration_override_details`

(optional)

`step_override_details`

(optional) Array of step override details. Only Step Configuration is allowed to be overridden.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_CREATE_PROJECT_DETAILS_T Type

Parameters needed to create a new project. Projects enable users to organize their data science work.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the project.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to create the project in.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_DATA_SCIENCE_PRIVATE_ENDPOINT_T Type

Data Science private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create private endpoint.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user friendly description. Avoid entering confidential information.

`display_name`

(required) A user friendly name. It doesn't have to be unique. Avoid entering confidential information.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of a private endpoint.

`lifecycle_details`

(optional) Details of the state of Data Science private endpoint.

`lifecycle_state`

(required) State of the Data Science private endpoint.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`nsg_ids`

(optional) An array of network security group OCIDs.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user that created the private endpoint.

`subnet_id`

(required) The OCID of a subnet.

`fqdn`

(optional) Accesing the Data Science resource using FQDN.

`data_science_resource_type`

(optional) Data Science resource type.

Allowed values are: 'NOTEBOOK_SESSION'

`time_created`

(required) The date and time that the Data Science private endpoint was created expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time that the Data Science private endpoint was updated expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATASCIENCE_DATA_SCIENCE_PRIVATE_ENDPOINT_SUMMARY_T Type

List of Data Science private endpoints.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create private Endpoint.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user friendly name. It doesn't have to be unique. Avoid entering confidential information.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of a private endpoint.

`lifecycle_state`

(required) State of a private endpoint.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(required) Details of the state of a private endpoint.

`data_science_resource_type`

(required) Data Science resource type.

Allowed values are: 'NOTEBOOK_SESSION'

`nsg_ids`

(optional) An array of network security group OCIDs.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user that created the private endpoint.

`subnet_id`

(required) The OCID of a subnet.

`fqdn`

(required) Accesing Data Science resource using FQDN.

`time_created`

(required) The date and time that the Data Science private endpoint was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time that the Data Science private endpoint was updated expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATASCIENCE_DEFAULT_JOB_CONFIGURATION_DETAILS_T Type

The default job configuration.

Syntax
```

```

`dbms_cloud_oci_datascience_default_job_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_job_configuration_details_t`type.

Fields

Field Description

`environment_variables`

(optional) Environment variables to set for the job.

`command_line_arguments`

(optional) The arguments to pass to the job.

`maximum_runtime_in_minutes`

(optional) A time bound for the execution of the job. Timer starts when the job becomes active.

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type

The configuration to carry the environment details thats used in Model Deployment creation

Syntax
```

```

Fields

Field Description

`environment_configuration_type`

(required) The environment configuration type

Allowed values are: 'DEFAULT', 'OCIR_CONTAINER'

### DBMS_CLOUD_OCI_DATASCIENCE_DEFAULT_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type

The environment configuration details object for managed container

Syntax
```

```

`dbms_cloud_oci_datascience_default_model_deployment_environment_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_model_deployment_environment_configuration_details_t`type.

Fields

Field Description

`environment_variables`

(optional) Environment variables to set for the web server container. The size of envVars must be less than 2048 bytes. Key should be under 32 characters. Key should contain only letters, digits and underscore (_) Key should start with a letter. Key should have at least 2 characters. Key should not end with underscore eg. `TEST_` Key if added cannot be empty. Value can be empty. No specific size limits on individual Values. But overall environment variables is limited to 2048 bytes. Key can't be reserved Model Deployment environment variables.

### DBMS_CLOUD_OCI_DATASCIENCE_ERROR_T Type

Error schema.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, which is meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DATASCIENCE_EXPORT_MODEL_ARTIFACT_DETAILS_T Type

Details required for exporting the model artifact from source to service bucket

Syntax
```

```

Fields

Field Description

`artifact_export_details`

(required)

### DBMS_CLOUD_OCI_DATASCIENCE_FAST_LAUNCH_JOB_CONFIG_SUMMARY_T Type

The shape config to launch a fast launch capable job instance

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the fast launch job config

`shape_name`

(required) The name of the fast launch job shape.

`core_count`

(required) The number of cores associated with this fast launch job shape.

`memory_in_g_bs`

(required) The number of cores associated with this fast launch job shape.

`shape_series`

(required) The family that the compute shape belongs to.

Allowed values are: 'AMD_ROME', 'INTEL_SKYLAKE', 'NVIDIA_GPU', 'LEGACY', 'ARM'

`managed_egress_support`

(required) The managed egress support

Allowed values are: 'REQUIRED', 'SUPPORTED', 'UNSUPPORTED'

### DBMS_CLOUD_OCI_DATASCIENCE_FILE_STORAGE_MOUNT_CONFIGURATION_DETAILS_T Type

The File Storage Mount Configuration Details.

Syntax
```

```

`dbms_cloud_oci_datascience_file_storage_mount_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_storage_mount_configuration_details_t`type.

Fields

Field Description

`mount_target_id`

(required) OCID of the mount target

`export_id`

(required) OCID of the export

### DBMS_CLOUD_OCI_DATASCIENCE_SCALING_POLICY_T Type

The scaling policy to apply to each model of the deployment.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) The type of scaling policy.

Allowed values are: 'FIXED_SIZE'

### DBMS_CLOUD_OCI_DATASCIENCE_FIXED_SIZE_SCALING_POLICY_T Type

The fixed size scaling policy.

Syntax
```

```

`dbms_cloud_oci_datascience_fixed_size_scaling_policy_t`is a subtype of the`dbms_cloud_oci_datascience_scaling_policy_t`type.

Fields

Field Description

`instance_count`

(required) The number of instances for the model deployment.

### DBMS_CLOUD_OCI_DATASCIENCE_IMPORT_MODEL_ARTIFACT_DETAILS_T Type

Details required for importing the artifact from service bucket

Syntax
```

```

Fields

Field Description

`artifact_import_details`

(required)

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_INSTANCE_SHAPE_CONFIG_DETAILS_T Type

Details for the model-deployment instance shape configuration.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows the ocpu count to be specified with in the range of 1 to 64 ocpu. VM.Standard3.Flex OCPU range is between 1 to 32 ocpu and for VM.Optimized3.Flex OCPU range is 1 to 18 ocpu.

`memory_in_g_bs`

(optional) A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows the memory to be specified with in the range of 6 to 1024 GB. VM.Standard3.Flex memory range is between 6 to 512 GB and VM.Optimized3.Flex memory range is between 6 to 256 GB.

### DBMS_CLOUD_OCI_DATASCIENCE_INSTANCE_CONFIGURATION_T Type

The model deployment instance configuration

Syntax
```

```

Fields

Field Description

`instance_shape_name`

(required) The shape used to launch the model deployment instances.

`model_deployment_instance_shape_config_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_T Type

A job for training models.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2020-08-06T21:10:29.41Z

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the job.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the job with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`display_name`

(optional) A user-friendly display name for the resource.

`description`

(optional) A short description of the job.

`job_configuration_details`

(required)

`job_infrastructure_configuration_details`

(required)

`job_log_configuration_details`

(optional)

`job_storage_mount_configuration_details_list`

(optional) Collection of JobStorageMountConfigurationDetails.

`lifecycle_state`

(required) The state of the job.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'DELETED'

`lifecycle_details`

(optional) The state of the job.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_RUN_LOG_DETAILS_T Type

Customer logging details for job run.

Syntax
```

```

Fields

Field Description

`log_group_id`

(required) The log group id for where log objects will be for job runs.

`log_id`

(required) The log id of the log object the job run logs will be shipped to.

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_RUN_T Type

A job run.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`time_accepted`

(required) The date and time the job run was accepted in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the job run request was started in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the job run request was finished in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the job run.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the job with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`display_name`

(optional) A user-friendly display name for the resource.

`job_configuration_override_details`

(required)

`job_infrastructure_configuration_details`

(required)

`job_log_configuration_override_details`

(optional)

`job_storage_mount_configuration_details_list`

(optional) Collection of JobStorageMountConfigurationDetails.

`log_details`

(optional)

`lifecycle_state`

(required) The state of the job run.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details of the state of the job run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_RUN_SUMMARY_T Type

Summary information for a Job.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`time_accepted`

(required) The date and time the job run was accepted in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the job run request was started in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the job run request was finished in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the job run.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the job with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run.

`display_name`

(optional) A user-friendly display name for the resource.

`lifecycle_state`

(required) The state of the job.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details of the state of the job run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_SHAPE_CONFIG_DETAILS_T Type

Details for the job run shape configuration. Specify only when a flex shape is selected.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the job run instance.

`memory_in_g_bs`

(optional) The total amount of memory available to the job run instance, in gigabytes.

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_SHAPE_SUMMARY_T Type

The compute shape used to launch a job compute instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the job shape.

`core_count`

(required) The number of cores associated with this job run shape.

`memory_in_g_bs`

(required) The number of cores associated with this job shape.

`shape_series`

(required) The family that the compute shape belongs to.

Allowed values are: 'AMD_ROME', 'INTEL_SKYLAKE', 'NVIDIA_GPU', 'LEGACY', 'ARM'

### DBMS_CLOUD_OCI_DATASCIENCE_JOB_SUMMARY_T Type

Summary information for a Job.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2020-08-06T21:10:29.41Z

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the project.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the job with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`display_name`

(optional) A user-friendly display name for the resource.

`lifecycle_state`

(required) The state of the job.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'DELETED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_MANAGED_EGRESS_STANDALONE_JOB_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type

The standalone job infrastructure configuration with network egress settings preconfigured.

Syntax
```

```

`dbms_cloud_oci_datascience_managed_egress_standalone_job_infrastructure_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_job_infrastructure_configuration_details_t`type.

Fields

Field Description

`shape_name`

(required) The shape used to launch the job run instances.

`block_storage_size_in_g_bs`

(required) The size of the block storage volume to attach to the instance running the job

`job_shape_config_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_T Type

Models are mathematical representations of the relationships between data. Models are represented by their associated metadata and artifacts.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model's compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the model.

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the model.

`lifecycle_state`

(required) The state of the model.

Allowed values are: 'ACTIVE', 'DELETED', 'FAILED', 'INACTIVE'

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the model.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`custom_metadata_list`

(optional) An array of custom metadata details for the model.

`defined_metadata_list`

(optional) An array of defined metadata details for the model.

`input_schema`

(optional) Input schema file content in String format

`output_schema`

(optional) Output schema file content in String format

`model_version_set_id`

(required) The OCID of the model version set that the model is associated to.

`model_version_set_name`

(required) The name of the model version set that the model is associated to.

`version_id`

(required) Unique identifier assigned to each version of the model.

`version_label`

(required) The version label can add an additional description of the lifecycle state of the model or the application using and training the model.

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_CONFIGURATION_DETAILS_T Type

The model configuration details.

Syntax
```

```

Fields

Field Description

`model_id`

(required) The OCID of the model you want to deploy.

`instance_configuration`

(required)

`scaling_policy`

(optional)

`bandwidth_mbps`

(optional) The minimum network bandwidth for the model deployment.

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_T Type

Model deployments are used by data scientists to perform predictions from the model hosted on an HTTP server.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`time_created`

(required) The date and time the resource was created, in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`display_name`

(required) A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`

`description`

(optional) A short description of the model deployment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the model deployment.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the model deployment.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment's compartment.

`model_deployment_configuration_details`

(optional)

`category_log_details`

(optional)

`model_deployment_url`

(required) The URL to interact with the model deployment.

`lifecycle_state`

(required) The state of the model deployment.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING', 'DELETED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details about the state of the model deployment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_SHAPE_SUMMARY_T Type

The compute shape used to launch a model deployment compute instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the model deployment shape.

`core_count`

(required) The number of cores associated with this model deployment shape.

`memory_in_g_bs`

(required) The amount of memory in GBs associated with this model deployment shape.

`shape_series`

(required) The family that the compute shape belongs to.

Allowed values are: 'AMD_ROME', 'INTEL_SKYLAKE', 'NVIDIA_GPU', 'LEGACY', 'ARM'

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_SUMMARY_T Type

Summary information for a model deployment.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment.

`time_created`

(required) The date and time the resource was created, in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`display_name`

(required) A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`

`description`

(optional) A short description of the model deployment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the model deployment.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the model deployment.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model deployment's compartment.

`model_deployment_configuration_details`

(optional)

`category_log_details`

(optional)

`model_deployment_url`

(required) The URL to interact with the model deployment.

`lifecycle_state`

(required) The state of the model deployment.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING', 'DELETED', 'NEEDS_ATTENTION'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_PROVENANCE_T Type

Model provenance gives data scientists information about the origin of their model. This information allows data scientists to reproduce the development environment in which the model was trained.

Syntax
```

```

Fields

Field Description

`repository_url`

(optional) For model reproducibility purposes. URL of the git repository associated with model training.

`git_branch`

(optional) For model reproducibility purposes. Branch of the git repository associated with model training.

`git_commit`

(optional) For model reproducibility purposes. Commit ID of the git repository associated with model training.

`script_dir`

(optional) For model reproducibility purposes. Path to model artifacts.

`training_script`

(optional) For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\"

`training_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a training session(Job or NotebookSession) in which the model was trained. It is used for model reproducibility purposes.

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_SUMMARY_T Type

Summary information for a model.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model's compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the model.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model.

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the model.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`lifecycle_state`

(required) The state of the model.

Allowed values are: 'ACTIVE', 'DELETED', 'FAILED', 'INACTIVE'

`model_version_set_id`

(required) The OCID of the model version set that the model is associated to.

`model_version_set_name`

(required) The name of the model version set that the model is associated to.

`version_id`

(required) Unique identifier assigned to each version of the model.

`version_label`

(required) The version label can add an additional description of the lifecycle state of the model or the application using and training the model.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_VERSION_SET_T Type

A model version set to associate different versions of machine learning models.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the model version set.

`name`

(required) A user-friendly name for the resource.

`description`

(required) A short description of the model version set.

`lifecycle_state`

(required) The state of the model version set.

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time that the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`time_updated`

(required) The date and time that the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the model version set.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_MODEL_VERSION_SET_SUMMARY_T Type

Summary information for a model version set.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the model version set compartment.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the model version set.

`name`

(required) A user-friendly name for the resource. It must be unique and can't be modified.

`lifecycle_state`

(required) The state of the model version set.

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time that the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`time_updated`

(required) The date and time that the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the model version set.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_T Type

Notebook sessions are interactive coding environments for data scientists.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My NotebookSession`

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the notebook session.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the notebook session.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session's compartment.

`notebook_session_configuration_details`

(optional)

`notebook_session_config_details`

(optional)

`notebook_session_runtime_config_details`

(optional)

`notebook_session_storage_mount_configuration_details_list`

(optional) Collection of NotebookSessionStorageMountConfigurationDetails.

`notebook_session_url`

(optional) The URL to interact with the notebook session.

`lifecycle_state`

(required) The state of the notebook session.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE', 'UPDATING'

`lifecycle_details`

(optional) Details about the state of the notebook session.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_SHAPE_SUMMARY_T Type

The compute shape used to launch a notebook session compute instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the notebook session shape.

`core_count`

(required) The number of cores associated with this notebook session shape.

`memory_in_g_bs`

(required) The amount of memory in GBs associated with this notebook session shape.

`shape_series`

(required) The family that the compute shape belongs to.

Allowed values are: 'AMD_ROME', 'INTEL_SKYLAKE', 'NVIDIA_GPU', 'LEGACY', 'ARM'

### DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_SUMMARY_T Type

Summary information for a notebook session.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My NotebookSession`

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project associated with the notebook session.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the notebook session.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the notebook session's compartment.

`notebook_session_configuration_details`

(optional)

`notebook_session_config_details`

(optional)

`notebook_session_url`

(optional) The URL to interact with the notebook session.

`lifecycle_state`

(required) The state of the notebook session.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE', 'UPDATING'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_OBJECT_STORAGE_MOUNT_CONFIGURATION_DETAILS_T Type

The Object Storage Configuration Details.

Syntax
```

```

`dbms_cloud_oci_datascience_object_storage_mount_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_storage_mount_configuration_details_t`type.

Fields

Field Description

`namespace`

(required) The object storage namespace

`bucket`

(required) The object storage bucket

`prefix`

(optional) Prefix in the bucket to mount

### DBMS_CLOUD_OCI_DATASCIENCE_OCIR_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type

The environment configuration details object for OCI Registry

Syntax
```

```

`dbms_cloud_oci_datascience_ocir_model_deployment_environment_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_model_deployment_environment_configuration_details_t`type.

Fields

Field Description

`image`

(required) The full path to the Oracle Container Repository (OCIR) registry, image, and tag in a canonical format. Acceptable format: `&lt;region&gt;.ocir.io/&lt;registry&gt;/&lt;image&gt;:&lt;tag&gt;` `&lt;region&gt;.ocir.io/&lt;registry&gt;/&lt;image&gt;:&lt;tag&gt;@digest`

`image_digest`

(optional) The digest of the container image. For example, `sha256:881303a6b2738834d795a32b4a98eb0e5e3d1cad590a712d1e04f9b2fa90a030`

`cmd`

(optional) The container image run[CMD](https://docs.docker.com/engine/reference/builder/#cmd)as a list of strings. Use `CMD` as arguments to the `ENTRYPOINT` or the only command to run in the absence of an `ENTRYPOINT`. The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes.

`entrypoint`

(optional) The container image run[ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint)as a list of strings. Accept the `CMD` as extra arguments. The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes. More information on how `CMD` and `ENTRYPOINT` interact are[here](https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact).

`server_port`

(optional) The port on which the web server serving the inference is running. The port can be anything between `1024` and `65535`. The following ports cannot be used `24224`, `8446`, `8447`.

`health_check_port`

(optional) The port on which the container[HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck)would listen. The port can be anything between `1024` and `65535`. The following ports cannot be used `24224`, `8446`, `8447`.

`environment_variables`

(optional) Environment variables to set for the web server container. The size of envVars must be less than 2048 bytes. Key should be under 32 characters. Key should contain only letters, digits and underscore (_) Key should start with a letter. Key should have at least 2 characters. Key should not end with underscore eg. `TEST_` Key if added cannot be empty. Value can be empty. No specific size limits on individual Values. But overall environment variables is limited to 2048 bytes. Key can't be reserved Model Deployment environment variables.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_T Type

A Pipeline to orchestrate and execute machine learning workflows.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2020-08-06T21:10:29.41Z

`time_updated`

(optional) The date and time the resource was updated in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2020-08-06T21:10:29.41Z

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the pipeline.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the pipeline with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the pipeline.

`display_name`

(required) A user-friendly display name for the resource.

`description`

(optional) A short description of the pipeline.

`configuration_details`

(optional)

`log_configuration_details`

(optional)

`infrastructure_configuration_details`

(optional)

`step_details`

(required) Array of step details for each step.

`lifecycle_state`

(required) The current state of the pipeline.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CUSTOM_SCRIPT_STEP_DETAILS_T Type

The type of step where user provides the step artifact to be executed on an execution engine managed by the pipelines service.

Syntax
```

```

`dbms_cloud_oci_datascience_pipeline_custom_script_step_details_t`is a subtype of the`dbms_cloud_oci_datascience_pipeline_step_details_t`type.

Fields

Field Description

`step_infrastructure_configuration_details`

(optional)

`is_artifact_uploaded`

(optional) A flag to indicate whether the artifact has been uploaded for this step or not.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_RUN_T Type

Detail of each StepRun.

Syntax
```

```

Fields

Field Description

`step_type`

(required) The type of step.

Allowed values are: 'ML_JOB', 'CUSTOM_SCRIPT'

`time_started`

(required) The date and time the pipeline step run was started in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the pipeline step run finshed executing in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`step_name`

(required) The name of the step.

`lifecycle_state`

(optional) The state of the step run.

Allowed values are: 'WAITING', 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETED', 'SKIPPED'

`lifecycle_details`

(optional) Details of the state of the step run.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CUSTOM_SCRIPT_STEP_RUN_T Type

Detail of each CustomScriptStepRun.

Syntax
```

```

`dbms_cloud_oci_datascience_pipeline_custom_script_step_run_t`is a subtype of the`dbms_cloud_oci_datascience_pipeline_step_run_t`type.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_UPDATE_DETAILS_T Type

The details of the step to update.

Syntax
```

```

Fields

Field Description

`step_type`

(required) The type of step.

Allowed values are: 'ML_JOB', 'CUSTOM_SCRIPT'

`step_name`

(required) The name of the step.

`description`

(optional) A short description of the step.

`step_configuration_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CUSTOM_SCRIPT_STEP_UPDATE_DETAILS_T Type

The type of step where user provides the step artifact to be executed on an execution engine managed by the pipelines service.

Syntax
```

```

`dbms_cloud_oci_datascience_pipeline_custom_script_step_update_details_t`is a subtype of the`dbms_cloud_oci_datascience_pipeline_step_update_details_t`type.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_DEFAULT_CONFIGURATION_DETAILS_T Type

The default pipeline configuration.

Syntax
```

```

`dbms_cloud_oci_datascience_pipeline_default_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_pipeline_configuration_details_t`type.

Fields

Field Description

`maximum_runtime_in_minutes`

(optional) A time bound for the execution of the entire Pipeline. Timer starts when the Pipeline Run is in progress.

`environment_variables`

(optional) Environment variables to set for steps in the pipeline.

`command_line_arguments`

(optional) The command line arguments to set for steps in the pipeline.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_ML_JOB_STEP_DETAILS_T Type

The type of step where the job is pre-created by the user.

Syntax
```

```

`dbms_cloud_oci_datascience_pipeline_ml_job_step_details_t`is a subtype of the`dbms_cloud_oci_datascience_pipeline_step_details_t`type.

Fields

Field Description

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job to be used as a step.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_ML_JOB_STEP_RUN_T Type

Detail of each MLJobStepRun.

Syntax
```

```

`dbms_cloud_oci_datascience_pipeline_ml_job_step_run_t`is a subtype of the`dbms_cloud_oci_datascience_pipeline_step_run_t`type.

Fields

Field Description

`job_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job run triggered for this step run.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_ML_JOB_STEP_UPDATE_DETAILS_T Type

The type of step where the job is pre-created by the user.

Syntax
```

```

`dbms_cloud_oci_datascience_pipeline_ml_job_step_update_details_t`is a subtype of the`dbms_cloud_oci_datascience_pipeline_step_update_details_t`type.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_RUN_LOG_DETAILS_T Type

Customer logging details for pipeline run.

Syntax
```

```

Fields

Field Description

`log_group_id`

(required) The log group id for where log objects will be for pipeline runs.

`log_id`

(required) The log id of the log object the pipeline run logs will be shipped to.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_RUN_TBL Type

Nested table type of dbms_cloud_oci_datascience_pipeline_step_run_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_RUN_T Type

Description of PipelineRun.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline run.

`time_accepted`

(required) The date and time the pipeline run was accepted in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the pipeline run request was started in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the pipeline run was updated in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the pipeline run request was finished in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the pipeline run.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the pipeline run with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the pipeline run.

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`display_name`

(required) A user-friendly display name for the resource.

`configuration_details`

(optional)

`configuration_override_details`

(optional)

`log_configuration_override_details`

(optional)

`step_override_details`

(optional) Array of step override details. Only Step Configuration is allowed to be overridden.

`log_details`

(optional)

`step_runs`

(required) Array of StepRun object for each step.

`lifecycle_state`

(required) The current state of the pipeline run.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_RUN_SUMMARY_T Type

Summary of the PipelineRun.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline run.

`time_accepted`

(required) The date and time the pipeline run was accepted in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the pipeline run request was started in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the pipeline run request was finished in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the pipeline run was updated in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the pipeline run.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the pipeline run with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the pipeline run.

`pipeline_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline for which pipeline run is created.

`display_name`

(required) A user-friendly display name for the resource.

`lifecycle_state`

(required) The state of the pipeline run.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_SUMMARY_T Type

Summary of the Pipeline.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pipeline.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2020-08-06T21:10:29.41Z

`time_updated`

(optional) The date and time the resource was updated in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2020-08-06T21:10:29.41Z

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the project.

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project to associate the pipeline with.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the pipeline.

`display_name`

(required) A user-friendly display name for the resource.

`lifecycle_state`

(required) The state of the pipeline.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'FAILED', 'DELETED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_PROJECT_T Type

Projects enable users to organize their data science work.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the project.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project's compartment.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created this project.

`lifecycle_state`

(required) The state of the project.

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_PROJECT_SUMMARY_T Type

Summary information for a project.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project.

`time_created`

(required) The date and time the resource was created in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: 2019-08-25T21:10:29.41Z

`display_name`

(required) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the project.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the project's compartment.

`created_by`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the project.

`lifecycle_state`

(required) The state of the project.

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_SINGLE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type

The single model type deployment.

Syntax
```

```

`dbms_cloud_oci_datascience_single_model_deployment_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_model_deployment_configuration_details_t`type.

Fields

Field Description

`model_configuration_details`

(required)

`environment_configuration_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_STANDALONE_JOB_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type

The standalone job infrastructure configuration.

Syntax
```

```

`dbms_cloud_oci_datascience_standalone_job_infrastructure_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_job_infrastructure_configuration_details_t`type.

Fields

Field Description

`shape_name`

(required) The shape used to launch the job run instances.

`subnet_id`

(required) The subnet to create a secondary vnic in to attach to the instance running the job

`block_storage_size_in_g_bs`

(required) The size of the block storage volume to attach to the instance running the job

`job_shape_config_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_CATEGORY_LOG_DETAILS_T Type

The log details for each category for update.

Syntax
```

```

Fields

Field Description

`l_access`

(optional)

`predict`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_DATA_SCIENCE_PRIVATE_ENDPOINT_DETAILS_T Type

The details required to update a private endpoint.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user friendly description. Avoid entering confidential information.

`display_name`

(optional) A user friendly name. It doesn't have to be unique. Avoid entering confidential information.

`nsg_ids`

(optional) An array of network security group OCIDs.

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type

The configuration to carry the environment details thats used in Model Deployment update

Syntax
```

```

Fields

Field Description

`environment_configuration_type`

(required) The environment configuration type

Allowed values are: 'DEFAULT', 'OCIR_CONTAINER'

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_DEFAULT_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type

The update environment configuration details object for managed container

Syntax
```

```

`dbms_cloud_oci_datascience_update_default_model_deployment_environment_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_update_model_deployment_environment_configuration_details_t`type.

Fields

Field Description

`environment_variables`

(optional) Environment variables to set for the web server container. The size of envVars must be less than 2048 bytes. Key should be under 32 characters. Key should contain only letters, digits and underscore (_) Key should start with a letter. Key should have at least 2 characters. Key should not end with underscore eg. `TEST_` Key if added cannot be empty. Value can be empty. No specific size limits on individual Values. But overall environment variables is limited to 2048 bytes. Key can't be reserved Model Deployment environment variables.

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_JOB_DETAILS_T Type

Details for updating a job.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource.

`description`

(optional) A short description of the job.

`job_infrastructure_configuration_details`

(optional)

`job_storage_mount_configuration_details_list`

(optional) Collection of JobStorageMountConfigurationDetails.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_JOB_RUN_DETAILS_T Type

Details for updating a job run.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_CONFIGURATION_DETAILS_T Type

The model configuration details for update.

Syntax
```

```

Fields

Field Description

`model_id`

(required) The OCID of the model you want to update.

`instance_configuration`

(optional)

`scaling_policy`

(optional)

`bandwidth_mbps`

(optional) The minimum network bandwidth for the model deployment.

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type

The model deployment configuration details for update.

Syntax
```

```

Fields

Field Description

`deployment_type`

(optional) The type of the model deployment.

Allowed values are: 'SINGLE_MODEL'

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DEPLOYMENT_DETAILS_T Type

Details for updating a model deployment. You can update `modelDeploymentConfigurationDetails` and change `instanceShapeName` and `modelId` when the model deployment is in the ACTIVE lifecycle state. The `bandwidthMbps` or `instanceCount` can only be updated while the model deployment is in the `INACTIVE` state. Changes to the `bandwidthMbps` or `instanceCount` will take effect the next time the `ActivateModelDeployment` action is invoked on the model deployment resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`

`description`

(optional) A short description of the model deployment.

`model_deployment_configuration_details`

(optional)

`category_log_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DETAILS_T Type

Details for updating a model.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My Model`

`description`

(optional) A short description of the model.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`custom_metadata_list`

(optional) An array of custom metadata details for the model.

`defined_metadata_list`

(optional) An array of defined metadata details for the model.

`model_version_set_id`

(optional) The OCID of the model version set that the model is associated to.

`version_label`

(optional) The version label can add an additional description of the lifecycle state of the model or the application using/training the model.

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_PROVENANCE_DETAILS_T Type

Model provenance gives data scientists information about the origin of their model. This information allows data scientists to reproduce the development environment in which the model was trained.

Syntax
```

```

Fields

Field Description

`repository_url`

(optional) For model reproducibility purposes. URL of the git repository associated with model training.

`git_branch`

(optional) For model reproducibility purposes. Branch of the git repository associated with model training.

`git_commit`

(optional) For model reproducibility purposes. Commit ID of the git repository associated with model training.

`script_dir`

(optional) For model reproducibility purposes. Path to model artifacts.

`training_script`

(optional) For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\"

`training_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a training session(Job or NotebookSession) in which the model was trained. It is used for model reproducibility purposes.

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_VERSION_SET_DETAILS_T Type

Details for updating a model version set.

Syntax
```

```

Fields

Field Description

`description`

(optional) A short description of the model version set.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_NOTEBOOK_SESSION_DETAILS_T Type

Details for updating a notebook session. `notebookSessionConfigurationDetails` can only be updated while the notebook session is in the `INACTIVE` state. Changes to the `notebookSessionConfigurationDetails` take effect the next time the `ActivateNotebookSession` action is invoked on the notebook session resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My NotebookSession`

`notebook_session_configuration_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`notebook_session_runtime_config_details`

(optional)

`notebook_session_storage_mount_configuration_details_list`

(optional) Collection of NotebookSessionStorageMountConfigurationDetails.

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_OCIR_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type

The update environment configuration details object for OCI Registry

Syntax
```

```

`dbms_cloud_oci_datascience_update_ocir_model_deployment_environment_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_update_model_deployment_environment_configuration_details_t`type.

Fields

Field Description

`image`

(optional) The full path to the Oracle Container Repository (OCIR) registry, image, and tag in a canonical format. Acceptable format: `&lt;region&gt;.ocir.io/&lt;registry&gt;/&lt;image&gt;:&lt;tag&gt;` `&lt;region&gt;.ocir.io/&lt;registry&gt;/&lt;image&gt;:&lt;tag&gt;@digest`

`image_digest`

(optional) The digest of the container image. For example, `sha256:881303a6b2738834d795a32b4a98eb0e5e3d1cad590a712d1e04f9b2fa90a030`

`cmd`

(optional) The container image run[CMD](https://docs.docker.com/engine/reference/builder/#cmd)as a list of strings. Use `CMD` as arguments to the `ENTRYPOINT` or the only command to run in the absence of an `ENTRYPOINT`. The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes.

`entrypoint`

(optional) The container image run[ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint)as a list of strings. Accept the `CMD` as extra arguments. The combined size of `CMD` and `ENTRYPOINT` must be less than 2048 bytes. More information on how `CMD` and `ENTRYPOINT` interact are[here](https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact).

`server_port`

(optional) The port on which the web server serving the inference is running. The port can be anything between `1024` and `65535`. The following ports cannot be used `24224`, `8446`, `8447`.

`health_check_port`

(optional) The port on which the container[HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck)would listen. The port can be anything between `1024` and `65535`. The following ports cannot be used `24224`, `8446`, `8447`.

`environment_variables`

(optional) Environment variables to set for the web server container. The size of envVars must be less than 2048 bytes. Key should be under 32 characters. Key should contain only letters, digits and underscore (_) Key should start with a letter. Key should have at least 2 characters. Key should not end with underscore eg. `TEST_` Key if added cannot be empty. Value can be empty. No specific size limits on individual Values. But overall environment variables is limited to 2048 bytes. Key can't be reserved Model Deployment environment variables.

### DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_UPDATE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_datascience_pipeline_step_update_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_PIPELINE_DETAILS_T Type

The information of pipeline to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource.

`description`

(optional) A short description for the resource.

`configuration_details`

(optional)

`log_configuration_details`

(optional)

`step_details`

(optional) Array of update details for each step. Only step configurations are allowed to be updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_PIPELINE_RUN_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name of the pipeline run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_PROJECT_DETAILS_T Type

Details for updating a project.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.

`description`

(optional) A short description of the project.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_SINGLE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type

The single model type deployment for update.

Syntax
```

```

`dbms_cloud_oci_datascience_update_single_model_deployment_configuration_details_t`is a subtype of the`dbms_cloud_oci_datascience_update_model_deployment_configuration_details_t`type.

Fields

Field Description

`model_configuration_details`

(optional)

`environment_configuration_details`

(optional)

### DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_RESOURCE_T Type

The properties that define a work request resource.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The way in which this resource was affected by the work tracked by the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'IN_PROGRESS'

`entity_type`

(required) The resource type the work request affects.

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource the work request affects.

`entity_uri`

(optional) The URI path on which the user can issue a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_datascience_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`operation_type`

(required) The type of work the work request is doing.

Allowed values are: 'NOTEBOOK_SESSION_CREATE', 'NOTEBOOK_SESSION_DELETE', 'NOTEBOOK_SESSION_ACTIVATE', 'NOTEBOOK_SESSION_DEACTIVATE', 'MODELVERSIONSET_DELETE', 'EXPORT_MODEL_ARTIFACT', 'IMPORT_MODEL_ARTIFACT', 'MODEL_DEPLOYMENT_CREATE', 'MODEL_DEPLOYMENT_DELETE', 'MODEL_DEPLOYMENT_ACTIVATE', 'MODEL_DEPLOYMENT_DEACTIVATE', 'MODEL_DEPLOYMENT_UPDATE', 'PROJECT_DELETE', 'WORKREQUEST_CANCEL', 'JOB_DELETE', 'PIPELINE_CREATE', 'PIPELINE_DELETE', 'PIPELINE_RUN_CREATE', 'PIPELINE_RUN_CANCEL', 'PIPELINE_RUN_DELETE', 'PRIVATE_ENDPOINT_CREATE', 'PRIVATE_ENDPOINT_DELETE', 'PRIVATE_ENDPOINT_MOVE', 'PRIVATE_ENDPOINT_UPDATE'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request's compartment.

`percent_complete`

(required) Percentage of the request completed.

`resources`

(required) The resources affected by this work request.

`time_accepted`

(required) The time the work request was accepted in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The time the work request was started in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The time the work request was finished in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_ERROR_T Type

Errors related to a specific work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, which is meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time the error occurred.

### DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_LOG_ENTRY_T Type

Log entries related to a specific work request.

Syntax
```

```

Fields

Field Description

`message`

(required) The description of an action that occurred.

`l_timestamp`

(required) The date and time the log entry occurred.

### DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_SUMMARY_T Type

Summary information for a work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`operation_type`

(required) The type of work the work request is doing.

Allowed values are: 'NOTEBOOK_SESSION_CREATE', 'NOTEBOOK_SESSION_DELETE', 'NOTEBOOK_SESSION_ACTIVATE', 'NOTEBOOK_SESSION_DEACTIVATE', 'MODELVERSIONSET_DELETE', 'EXPORT_MODEL_ARTIFACT', 'IMPORT_MODEL_ARTIFACT', 'MODEL_DEPLOYMENT_CREATE', 'MODEL_DEPLOYMENT_DELETE', 'MODEL_DEPLOYMENT_ACTIVATE', 'MODEL_DEPLOYMENT_DEACTIVATE', 'MODEL_DEPLOYMENT_UPDATE', 'PROJECT_DELETE', 'WORKREQUEST_CANCEL', 'JOB_DELETE', 'PIPELINE_CREATE', 'PIPELINE_DELETE', 'PIPELINE_RUN_CREATE', 'PIPELINE_RUN_CANCEL', 'PIPELINE_RUN_DELETE', 'PRIVATE_ENDPOINT_CREATE', 'PRIVATE_ENDPOINT_DELETE', 'PRIVATE_ENDPOINT_MOVE', 'PRIVATE_ENDPOINT_UPDATE'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request's compartment.

`percent_complete`

(required) Percentage of the request completed.

`resources`

(required) The resources affected by this work request.

`time_accepted`

(required) The date and time the work request was accepted in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_started`

(optional) The date and time the work request was started in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request was finished in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

- [Data Science Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-472D2BAA-29FE-4224-BB24-4AB36AB578A4)
- [DBMS_CLOUD_OCI_DATASCIENCE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-DECF657D-1D57-47D1-B749-5D9A7A755C0A)
- [DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_EXPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-F3814219-6C03-4146-BD79-BB3CF15524CA)
- [DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_EXPORT_DETAILS_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-76758E05-953A-4B3A-A6B6-ECA5E6C62EFE)
- [DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_IMPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-2F511A6C-DBAB-4E13-929A-2E9EBFE31976)
- [DBMS_CLOUD_OCI_DATASCIENCE_ARTIFACT_IMPORT_DETAILS_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-3E60F541-308E-4001-9678-3D9606D7133D)
- [DBMS_CLOUD_OCI_DATASCIENCE_LOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-2D9DF9DE-B537-4E4B-8892-80394F86A379)
- [DBMS_CLOUD_OCI_DATASCIENCE_CATEGORY_LOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-6D1254F4-E6FE-4D9E-81E7-E4F63C7686DF)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_DATA_SCIENCE_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-E71F588D-F9FC-449F-AADF-53DA5B1B8D42)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_JOB_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-D9E858BB-3C6C-496F-9FC9-AC404438C2A4)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_JOB_RUN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-5C45F3F5-77C8-41D0-A0A0-D4809A5A134F)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_MODEL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-856FCA8A-CFB5-4F4B-9090-1ABC967D7431)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_MODEL_DEPLOYMENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-C63ED5C1-6709-4C7E-8FB5-E4816F81DAFA)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_MODEL_VERSION_SET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-5EE85FAF-AC6F-41B1-BDB1-0425C911901A)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_NOTEBOOK_SESSION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-4D3A3A8F-DF90-48BD-882B-6E17BCAFCAC4)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_PIPELINE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-C2681A2F-6A08-4F1F-A022-61F67F9F4587)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_PIPELINE_RUN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-AD9E62CC-082D-43E2-A281-743DE341DC8F)
- [DBMS_CLOUD_OCI_DATASCIENCE_CHANGE_PROJECT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-4C034FE8-E2BD-4AF4-B929-BCE5C8970E38)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_DATA_SCIENCE_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-D2FC8770-5077-4315-B8E4-76CA834B7E50)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-FC51C850-5FF0-4406-92B3-C0076C34507A)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-71B1664A-CC11-4AD0-9B41-D15047F69C81)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_LOG_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-0DDFAE04-9A3E-4A04-ADF4-9FC436FCDDAC)
- [DBMS_CLOUD_OCI_DATASCIENCE_STORAGE_MOUNT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-FBD66A58-E8F4-4347-8D8E-C3E4EFF4E2B3)
- [DBMS_CLOUD_OCI_DATASCIENCE_STORAGE_MOUNT_CONFIGURATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A5AD71AC-B126-40B1-AE26-76B55302D42B)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-C9203EC3-8316-4093-A623-215314E4F1A9)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_JOB_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-67D4195C-5A6C-4CAB-862B-916BDA5886D7)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-B8C0CEC6-DEF5-4863-BF27-797F7043AAE1)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-1BF55AB6-048B-4BF8-BC69-0A4B7961C26F)
- [DBMS_CLOUD_OCI_DATASCIENCE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-3D14E42D-7AAA-422E-81C9-EEDF3772BA85)
- [DBMS_CLOUD_OCI_DATASCIENCE_METADATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-2A17D942-784B-43A2-9989-329A9B6CC739)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-2D30D096-8095-4B0A-99E6-125478E9B2F9)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_PROVENANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-670F054B-1D30-4887-83F8-6CCBB8AEC813)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_MODEL_VERSION_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-CEC30A2E-E4FD-474F-A2C0-333E1F75E238)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-BC0F6591-3AF4-4C1A-AA50-66F649F50312)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-2F173410-2ACA-442B-B025-B5B681E979A0)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-F93E95E9-4733-4A45-9664-E3B90C83354B)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_GIT_REPO_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-BD4BC548-F349-41FD-8F83-9F1F4052C470)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_GIT_REPO_CONFIG_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A1377C3E-F17B-4BD2-A743-199F27C91377)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_GIT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A886F639-E87A-49E5-AAE3-27EF9C6AC1CB)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_RUNTIME_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-19FFBFA6-2804-4238-90EC-A7524198C9B6)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_NOTEBOOK_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-4FB9898A-49DD-444E-9B80-ECCE3F22818D)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-0099FB59-1D0D-449D-A97B-C5B26039B6F1)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_LOG_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-C82CB265-177C-408E-8BDF-8C18F7CBA29B)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-CFE2A28D-0323-47F1-9E58-98C73F3E6814)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-95F08359-B77F-4B2B-A0F3-8B6AF16A8A79)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-E3034046-F59F-488E-A92C-30FC71625D57)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-0DC27C99-5374-4E86-B91C-93312F52AE3A)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7BEFC348-CF21-4F90-84CF-8CE66AAA9B9B)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-F78F6944-5B59-4B71-8DBE-EF78497294E3)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_OVERRIDE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-1BCBF661-12E1-4846-9899-F368E9E966A6)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_OVERRIDE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-AFFA519D-0490-485A-9092-49419ED4311B)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_PIPELINE_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-C92884C3-DA07-4B97-8155-99558F3A1291)
- [DBMS_CLOUD_OCI_DATASCIENCE_CREATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A6B98861-37CD-46DD-8348-230A673ABF06)
- [DBMS_CLOUD_OCI_DATASCIENCE_DATA_SCIENCE_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-772293CC-DC2B-420F-A4FC-DE4074473494)
- [DBMS_CLOUD_OCI_DATASCIENCE_DATA_SCIENCE_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-8461E274-D106-4BC2-A726-6F7B15940150)
- [DBMS_CLOUD_OCI_DATASCIENCE_DEFAULT_JOB_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-AA241CE8-103A-4F24-B0BD-6EE381F8541C)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-9533ABF4-39F1-4D10-B740-AA19F78F2068)
- [DBMS_CLOUD_OCI_DATASCIENCE_DEFAULT_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-5871E7AE-8B58-4609-822B-8568340CEB9D)
- [DBMS_CLOUD_OCI_DATASCIENCE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-04D84F4F-E6A4-45C6-8961-12DF3EA9F61E)
- [DBMS_CLOUD_OCI_DATASCIENCE_EXPORT_MODEL_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7528389F-D4BD-47E6-BE26-A80669E0DB0B)
- [DBMS_CLOUD_OCI_DATASCIENCE_FAST_LAUNCH_JOB_CONFIG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A770ADD4-FFFC-4B9A-AA4A-E69E9F78AEA1)
- [DBMS_CLOUD_OCI_DATASCIENCE_FILE_STORAGE_MOUNT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-D9CDE411-54D3-425D-A515-0983E421D862)
- [DBMS_CLOUD_OCI_DATASCIENCE_SCALING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-1D67E4FF-BAFE-4278-B093-48C9DFE9B96A)
- [DBMS_CLOUD_OCI_DATASCIENCE_FIXED_SIZE_SCALING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-C3313814-E90C-4FE1-9D0C-84C2D6061E0E)
- [DBMS_CLOUD_OCI_DATASCIENCE_IMPORT_MODEL_ARTIFACT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7D4908ED-4B84-4FC3-AF37-170BC16F3665)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_INSTANCE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-EF00AC33-13D0-4B0D-827C-117A8529DA60)
- [DBMS_CLOUD_OCI_DATASCIENCE_INSTANCE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-234A3224-0FBA-4800-B476-0CCE3E3969B7)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-328458C8-EE4E-42D3-B0F2-13290447AFF4)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_RUN_LOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-742BA538-362C-4F68-B947-BFF399EAE517)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-087EE826-5B8A-4E10-815E-71BF9F1ADCBE)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7C0613E4-BAB4-44C6-9E5B-5927C2E2F657)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A051A304-CE3D-4C0E-8088-5DB1D3B996B8)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-007F2822-988B-4A86-9FE9-A7D6F1B235A7)
- [DBMS_CLOUD_OCI_DATASCIENCE_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-91E248F1-4982-46FE-BF14-B1355D2DAD3D)
- [DBMS_CLOUD_OCI_DATASCIENCE_MANAGED_EGRESS_STANDALONE_JOB_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A1DAE8B3-125E-4AAA-8DA1-A745F3312D3A)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-3F51B7F4-505B-4C79-BF7B-775BFEBA768B)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-23CD88C9-056D-4B85-80E8-9C144828E961)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7CCEC93C-4DDB-4DAB-AB15-7FCE151A2D72)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-FCB887C9-1F93-40EF-AB78-A354AC69F3E2)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_DEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-17AC70E0-F5BF-4959-BA9C-EDB231A6D36C)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_PROVENANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-E70591BD-E83A-4790-9A0D-1054B6FAD890)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7960F955-F765-4A93-B63B-77091D33B063)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_VERSION_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-BF747AF4-7F7C-4713-87C5-3A52E85EA132)
- [DBMS_CLOUD_OCI_DATASCIENCE_MODEL_VERSION_SET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-385D69F3-1745-40D5-BFFB-A2A526E6B26D)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-293E5D8A-C4F1-4BE9-B8CD-7EBDCFAF09B1)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-93725311-25AF-44E3-AE6C-A526CD141A5F)
- [DBMS_CLOUD_OCI_DATASCIENCE_NOTEBOOK_SESSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-1BDA4D0C-A2E4-498A-8CF9-59BA175519F6)
- [DBMS_CLOUD_OCI_DATASCIENCE_OBJECT_STORAGE_MOUNT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-D8794267-C244-4746-9100-FF706EF27896)
- [DBMS_CLOUD_OCI_DATASCIENCE_OCIR_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-02AACBD3-D16E-45EB-B2AE-6CFD6326BFF2)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-571C3BE9-3C30-4774-B06C-E0FF8D098EA5)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CUSTOM_SCRIPT_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-0409C639-45A8-40FD-B702-E62BA6777C6A)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-400C36A9-9436-41CF-9903-16C6E7479237)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CUSTOM_SCRIPT_STEP_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-2133D8F7-E360-431D-AD33-C005625977C0)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7A987520-3D86-4BB1-91BE-CC6FF675B7D4)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_CUSTOM_SCRIPT_STEP_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-35C1D4AD-A40B-47FB-AD8D-074504CA9436)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_DEFAULT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-62BF0FFD-C238-4B14-9C37-B533FD7855AA)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_ML_JOB_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-350E7859-02FE-4F12-9F4A-579AF4E249CF)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_ML_JOB_STEP_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-388FDD24-433D-44E5-93A3-EB6B53D1AD2F)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_ML_JOB_STEP_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-59A37442-39C0-42A5-8688-B3AF2F2DE08F)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_RUN_LOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-F11622C2-8FD2-4982-8A3C-4BD3B371B448)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_RUN_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-31624B3D-6A56-422C-9210-66D3F4DE4A7C)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-05B48E3C-6E49-49FD-8A90-CF03E0816D78)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-1C885162-C310-4227-9E24-90743330C85E)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-AF9E9561-4C56-4F14-B255-7F57B7684C6F)
- [DBMS_CLOUD_OCI_DATASCIENCE_PROJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-13E1EA21-3493-4629-AC06-144371A6C140)
- [DBMS_CLOUD_OCI_DATASCIENCE_PROJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-D7B7F24C-4BA7-4E1F-87D4-32078384B946)
- [DBMS_CLOUD_OCI_DATASCIENCE_SINGLE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-3F523BCD-08A5-4A88-9B50-58B33812E6A0)
- [DBMS_CLOUD_OCI_DATASCIENCE_STANDALONE_JOB_INFRASTRUCTURE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-849005FD-497C-43DF-9BB6-1C45575EF38F)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_CATEGORY_LOG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-5EF90DAF-3963-4C2C-A0AD-CC0BDA9D223A)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_DATA_SCIENCE_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-205FEF76-4E3A-4DD1-9C2C-F78BCFD5ACBA)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-CA500709-DE08-47F5-88DF-E2071372BD93)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_DEFAULT_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-F02FE9B5-F8AB-44E5-9583-1BCD08A9A4A1)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-60504D0B-1C39-45AA-A239-52BD93260E5C)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_JOB_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-5F11761E-BCB5-4E15-8C7B-59A323A4651F)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-3117CDB6-52F1-4724-8273-B04EEC98C9AE)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-2C68FB5C-721C-4148-A19B-A83432081218)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-B485A493-A797-4EDC-AC82-148B19C21C36)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-159E9E80-6870-4F9B-ADDA-78E250033CD9)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_PROVENANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-1D5D9BA8-A207-4481-89FB-265548C2FF61)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_MODEL_VERSION_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-48304EA8-6FFF-45E6-847D-C54B4FD9B8FF)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_NOTEBOOK_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-39091EB6-2A51-45CE-8DF4-804D4480F58C)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_OCIR_MODEL_DEPLOYMENT_ENVIRONMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-E435435E-0D78-43F0-AD54-E4360A04BD3F)
- [DBMS_CLOUD_OCI_DATASCIENCE_PIPELINE_STEP_UPDATE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-31EF508A-77F0-44F3-B730-16A4FE5001F6)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7C478629-AF8A-4985-8854-2388B0D30ECC)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_PIPELINE_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-6FDA8832-507C-466A-838E-1B44C81AD8A8)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-D539D4DE-5633-4248-B61C-667FB85DC14B)
- [DBMS_CLOUD_OCI_DATASCIENCE_UPDATE_SINGLE_MODEL_DEPLOYMENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-74D45588-04D6-4898-B5F8-359938017043)
- [DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-45FF066B-7052-4789-A6E9-2667DF6A7E8E)
- [DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-7AE00E03-9409-4E45-BA7E-439983C06DEC)
- [DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-40EE34D6-81D3-4043-9930-5C1D4D85E6C9)
- [DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-08C682A8-1C0A-4730-ABEF-0272729E093C)
- [DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-A251C2E6-3A9B-481C-AE0F-3A860C1946A9)
- [DBMS_CLOUD_OCI_DATASCIENCE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/datascience_t.html#ADSDK-GUID-61CB72A8-13CA-4BB4-8BCE-D5EEB3B83782)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
