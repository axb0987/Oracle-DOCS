# Asynchronous Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/workrequests.htm
- Fetched: 2026-09-05 01:35 CDT

# Asynchronous Work Requests

This topic describes asynchronous work requests for long-running operations against Oracle Cloud Infrastructure services. It also provides guidance on obtaining request status, and for inspecting the request response to enable filtering for affected resources.

## Overview

API calls to Oracle Cloud Infrastructure services can launch long-running operations that do not complete the client's request before a response is returned. In these cases, the service spawns an asynchronous work request that allows for visibility into the progress of long-running, asynchronous operations. The response to the REST API call contains a work request ID in the`opc-work-request-id`header, which allows you to monitor its progress and status. The work request itself remains in a queue until the operation has completed.

You can monitor the status of the work request at any time by calling`GetWorkRequest`and passing in the work request ID.
Note  
  

Some Oracle Cloud Infrastructure services, such as Compute and Database, support work requests using the[Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/), which contains the`GetWorkRequest`operation.

Some services offer work requests supported by the service API rather than the Work Requests API discussed in this topic. These service APIs each include operations that work in a similar manner to the`GetWorkRequest`operation used by the Work Requests API.

See the reference documentation for each service's work request API for details. Links to each are provided in the[For More Information](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/workrequests.htm#moreinfo)section.

Two features of the request response are of particular interest: the status of the work request, and a list of the resources that are affected by the work request. The status is important because asynchronous work requests must know when an operation has completed, is still running, or whether it has failed altogether.

To retrieve information about work request failures or errors, each service provides APIs for fetching information about errors, and logs. For links to API reference documentation for each of the services, see the section[For More Information](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/workrequests.htm#moreinfo).

Also important in cases where a work request operation affects several resources is having a list of the resources that a work request affects, along with each one's`entityType`and`actionType`attributes.

## Work Request Status

Asynchronous work requests allow you to monitor their progress by providing a status attribute on the`WorkRequest`object. Each of the supported services provides its own API for obtaining status, as listed in the following sections.
Note  
  
There is a[ContainerEngineWaiters](https://docs.oracle.com/iaas/tools/java/latest/com/oracle/bmc/containerengine/ContainerEngineWaiters.html)class that allows you to create a callback using the`forWorkRequest`method. Use this API to forward a notification when an operation's status changes, for example, from`IN_PROGRESS`to`COMPLETED`.

The following table lists status attributes that are supported by the`WorkRequest`object on the respective services.

Service Status Attributes
Application Performance Monitoring
- `ACCEPTED`
- `IN_PROGRESS`
- `SUCCEEDED`
- `FAILED`
- `CANCELING`
- `CANCELED`
Autonomous Recovery Service
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `SUCCEEDED`
- `FAILED`
- `CANCELING`
- `CANCELED`
Big Data Service
- `CREATING`
- `ACTIVE`
- `UPDATING`
- `SUSPENDING`
- `SUSPENDED`
- `RESUMING`
- `DELETING`
- `DELETED`
- `FAILED`
Blockchain Platform
- `ACCEPTED`
- `IN PROGRESS`
- `SUCCEEDED`
- `FAILED`
- `CANCELING`
- `CANCELED`
Cluster Placement Groups
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Compute
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Connector Hub
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Content Management
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Database Management
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
OCI Database with PostgreSQL
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Data Catalog
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Data Integration
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Data Labeling
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
- `FAILED`
Data Science
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Database
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
Database Migration
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
DevOps
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
File Storage
- `CREATING`
- `ACTIVE`
- `DELETING`
- `DELETED`
- `FAILED`
- `UPDATED`
File Storage with Lustre
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `CANCELING`
- `CANCELED`
- `SUCCEEDED`
- `NEEDS_ATTENTION`
- `FAILED`
Fleet Application Management
- `ACCEPTED`
- `IN_PROGRESS`
- `CANCELING`
- `CANCELED`
- `SUCCEEDED`
- `FAILED`
Full Stack Disaster Recovery
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `CANCELING`
- `CANCELED`
- `SUCCEEDED`
- `FAILED`
- `NEEDS_ATTENTION`
Globally Distributed Autonomous AI Database
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Globally Distributed Exadata Database on Exascale Infrastructure
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
GoldenGate
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELLED`
IAM
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Integration
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Java Management
- `ACCEPTED`
- `IN_PROGRESS`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
- `FAILED`
Kubernetes Engine
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Load Balancer
- `CREATING`
- `FAILED`
- `ACTIVE`
- `DELETING`
- `DELETED`
Log Analytics for`LogAnalyticsQueryJobWorkRequest`
- `ACCEPTED`
- `IN_PROGRESS`
- `SUCCEEDED`
- `CANCELLED`
- `FAILED`
Log Analytics for`LogAnalyticsStorageWorkRequest`
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELED`
Log Analytics for`LogAnalyticsConfigWorkRequest`
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
Management Agent
- `CREATED`
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Network Firewall
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Object Storage
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `COMPLETED`
- `CANCELING`
- `CANCELED`
Oracle Cloud Bridge
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Oracle Cloud Migrations
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
- `NEEDS_ATTENTION`
OS Management Hub
- `ACCEPTED`
- `IN_PROGRESS`
- `SUCCEEDED`
- `FAILED`
- `CANCELING`
- `CANCELED`
Process Automation
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Queue
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Resource Manager
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
Secure Desktops
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Service Mesh
- `ACCEPTED`
- `IN_PROGRESS`
- `FAILED`
- `SUCCEEDED`
- `WAITING`
- `CANCELING`
- `CANCELED`
WebLogic Management
- `Accepted`
- `In Progress`
- `Succeeded`
- `Failed`

## Filtering the Request Response

You sometimes need to know which resources are affected by a given asynchronous work request. In cases where the request response includes just one or two affected resources, the body of the request response is probably sufficient. However, in cases where a request response affects a great many resources, you must filter the response to identify the resources that you're interested in.

Filtering of resources listed in a work request response relies on two attributes of the`WorkRequestResource`type:`entityType`and`actionType`.
- entityType: Represents the resource type which the work request affects. This is an optional attribute, but each resource can have only one`entityType`.
- actionType: Represents how the specified resource is affected by the operation associated with the work request. Each service specifies a fixed list of allowable`actionType`values (shown in the sections following).

To obtain resource information on a work request, call`GetWorkRequest`and pass in the work request ID. The call returns a response in JSON format. Following is an example from calling`[](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/WorkRequest/GetWorkRequest)GetWorkRequest`on the Object Storage service.
```

```

Note  
  
Different services provide slightly different responses. See the reference documentation for each service's work request API for details. Links to each are provided in the[For More Information](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/workrequests.htm#moreinfo)section.

The following table lists the entity types and action types that are supported by Oracle Cloud Infrastructure services.

Service Name Operation entityType actionType
Application Performance Monitoring

[CreateApmDomain](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/ApmDomain/CreateApmDomain)

[UpdateApmDomain](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/ApmDomain/UpdateApmDomain)

[DeleteApmDomain](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/ApmDomain/DeleteApmDomain)

[GenerateDataKeys](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/DataKey/GenerateDataKeys)

[RemoveDataKeys](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/DataKey/RemoveDataKeys)`apm-domains`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`
Autonomous Recovery Service

[CreateProtectionPolicy](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectionPolicy/CreateProtectionPolicy/)

[UpdateProtectionPolicy](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectionPolicy/UpdateProtectionPolicy/)

[DeleteProtectionPolicy](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectionPolicy/DeleteProtectionPolicy/)

[ChangeProtectionPolicyCompartment](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectionPolicy/ChangeProtectionPolicyCompartment/)

[CreateRecoveryServiceSubnet](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/RecoveryServiceSubnet/CreateRecoveryServiceSubnet/)

[UpdateRecoveryServiceSubnet](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/RecoveryServiceSubnet/UpdateRecoveryServiceSubnet/)

[DeleteRecoveryServiceSubnet](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/RecoveryServiceSubnet/DeleteRecoveryServiceSubnet/)

[ChangeRecoveryServiceSubnetCompartment](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/RecoveryServiceSubnet/ChangeRecoveryServiceSubnetCompartment/)

[CreateProtectedDatabase](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectedDatabase/CreateProtectedDatabase/)

[UpdateProtectedDatabase](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectedDatabase/UpdateProtectedDatabase/)

[DeleteProtectedDatabase](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectedDatabase/DeleteProtectedDatabase/)

[FetchProtectedDatabaseConfiguration](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectedDatabase/FetchProtectedDatabaseConfiguration/)

[ChangeProtectedDatabaseCompartment](https://docs.oracle.com/iaas/api/#%23/en/recovery-service/20210216/ProtectedDatabase/ChangeProtectedDatabaseCompartment/)

`protectedDatabase`

`protectionPolicy`

`recoveryServiceSubnet`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`

`FAILED`
Blockchain Platform

[CreateBlockchainPlatform](https://docs.oracle.com/iaas/api/#/en/blockchain/latest/BlockchainPlatform/CreateBlockchainPlatform)

[UpdateBlockchainPlatform](https://docs.oracle.com/iaas/api/#/en/blockchain/latest/BlockchainPlatform/UpdateBlockchainPlatform)

[DeleteBlockchainPlatform](https://docs.oracle.com/iaas/api/#/en/blockchain/latest/BlockchainPlatform/DeleteBlockchainPlatform)

[ScaleBlockchainPlatform](https://docs.oracle.com/iaas/api/#/en/blockchain/latest/BlockchainPlatform/ScaleBlockchainPlatform)

[StopBlockchainPlatform](https://docs.oracle.com/iaas/api/#/en/blockchain/latest/BlockchainPlatform/StopBlockchainPlatform)

[StartBlockchainPlatform](https://docs.oracle.com/iaas/api/#/en/blockchain/latest/BlockchainPlatform/StartBlockchainPlatform)`instance`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`
Cluster Placement Groups

[CreateClusterPlacementGroup](https://docs.oracle.com/iaas/api/#/en/clusterplacementgroups/latest/ClusterPlacementGroup/CreateClusterPlacementGroup)

[UpdateClusterPlacementGroup](https://docs.oracle.com/iaas/api/#/en/clusterplacementgroups/latest/ClusterPlacementGroup/UpdateClusterPlacementGroup)

[DeleteClusterPlacementGroup](https://docs.oracle.com/iaas/api/#/en/clusterplacementgroups/latest/ClusterPlacementGroup/DeleteClusterPlacementGroup)

[ChangeClusterPlacementGroupCompartment](https://docs.oracle.com/iaas/api/#/en/clusterplacementgroups/latest/ClusterPlacementGroup/ChangeClusterPlacementGroupCompartment)

`clusterplacementgroup`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`

`FAILED`
Content Management

[CreateOceInstance](https://docs.oracle.com/iaas/api/#/en/oce/latest/OceInstance/CreateOceInstance)

[DeleteOceInstance](https://docs.oracle.com/iaas/api/#/en/oce/latest/OceInstance/DeleteOceInstance)

[UpdateOceInstance](https://docs.oracle.com/iaas/api/#/en/oce/latest/OceInstance/UpdateOceInstance)`oceInstance`

`ACCEPTED`

`IN_PROGRESS`

`FAILED`

`SUCCEEDED`

`CANCELING`

`CANCELED`
Database Management

[ChangeDbManagementPrivateEndpointCompartment](https://docs.oracle.com/iaas/api/#/en/database-management/latest/DbManagementPrivateEndpoint/ChangeDbManagementPrivateEndpointCompartment)

[CreateDbManagementPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/database-management/latest/DbManagementPrivateEndpoint/CreateDbManagementPrivateEndpoint)

[DeleteDbManagementPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/database-management/latest/DbManagementPrivateEndpoint/DeleteDbManagementPrivateEndpoint)

[GetDbManagementPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/database-management/latest/DbManagementPrivateEndpoint/GetDbManagementPrivateEndpoint)

[ListDbManagementPrivateEndpoints](https://docs.oracle.com/iaas/api/#/en/database-management/latest/DbManagementPrivateEndpoint/ListDbManagementPrivateEndpoints)

[UpdateDbManagementPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/database-management/latest/DbManagementPrivateEndpoint/UpdateDbManagementPrivateEndpoint)`private-endpoints`

[CreateWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/CreateWorkspace)

[DeleteWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/DeleteWorkspace)

[ChangeCompartment](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/ChangeCompartment)

[StartWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/StartWorkspace)

[StopWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/StopWorkspace)
Database Migration

[CreateMigration](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Migration/CreateMigration)

[CloneMigration](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Migration/CloneMigration)

[EvaluateMigration](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Job/EvaluateMigration)

[StartMigration](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Job/StartMigration)

[UpdateMigration](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Migration/UpdateMigration)

[DeleteMigration](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Migration/DeleteMigration)

[CreateConnection](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Connection/CreateConnection)

[UpdateConnection](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Connection/UpdateConnection)

[DeleteConnection](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Connection/DeleteConnection)

[DeleteAgent](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/Agent/DeleteAgent)

`odms-connection`

`odms-migration`

`odms-agent`

`ACTIVE`

`INACTIVE`

`ACCEPTED`

`IN_PROGRESS`

`WAITING`

`SUCCEEDED`

`FAILED`
OCI Database with PostgreSQL

[CreateBackup](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/Backup/CreateBackup)

[UpdateBackup](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/Backup/UpdateBackup)

[DeleteBackup](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/Backup/DeleteBackup)

[ChangeBackupCompartment](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/Backup/ChangeBackupCompartment)

[CreateDbSystem](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/DbSystem/CreateDbSystem)

[UpdateDbSystem](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/DbSystem/UpdateDbSystem)

[DeleteDbSystem](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/DbSystem/DeleteDbSystem)

[ChangeDbSystemCompartment](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/DbSystem/ChangeDbSystemCompartment)
Data Catalog

[CreateCatalog](https://docs.oracle.com/iaas/api/#/en/data-catalog/latest/Catalog/CreateCatalog)

[DeleteCatalog](https://docs.oracle.com/iaas/api/#/en/data-catalog/latest/Catalog/DeleteCatalog)

[ChangeCatalogCompartment](https://docs.oracle.com/iaas/api/#/en/data-catalog/latest/Catalog/ChangeCatalogCompartment)`catalog`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`MOVED`
Data Integration

[CreateWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/CreateWorkspace)

[DeleteWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/DeleteWorkspace)

[ChangeCompartment](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/ChangeCompartment)

[StartWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/StartWorkspace)

[StopWorkspace](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/Workspace/StopWorkspace)`disworkspace`

`CREATED`

`UPDATED`

`DELETED`

`MOVED`

`IN_PROGRESS`

`FAILED`
Data Labeling

[CreateDataset](https://docs.oracle.com/iaas/api/#/en/datalabeling/latest/Dataset/CreateDataset)

[DeleteDataset](https://docs.oracle.com/iaas/api/#/en/data-labeling/latest/Dataset/DeleteDataset)

[ChangeDatasetCompartment](https://docs.oracle.com/iaas/api/#/en/data-labeling/latest/Dataset/ChangeDatasetCompartment)

[GenerateDatasetRecords](https://docs.oracle.com/iaas/api/#/en/data-labeling/latest/Dataset/GenerateDatasetRecords)

[SnapshotDataset](https://docs.oracle.com/iaas/api/#/en/data-labeling/latest/Dataset/SnapshotDataset)

[AddDatasetLabels](https://docs.oracle.com/iaas/api/#/en/data-labeling/latest/Dataset/AddDatasetLabels)

[RemoveDatasetLabels](https://docs.oracle.com/iaas/api/#/en/data-labeling/latest/Dataset/RemoveDatasetLabels)

[RenameDatasetLabels](https://docs.oracle.com/iaas/api/#/en/data-labeling/latest/Dataset/RenameDatasetLabels)`datalabelingdataset`

`ACCEPTED`

`IN_PROGRESS`

`WAITING`

`SUCCEEDED`

`CANCELING`

`CANCELED`

`FAILED`
Data Science

[CreateNotebookSession](https://docs.oracle.com/iaas/api/#/en/data-science/latest/NotebookSession/CreateNotebookSession)

[DeleteNotebookSession](https://docs.oracle.com/iaas/api/#/en/data-science/latest/NotebookSession/DeleteNotebookSession)

[DeleteProject](https://docs.oracle.com/iaas/api/#/en/data-science/latest/Project/DeleteProject)

`NotebookSession`

`Project`

`ACCEPTED`

`IN_PROGRESS`

`FAILED`

`SUCCEEDED`

`CANCELING`

`CANCELED`
DevOps

[CreateProject](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/Project/CreateProject)

[UpdateProject](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/Project/UpdateProject)

[ChangeProjectCompartment](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/Project/ChangeProjectCompartment)

[DeleteProject](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/Project/DeleteProject)

[CreateDeployEnvironment](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployEnvironment/CreateDeployEnvironment)

[UpdateDeployEnvironment](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployEnvironment/UpdateDeployEnvironment)

[DeleteDeployEnvironment](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployEnvironment/DeleteDeployEnvironment)

[CreateDeployArtifact](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployArtifact/CreateDeployArtifact)

[UpdateDeployArtifact](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployArtifact/UpdateDeployArtifact)

[DeleteDeployArtifact](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployArtifact/DeleteDeployArtifact)

[CreateDeployPipeline](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployPipeline/CreateDeployPipeline)

[CreateDeployStage](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployStage/CreateDeployStage)

[UpdateDeployPipeline](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployPipeline/UpdateDeployPipeline)

[UpdateDeployStage](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployStage/UpdateDeployStage)

[DeleteDeployPipeline](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployPipeline/DeleteDeployPipeline)

[DeleteDeployStage](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/DeployStage/DeleteDeployStage)

[CreateDeployment](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/Deployment/CreateDeployment)

[UpdateDeployment](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/Deployment/UpdateDeployment)

[CancelDeployment](https://docs.oracle.com/iaas/api/#%23/en/devops/latest/Deployment/CancelDeployment)

`Project`

`DeployEnvironment`

`DeployArtifact`

`DeployPipeline`

`DeployStage`

`Deployment`

`ACCEPTED`

`IN_PROGRESS`

`FAILED`

`SUCCEEDED`

`CANCELING`

`CANCELED`
File Storage with Lustre

[CreateLustreFileSystem](https://docs.oracle.com/iaas/api/#/en/lustre/latest/LustreFileSystem/CreateLustreFileSystem)

[UpdateLustreFileSystem](https://docs.oracle.com/iaas/api/#/en/lustre/latest/LustreFileSystem/UpdateLustreFileSystem)

[ChangeLustreFileSystemCompartment](https://docs.oracle.com/iaas/api/#/en/lustre/latest/LustreFileSystem/ChangeLustreFileSystemCompartment)

[DeleteLustreFileSystem](https://docs.oracle.com/iaas/api/#/en/lustre/latest/LustreFileSystem/DeleteLustreFileSystem)

`lustrefilesystem`

`ACCEPTED`

`IN_PROGRESS`

`WAITING`

`SUCCEEDED`

`CANCELING`

`CANCELED`

`NEEDS_ATTENTION`

`FAILED`
Full Stack Disaster Recovery

[CreateDrProtectionGroup](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrProtectionGroup/CreateDrProtectionGroup)

[UpdateDrProtectionGroup](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrProtectionGroup/UpdateDrProtectionGroup)

[DeleteDrProtectionGroup](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrProtectionGroup/DeleteDrProtectionGroup)

[ChangeDrProtectionGroupCompartment](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrProtectionGroup/ChangeDrProtectionGroupCompartment)

[AssociateDrProtectionGroup](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrProtectionGroup/AssociateDrProtectionGroup)

[DisassociateDrProtectionGroup](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrProtectionGroup/DisassociateDrProtectionGroup)

[UpdateDrProtectionGroupRole](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrProtectionGroup/UpdateDrProtectionGroupRole)

[CreateDrPlan](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlan/CreateDrPlan)

[UpdateDrPlan](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlan/UpdateDrPlan)

[DeleteDrPlan](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlan/DeleteDrPlan)

[CreateDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/CreateDrPlanExecution)

[UpdateDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/UpdateDrPlanExecution)

[DeleteDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/DeleteDrPlanExecution)

[RetryDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/RetryDrPlanExecution)

[IgnoreDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/IgnoreDrPlanExecution)

[CancelDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/CancelDrPlanExecution)

[PauseDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/PauseDrPlanExecution)

[ResumeDrPlanExecution](https://docs.oracle.com/iaas/api/#%23/en/disaster-recovery/latest/DrPlanExecution/ResumeDrPlanExecution)

`DrProtectionGroup`

`DrPlan`

`DrPlanExecution`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`

`FAILED`
Globally Distributed Autonomous AI Database

[ListShardedDatabases](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabaseCollection/ListShardedDatabases)

[GetShardedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/GetShardedDatabase)

[GenerateWallet](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/GenerateWallet)

[UpdateShardedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/UpdateShardedDatabase)

[ValidateNetwork](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/ValidateNetwork)

[StartShardedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/StartShardedDatabase)

[StopShardedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/StopShardedDatabase)

[ChangeShardedDatabaseCompartment](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/ChangeShardedDatabaseCompartment)

[CreateShardedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/CreateShardedDatabase)

[DeleteShardedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/ShardedDatabase/DeleteShardedDatabase)

[ChangePrivateEndpointCompartment](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/PrivateEndpoint/ChangePrivateEndpointCompartment)

[CreatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/PrivateEndpoint/CreatePrivateEndpoint)

[DeletePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/PrivateEndpoint/DeletePrivateEndpoint)

[GetPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/PrivateEndpoint/GetPrivateEndpoint)

[UpdatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/PrivateEndpoint/UpdatePrivateEndpoint)

[ListPrivateEndpoints](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/PrivateEndpointCollection/ListPrivateEndpoints)

`OsdShardedDatabase`

`OsdPrivateEndpoint`

`ACCEPTED`

`IN_PROGRESS`

`WAITING`

`FAILED`

`SUCCEEDED`

`CANCELING`

`CANCELED`
Globally Distributed Exadata Database on Exascale Infrastructure

[ChangeDistributedDatabaseCompartment](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/ChangeDistributedDatabaseCompartment)

[ConfigureDistributedDatabaseSharding](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/ConfigureDistributedDatabaseSharding)

[CreateDistributedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/CreateDistributedDatabase)

[DeleteDistributedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/DeleteDistributedDatabase)

[PatchDistributedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/PatchDistributedDatabase)

[StartDistributedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/StartDistributedDatabase)

[StopDistributedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/StopDistributedDatabase)

[UpdateDistributedDatabase](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabase/UpdateDistributedDatabase)

[ChangeDistributedDatabasePrivateEndpointCompartment](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabasePrivateEndpoint/ChangeDistributedDatabasePrivateEndpointCompartment)

[CreateDistributedDatabasePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabasePrivateEndpoint/CreateDistributedDatabasePrivateEndpoint)

[DeleteDistributedDatabasePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabasePrivateEndpoint/DeleteDistributedDatabasePrivateEndpoint)

[UpdateDistributedDatabasePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/DistributedDatabasePrivateEndpoint/UpdateDistributedDatabasePrivateEndpoint)

`osddistributeddb`

`osddistributeddbprivateendpoint`

`ACCEPTED`

`IN_PROGRESS`

`WAITING`

`FAILED`

`SUCCEEDED`

`CANCELING`

`CANCELED`
GoldenGate

[CreateDeployment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/CreateDeployment)

[DeleteDeployment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/DeleteDeployment)

[StartDeployment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/StartDeployment)

[StopDeployment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/StopDeployment)

[UpdateDeployment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/UpdateDeployment)

[UpgradeDeployment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/UpgradeDeployment)

[ChangeDeploymentCompartment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/Deployment/ChangeDeploymentCompartment)

[CreateDatabaseRegistration](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/DatabaseRegistration/CreateDatabaseRegistration)

[UpdateDatabaseRegistration](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/DatabaseRegistration/UpdateDatabaseRegistration)

[DeleteDatabaseRegistration](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/DatabaseRegistration/DeleteDatabaseRegistration)

[ChangeDatabaseRegistrationCompartment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/DatabaseRegistration/ChangeDatabaseRegistrationCompartment)

[CreateDeploymentBackup](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/DeploymentBackup/CreateDeploymentBackup)

[DeleteDeploymentBackup](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/DeploymentBackup/DeleteDeploymentBackup)

[RestoreDeployment](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/DeploymentBackup/RestoreDeployment)

`Deployment`

`DatabaseRegistration`

`DeploymentBackup`

`CREATING`

`UPDATING`

`ACTIVE`

`INACTIVE`

`DELETING`

`DELETED`

`FAILED`
Integration

[CreateIntegrationInstance](https://docs.oracle.com/iaas/api/#/en/integration/latest/IntegrationInstance/CreateIntegrationInstance/)

[DeleteIntegrationInstance](https://docs.oracle.com/iaas/api/#/en/integration/latest/IntegrationInstance/DeleteIntegrationInstance/)

[GetIntegrationInstance](https://docs.oracle.com/iaas/api/#/en/integration/latest/IntegrationInstance/GetIntegrationInstance/)

[StartIntegrationInstance](https://docs.oracle.com/iaas/api/#/en/integration/latest/IntegrationInstance/StartIntegrationInstance/)

[StopIntegrationInstance](https://docs.oracle.com/iaas/api/#/en/integration/latest/IntegrationInstance/StopIntegrationInstance/)

[UpdateIntegrationInstance](https://docs.oracle.com/iaas/api/#/en/integration/latest/IntegrationInstance/UpdateIntegrationInstance/)`instance`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`

`FAILED`
Kubernetes Engine

[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)

[DeleteCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/DeleteCluster)

[UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)

[CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool)

[DeleteNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/DeleteNodePool)

[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)

`cluster`

`nodepool`

`ACCEPTED`

`IN_PROGRESS`

`FAILED`

`SUCCEEDED`

`CANCELING`

`CANCELED`
Load Balancer

[CreateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/CreateLoadBalancer)

[UpdateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/UpdateLoadBalancer)

[DeleteLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/DeleteLoadBalancer)`LoadBalancer`

`ACCEPTED`

`IN_PROGRESS`

`FAILED`

`SUCCEEDED`
Management Agent[DeployPlugins](https://docs.oracle.com/iaas/api/#/en/management-agent/latest/ManagementAgent/DeployPlugins)`managementAgent`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`
Network Firewall

[CreateNetworkFirewall](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewall/CreateNetworkFirewall/)

[UpdateNetworkFirewall](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewall/UpdateNetworkFirewall/)

[DeleteNetworkFirewall](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewall/DeleteNetworkFirewall/)

[ChangeNetworkFirewallCompartment](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewall/ChangeNetworkFirewallCompartment/)

[CreateNetworkFirewallPolicy](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewallPolicy/CreateNetworkFirewallPolicy/)

[UpdateNetworkFirewallPolicy](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewallPolicy/UpdateNetworkFirewallPolicy/)

[DeleteNetworkFirewallPolicy](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewallPolicy/DeleteNetworkFirewallPolicy/)

[ChangeNetworkFirewallPolicyCompartment](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/NetworkFirewallPolicy/ChangeNetworkFirewallPolicyCompartment/)

`NetworkFirewall`

`NetworkFirewallPolicy`
- `ACCEPTED`
- `IN_PROGRESS`
- `WAITING`
- `FAILED`
- `SUCCEEDED`
- `CANCELING`
- `CANCELED`
Object Storage[CopyObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject)`object`

`READ`

`WRITTEN`
Oracle Cloud Bridge

[CreateEnvironment](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Environment/CreateEnvironment/)

[UpdateEnvironment](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Environment/UpdateEnvironment)

[DeleteEnvironment](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Environment/DeleteEnvironment/)

[ChangeEnvironmentCompartment](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Environment/ChangeEnvironmentCompartment)

[CreateAgent](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Agent/CreateAgent)

[UpdateAgent](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Agent/UpdateAgent)

[DeleteAgent](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Agent/DeleteAgent)

[ChangeAgentCompartment](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Agent/ChangeAgentCompartment)

[CreateAgentDependency](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AgentDependency/CreateAgentDependency)

[UpdateAgentDependency](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AgentDependency/UpdateAgentDependency)

[DeleteAgentDependency](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AgentDependency/DeleteAgentDependency)

[ChangeAgentDependencyCompartment](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AgentDependency/ChangeAgentDependencyCompartment)

[CreateInventory](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Inventory/CreateInventory)

[DeleteInventory](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Inventory/DeleteInventory)

[ImportInventory](https://docs.oracle.com/iaas/api/#/en/OCB/latest/Inventory/ImportInventory)

[DeleteAssetSource](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AssetSource/DeleteAssetSource)

[RefreshAssetSource](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AssetSource/RefreshAssetSource)

[CreateAssetSource](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AssetSource/CreateAssetSource)

[UpdateAssetSource](https://docs.oracle.com/iaas/api/#/en/OCB/latest/AssetSource/UpdateAssetSource)`ocbworkrequest`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED``FAILED`
Oracle Cloud Migrations

[CreateMigration](https://docs.oracle.com/iaas/api/#/en/ocm/latest/Migration/CreateMigration)

[UpdateMigration](https://docs.oracle.com/iaas/api/#/en/ocm/latest/Migration/UpdateMigration)

[RefreshMigration](https://docs.oracle.com/iaas/api/#/en/ocm/latest/Migration/RefreshMigration)

[DeleteMigration](https://docs.oracle.com/iaas/api/#/en/ocm/latest/Migration/DeleteMigration)

[ChangeMigrationCompartment](https://docs.oracle.com/iaas/api/#/en/ocm/latest/Migration/ChangeMigrationCompartment)

[StartAssetReplication](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationAsset/StartAssetReplication)

[StartMigrationReplication](https://docs.oracle.com/iaas/api/#/en/ocm/latest/Migration/StartMigrationReplication)

[CreateReplicationSchedule](https://docs.oracle.com/iaas/api/#/en/ocm/latest/ReplicationSchedule/CreateReplicationSchedule)

[UpdateReplicationSchedule](https://docs.oracle.com/iaas/api/#/en/ocm/latest/ReplicationSchedule/UpdateReplicationSchedule)

[DeleteReplicationSchedule](https://docs.oracle.com/iaas/api/#/en/ocm/latest/ReplicationSchedule/DeleteReplicationSchedule)

[ChangeReplicationScheduleCompartment](https://docs.oracle.com/iaas/api/#/en/ocm/latest/ReplicationSchedule/ChangeReplicationScheduleCompartment)

[CreateMigrationPlan](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationPlan/CreateMigrationPlan)

[UpdateMigrationPlan](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationPlan/UpdateMigrationPlan)

[DeleteMigrationPlan](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationPlan/DeleteMigrationPlan)

[ChangeMigrationPlanCompartment](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationPlan/ChangeMigrationPlanCompartment)

[RefreshMigrationPlan](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationPlan/RefreshMigrationPlan)

[ExecuteMigrationPlan](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationPlan/ExecuteMigrationPlan)

[RefreshMigrationAsset](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationAsset/RefreshMigrationAsset)

[CreateMigrationAsset](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationAsset/CreateMigrationAsset)

[DeleteMigrationAsset](https://docs.oracle.com/iaas/api/#/en/ocm/latest/MigrationAsset/DeleteMigrationAsset)

[CreateTargetAsset](https://docs.oracle.com/iaas/api/#/en/ocm/latest/TargetAsset/CreateTargetAsset)

[UpdateTargetAsset](https://docs.oracle.com/iaas/api/#/en/ocm/latest/TargetAsset/UpdateTargetAsset)

[DeleteTargetAsset](https://docs.oracle.com/iaas/api/#/en/ocm/latest/TargetAsset/DeleteTargetAsset)`ocmworkrequest`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED``FAILED`
OS Management Hub

[AttachManagedInstancesToLifecycleStage](https://docs.oracle.com/iaas/api/#/en/osmh/latest/LifecycleStage/AttachManagedInstancesToLifecycleStage/)

[AttachManagedInstancesToManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/AttachManagedInstancesToManagedInstanceGroup/)

[AttachSoftwareSourcesToManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/AttachSoftwareSourcesToManagedInstance/)

[AttachSoftwareSourcesToManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/AttachSoftwareSourcesToManagedInstanceGroup/)

[DeleteLifecycleEnvironment](https://docs.oracle.com/iaas/api/#/en/osmh/latest/LifecycleEnvironment/DeleteLifecycleEnvironment/)

[DeleteManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/DeleteManagedInstanceGroup/)

[DetachManagedInstancesFromLifecycleStage](https://docs.oracle.com/iaas/api/#/en/osmh/latest/LifecycleStage/DetachManagedInstancesFromLifecycleStage/)

[DetachManagedInstancesFromManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/DetachManagedInstancesFromManagedInstanceGroup/)

[DetachSoftwareSourcesFromManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/DetachSoftwareSourcesFromManagedInstance/)

[DisableModuleStreamOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/DisableModuleStreamOnManagedInstance/)

[DisableModuleStreamOnManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/DisableModuleStreamOnManagedInstanceGroup/)

[EnableModuleStreamOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/EnableModuleStreamOnManagedInstance/)

[EnableModuleStreamOnManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/EnableModuleStreamOnManagedInstanceGroup/)

[InstallModuleStreamProfileOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/InstallModuleStreamProfileOnManagedInstance/)

[InstallModuleStreamProfileOnManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/InstallModuleStreamProfileOnManagedInstanceGroup/)

[InstallPackagesOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/InstallPackagesOnManagedInstance/)

[InstallPackagesOnManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/InstallPackagesOnManagedInstanceGroup/)

[InstallWindowsUpdatesOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/InstallWindowsUpdatesOnManagedInstance/)

[InstallAllWindowsUpdatesOnManagedInstancesInCompartment](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/InstallAllWindowsUpdatesOnManagedInstancesInCompartment/)

[InstallWindowsUpdatesOnManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/InstallWindowsUpdatesOnManagedInstanceGroup/)

[ManageModuleStreamsOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/ManageModuleStreamsOnManagedInstance/)

[ManageModuleStreamsOnManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/ManageModuleStreamsOnManagedInstanceGroup/)

[PromoteSoftwareSourceToLifecycleStage](https://docs.oracle.com/iaas/api/#/en/osmh/latest/LifecycleStage/PromoteSoftwareSourceToLifecycleStage/)

[RefreshSoftwareOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/RefreshSoftwareOnManagedInstance/)

[RemoveModuleStreamProfileFromManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/RemoveModuleStreamProfileFromManagedInstance/)

[RemoveModuleStreamProfileFromManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/RemoveModuleStreamProfileFromManagedInstanceGroup/)

[RemovePackagesFromManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/RemovePackagesFromManagedInstance/)

[RemovePackagesFromManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/InstallPackagesOnManagedInstanceGroup/)

[ScheduledJob/RunScheduledJobNow](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ScheduledJob/RunScheduledJobNow/)

[SwitchModuleStreamOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/SwitchModuleStreamOnManagedInstance/)

[SynchronizeMirrors](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagementStation/SynchronizeMirrors/)

[SynchronizeSingleMirrors](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagementStation/SynchronizeSingleMirrors/)

[UpdateAllPackagesOnManagedInstanceGroup](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/UpdateAllPackagesOnManagedInstanceGroup/)

[UpdateAllPackagesOnManagedInstancesInCompartment](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/UpdateAllPackagesOnManagedInstancesInCompartment/)

[UpdateManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/UpdateManagedInstance/)

[UpdateManagementStation](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagementStation/UpdateManagementStation/)

[UpdatePackagesOnManagedInstance](https://docs.oracle.com/iaas/api/#/en/osmh/latest/ManagedInstance/UpdatePackagesOnManagedInstance/)

[UpdateSoftwareSource](https://docs.oracle.com/iaas/api/#/en/osmh/latest/SoftwareSource/UpdateSoftwareSource/)

`managementagent`

`osmhlifecycleenvironment`

`osmhlifecyclestage`

`osmhmanagedinstancegroup`

`osmhmanagementstation`

`osmhsoftwaresource`

`ACCEPTED`

`IN_PROGRESS`

`SUCCEEDED`

`FAILED`

`CANCELING`

`CANCELED`
Process Automation

[CreateOpaInstance](https://docs.oracle.com/iaas/api/#/en/opa/latest/OpaInstance/CreateOpaInstance/)

[UpdateOpaInstance](https://docs.oracle.com/iaas/api/#/en/opa/latest/OpaInstance/UpdateOpaInstance/)

[DeleteOpaInstance](https://docs.oracle.com/iaas/api/#/en/opa/latest/OpaInstance/DeleteOpaInstance/)

[ChangeOpaInstanceCompartment](https://docs.oracle.com/iaas/api/#/en/opa/latest/OpaInstance/ChangeOpaInstanceCompartment/)`instance`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`

`FAILED`
Queue

[CreateQueue](https://docs.oracle.com/iaas/api/#/en/queue/latest/Queue/CreateQueue)

[UpdateQueue](https://docs.oracle.com/iaas/api/#/en/queue/latest/Queue/UpdateQueue)

[PurgeQueue](https://docs.oracle.com/iaas/api/#/en/queue/latest/Queue/PurgeQueue)

[DeleteQueue](https://docs.oracle.com/iaas/api/#/en/queue/latest/Queue/DeleteQueue)

[ChangeQueueCompartment](https://docs.oracle.com/iaas/api/#/en/queue/latest/Queue/ChangeQueueCompartment)
Resource Manager

[ChangeStackCompartment](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/ChangeStackCompartment)

[CreatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/CreatePrivateEndpoint)

[CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack)

[DeletePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/DeletePrivateEndpoint)

[DetectStackDrift](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/DetectStackDrift)

[UpdatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/UpdatePrivateEndpoint)

`ormprivateendpoint`

`ormstack`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`
Secure Desktops

[CreateDesktopPool](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/DesktopPool/CreateDesktopPool)

[UpdateDesktopPool](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/DesktopPool/UpdateDesktopPool)

[DeleteDesktopPool](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/DesktopPool/DeleteDesktopPool)

[ChangeDesktopPoolCompartment](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/DesktopPool/ChangeDesktopPoolCompartment)

[StartDesktopPool](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/DesktopPool/StartDesktopPool)

[StopDesktopPool](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/DesktopPool/StopDesktopPool)

[DeleteDesktop](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/Desktop/DeleteDesktop)

[UpdateDesktop](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/Desktop/UpdateDesktop)

[StartDesktop](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/Desktop/StartDesktop)

[StopDesktop](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/Desktop/StopDesktop)

`desktop`

`desktoppool`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`

`FAILED`
Service Mesh

[CreateMesh](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/Mesh/CreateMesh)

[UpdateMesh](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/Mesh/UpdateMesh)

[DeleteMesh](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/Mesh/DeleteMesh)

[MoveMesh](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/Mesh/ChangeMeshCompartment)

[CreateAccessPolicy](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/AccessPolicy/CreateAccessPolicy)

[UpdateAccessPolicy](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/AccessPolicy/UpdateAccessPolicy)

[DeleteAccessPolicy](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/AccessPolicy/DeleteAccessPolicy)

[MoveAccessPolicy](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/AccessPolicy/ChangeAccessPolicyCompartment)

[CreateVirtualService](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualService/CreateVirtualService)

[UpdateVirtualService](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualService/UpdateVirtualService)

[DeleteVirtualService](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualService/DeleteVirtualService)

[MoveVirtualService](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualService/ChangeVirtualServiceCompartment)

[CreateVirtualServiceRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualServiceRouteTable/VirtualServiceRouteTableCreate)

[UpdateVirtualServiceRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualServiceRouteTable/VirtualServiceRouteTableUpdate)

[DeleteVirtualServiceRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualServiceRouteTable/VirtualServiceRouteTableDelete)

[MoveVirtualServiceRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualServiceRouteTable/ChangeVirtualServiceRouteTableCompartment)

[CreateVirtualDeployment](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualDeployment/VirtualDeploymentCreate)

[UpdateVirtualDeployment](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualDeployment/VirtualDeploymentUpdate)

[DeleteVirtualDeployment](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualDeployment/VirtualDeploymentDelete)

[MoveVirtualDeployment](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/VirtualDeployment/ChangeVirtualDeploymentCompartment)

[CreateIngressGateway](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGateway/IngressGatewayCreate)

[UpdateIngressGateway](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGateway/IngressGatewayUpdate)

[DeleteIngressGateway](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGateway/IngressGatewayDelete)

[MoveIngressGateway](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGateway/ChangeIngressGatewayCompartment)

[CreateIngressGatewayRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGatewayRouteTable/IngressGatewayRouteTableCreate)

[UpdateIngressGatewayRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGatewayRouteTable/IngressGatewayRouteTableUpdate)

[DeleteIngressGatewayRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGatewayRouteTable/IngressGatewayRouteTableDelete)

[MoveIngressGatewayRouteTable](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/IngressGatewayRouteTable/ChangeIngressGatewayRouteTableCompartment)

`AccessPolicy`

`IngressGateway`

`IngressGatewayRouteTable`

`Mesh`

`VirtualDeployment`

`VirtualService`

`VirtualServiceRouteTable`

`CREATED`

`UPDATED`

`DELETED`

`IN_PROGRESS`

`RELATED`

`FAILED`
WebLogic Management

[StartWlsDomain](https://docs.oracle.com/iaas/api/#/en/wlms/latest/WlsDomain/StartWlsDomain/)

[StopWlsDomain](https://docs.oracle.com/iaas/api/#/en/wlms/latest/WlsDomain/StopWlsDomain/)

[RestartWlsDomain](https://docs.oracle.com/iaas/api/#/en/wlms/latest/WlsDomain/RestartWlsDomain/)

[ScanWlsDomain](https://docs.oracle.com/iaas/api/#/en/wlms/latest/WlsDomain/ScanWlsDomain/)

[ScanManagedInstance](https://docs.oracle.com/iaas/api/#/en/wlms/latest/ManagedInstance/ScanManagedInstance/)

[InstallLatestPatchesOnWlsDomain](https://docs.oracle.com/iaas/api/#/en/wlms/latest/WlsDomain/InstallLatestPatchesOnWlsDomain/)

[RestoreWlsDomain](https://docs.oracle.com/iaas/api/#/en/wlms/latest/WlsDomain/RestoreWlsDomain/)

`wlsDomain`

`managedInstance`

`CREATED`

`IN_PROGRESS`

`UPDATED`

`DELETED`

`FAILED`

`RELATED`

## Request/Response Sample

Following is a sequence of REST API calls to create a cluster, which is a common long-running operation. The caller retrieves the work request ID from the response to the initial`POST`call and then periodically polls the`WorkRequest`to determine the status of the operation. The request/response sequence that follows depicts this workflow:
- The user issues a`CreateCluster`API call.
- The service responds with status code 202, indicating that the request has been accepted and returns a work request ID in the`opc-work-request-id`header.
- Next, the user issues a`GET`call on the work request ID to obtain the status of the work request.
- The service responds with status code 200, indicating in the response body that the`CLUSTER_CREATE`operation has the status`ACCEPTED`.
- With continued polling, we see another`GET`call for the work request.
- The service responds with status code 200. The response body reports that the operation`SUCCEEDED`.

Step 1 . Initial API call to initiate a`CLUSTER_CREATE`operation.

```

```

Step 2 . The response to the initial API call, which contains the work request ID in the`Opc-Work-Request-Id header`.

```

```

Step 3 . Because this is a long-running operation, the user periodically polls the work request using a`GET`call to determine its status.

```

```

Step 4 . The`GET`call returns the following response, which indicates in the response body that the`CLUSTER_CREATE`operation has a status of`ACCEPTED`.

```

```

Step 5 . The operation continues, and the user continues to poll the work request using the`GET`method.

```

```

Step 6 . The last`GET`call produced the following response, which indicates that the operation has completed. Note the`entityType`is "cluster" and the`actionType`is "CREATED".

```

```

## For More Information

- [Application Performance Monitoring work request API](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/WorkRequest/)
- [Autonomous Recovery Service work request API](https://docs.oracle.com/iaas/api/#/en/recovery-service/latest/WorkRequest/)
- [Bastion work request API](https://docs.oracle.com/iaas/api/#/en/bastion/latest/WorkRequest/)
- [Batch work request API](https://docs.oracle.com/iaas/api/#/en/batch/latest/WorkRequest/)
- [Blockchain Platform work requests](https://docs.oracle.com/en/cloud/paas/blockchain-cloud/administeroci/getting-started.html)
- [Cloud Advisor work request API](https://docs.oracle.com/iaas/api/#/en/advisor/latest/WorkRequest/)
- [Cluster Placement Groups work request API](https://docs.oracle.com/iaas/api/#/en/clusterplacementgroups/latest/WorkRequest/)
- [Compute work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
- 

Connector Hub:
- [Viewing the State of a Connector Hub Work Request](https://docs.oracle.com/iaas/Content/connector-hub/workrequests.htm)
- [Connector Hub work request API](https://docs.oracle.com/iaas/api/#/en/serviceconnectors/latest/WorkRequest)
- [Container Instances work request API](https://docs.oracle.com/iaas/api/#/en/container-instances/latest/WorkRequest/)
- [Content Management work request API](https://docs.oracle.com/iaas/api/#/en/oce/latest/WorkRequest)
- 

Data Catalog:
- [Data Catalog Work Requests](https://docs.oracle.com/iaas/Content/data-catalog/using/work-request.htm)
- [Data Catalog work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
- [Data Integration work request API](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/WorkRequest/)
- 

Data Labeling:
- [Data Labeling Work Requests](https://docs.oracle.com/iaas/Content/data-labeling/using/work-requests.htm)
- [Data Labeling work request API](https://docs.oracle.com/iaas/api/#/en/datalabeling/latest/WorkRequest/)
- 

Data Science:
- [Creating Notebook Sessions](https://docs.oracle.com/iaas/Content/data-science/using/create-notebook-sessions.htm)and[Deleting Projects](https://docs.oracle.com/iaas/Content/data-science/using/manage-projects.htm#delete-projects)
- [Data Science work request API](https://docs.oracle.com/iaas/api/#/en/data-science/latest/WorkRequest/)
- [Database work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
- [Database Management work request API](https://docs.oracle.com/iaas/api/#/en/database-management/latest/WorkRequest/)
- [Database Migration work request API](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/WorkRequest/)
- [Database Tools work request API](https://docs.oracle.com/iaas/api/#/en/database-tools/latest/WorkRequest/)
- [OCI Database with PostgreSQL work request API](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/WorkRequest/)
- [DevOps work request API](https://docs.oracle.com/iaas/api/#/en/devops/latest/WorkRequest/)
- [File Storage work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
- [File Storage with Lustre work request API](https://docs.oracle.com/iaas/api/#/en/lustre/latest/WorkRequest/)
- [Fleet Application Management work request API](https://docs.oracle.com/iaas/api/#/en/fleet-management/latest/WorkRequest/)
- [Full Stack Disaster Recovery work request API](https://docs.oracle.com/iaas/api/#/en/disaster-recovery/latest/WorkRequest/)
- [Globally Distributed Autonomous Database work request API](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/WorkRequest/)
- [Globally Distributed Exadata Database on Exascale Infrastructure Work Request API](https://docs.oracle.com/iaas/api/#/en/globally-distributed-database/latest/WorkRequest/)
- [GoldenGate work request API](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/WorkRequest/)
- 

IAM:
- [IAM work request API](https://docs.oracle.com/iaas/api/#/en/identity/latest/WorkRequest/)([To delete a different compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To_delete_a_compartment))
- [TaggingWorkRequest API](https://docs.oracle.com/iaas/api/#/en/identity/latest/TaggingWorkRequest/)([Tags and Tag Namespace Concepts](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm))
- [Integration work request API](https://docs.oracle.com/iaas/api/#/en/integration/latest/WorkRequest/)
- [Java Management work request API](https://docs.oracle.com/iaas/api/#/en/jms/latest/WorkRequest/)
- [Kubernetes Engine work request API](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/WorkRequest/)
- 

Load Balancer:
- [Work Requests for Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/viewingworkrequest.htm)
- [Load Balancer work request API](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/WorkRequest/)
- [Log Analytics work request API](https://docs.oracle.com/iaas/api/#/en/logan-api-spec/latest/WorkRequest/)
- [Management Agent work request API](https://docs.oracle.com/iaas/api/#/en/management-agent/latest/WorkRequest/)
- [MySQL HeatWave work request API](https://docs.oracle.com/iaas/api/#/en/mysql/latest/WorkRequest/)
- [Network Firewall work request API](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/WorkRequest/)
- 

Object Storage:
- [Copy Object Work Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/copyingobjects.htm#workrequests)
- [Object Storage work request API](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/WorkRequest/)
- [Oracle Cloud Bridge work request API](https://docs.oracle.com/iaas/api/#/en/OCB/latest/WorkRequest/)
- [Oracle Cloud Migrations work request API](https://docs.oracle.com/iaas/api/#/en/ocm/latest/WorkRequest/)
- [OS Management Hub work request API](https://docs.oracle.com/iaas/api/#/en/osmh/latest/WorkRequest/)
- [Process Automation work request API](https://docs.oracle.com/iaas/api/#/en/opa/latest/WorkRequest/)
- [Queue work request API](https://docs.oracle.com/iaas/api/#/en/queue/latest/WorkRequest/)
- [Resource Manager work request API](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/)
- [Secure Desktops work request API](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/WorkRequest/)
- [Service Mesh work request API](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/WorkRequest/)
- [Stack Monitoring work request API](https://docs.oracle.com/iaas/api/#/en/stack-monitoring/latest/WorkRequest/)
- [Vision work request API](https://docs.oracle.com/iaas/api/#/en/vision/latest/WorkRequest/)
- Visual Builder Studio:[WorkRequest API](https://docs.oracle.com/iaas/api/#/en/visual-builder-studio/latest/WorkRequest)
- [Vulnerability Scanning work request API](https://docs.oracle.com/iaas/api/#/en/scanning/latest/WorkRequest/)
- [WebLogic Management work request API](https://docs.oracle.com/iaas/api/#/en/wlms/latest/WorkRequest/)
