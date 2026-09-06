# Marketplace Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#dcoc-content-body)

## Marketplace Functions

Package: DBMS_CLOUD_OCI_MP_MARKETPLACE

### CHANGE_PUBLICATION_COMPARTMENT Function

Moves the specified publication from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`publication_id`

(required) The unique identifier for the publication.

`change_publication_compartment_details`

(required) The details of the request to change the compartment of a given publication.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ACCEPTED_AGREEMENT Function

Accepts a terms of use agreement for a specific package version of a listing. You must accept all terms of use for a package before you can deploy the package.

Syntax
```

```

Parameters

Parameter Description

`create_accepted_agreement_details`

(required) Details necessary to accept an agreement.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PUBLICATION Function

Creates a publication of the specified listing type with an optional default package.

Syntax
```

```

Parameters

Parameter Description

`create_publication_details`

(required) The details for creating the publication.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ACCEPTED_AGREEMENT Function

Removes a previously accepted terms of use agreement from the list of agreements that Marketplace checks before initiating a deployment. Listings in Marketplace that require acceptance of the specified terms of use can no longer be deployed, but existing deployments aren't affected.

Syntax
```

```

Parameters

Parameter Description

`accepted_agreement_id`

(required) The unique identifier for the accepted terms of use agreement.

`signature`

(optional) Previously, the signature generated for the listing package terms of use agreement, but now deprecated and ignored.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PUBLICATION Function

Deletes a publication, which also removes the associated listing from anywhere it was published, such as Marketplace or Compute.

Syntax
```

```

Parameters

Parameter Description

`publication_id`

(required) The unique identifier for the publication.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_LISTING Function

Exports container images or helm chart from marketplace to customer's registry.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The unique identifier for the listing.

`package_version`

(required) The version of the package. Package versions are unique within a listing.

`export_package_details`

(required) The details for exporting container images or helm chart.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ACCEPTED_AGREEMENT Function

Gets the details of a specific, previously accepted terms of use agreement.

Syntax
```

```

Parameters

Parameter Description

`accepted_agreement_id`

(required) The unique identifier for the accepted terms of use agreement.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AGREEMENT Function

Returns a terms of use agreement for a package with a time-based signature that can be used to accept the agreement.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The unique identifier for the listing.

`package_version`

(required) The version of the package. Package versions are unique within a listing.

`agreement_id`

(required) The unique identifier for the agreement.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LISTING Function

Gets detailed information about a listing, including the listing's name, version, description, and resources. If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want. Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a[GetAppCatalogListingAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements)API call. The[AppCatalogListingResourceVersionAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements)object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a[CreateAppCatalogSubscription](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription)API call. To get the image ID to launch an instance, issue a[GetAppCatalogListingResourceVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion)API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a[LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)API call.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The unique identifier for the listing.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PACKAGE Function

Get the details of the specified version of a package, including information needed to launch the package. If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want. Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a[GetAppCatalogListingAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements)API call. The[AppCatalogListingResourceVersionAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements)object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a[CreateAppCatalogSubscription](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription)API call. To get the image ID to launch an instance, issue a[GetAppCatalogListingResourceVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion)API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a[LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)API call.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The unique identifier for the listing.

`package_version`

(required) The version of the package. Package versions are unique within a listing.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLICATION Function

Gets the details of the specified publication.

Syntax
```

```

Parameters

Parameter Description

`publication_id`

(required) The unique identifier for the publication.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLICATION_PACKAGE Function

Gets the details of a specific package version within a given publication.

Syntax
```

```

Parameters

Parameter Description

`publication_id`

(required) The unique identifier for the publication.

`package_version`

(required) The version of the package. Package versions are unique within a listing.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the details of the specified work request

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ACCEPTED_AGREEMENTS Function

Lists the terms of use agreements that have been accepted in the specified compartment. You can filter results by specifying query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`display_name`

(optional) The display name of the resource.

`listing_id`

(optional) The unique identifier for the listing.

`package_version`

(optional) The version of the package. Package versions are unique within a listing.

`accepted_agreement_id`

(optional) The unique identifier for the accepted terms of use agreement.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to use to sort listed results. You can only specify one field to sort by. `TIMEACCEPTED` displays results in descending order by default. You can change your preference by specifying a different sort order.

Allowed values are: 'TIMEACCEPTED'

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AGREEMENTS Function

Returns the terms of use agreements that must be accepted before you can deploy the specified version of a package.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The unique identifier for the listing.

`package_version`

(required) The version of the package. Package versions are unique within a listing.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CATEGORIES Function

Gets the list of all the categories for listings published to Oracle Cloud Infrastructure Marketplace. Categories apply to the software product provided by the listing.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTINGS Function

Gets a list of listings from Oracle Cloud Infrastructure Marketplace by searching keywords and filtering according to listing attributes. If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want. Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a[GetAppCatalogListingAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements)API call. The[AppCatalogListingResourceVersionAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements)object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a[CreateAppCatalogSubscription](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription)API call. To get the image ID to launch an instance, issue a[GetAppCatalogListingResourceVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion)API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a[LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)API call.

Syntax
```

```

Parameters

Parameter Description

`name`

(optional) The name of the listing.

`listing_id`

(optional) The unique identifier for the listing.

`image_id`

(optional) The image identifier of the listing.

`publisher_id`

(optional) Limit results to just this publisher.

`package_type`

(optional) A filter to return only packages that match the given package type exactly.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.

Allowed values are: 'TIMERELEASED'

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`category`

(optional) Name of the product category or categories. If you specify multiple categories, then Marketplace returns any listing with one or more matching categories.

`pricing`

(optional) Name of the pricing type. If multiple pricing types are provided, then any listing with one or more matching pricing models will be returned.

Allowed values are: 'FREE', 'BYOL', 'PAYGO'

`is_featured`

(optional) Indicates whether to show only featured listings. If this is set to `false` or is omitted, then all listings will be returned.

`listing_types`

(optional) The type of the listing.

Allowed values are: 'COMMUNITY', 'PARTNER', 'PRIVATE'

`operating_systems`

(optional) The operating system of the listing.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PACKAGES Function

Gets the list of packages for a listing. If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want. Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a[GetAppCatalogListingAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements)API call. The[AppCatalogListingResourceVersionAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements)object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a[CreateAppCatalogSubscription](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription)API call. To get the image ID to launch an instance, issue a[GetAppCatalogListingResourceVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion)API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a[LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)API call.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The unique identifier for the listing.

`package_version`

(optional) The version of the package. Package versions are unique within a listing.

`package_type`

(optional) A filter to return only packages that match the given package type exactly.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.

Allowed values are: 'TIMERELEASED'

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLICATION_PACKAGES Function

Lists the packages in the specified publication.

Syntax
```

```

Parameters

Parameter Description

`publication_id`

(required) The unique identifier for the publication.

`package_version`

(optional) The version of the package. Package versions are unique within a listing.

`package_type`

(optional) A filter to return only packages that match the given package type exactly.

`sort_by`

(optional) The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.

Allowed values are: 'TIMERELEASED'

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLICATIONS Function

Lists the publications in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`listing_type`

(required) The type of the listing.

Allowed values are: 'COMMUNITY', 'PARTNER', 'PRIVATE'

`name`

(optional) The name of the publication.

`publication_id`

(optional) The unique identifier for the publication.

`operating_systems`

(optional) The operating system of the listing.

`sort_by`

(optional) The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.

Allowed values are: 'TIMERELEASED'

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLISHERS Function

Gets the list of all the publishers of listings available in Oracle Cloud Infrastructure Marketplace.

Syntax
```

```

Parameters

Parameter Description

`publisher_id`

(optional) Limit results to just this publisher.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPORT_TYPES Function

Lists available types of reports for the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPORTS Function

Lists reports in the compartment that match the specified report type and date.

Syntax
```

```

Parameters

Parameter Description

`report_type`

(required) The type of the report.

`l_date`

(required) Date, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. The service only interprets the year, month, and day parts in the input value, and ignores the hour, minute, and second parts.

`compartment_id`

(required) The unique identifier for the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAXES Function

Returns list of all tax implications that current tenant may be liable to once they launch the listing.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The unique identifier for the listing.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) The unique identifier for the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

List all errors for a work request

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

List all logs for a work request

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

List all work requests in a compartment

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`work_request_id`

(optional) The OCID of the work request.

`status`

(optional) A filter to return only resources whose status matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED'

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_LISTINGS Function

Queries all Marketplace Applications to find listings that match the specified criteria. To search for a listing, you can use a free text or structured search.

Syntax
```

```

Parameters

Parameter Description

`search_listings_details`

(required) Details related to the search query

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ACCEPTED_AGREEMENT Function

Updates the display name or tags associated with a listing's previously accepted terms of use agreement.

Syntax
```

```

Parameters

Parameter Description

`accepted_agreement_id`

(required) The unique identifier for the accepted terms of use agreement.

`update_accepted_agreement_details`

(required) Details to update for an accepted agreement.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PUBLICATION Function

Updates the details of an existing publication.

Syntax
```

```

Parameters

Parameter Description

`publication_id`

(required) The unique identifier for the publication.

`update_publication_details`

(required) The details for updating the publication.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Marketplace Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-FAC224DF-DFE2-4B27-B6EB-5EB5CA9E7673)
- [CHANGE_PUBLICATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-F36DAF38-6BE5-4B4A-ABBB-C55CB922B626)
- [CREATE_ACCEPTED_AGREEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-6BE49782-26FB-4666-AE4B-04EC313EE730)
- [CREATE_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-36E5AB55-D809-446A-A903-BE9576547005)
- [DELETE_ACCEPTED_AGREEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-2FE3CD61-9775-4E08-A04A-E03A8466D845)
- [DELETE_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-86A33CB1-E3FE-4611-B9D1-8D8FD05B6A1A)
- [EXPORT_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-F0132BB0-356D-4F40-A4AA-17BB62BD4EB0)
- [GET_ACCEPTED_AGREEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-1830ABB2-856E-4446-952A-2FE9527BDF0A)
- [GET_AGREEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-40152BEA-6DEF-4BDC-8E76-40A65AD87D36)
- [GET_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-F5017569-2AC0-4762-9B1F-5C8D7766DB95)
- [GET_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-AF4252D8-3B48-4396-85F8-F0D80E030F6E)
- [GET_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-866A3045-8C7E-45E7-A3A4-D54B264D8B87)
- [GET_PUBLICATION_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-FB6E2180-4061-4728-B5F7-1193A7338457)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-9F8C0327-2A26-44AF-8036-2085A7865D1A)
- [LIST_ACCEPTED_AGREEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-37D9881C-C229-4352-AD20-5BC2BC563C7F)
- [LIST_AGREEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-EEE8DEA5-ED3F-4480-8000-518787815933)
- [LIST_CATEGORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-95BE4E8A-576B-47EE-9E08-93CAF5D01645)
- [LIST_LISTINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-EE655E6B-6127-4331-B44D-354E61F880C8)
- [LIST_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-D38974B6-96FB-4197-87EF-17994948A8C9)
- [LIST_PUBLICATION_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-9E11ACD7-114C-4317-9C4D-9BA16C9FDBA6)
- [LIST_PUBLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-5744D39F-8D25-4A71-AFC9-B77C6EE8A25C)
- [LIST_PUBLISHERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-78620F5F-FB30-4741-AFDD-5CA46D475CD7)
- [LIST_REPORT_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-EB6D54AF-6187-44CD-AFB6-1A71361BFAF3)
- [LIST_REPORTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-B6A895F5-1BB5-442E-A95C-917198BB1A4A)
- [LIST_TAXES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-A8E7DE17-34E5-496F-9F04-1DFDC3135EB2)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-4184A2F7-176C-4266-A15F-7DF579B32C9C)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-7D5C20D0-BB69-40A0-B0DB-AB26E2061E1E)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-BD50966A-BCDA-4651-8EC9-603CA4CD4AD6)
- [SEARCH_LISTINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-B2CF07D5-923B-483F-8E7A-3A7D3886D2B4)
- [UPDATE_ACCEPTED_AGREEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-AA966467-6417-4A3D-941A-5AF8779EAFE3)
- [UPDATE_PUBLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_marketplace.html#ADSDK-GUID-90DBF074-DD25-4F98-96B3-7995C535F9E4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
