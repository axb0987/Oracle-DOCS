# Examples
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/plsqlsdkexamples.htm
- Fetched: 2026-09-05 01:36 CDT

# Examples

This section contains examples of how to use the PL/SQL SDK.

This section contains examples of how to use the PL/SQL SDK.

## Working with Object Storage Buckets

The following example shows examples of how to use the PL/SQL SDK to create and delete buckets using the OCI Object Storage service:
```

```

## Working with Object Storage Objects

The following example shows how to use the PL/SQL SDK to store and retrieve objects using the OCI Object Storage service:
```

```

## Listing Compartments

The following example shows how to list compartments using the PL/SQL SDK:-- ###################### -- ## ListCompartments ## -- ###################### set serveroutput on declare response_body dbms_cloud_oci_identity_compartment_tbl; response dbms_cloud_oci_id_identity_list_compartments_response_t; json_obj json_object_t; l_keys json_key_list; begin response := dbms_cloud_oci_id_identity.list_compartments( compartment_id =&gt; 'compartment_OCID', limit =&gt; 2, credential_name =&gt; 'OCI_KEY_CRED', region =&gt; 'region-identifier'); response_body := response.response_body; -- Response Headers dbms_output.put_line('Headers: ' || CHR(10) ||'------------'); json_obj := response.headers; l_keys := json_obj.get_keys; for i IN 1..l_keys.count loop dbms_output.put_line(l_keys(i)||':'||json_obj.get(l_keys(i)).to_string); end loop; -- Response status code dbms_output.put_line('Status Code: ' || CHR(10) || '------------' || CHR(10) || response.status_code); dbms_output.put_line(CHR(10)); for i in 1 .. response_body.count loop dbms_output.put_line(response_body(i).id); dbms_output.put_line(response_body(i).compartment_id); dbms_output.put_line(response_body(i).name); dbms_output.put_line(response_body(i).description); dbms_output.put_line(response_body(i).time_created); dbms_output.put_line(response_body(i).lifecycle_state); dbms_output.put_line(response_body(i).inactive_status); dbms_output.put_line(response_body(i).is_accessible); dbms_output.put_line(response_body(i).freeform_tags.to_string()); dbms_output.put_line(response_body(i).defined_tags.to_string()); end loop; end; /

## Working With Streams

The following example shows how to create and delete stream pools using the PL/SQL SDK:
```

```
