# Supported App Gateway Docker and OVA Releases and Patches
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/app-gateway-docker-ova-supported-releases-patches.htm
- Fetched: 2026-09-05 02:18 CDT

# Supported App Gateway Docker and OVA Releases and Patches

App Gateway releases are done to provide feature enhancements and bug fixes. Releases are for both the Docker and OVA formats, and each might be released independently.

## Supported App Gateway Docker (26.1.06) and OVA (25.4.3) Releases

App Gateway releases are done to provide feature enhancements and bug fixes. Releases are for both the Docker and OVA formats, and each might be released independently.
- [App Gateway Docker Release 26.1.06](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/app-gateway-docker-ova-supported-releases-patches.htm#top__app-gateway-docker-releases)
- [App Gateway OVA Release 25.4.3](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/app-gateway-docker-ova-supported-releases-patches.htm#top__app-gateway-ova-releases)

App Gateway Docker Release 26.1.06

Package: idcs-appgateway-docker-26.1.06-2602110936.zip

Image Family: Oracle Linux 8

Notable Changes
- Log rotation is supported by default.
- Idle Session Logout feature is disabled by default in this release.
- Logout isn't triggered on Idle Sessions in the following cases:
- The authentication method configured in the Web Tier Policy for the request API is anonymous.
- The Authorization Request Header is configured to`Session`.
- Refactored the customer headers added to requests by Cloud Gate to support:`$subject.user.givenName`,`$subject.user.middleName`, and`$subject.user.familyName`.

App Gateway OVA Release 25.4.3

Package: idcs-app-gateway-25.4.3-10.0.0

Image Family: Oracle Linux 8

Notable Changes
- Log rotation support through the`logrotate`utility and`manage-logs`through cron is disabled.
- Fixed`cg-upgrade`script issues.
- Fixed a curl issue caused by the Libcurl upgrade.
- Fixed creation of`nginx-cg-resolv.conf`.
- Fixed the SSL certificate issue during calls to IDCS by Python.
- Fixed an issue where`ociregion`defaulted to Mumbai. The`ocidomain`value is set to`oracle.com`and`ociregion`is set to`null`, so it points to the public YUM repository.
- Idle Session Logout feature is disabled by default in this release.

## Supported App Gateway Docker (25.3.32) and OVA Releases (25.1.1)

App Gateway releases and patches are done to provide feature enhancements and bug fixes. Releases are for both the Docker and OVA formats, and each might be released independently.
- [App Gateway Docker 25.3.32](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/app-gateway-docker-ova-supported-releases-patches.htm#top__idcs-appgateway-docker-25.3.32)
- [App Gateway OVA Releases-25-1-1](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/app-gateway-docker-ova-supported-releases-patches.htm#top__app-gateway-ova-releases-25-1-1)
- [App Gateway OVA Patches 25.3.1](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/app-gateway-docker-ova-supported-releases-patches.htm#top__app-gateway-ova-patches)

idcs-appgateway-docker-25.3.32-2508110511
- Release date: 2025-09-12
- Image family: Oracle Linux 8
- NGINX version: 1.28.0

idcs-appgateway-docker-25.1.03-2501230623
- Release date: 2025-02-01
- Image family: Oracle Linux 8
- NGINX version: 1.25.5
- `cloudgate.config`override during container restart: Custom changes made to the`cloudgate.config`file now persist after a container restart.
- Mapping through query parameters match: Enterprise applications can now be mapped based on query parameters, in addition to the URL path.
- Script-based health check: The existing`cloudgate/v1/status`API provides the status of the`cloudgate`module and the NGINX server (as the API is served by NGINX). To obtain the status of the agent and configuration, a dedicated health check script has been introduced.
- Package updates: Upgraded`libcurl`to version 8.10.1.

App Gateway OVA Releases

idcs-app-gateway-25.1.1-9.0.0
- Release date: 2025-02-01
- Image family: Oracle Linux 8
- NGINX upgraded to: 1.25.5
- `cloudgate.config`override during container restart: Custom changes made to`cloudgate.config`now persist after a container restart.
- Mapping through query parameters match: Enterprise applications can now be mapped based on query parameters, in addition to the URL path.
- Script-based health check: The existing`cloudgate/v1/status`API provides the status of the`cloudgate`module and the NGINX server (as the API is served by NGINX). To obtain the status of the agent and configuration, a dedicated health check script has been introduced.
- Package updates: Upgraded`libcurl`to version 8.10.1.

App Gateway OVA Patches

idcs-app-gateway-patch-25.3.1-9.0.1
- Release date: 2025-09-12
- Base OVA Version: 9.0.0
-
