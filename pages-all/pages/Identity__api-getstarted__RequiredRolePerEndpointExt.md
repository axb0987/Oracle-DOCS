# AppRole Permissions
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm
- Fetched: 2026-09-05 02:17 CDT

# AppRole Permissions

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following pages are organized by AppRole and provide the endpoints and the allowed operations for that endpoint.
- 

[Application Administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEAppAdmExt)
- 

[Audit Administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEAuditAdmExt)
- 

[Authenticated Client](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEAuthClientExt)
- 

[Authenticator Client](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEAuthorClientExt)
- 

[Change Password](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPECngePsswrdExt)
- 

[Cloud Gate](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPECldGateExt)
- 

[DB administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEDBAdminExt)
- 

[Forgot Password](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEFrgtPsswordExt)
- 

[Help Desk administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEHelpDeskAdmExt)
- 

[Identity Domain Administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEIdDAdmnExt)
- 

[Kerberos administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEKerberosExt)
- 

[Me](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEMeExt)
- 

[MFA Client](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEMFAClientExt)
- 

[POSIX Viewer](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEUserAdmExt)
- 

[Reset Password](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEResetPassExt)
- 

[Security Administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPESecAdminExt)
- 

[Self Registration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPESelfRegExt)
- 

[Signin](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPESignInExt)
- 

[User Administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEUserAdmExt-7)
- 

[User Manager](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEUserManagExt)
- 

[Verify Email](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RRPEVerifyEmailExt)

## Application Administrator

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that an application administrator AppRole can access.

Endpoint Allowed Operations
AdaptiveAccessSettings GET/&lt;ID&gt;, GET(Search)
AccountMgmtInfos ALL
AccountObjectClasses ALL
AccountObjectClassTemplates GET/&lt;ID&gt;, GET(Search)
AccountOwnerLinker ALL
AccountPasswordResetter ALL
AccountStatusChanger ALL
AnalyticEvents GET/&lt;ID&gt;, GET(Search)
AppAllowedScopesChanger ALL
AppClientSecretRegenerator ALL
AppEntitlementCollections ALL
AppRoleExportJob GET/&lt;ID&gt;, GET(Search)
AppRoleExportJobHistory GET/&lt;ID&gt;, GET(Search)
AppRoleExportJobProgress ALL
AppRoleExportJobReport GET/&lt;ID&gt;, GET(Search)
AppRoleExportJobSchedule ALL
AppRoleImportJob GET/&lt;ID&gt;, GET(Search)
AppRoleImportJobHistory GET/&lt;ID&gt;, GET(Search)
AppRoleImportJobReport GET/&lt;ID&gt;, GET(Search)
AppRoleImportJobProgress ALL
AppRoleImportJobSchedule ALL
AppRoleMembershipImportDetailedJobReports GET/&lt;ID&gt;, GET(Search)
AppRoleMembershipImportSummaryJobReports ALL
AppRoles ALL
Apps ALL
AppStatusChanger ALL
AppTemplates GET/&lt;ID&gt;, GET(Search)
AppTemplateStatusChanger GET/&lt;ID&gt;, GET(Search)
AppUpgrader ALL
AsyncTargetActions ALL
AuditEvents GET/&lt;ID&gt;, GET(Search)
Bulk ALL
ConditionGroups ALL
Conditions ALL
ConnectorBundles GET/&lt;ID&gt;, GET(Search)
CustomAllowedValues ALL
Files ALL
GrantEvaluationJob GET/&lt;ID&gt;, GET(Search)
GrantEvaluationJobHistory GET/&lt;ID&gt;, GET(Search)
GrantEvaluationJobProgress ALL
GrantEvaluationJobReport GET/&lt;ID&gt;, GET(Search)
GrantEvaluationJobSchedule ALL
GrantImportDetailedJobReports GET/&lt;ID&gt;, GET(Search)
GrantImportSummaryJobReports GET/&lt;ID&gt;, GET(Search)
Grants ALL
Groups GET/&lt;ID&gt;, GET(Search)
IDCSGroups GET/&lt;ID&gt;, GET(Search)
IDCSUsers GET/&lt;ID&gt;, GET(Search)
Images GET/&lt;ID&gt;, GET(Search)
Jobs GET/&lt;ID&gt;, GET(Search)
JobHistories GET/&lt;ID&gt;, GET(Search)
JobProgress GET/&lt;ID&gt;, GET(Search)
JobReports GET/&lt;ID&gt;, GET(Search)
JobSchedules GET/&lt;ID&gt;, GET(Search)
ManagedApp ALL
ManagedAppAttributeMappings ALL
ManagedAppConnectionTester ALL
ManagedAppOperations ALL
ManagedAppOperationTemplates GET/&lt;ID&gt;, GET(Search)
ManagedObjectClasses ALL
ManagedObjectClassTemplates GET/&lt;ID&gt;, GET(Search)
ManagedObjectSyncDetailedJobReports GET/&lt;ID&gt;, GET(Search)
ManagedObjectSyncJob GET/&lt;ID&gt;, GET(Search)
ManagedObjectSyncJobHistory GET/&lt;ID&gt;, GET(Search)
ManagedObjectSyncJobProgress ALL
ManagedObjectSyncJobReports GET/&lt;ID&gt;, GET(Search)
ManagedObjectSyncJobSchedule ALL
MappedActions ALL
MappedActionTemplates GET/&lt;ID&gt;, GET(Search)
MappedAttributes ALL
MappedAttributeTemplates GET/&lt;ID&gt;, GET(Search)
NetworkPerimeters ALL
OAuthClientCertificates ALL
ObjectMgmtInfos ALL
Policies ALL
RefreshAccessStatisticsJob GET/&lt;ID&gt;, GET(Search)
RefreshAccessStatisticsJobHistory GET/&lt;ID&gt;, GET(Search)
RefreshAccessStatisticsJobProgres ALL
RefreshAccessStatisticsJobReport GET/&lt;ID&gt;, GET(Search)
RefreshAccessStatisticsJobSchedule ALL
RefreshAppAccessTokensJob GET/&lt;ID&gt;, GET(Search)
RefreshAppAccessTokensJobHistory GET/&lt;ID&gt;, GET(Search)
RefreshAppAccessTokensJobProgress GET/&lt;ID&gt;, GET(Search)
RefreshAppAccessTokensJobSchedule ALL
Reports POST
RiskProviderProflies GET/&lt;ID&gt;, GET(Search)
RiskScoreHistories GET/&lt;ID&gt;, GET(Search)
Rules ALL
SFFCustomApps ALL
SigningCert/jwk GET/&lt;ID&gt;, GET(Search)
SocialAccounts GET/&lt;ID&gt;, GET(Search)
SyncEvents ALL
Tags GET/&lt;ID&gt;, GET(Search), POST/.search
TargetActionResults ALL
TargetActions ALL
TermsOfUseConsents GET/&lt;ID&gt;, GET(Search)
TermsOfUses ALL
TermsOfUseStatements ALL
UserAppsEnabledForAuthentication GET/&lt;ID&gt;, GET(Search)
UserAppsEnabledForDelegatedAuthentication GET/&lt;ID&gt;, GET(Search)
Users GET/&lt;ID&gt;, GET(Search)
WebTierPolicyJsonValidator ALL

## Audit Administrator

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that an audit administrator AppRole can access.

Endpoint Allowed Operations
AdaptiveAccessSettings GET/&lt;ID&gt;, GET(Search)
AnalyticEvents GET/&lt;ID&gt;, GET(Search)
AuditEvents GET/&lt;ID&gt;, GET(Search)
Files GET/&lt;ID&gt;, GET(Search)
Groups GET/&lt;ID&gt;, GET(Search)
IDBridgeConfig GET/&lt;ID&gt;, GET(Search)
IDCSGroups GET/&lt;ID&gt;, GET(Search)
IDSUsers GET/&lt;ID&gt;, GET(Search)
IdentityAgents GET/&lt;ID&gt;, GET(Search)
IdentitySources GET/&lt;ID&gt;, GET(Search)
IdentitySourceContainers GET/&lt;ID&gt;, GET(Search)
Images GET/&lt;ID&gt;, GET(Search)
MappedIdcsAttributes GET/&lt;ID&gt;, GET(Search)
Reports POST
RiskProviderProfiles GET/&lt;ID&gt;, GET(Search)
RiskScoreHistories GET/&lt;ID&gt;, GET(Search)
SocialAccounts GET/&lt;ID&gt;, GET(Search)
TermsOfUseConsents GET/&lt;ID&gt;, GET(Search)
UnMappedIdcsAttributes GET/&lt;ID&gt;, GET(Search)
UserAppEnabledForAuthentication GET/&lt;ID&gt;, GET(Search)
UserAppsEnabledForDelegatedAuthentication GET/&lt;ID&gt;, GET(Search)
Users GET/&lt;ID&gt;, GET(Search)

## Authenticated Client

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that an Authenticated Client AppRole can access.

Endpoint Allowed Operations
AccountObjectClassTemplates ALL
AdaptiveAccessConfig ALL
AdaptiveAccessSettings GET/&lt;ID&gt;, GET(Search)
AdminSharedFiles GET
AllIdentityProviders GET(Search), POST/.search
AllowedValues ALL
AppAllowedScopesChanger POST
AppClientSecretRegenerator ALL
AppConfig ALL
ApplicablePasswordPolicyRetriever ALL
AppRoles DELETE, GET(Search), POST, POST/.search, GET, PATCH
Apps GET(Search), POST/.search, GET/&lt;ID&gt;, PUT, PATCH
AppStatusChanger PUT
AppTemplates ALL
AppTemplateStatusChanger ALL
AuditEvents GET/&lt;ID&gt;, GET(Search)
AuthenticationFactorSettings GET/&lt;ID&gt;, GET(Search)
BinaryFileInfos DELETE, POST, GET(Search), POST/.search, GET&lt;ID&gt;, PATCH
BrandingSettings GET/&lt;ID&gt;, GET(Search)
Bulk ALL
BulkConfig ALL
CacheFlusher ALL
CacheStats GET/&lt;ID&gt;, GET(Search)
CASettings ALL
CertificateGetter POST
ConditionGroupTemplates ALL
ConditionTemplates ALL
ConnectorBundles ALL
CredentialMaps GET/&lt;ID&gt;, GET(Search)
Credentials GET/&lt;ID&gt;, GET(Search)
DataMigrationJob GET/&lt;ID&gt;, GET(Search)
DataMigrationJobHistory GET/&lt;ID&gt;, GET(Search)
DataMigrationJobProgress ALL
DataMigrationJobReport GET/&lt;ID&gt;, GET(Search)
DataMigrationJobSchedule ALL
DataMigrationWorkerJob GET/&lt;ID&gt;, GET(Search)
DataMigrationWorkerJobHistory GET/&lt;ID&gt;, GET(Search)
DataMigrationWorkerJobProgress ALL
DataMigrationWorkerJobReport GET/&lt;ID&gt;, GET(Search)
DataMigrationWorkerJobSchedule ALL
DefaultSocialIdentityProviders ALL
ExternalIdentityProviders GET(Search), POST/.search
Files GET/&lt;ID&gt;, GET(Search)
GlobalConfig ALL
Grants DELETE, GET(Search), POST, POST/.search, GET
GroupOwnerUpdateJob GET/&lt;ID&gt;, GET(Search)
GroupOwnerUpdateJobHistory GET/&lt;ID&gt;, GET(Search)
GroupOwnerUpdateJobProgress GET/&lt;ID&gt;, GET(Search)
GroupOwnerUpdateJobReport GET/&lt;ID&gt;, GET(Search)
GroupOwnerUpdateJobSchedule GET/&lt;ID&gt;, GET(Search)
Groups GET/&lt;ID&gt;, GET(Search)
IDBridgeConfig ALL
IDSGroups GET/&lt;ID&gt;, GET(Search)
IDSUsers GET/&lt;ID&gt;, GET(Search)
IdentitySourceTemplates ALL
IdentitySettings GET/&lt;ID&gt;, GET(Search)
Images GET/&lt;ID&gt;, GET(Search)
JobConfig ALL
JobHistories GET/&lt;ID&gt;, GET(Search)
JobProgress GET/&lt;ID&gt;, GET(Search)
JobReports GET/&lt;ID&gt;, GET(Search)
Jobs GET/&lt;ID&gt;, GET(Search)
JobSchedules GET/&lt;ID&gt;, GET(Search)
KeyGetter POST
KeyStoreGetter POST
KeyStores GET/&lt;ID&gt;, GET(Search)
KMSConfig ALL
LatestBinaryFileInfoVersionRetriever GET(Search), POST/.search
LicenseConfig ALL
ManagedAppOperationTemplates ALL
ManagedObjectClassTemplates ALL
ManageSigningKeyJob GET/&lt;ID&gt;, GET(Search)
ManageSigningKeyJobHistory GET/&lt;ID&gt;, GET(Search)
ManageSigningKeyJobProgress ALL
ManageSigningKeyJobReport GET/&lt;ID&gt;, GET(Search)
ManageSigningKeyJobSchedule ALL
MappedActionTemplates ALL
MappedAttributeTemplates ALL
Me GET/&lt;ID&gt;, GET(Search) for MeteringJobJobHistory, MeteringJob, MeteringJobJobReport

ALL for MeteringJobJobSchedule, MeteringJobJobProgress
MeEmailVerifier ALL
MePasswordChanger ALL
MessagingConfig ALL
MyAccesses ALL
MyAppFavoriteSetter ALL
MyApps ALL
MyAuthenticationFactorEnroller. POST
MyAuthenticationFactorInitiator POST
MyAuthenticationFactorsRemover POST
MyAuthenticationFactorValidator POST
MyBypassCodes DELETE, POST, GET(Search), POST/.search, GET
MyBypassCodeNotifications POST
MyDevices DELETE, GET(Search), GET, PATCH
MyGroups GET(Search), POST/.search
MyRequestableApps GET(Search), POST/.search
MyRequestableGroups GET(Search), POST/.search
MyRequests POST, GET(Search), POST/.search
MySFFCredentials ALL
MySocialAccounts ALL
MyTermsOfUseConsents DELETE, GET(Search), POST/.search, GET
MyTrustedUserAgents DELETE, GET(Search), GET
NotificationConfig ALL
OAuthConfig ALL
OAuthConsents DELETE, GET(Search), GET
PasswordPolicies GET/&lt;ID&gt;, GET(Search)
PolicyTemplates ALL
PolicyTypes ALL
POSIXSetupJob GET/&lt;ID&gt;, GET(Search)
POSIXSetupJobHistory GET/&lt;ID&gt;, GET(Search)
POSIXSetupJobProgress ALL
POSIXSetupJobReport GET/&lt;ID&gt;, GET(Search)
POSIXSetupJobSchedule ALL
PurgeResourcesJob GET/&lt;ID&gt;, GET(Search)
PurgeResourcesJobHistory GET/&lt;ID&gt;, GET(Search)
PurgeResourcesJobProgress ALL
PurgeResourcesJobReport GET/&lt;ID&gt;, GET(Search)
PurgeResourcesJobSchedule ALL
Reports POST
ResourceTypes ALL
ResourceTypeSchemaAttributes ALL
RuleTemplates ALL
SamlRuntimeData ALL
Schemas ALL
SecurityQuestions GET/&lt;ID&gt;, GET(Search)
SecurityQuestionSettings GET/&lt;ID&gt;, GET(Search)
SeededAuthorizationPolicies ALL
ServiceProviderConfig ALL
SffXtnUrl GET/&lt;ID&gt;, GET(Search)
SigningCert/jwk GET/&lt;ID&gt;, GET(Search)
SignJWT POST
SMRequests GET/&lt;ID&gt;, GET(Search)
SocialAccounts GET/&lt;ID&gt;, GET(Search)
SocialIdentityProviderMetadata ALL
SsoConfig ALL
SsoEncryptionKey GET/&lt;ID&gt;, GET(Search) for SsoEncryptionKeyRollOverJobReport, SsoEncryptionKeyRollOverJob, SsoEncryptionKeyRollOverJobHistory

ALL for SsoEncryptionKeyRollOverJobSchedule, SsoEncryptionKeyRollOverJobProgress,
StorageConfig ALL
Tags GET(Search), POST/.search, GET/&lt;ID&gt;
Tenants GET/&lt;ID&gt;, GET(Search)
TermsOfUseConsents GET/&lt;ID&gt;, GET(Search)
UpdateFromEmailDomainValidationStatusJob GET/&lt;ID&gt;, GET(Search)
UpdateFromEmailDomainValidationStatusJobHistory GET/&lt;ID&gt;, GET(Search)
UpdateFromEmailDomainValidationStatusJobProgress ALL
UpdateFromEmailDomainValidationStatusJobReport GET/&lt;ID&gt;, GET(Search)
UpdateFromEmailDomainValidationStatusJobSchedule ALL
UpdateQuotaResourcesJob GET/&lt;ID&gt;, GET(Search)
UpdateQuotaResourcesJobHistory GET/&lt;ID&gt;, GET(Search)
UpdateQuotaResourcesJobProgress ALL
UpdateQuotaResourcesJobReport GET/&lt;ID&gt;, GET(Search)
UpdateQuotaResourcesJobSchedule ALL
UpdateTenantSigningKeyChainJob GET/&lt;ID&gt;, GET(Search)
UpdateTenantSigningKeyChainJobHistory GET/&lt;ID&gt;, GET(Search)
UpdateTenantSigningKeyChainJobProgress ALL
UpdateTenantSigningKeyChainJobReport GET/&lt;ID&gt;, GET(Search)
UpdateTenantSigningKeyChainJobSchedule ALL
UserAppsEnabledForAuthentication GET/&lt;ID&gt;, GET(Search)
UserAppsEnabledForDelegatedAuthentication GET/&lt;ID&gt;, GET(Search)
UserPasswordValidator PUT
UserSharedFiles GET
UserTokens ALL
VerifyCredentials POST
VerifyJWT POST

## Authenticator Client

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that an Authenticator Client AppRole can access.

Endpoint Allowed Operations
Asserter ALL
HTTPAuthenticator ALL
PasswordAuthenticator ALL
/mfa/v1/requests POST, GET, PATCH
/mfa/v1/users GET

## Change Password

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Change Password AppRole can access.

Endpoint Allowed Operations
AccountRecoverySettings ALL
AllowedValues GET/&lt;ID&gt;, GET(Search)
ApplicablePasswordPolicyRetriever ALL
Authenticate ALL
AuthenticationFactorSettings GET/&lt;ID&gt;, GET(Search)
BrandingSettings GET/&lt;ID&gt;, GET(Search)
MePasswordMustChanger ALL
PasswordPolicies GET/&lt;ID&gt;, GET(Search)
SecurityQuestionSettings GET/&lt;ID&gt;, GET(Search)
TermsOfUseStatements GET/&lt;ID&gt;, GET(Search)
UserPasswordValidator ALL

## Cloud Gate

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Cloud Gate AppRole can access.

Endpoint Allowed Operations
AccountRecoverySettings ALL
AdaptiveAccessSettings GET/&lt;ID&gt;, GET(Search)
AdaptiveEvents GET/&lt;ID&gt;, GET(Search)
ApplicablePasswordPolicyRetriever ALL
Apps GET/&lt;ID&gt;, GET(Search)
Asserter ALL
AuthenticationFactorSettings GET/&lt;ID&gt;, GET(Search)
BrandingSettings GET/&lt;ID&gt;, GET(Search)
DiagnosticRecords POST, PUT, PATCH
EncryptionKeys ALL
EmailTemplates GET/&lt;ID&gt;, GET(Search)
Files GET/&lt;ID&gt;, GET(Search)
HTTPAuthenticator ALL
IDBridgeSettings GET/&lt;ID&gt;, GET(Search)
IDSUsers GET/&lt;ID&gt;, GET(Search)
IdentitySettings GET/&lt;ID&gt;, GET(Search)
Images GET/&lt;ID&gt;, GET(Search)
IncidentDetails GET/&lt;ID&gt;, GET(Search)
Notifications GET/&lt;ID&gt;, GET(Search)
NotificationSettings GET/&lt;ID&gt;, GET(Search)
PasswordAuthenticator ALL
PasswordPolicies GET/&lt;ID&gt;, GET(Search)
RiskProviderProfiles GET/&lt;ID&gt;, GET(Search)
RiskScoreHistories GET/&lt;ID&gt;, GET(Search)
Rules GET/&lt;ID&gt;, GET(Search)
SamlSettings GET/&lt;ID&gt;, GET(Search)
SecurityQuestionSettings GET/&lt;ID&gt;, GET(Search)
Settings GET/&lt;ID&gt;, GET(Search)
SMSTemplates GET/&lt;ID&gt;, GET(Search)
SocialAccounts GET/&lt;ID&gt;, GET(Search)
SsoSettings GET/&lt;ID&gt;, GET(Search)
TermsOfUseConsents GET/&lt;ID&gt;, GET(Search)
Threats GET/&lt;ID&gt;, GET(Search)
UserAgentLocations GET/&lt;ID&gt;, GET(Search)
UserAuditEventsPurger GET/&lt;ID&gt;, GET(Search)
UserDevices GET/&lt;ID&gt;, GET(Search)
UserAppsEnabledForAuthentication GET/&lt;ID&gt;, GET(Search)
UserAppsEnabledForDelegatedAuthentication GET/&lt;ID&gt;, GET(Search)
Users GET/&lt;ID&gt;, GET(Search)

## DB Admin

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a DB Admin AppRole can access.

Endpoint Allowed Operations
DBGroups GET(Search), POST/.search, GET&lt;ID&gt;
DBUserAuthenticationStatus PATCH
DBUsers GET(Search), POST/.search, GET&lt;ID&gt;

## Forgot Password

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Forgot Password AppRole can access.

Endpoint Allowed Operations
BrandingSettings GET(Search), GET&lt;ID&gt;
MePasswordRecoveryFactorValidator ALL
MePasswordRecoveryOptionRetriever ALL
MePasswordResetRequestor ALL
MeSecurityQuestionsRetriever ALL

## Help Desk Administrator

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a help desk administrator AppRole can access.

Endpoint Allowed Operations
Apps GET/&lt;ID&gt;
AnalyticEvents GET/&lt;ID&gt;
AuditEvents GET/&lt;ID&gt;
AuthenticationFactorsRemover POST
Bulk ALL
BulkUserPasswordChanger ALL
BulkUserPasswordResetter ALL
BypassCodeNotifications POST
BypassCodes POST
IDSGroups GET/&lt;ID&gt;
IDSUser GET/&lt;ID&gt;
Images ALL
Groups GET/&lt;ID&gt;
Requests GET(Search), POST
UserActivationInitiator ALL
UserAppsEnabledForAuthentication GET/&lt;ID&gt;
UserLockedStateChanger ALL
UserPasswordChanger ALL
UserPasswordGenerator ALL
UserPasswordResetter ALL
UserPasswordValidator ALL
Users GET/&lt;ID&gt;
UserStateChanger ALL

## Identity Domain Administrator

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that an identity domain administrator AppRole can access.

Endpoint Allowed Operations
AdminSharedFiles GET
AccountMgmtInfos ALL
AccountObjectClasses ALL
AccountObjectClassTemplates GET(Search), GET&lt;ID&gt;
AccountOwnerLinker ALL
AccountPasswordResetter ALL
AccountRecoverySettings ALL
AccountStatusChanger ALL
AdaptiveAccessSettings ALL
AdaptiveEvents ALL
AllIdentityProviders GET(Search), POST/.search
AllowedValues GET(Search), GET&lt;ID&gt;
AnalyticEvents GET(Search), GET&lt;ID&gt;
AppAllowedScopesChanger ALL
AppClientSecretRegenerator ALL
AppEntitlementCollections ALL
AppKerberosRealmUpdater ALL
ApplicablePasswordPolicyRetriever ALL
AppRoleExportJob GET(Search), GET&lt;ID&gt;
AppRoleExportJobHistory GET(Search), GET&lt;ID&gt;
AppRoleExportJobProgress ALL
AppRoleExportJobReport GET(Search), GET&lt;ID&gt;
AppRoleExportJobSchedule ALL
AppRoleImportJob GET(Search), GET&lt;ID&gt;
AppRoleImportJobHistory GET(Search), GET&lt;ID&gt;
AppRoleImportJobProgressv ALL
AppRoleImportJobReport GET(Search), GET&lt;ID&gt;
AppRoleImportJobSchedule ALL
AppRoleMembershipImportDetailedJobReports GET(Search), GET&lt;ID&gt;
AppRoleMembershipImportSummaryJobReports GET(Search), GET&lt;ID&gt;
AppRoles ALL
Apps ALL
AppStatusChanger ALL
AppTemplates GET(Search), GET&lt;ID&gt;
AppTemplateStatusChanger GET(Search), GET&lt;ID&gt;
AppUpgrader ALL
Asserter ALL
AsyncTargetActions ALL
AuditEvents GET(Search), GET&lt;ID&gt;
AuthenticationFactorEnroller POST
AuthenticationFactorEnrollmentRequest POST
AuthenticationFactorInitiator POST
AuthenticationFactorSettings ALL
AuthenticationFactorsRemover POST
AuthenticationFactorValidator POST
BinaryFileInfos GET(Search), GET&lt;ID&gt;
BrandingSettings GET(Search), GET&lt;ID&gt;
Bulk ALL for BulkUserPasswordResetJobProgress, BulkUserPasswordMustChangeSetJobProgress, BulkUserPasswordResetJobSchedule, BulkUserPasswordMustChangeSetJobSchedule

GET(Search), GET&lt;ID&gt; for BulkUserPasswordResetJobHistory, BulkUserPasswordMustChangeSetJobReport, BulkUserPasswordMustChangeSetJobHistory, BulkUserPasswordResetJob, BulkUserPasswordMustChangeSetJob
BulkSourceEvents ALL
BulkUserPasswordChanger ALL
BulkUserPasswordResetJobReports GET(Search), GET&lt;ID&gt;
BulkUserPasswordResetter ALL
BypassCodeNotifications POST
BypassCodes ALL
ConnectorBundles GET(Search), GET&lt;ID&gt;
CustomAllowedValues ALL
ConditionGroups ALL
Conditions ALL
DBGroups GET(Search), POST/.search, GET&lt;ID&gt;
DBUserAuthenticationStatus PATCH
DBUsers GET(Search), POST/.search, GET&lt;ID&gt;
Devices ALL
DiagnosticRecords GET(Search), GET&lt;ID&gt;
EmailTemplates ALL
ExportJob GET(Search), GET&lt;ID&gt;
ExportJobHistory GET(Search), GET&lt;ID&gt;
ExportJobProgress ALL
ExportJobReport GET(Search), GET&lt;ID&gt;
ExportJobSchedule ALL
ExternalIdentityProviders GET(Search), POST/.search
Files ALL
GrantEvaluationJob GET(Search), GET&lt;ID&gt;
GrantEvaluationJobHistory GET(Search), GET&lt;ID&gt;
GrantEvaluationJobProgress ALL
GrantEvaluationJobReport GET(Search), GET&lt;ID&gt;
GrantEvaluationJobSchedule ALL
GrantImportDetailedJobReports GET(Search), GET&lt;ID&gt;
GrantImportSummaryJobReports GET(Search), GET&lt;ID&gt;
Grants ALL
GroupExportJob GET(Search), GET&lt;ID&gt;
GroupExportJobHistory GET(Search), GET&lt;ID&gt;
GroupExportJobProgress ALL
GroupExportJobReport GET(Search), GET&lt;ID&gt;
GroupExportJobSchedule ALL
GroupImportDetailedJobReports GET(Search), GET&lt;ID&gt;
GroupImportJob GET(Search), GET&lt;ID&gt;
GroupImportJobHistory GET(Search), GET&lt;ID&gt;
GroupImportJobProgress ALL
GroupImportJobReport GET(Search), GET&lt;ID&gt;
GroupImportJobSchedule ALL
GroupImportSummaryJobReports GET(Search), GET&lt;ID&gt;
Groups ALL
HTTPAuthenticator ALL
IdBridgeAppRegistrar ALL
IDBridgeConfig GET(Search), GET&lt;ID&gt;
IDBridgeSettings ALL
IDSGroups ALL
IDSUsers ALL
IdentityAgents ALL
IdentityProviders ALL
IdentitySettings ALL
IdentitySourceContainers ALL
IdentitySources ALL
IdentitySourceTemplates GET(Search), GET&lt;ID&gt;
Images ALL
ImportJob GET(Search), GET&lt;ID&gt;
ImportJobHistory GET(Search), GET&lt;ID&gt;
ImportJobProgress ALL
ImportJobReport GET(Search), GET&lt;ID&gt;
ImportJobSchedule ALL
IncidentDetails GET(Search), GET&lt;ID&gt;
Jobs GET(Search), GET&lt;ID&gt;
JobHistories GET(Search), GET&lt;ID&gt;
JobProgress GET(Search), GET&lt;ID&gt;
JobReports GET(Search), GET&lt;ID&gt;
JobSchedules GET(Search), GET&lt;ID&gt;
KerberosRealmUsers ALL
LatestBinaryFileInfoVersionRetriever GET(Search), GET&lt;ID&gt;
ManagedApp ALL
ManagedAppAttributeMappings ALL
ManagedAppConnectionTester ALL
ManagedAppOperations ALL
ManagedAppOperationTemplates GET(Search), GET&lt;ID&gt;
ManagedObjectClassTemplates GET(Search), GET&lt;ID&gt;
ManagedObjectSyncDetailedJobReports GET(Search), GET&lt;ID&gt;
ManagedObjectSyncJob GET(Search), GET&lt;ID&gt;
ManagedObjectSyncJobHistory GET(Search), GET&lt;ID&gt;
ManagedObjectSyncJobProgress ALL
ManagedObjectSyncJobReports GET(Search), GET&lt;ID&gt;
ManagedObjectSyncJobSchedule ALL
MappedActions ALL
MappedActionTemplates GET(Search), GET&lt;ID&gt;
MappedAttributes ALL
MappedAttributeTemplates GET(Search), GET&lt;ID&gt;
MappedIdcsAttributes ALL
Me GET, PATCH, PUT
MeEmailVerified ALL
MeEmailVerifier ALL
MePasswordMustChanger ALL
MePasswordRecoveryFactorValidator ALL
MePasswordRecoveryOptionRetriever ALL
MePasswordResetChanger ALL
MePasswordResetRequestor ALL
MePasswordResetter ALL
MeRemovePendingEmailVerification POST
MeSecurityQuestionAnswerValidator ALL
MeSecurityQuestionsRetriever ALL
MyAppFavoriteSetter ALL
MyApps ALL
MyAccesses ALL
MyAuthenticationFactorEnroller POST
MyAuthenticationFactorInitiator POST
MyAuthenticationFactorsRemover POST
MyAuthenticationFactorValidator POST
MyBypassCodeNotifications POST
MyBypassCodes DELETE, POST, GET(Search), POST/.search, GET&lt;ID&gt;
MyDevices DELETE, GET(Search), GET&lt;ID&gt;, PATCH
MyGroups GET(Search), POST/.search
MePasswordChanger ALL
MyRequestableApps GET(Search), POST/.search
MyRequestableGroups GET(Search), POST/.search
MyRequests POST, GET(Search), POST/.search
MySFFCredentials ALL
MySocialAccountLinker POST
MySocialAccounts ALL
MyTermsOfUseConsents DELETE, GET(Search), POST/.search, GET&lt;ID&gt;
MyTrustedUserAgents DELETE, GET(Search), GET&lt;ID&gt;
Notifications ALL
NotificationSettings ALL
OAuthClientCertificates ALL
OAuthPartnerCertificates ALL
ObjectMgmtInfos ALL
PasswordAuthenticator ALL
NetworkPerimeters ALL
PasswordPolicies ALL
Policies ALL
PushNotificationRequesters ALL
RefreshAccessStatisticsJob GET(Search), GET&lt;ID&gt;
RefreshAccessStatisticsJobHistory GET(Search), GET&lt;ID&gt;
RefreshAccessStatisticsJobProgress ALL
RefreshAccessStatisticsJobReport GET(Search), GET&lt;ID&gt;
RefreshAccessStatisticsJobSchedule ALL
RefreshAppAccessTokensJob GET(Search), GET&lt;ID&gt;
RefreshAppAccessTokensJobHistory GET(Search), GET&lt;ID&gt;
RefreshAppAccessTokensJobProgress GET(Search), GET&lt;ID&gt;
RefreshAppAccessTokensJobSchedule ALL
Reports POST
Requests GET(Search), POST/.search
ResourceExporter POST
ResourceImporter POST
RiskLevelUpdateJob GET(Search), GET&lt;ID&gt;
RiskLevelUpdateJobHistory GET(Search), GET&lt;ID&gt;
RiskLevelUpdateJobProgress ALL
RiskLevelUpdateJobReport GET(Search), GET&lt;ID&gt;
RiskLevelUpdateJobSchedule ALL
RiskProviderProfiles ALL
RiskProviderProfileValidation ALL
RiskScoreCleanupJob GET(Search), GET&lt;ID&gt;
RiskScoreCleanupJobHistory GET(Search), GET&lt;ID&gt;
RiskScoreCleanupJobProgress ALL
RiskScoreCleanupJobReport GET(Search), GET&lt;ID&gt;
RiskScoreCleanupJobSchedule ALL
RiskScoreHistories ALL
RiskScoreProviderJob GET(Search), GET&lt;ID&gt;
RiskScoreProviderJobHistory GET(Search), GET&lt;ID&gt;
RiskScoreProviderJobProgress ALL
RiskScoreProviderJobReport GET(Search), GET&lt;ID&gt;
RiskScoreProviderJobSchedule ALL
RiskScoreTemporalDecayJob GET(Search), GET&lt;ID&gt;
RiskScoreTemporalDecayJobHistory GET(Search), GET&lt;ID&gt;
RiskScoreTemporalDecayJobProgress ALL
RiskScoreTemporalDecayJobReport GET(Search), GET&lt;ID&gt;
RiskScoreTemporalDecayJobSchedule ALL
Rules ALL
SafeDeleteSocialIdentityProviderJob GET(Search), GET&lt;ID&gt;
SafeDeleteSocialIdentityProviderJobHistory GET(Search), GET&lt;ID&gt;
SafeDeleteSocialIdentityProviderJobProgress GET(Search), GET&lt;ID&gt;
SafeDeleteSocialIdentityProviderJobSchedule ALL
SafeDeleteSocialIdentityProviderJobReport GET(Search), GET&lt;ID&gt;
SamlSettings ALL
Schemas GET(Search), POST/.search, GET&lt;ID&gt;, PUT, PATCH
SecurityQuestions ALL
SecurityQuestionSettings ALL
SelfRegistrationProfiles ALL
Settings ALL
SFFCustomApps ALL
SffXtnUrl GET(Search), GET&lt;ID&gt;
SigningCert/jwk GET(Search), GET&lt;ID&gt;
SMSTemplates ALL
SocialAccounts ALL
SocialIdentityProviders ALL
SourceEvents ALL
SsoSettings ALL
SyncEvents ALL
Tags GET(Search), POST/.search, GET&lt;ID&gt;
TargetActionResults ALL
TargetActions ALL
TargetAuthenticationTester POST
TermsOfUseConsents ALL
TermsOfUses ALL
TermsOfUseStatements ALL
Threats ALL
TrustedUserAgents ALL
UnMappedIdcsAttributes GET(Search), POST/.search, GET&lt;ID&gt;, PATCH
UserActivationInitiator ALL
UserAgentLocations ALL
UserAttributesSettings GET(Search), POST, POST/.search, GET&lt;ID&gt;, PATCH
UserAuditEventsPurger ALL
UserAppsEnabledForAuthentication GET(Search), GET&lt;ID&gt;
UserAppsEnabledForDelegatedAuthentication GET(Search), GET&lt;ID&gt;
UserDevices ALL
UserExportJob GET(Search), GET&lt;ID&gt;
UserExportJobHistory GET(Search), GET&lt;ID&gt;
UserExportJobReport GET(Search), GET&lt;ID&gt;
UserExportJobSchedule ALL
UserImportJob GET(Search), GET&lt;ID&gt;
UserImportJobHistory GET(Search), GET&lt;ID&gt;
UserImportJobProgress ALL
UserImportJobReport GET(Search), GET&lt;ID&gt;
UserImportJobSchedule ALL
UserLockedStateChanger POST
UserNameGenerator ALL
UserPasswordChanger ALL
UserPasswordGenerator ALL
UserPasswordResetter ALL
UserPasswordValidator ALL
UserSharedFiles GET
UserStateChanger ALL
UserTokens ALL
UserTokenValidator ALL
Users ALL
UserStatusChanger PUT
WebTierPolicyJsonValidator ALL

## Kerberos

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Kerberos AppRole can access.

Endpoint Allowed Operations
AppKerberosRealmUpdater ALL
Groups GET/&lt;ID&gt;, GET(Search)
KerberosRealmUsers GET(Search), POST/.search, GET/&lt;ID&gt;, PATCH, PUT
PasswordAuthenticator ALL
PasswordPolicies GET/&lt;ID&gt;, GET(Search)
Users GET/&lt;ID&gt;, GET(Search)

## Me

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Me AppRole can access.

Endpoint Allowed Operations
AccountRecoverySettings ALL
AllIdentityProviders GET(Search), POST/.search
AllowedValues GET(Search), GET/&lt;ID&gt;
ApplicablePasswordPolicyRetriever ALL
AuthenticationFactorEnrollmentRequest POST
AuthenticationFactorSettings GET(Search), GET/&lt;ID&gt;
BrandingSettings GET(Search), GET/&lt;ID&gt;
ExternalIdentityProviders GET(Search), POST/.search
IdentitySettings GET(Search), GET/&lt;ID&gt;
Me ALL
MeEmailVerifier ALL
MePasswordChanger ALL
MeRemovePendingEmailVerification POST
MyAccesses ALL
MyAppFavoriteSetter ALL
MyApps ALL
MyAuthenticationFactorEnroller POST
MyAuthenticationFactorInitiator POST
MyAuthenticationFactorsRemover POST
MyAuthenticationFactorValidator POST
MyBypassCodeNotifications POST
MyBypassCodes DELETE, POST, GET(Search), POST/.search, GET/&lt;ID&gt;
MyDevices DELETE, GET(Search), GET/&lt;ID&gt;, PATCH
MyGroups GET(Search), POST/.search
MyRequestableApps GET(Search), POST/.search
MyRequestableGroups GET(Search), POST/.search
MyRequests POST, GET(Search), POST/.search
MySFFCredentials ALL
MySocialAccountLinker POST
MySocialAccounts ALL
MyTermsOfUseConsents DELETE, GET(Search), POST/.search, GET/&lt;ID&gt;
MyTrustedUserAgents DELETE, GET(Search), GET/&lt;ID&gt;
OAuthConsents DELETE, GET(Search), GET/&lt;ID&gt;
PasswordPolicies GET/&lt;ID&gt;, GET(Search)
SecurityQuestions GET/&lt;ID&gt;, GET(Search)
SecurityQuestionSettings GET/&lt;ID&gt;, GET(Search)
SffXtnUrl GET/&lt;ID&gt;, GET(Search)
SupportedSocialIdentityProviders GET
UserPasswordValidator PUT
UserSharedFiles GET/&lt;ID&gt;

## MFA Client

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that an MFA Client AppRole can access.

Endpoint Allowed Operations
Asserter ALL
HTTPAuthenticator ALL
PasswordAuthenticator ALL
/mfa/v1/requests POST, GET, PATCH
/mfa/v1/users DELETE, POST, GET, PATCH

## POSIX Viewer

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The POSIX Viewer role is intended to be granted to confidential applications for configuring the Linux-PAM. The role was meant for creating OAUTH Clients with lower privileges, that are supposed to be used for PAM. This role isn't meant for assigning to any users or groups. For more information see,[Configuring a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../linuxpam/configure-confidential-application.htm).

## Reset Password

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Reset Password AppRole can access.

Endpoint Allowed Operations
ApplicablePasswordPolicyRetriever ALL
BrandingSettings GET(Search), GET/&lt;ID&gt;
MePasswordRecoveryFactorValidator ALL
MePasswordResettert ALL
MeSecurityQuestionAnswerValidator ALL
PasswordPolicies GET(Search), GET/&lt;ID&gt;
UserPasswordValidator ALL
UserTokenValidator ALL

## Security Administrator

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a security administrator AppRole can access.

Endpoint Allowed Operations
AdminSharedFiles GET/&lt;ID&gt;
AccountObjectClassTemplates GET(Search), GET/&lt;ID&gt;
AccountRecoverySettings ALL
AdaptiveAccessSettings ALL
AdaptiveEvents ALL
AllIdentityProviders ALL
AnalyticEvents GET(Search), GET/&lt;ID&gt;
AppClientSecretRegenerator ALL
ApplicablePasswordPolicyRetriever ALL
Apps ALL
AppTemplates GET(Search), GET/&lt;ID&gt;
AppTemplateStatusChanger GET(Search), GET/&lt;ID&gt;
AuditEvents GET(Search), GET/&lt;ID&gt;
AuthenticationFactorEnroller GET(Search), GET/&lt;ID&gt;
AuthenticationFactorEnrollmentRequest GET(Search), GET/&lt;ID&gt;
AuthenticationFactorSettings ALL
AuthenticationFactorInitiator GET(Search), GET/&lt;ID&gt;
AuthenticationFactorsRemover GET(Search), GET/&lt;ID&gt;
AuthenticationFactorValidator GET(Search), GET/&lt;ID&gt;
BinaryFileInfos GET(Search), GET/&lt;ID&gt;
BrandingSettings ALL
Bulk ALL
BulkReports POST
BypassCodes GET(Search), GET/&lt;ID&gt;
Columns GET(Search), GET/&lt;ID&gt;
ConditionGroups ALL
Conditions ALL
ConnectorBundles GET(Search), GET/&lt;ID&gt;
Devices GET(Search), GET/&lt;ID&gt;
EmailTemplates ALL
ExternalIdentityProviders ALL
Files GET(Search), GET/&lt;ID&gt;
Groups GET(Search), GET/&lt;ID&gt;
IdBridgeAppRegistrar ALL
IDBridgeConfig GET(Search), GET/&lt;ID&gt;
IDBridgeSettings ALL
IdentitySettings ALL
IdentityAgents ALL
IdentityProviders ALL
IdentitySourceContainers ALL
IdentitySources ALL
IDSGroups GET(Search), GET/&lt;ID&gt;
IdcsReports POST
IDSUsers GET(Search), GET/&lt;ID&gt;
Images ALL
IncidentDetails GET(Search), GET/&lt;ID&gt;
LatestBinaryFileInfoVersionRetriever GET(Search), GET/&lt;ID&gt;
MappedActionTemplates GET(Search), GET/&lt;ID&gt;
MappedAttributeTemplates GET(Search), GET/&lt;ID&gt;
MappedIdcsAttributes ALL
ManagedAppOperationTemplates GET(Search), GET/&lt;ID&gt;
ManagedObjectClassTemplates GET(Search), GET/&lt;ID&gt;
NetworkPerimeters ALL
Notifications ALL
NotificationSettings ALL
OAuthClientCertificates ALL
OAuthPartnerCertificates ALL
PasswordPolicies ALL
Policies ALL
PushNotificationRequesters ALL
Reports POST
ReportTemplates GET(Search), GET/&lt;ID&gt;
RiskProviderProfiles ALL
RiskProviderProfileValidation ALL
RiskScoreHistories ALL
Rules ALL
SamlSettings ALL
SecurityQuestionSettings ALL
Settings ALL
SFFCustomApps ALL
SigningCert/jwk GET(Search), GET/&lt;ID&gt;
SMSTemplates ALL
SocialAccounts GET(Search), GET/&lt;ID&gt;
SocialIdentityProviders ALL
SsoSettings ALL
SupportedSocialIdentityProviders GET
TargetAuthenticationTester POST
TermsOfUseConsents GET(Search), GET/&lt;ID&gt;
TermsOfUses ALL
TermsOfUseStatements ALL
Threats ALL
TrustedUserAgents GET(Search), GET/&lt;ID&gt;
UnMappedIdcsAttributes GET(Search), GET/&lt;ID&gt;
UserAgentLocations ALL
UserAppsEnabledForAuthentication GET(Search), GET/&lt;ID&gt;
UserAppsEnabledForDelegatedAuthentication GET(Search), GET/&lt;ID&gt;
UserAuditEventsPurger ALL
UserDevices ALL
Users GET(Search), GET/&lt;ID&gt;

## Self Registration

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Self Registration AppRole can access.

Endpoint Allowed Operations
BrandingSettings GET/&lt;ID&gt;
Me POST
SelfRegistrationProfiles GET/&lt;ID&gt;
UserNameGenerator POST

## Signin

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Signin AppRole can access.

Endpoint Allowed Operations
AccountRecoverySettings ALL
AllowedValues GET(Search), GET/&lt;ID&gt;
Authenticate ALL
AuthenticationFactorSettings GET(Search), GET/&lt;ID&gt;
BrandingSettings GET(Search), GET/&lt;ID&gt;
SecurityQuestions GET(Search), GET/&lt;ID&gt;
SecurityQuestionSettings GET(Search), GET/&lt;ID&gt;
TermsOfUseStatements GET(Search), GET/&lt;ID&gt;

## User Administrator

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a user administrator AppRole can access.

Endpoint Allowed Operations
AccountMgmtInfos ALL
AdaptiveAccessSettings GET(Search), GET/&lt;ID&gt;
AnalyticEvents GET(Search), GET/&lt;ID&gt;
AppRoles GET(Search), GET/&lt;ID&gt;
Apps GET(Search), GET/&lt;ID&gt;
AppStatusChanger GET(Search), GET/&lt;ID&gt;
AuthenticationFactorsRemover POST
AuditEvents GET(Search), GET/&lt;ID&gt;
Bulk ALL
BulkReports POST
BulkUserPasswordChanger ALL
BulkUserPasswordMustChangeSetJob GET(Search), GET/&lt;ID&gt;
BulkUserPasswordMustChangeSetJobHistory GET(Search), GET/&lt;ID&gt;
BulkUserPasswordMustChangeSetJobProgress ALL
BulkUserPasswordMustChangeSetJobReport GET(Search), GET/&lt;ID&gt;
BulkUserPasswordMustChangeSetJobSchedule ALL
BulkUserPasswordResetJob GET(Search), GET/&lt;ID&gt;
BulkUserPasswordResetJobHistory GET(Search), GET/&lt;ID&gt;
BulkUserPasswordResetJobProgress ALL
BulkUserPasswordResetJobReports GET(Search), GET/&lt;ID&gt;
BulkUserPasswordResetJobSchedule ALL
BulkUserPasswordResetter ALL
BypassCodeNotifications POST
BypassCodes POST
Columns GET(Search), GET/&lt;ID&gt;
CustomAllowedValues ALL
Files ALL
Grants ALL
GroupExportJob GET(Search), GET/&lt;ID&gt;
GroupExportJobHistory GET(Search), GET/&lt;ID&gt;
GroupExportJobProgress ALL
GroupExportJobReport GET(Search), GET/&lt;ID&gt;
GroupExportJobSchedule ALL
GroupImportJob GET(Search), GET/&lt;ID&gt;
GroupImportJobHistory GET(Search), GET/&lt;ID&gt;
GroupImportJobProgress ALL
GroupImportJobReport GET(Search), GET/&lt;ID&gt;
GroupImportJobSchedule ALL
GroupImportDetailedJobReports GET(Search), GET/&lt;ID&gt;
GroupImportSummaryJobReports GET(Search), GET/&lt;ID&gt;
Groups ALL
IDBridgeConfig GET(Search), GET/&lt;ID&gt;
IdcsReports POST
IdentityAgents GET(Search), GET/&lt;ID&gt;
IdentitySourceContainers GET(Search), GET/&lt;ID&gt;
IdentitySources GET(Search), GET/&lt;ID&gt;
IDSGroups ALL
IDSUsers ALL
Images ALL
Jobs GET(Search), GET/&lt;ID&gt;
JobHistories GET(Search), GET/&lt;ID&gt;
JobReports GET(Search), GET/&lt;ID&gt;
JobProgress GET(Search), GET/&lt;ID&gt;
JobSchedules GET(Search), GET/&lt;ID&gt;
ManagedApp ALL
MappedIdcsAttributes GET(Search), GET/&lt;ID&gt;
MeEmailVerified ALL
MePasswordMustChanger ALL
MePasswordRecoveryFactorValidator ALL
MePasswordRecoveryOptionRetriever ALL
MePasswordResetChanger ALL
MePasswordResetRequestor ALL
MePasswordResetter ALL
MeSecurityQuestionAnswerValidator ALL
MeSecurityQuestionsRetriever ALL
OAuthClientCertificates GET(Search), GET/&lt;ID&gt;
ObjectMgmtInfos ALL
ReportTemplates GET(Search), GET/&lt;ID&gt;
RiskLevelUpdateJob GET(Search), GET/&lt;ID&gt;
RiskLevelUpdateJobHistory GET(Search), GET/&lt;ID&gt;
RiskLevelUpdateJobProgress ALL
RiskLevelUpdateJobReport GET(Search), GET/&lt;ID&gt;
RiskLevelUpdateJobSchedule ALL
RiskProviderProfiles GET(Search), GET/&lt;ID&gt;
RiskScoreCleanupJob GET(Search), GET/&lt;ID&gt;
RiskScoreCleanupJobHistory GET(Search), GET/&lt;ID&gt;
RiskScoreCleanupJobProgress ALL
RiskScoreCleanupJobReport GET(Search), GET/&lt;ID&gt;
RiskScoreCleanupJobSchedule ALL
RiskScoreHistories GET(Search), GET/&lt;ID&gt;
RiskScoreProviderJob GET(Search), GET/&lt;ID&gt;
RiskScoreProviderJobHistory GET(Search), GET/&lt;ID&gt;
RiskScoreProviderJobProgress ALL
RiskScoreProviderJobReport GET(Search), GET/&lt;ID&gt;
RiskScoreProviderJobSchedule ALL
RiskScoreTemporalDecayJob GET(Search), GET/&lt;ID&gt;
RiskScoreTemporalDecayJobHistory GET(Search), GET/&lt;ID&gt;
RiskScoreTemporalDecayJobProgress ALL
RiskScoreTemporalDecayJobReport GET(Search), GET/&lt;ID&gt;
RiskScoreTemporalDecayJobSchedule ALL
Reports POST
Requests GET(Search),POST/.search
SafeDeleteSocialIdentityProviderJob GET(Search), GET/&lt;ID&gt;
SafeDeleteSocialIdentityProviderJobReport GET(Search), GET/&lt;ID&gt;
SafeDeleteSocialIdentityProviderJobHistory GET(Search), GET/&lt;ID&gt;
SafeDeleteSocialIdentityProviderJobProgress ALL
SafeDeleteSocialIdentityProviderJobSchedule ALL
SecurityQuestions ALL
SocialAccounts ALL
TermsOfUseConsents ALL
UnMappedIdcsAttributes GET(Search), GET/&lt;ID&gt;
UserActivationInitiator ALL
UserAppsEnabledForAuthentication GET(Search), GET/&lt;ID&gt;
UserAppsEnabledForDelegatedAuthentication GET(Search), GET/&lt;ID&gt;
UserExportJob GET(Search), GET/&lt;ID&gt;
UserExportJobHistory GET(Search), GET/&lt;ID&gt;
UserExportJobProgress ALL
UserExportJobReport GET(Search), GET/&lt;ID&gt;
UserExportJobSchedule ALL
UserImportJob GET(Search), GET/&lt;ID&gt;
UserImportJobHistory GET(Search), GET/&lt;ID&gt;
UserImportJobProgress ALL
UserImportJobReport GET(Search), GET/&lt;ID&gt;
UserImportJobSchedule ALL
UserLockedStateChanger POST
UserNameGenerator ALL
UserPasswordChanger ALL
UserPasswordGenerator ALL
UserPasswordResetter ALL
UserPasswordValidator ALL
Users ALL
UserStateChanger ALL
UserTokens GET(Search), GET/&lt;ID&gt;
UserTokenValidator ALL

## User Manager

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a User Manager AppRole can access.

Endpoint Allowed Operations
AdaptiveAccessSettings GET/&lt;ID&gt;, GET(Search)
AnalyticEvents GET/&lt;ID&gt;
Apps GET/&lt;ID&gt;
AuditEvents GET/&lt;ID&gt;
AuthenticationFactorsRemover POST
Bulk ALL
BulkUserPasswordChanger ALL
BulkUserPasswordResetter ALL
BypassCodes POST
BypassCodeNotifications POST
IDCSGroups GET/&lt;ID&gt;, GET(Search), POST(Search), PATCH
IDSUser ALL
Images ALL
Groups GET/&lt;ID&gt;, GET(Search), POST(Search), PATCH
Jobs GET/&lt;ID&gt;
JobSchedules GET/&lt;ID&gt;, can schedule only BulkUserPasswordReset job.
JobHistories GET/&lt;ID&gt;
JobProgress GET/&lt;ID&gt;
JobReports GET/&lt;ID&gt;
Requests GET(Search), POST(Search)
RiskProviderProfiles GET/&lt;ID&gt;, GET(Search)
RiskScoreHistories GET/&lt;ID&gt;, GET(Search)
SecurityQuestions ALL
SocialAccounts ALL
UserActivationInitiator ALL
UserAppsEnabledForAuthentication GET/&lt;ID&gt;
UserAppsEnabledForDelegatedAuthentication GET/&lt;ID&gt;
UserLockedStateChanger ALL
UserPasswordChanger ALL
UserPasswordResetter ALL
UserPasswordGenerator ALL
UserPasswordValidator ALL
UserStateChanger ALL
Users ALL
UserStatusChanger ALL
WebrootUsage GET/&lt;ID&gt;, GET(Search)

## Verify Email

To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application.

The following table displays the endpoints and the allowed operations for that endpoint that a Verify Email AppRole can access.

Endpoint Allowed Operations
BrandingSettings GET(Search), GET/&lt;ID&gt;
MeEmailVerified ALL
