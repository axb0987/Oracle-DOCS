# Threat Intelligence Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html
- Fetched: 2026-09-05 19:21 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#dcoc-content-body)

## Threat Intelligence Common Types

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SOURCE_SUMMARY_T Type

Information about the source of threat indicator data.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the source.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_DATA_VISIBILITY_T Type

The visibility level of attribution data, including its[Traffic Light Protocol (TLP)](https://www.cisa.gov/tlp)color.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the visibility level.

`tlp_name`

(required) The Traffic Light Protocol (TLP) color of the visibility level.

Allowed values are: 'TLP_INTERNAL_AUDIT', 'TLP_WHITE', 'TLP_GREEN', 'TLP_AMBER', 'TLP_RED'

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_DATA_ATTRIBUTION_T Type

The confidence, source information, and visibility for a particular sighting or observation of some data associated with a threat indicator. This associated data can be the indicator's threat type, attribute, or relationship.

Syntax
```

```

Fields

Field Description

`confidence`

(required) An integer from 0 to 100 that provides a measure of our certainty in the maliciousness of data attributed to an indicator. For example, if the source of the data being attributed is the Tor Project, our confidence that the associated indicator is a tor exit node would be 100.

`source`

(required)

`visibility`

(required)

`time_first_seen`

(optional) The date and time the attribution data was first seen for this entity. If the data source does not provide this information, it is set to the last time it was seen. An RFC3339 formatted string.

`time_last_seen`

(required) The last date and time the attribution data was seen for this entity. An RFC3339 formatted string.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_ENTITY_REFERENCE_T Type

A reference to a resource or other entity.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the referenced entity.

Allowed values are: 'INDICATOR'

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_GEODATA_DETAILS_T Type

Geodata information for a given IP address

Syntax
```

```

Fields

Field Description

`routed_prefix`

(optional) Encompassing assigned prefix for the IP

`origin`

(required) ASN entry

`geo_id`

(optional) Unique Identifier (optional)

`country_code`

(required) Two-letter abbreviation for country of origin

`admin_div`

(required) State/Province/subdivision within the country

`city`

(required) City of origin

`latitude`

(required) Latitude

`longitude`

(required) Longitude

`label`

(required) Information on source providing the information

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_DATA_ATTRIBUTION_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_data_attribution_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_T Type

A threat type along with attribution data that associates it to a threat indicator.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the threat type.

`name`

(required) The name of the threat type.

`attribution`

(required) The list of supporting attribution information.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_T Type

An attribute name and list of values with attribution.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the attribute.

`value`

(required) The value of the attribute.

`attribution`

(required) The array of attribution data that support this attribute.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_RELATIONSHIP_T Type

A relationship name and list of releated entities.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the attribute.

`related_entity`

(required)

`attribution`

(required) The array of attribution data that support this relationship.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_threat_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_indicator_attribute_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_RELATIONSHIP_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_indicator_relationship_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_T Type

A data signature observed on a network or host that indicates a potential security threat. Indicators can be plain text or computed (hashed) values.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the indicator.

`l_type`

(required) The type of indicator.

Allowed values are: 'DOMAIN_NAME', 'FILE_NAME', 'MD5_HASH', 'SHA1_HASH', 'SHA256_HASH', 'IP_ADDRESS', 'URL'

`value`

(required) The value for this indicator. The value's format is dependent upon its `type`. Examples: DOMAIN_NAME \"evil.example.com\" MD5_HASH \"44d88612fea8a8f36de82e1278abb02f\" IP_ADDRESS \"2001:db8::1\"

`confidence`

(optional) An integer from 0 to 100 that represents how certain we are that the indicator is malicious and a potential threat if it is detected communicating with your cloud resources. This confidence value is aggregated from the confidence in the threat types, attributes, and relationships to create an overall value for the indicator.

`compartment_id`

(optional) The OCID of the compartment that contains this indicator.

`threat_types`

(required) Characteristics of the threat indicator based on previous observations or behavior. May include related tactics, techniques, and procedures.

`attributes`

(required) A map of attributes with additional information about the indicator. Each attribute has a name (string), value (string), and attribution (supporting data).

`relationships`

(required) A map of relationships between the indicator and other entities. Each relationship has a name (string), related entity, and attribution (supporting data).

`lifecycle_state`

(optional) The state of the indicator. It will always be `ACTIVE`.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) The date and time that the indicator was first detected. An RFC3339 formatted string.

`time_updated`

(required) The date and time that this indicator was last updated. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.

`time_last_seen`

(required) The date and time that this indicator was last seen. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.

`geodata`

(required)

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_SUMMARY_T Type

An attribute name and list of values.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the attribute.

`value`

(required) The value of the attribute.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_DIMENSIONS_T Type

The indicator dimension that was counted, such as the indicator type.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The compartment OCID that contains the indicator type.

`l_type`

(optional) The indicator type that was counted.

Allowed values are: 'DOMAIN_NAME', 'FILE_NAME', 'MD5_HASH', 'SHA1_HASH', 'SHA256_HASH', 'IP_ADDRESS', 'URL'

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_SUMMARY_T Type

A group of indicators with the same dimensions, such as the same indicator type.

Syntax
```

```

Fields

Field Description

`dimensions`

(required)

`l_count`

(required) The count of indicators in the group.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_indicator_count_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_COLLECTION_T Type

A list of indicator counts by indicator type.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of aggregated indicator counts.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_REFERENCE_T Type

A reference to a threat indicator resource.

Syntax
```

```

`dbms_cloud_oci_threat_intelligence_indicator_reference_t`is a subtype of the`dbms_cloud_oci_threat_intelligence_entity_reference_t`type.

Fields

Field Description

`indicator_id`

(required) The unique OCID of the referenced threat indicator.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_indicator_attribute_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SUMMARY_T Type

Summary of a data signature observed on a network or host that indicates a potential security threat.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the indicator.

`l_type`

(required) The type of indicator.

Allowed values are: 'DOMAIN_NAME', 'FILE_NAME', 'MD5_HASH', 'SHA1_HASH', 'SHA256_HASH', 'IP_ADDRESS', 'URL'

`value`

(required) The indicator data value.

`confidence`

(optional) An integer from 0 to 100 that represents how certain we are that the indicator is malicious and a potential threat if it is detected communicating with your cloud resources. This confidence value is aggregated from the confidence in the threat types, attributes, and relationships to create an overall value for the indicator.

`compartment_id`

(optional) The OCID of the compartment that contains this indicator.

`threat_types`

(required) Characteristics of the threat indicator based on previous observations or behavior. May include related tactics, techniques, and procedures.

`attributes`

(required) A map of attributes with additional information about the indicator. Each attribute has a name (string), value (string), and attribution (supporting data).

`lifecycle_state`

(optional) The state of the indicator. It will always be `ACTIVE`.

Allowed values are: 'ACTIVE', 'DELETED'

`time_created`

(required) The date and time that the indicator was first detected. An RFC3339 formatted string.

`time_updated`

(required) The date and time that this indicator was last updated by the system. Updates can include new reports or regular updates in confidence. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.

`time_last_seen`

(required) The date and time that this indicator was last seen. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.

`geodata`

(required)

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_indicator_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SUMMARY_COLLECTION_T Type

List of indicator summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of indicator summaries.

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_SUMMARIZE_INDICATORS_DETAILS_T Type

Query parameters to filter indicators

Syntax
```

```

Fields

Field Description

`indicator_type`

(optional) The type of indicator this is

Allowed values are: 'DOMAIN_NAME', 'FILE_NAME', 'MD5_HASH', 'SHA1_HASH', 'SHA256_HASH', 'IP_ADDRESS', 'URL'

`indicator_value`

(optional) The value for the type of indicator this is

`threat_types`

(optional) The threat type of entites to be returned.

`confidence_greater_than_or_equal_to`

(optional) The minimum level of confidence to return

`time_updated_greater_than_or_equal_to`

(optional) The oldest update time of entities to be returned.

`time_updated_less_than`

(optional) The newest update time of entities to be returned.

`time_last_seen_greater_than_or_equal_to`

(optional) The oldest last seen time of entities to be returned.

`time_last_seen_less_than`

(optional) The newest last seen time of entities to be returned.

`time_created_greater_than_or_equal_to`

(optional) The oldest creation time of entities to be returned.

`time_created_less_than`

(optional) The newest creation time of entities to be returned.

`indicator_seen_by`

(optional) Filter to include indicators that have been seen by the provided source.

`malware`

(optional) Filter to include indicators associated with the provided malware.

`threat_actor`

(optional) Filter to included indicators associated with the provided threat actor.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one field to sort by may be provided

Allowed values are: 'CONFIDENCE', 'TIMECREATED', 'TIMEUPDATED', 'TIMELASTSEEN'

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_SUMMARY_T Type

The name of a threat type and its ID.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the threat type

`name`

(required) The name of the threat type

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_threat_intelligence_threat_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPES_COLLECTION_T Type

List of threat types that can be associated with threat indicators.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of threat types that can be used to search for threat indicators.

- [Threat Intelligence Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-3A57E3C3-03B2-43DE-8802-D07DCA562220)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-3BC9C59D-A64B-44E3-9195-929C1FC7ADE8)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-0613938B-55F0-4944-94A7-F609717418A3)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_DATA_VISIBILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-801C9506-D550-4795-9C35-0772798E9648)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_DATA_ATTRIBUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-CD40BB37-6911-48D2-9D16-261020122713)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_ENTITY_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-FBEDF684-0A15-404F-8ED8-815154902884)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-9601028F-4B29-4E8B-8C17-5A5933C3401F)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_GEODATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-E8399A03-CFB7-44C8-9F2B-D5EB9B186715)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_DATA_ATTRIBUTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-F04CDFC8-81E0-49F8-89AB-196DFA61D031)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-635472F6-7D71-45C2-AC13-9D72570E080C)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-25017FFE-F3DB-42AF-9558-2E2E47A36B8D)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_RELATIONSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-29E296AB-9A29-4E23-982E-C19F7636F8CB)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-26422FA8-D7C6-4D00-8188-C66EBB50F3CF)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-1C594F7F-7CDC-4659-9174-34BBE7970A4B)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_RELATIONSHIP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-F2F4D966-9E4D-4932-A68B-0958D680A8A7)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-8376B301-C95F-4A43-9298-265B2E690E48)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-53DE962E-E42A-4FAA-AFBF-865E62B731E1)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-0C7035A5-DE95-45F2-9AE5-4E45CBA7CAF0)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-8187C2D7-49B6-4692-B47F-4A4442B3FAE3)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-F925539D-D3BC-459E-9E68-06093D2C0678)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_COUNT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-5D6A3BEF-6097-494F-8CB5-2C6E17BFF274)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-12202C8C-9682-4D0F-AE67-90E7C9AFC8E8)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_ATTRIBUTE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-B8DC5F60-8B52-4BC5-8AF3-EF6483E18BDD)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-2D783B61-9399-427B-8061-3E05120C762E)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-C5A40E11-2AAA-43C8-90C9-AB0764F30060)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_INDICATOR_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-765B7306-6C48-42C8-9310-02FFA3C9700E)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_SUMMARIZE_INDICATORS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-6C6A0C7A-8C2E-4033-A0C9-BC4CFA3E8453)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-5AD98A89-7BA3-449B-A886-3A6163649E6D)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-9190461B-A27E-46E9-B124-1C6F4C36BB94)
- [DBMS_CLOUD_OCI_THREAT_INTELLIGENCE_THREAT_TYPES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/threat_intelligence_t.html#ADSDK-GUID-C1E17D57-0EA0-4F84-B526-9599A59C6010)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
