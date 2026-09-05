# Object Storage Storage Tiers
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm
- Fetched: 2026-09-05 02:50 CDT

# Object Storage Storage Tiers

Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.

Object Storage offers distinct storage class tiers to address the need for both performant, frequently accessed "hot" storage, less often accessed "cool" storage, and rarely accessed "cold" storage. Every object uploaded to Object Storage is assigned to a storage tier. The storage tier property of the object determines its storage costs and any associated retrieval fees. The storage tier property is assigned to an object in one of two ways:
- The object is automatically assigned the default storage tier of the bucket (Standard or Archive) that you're uploading the object to.
- If you're uploading an object to a Standard default storage tier bucket, you can explicitly assign any permitted storage tier (Standard, Infrequent Access, or Archive) to the object.
Important  
  
Standard storage tier buckets can contain a mix of objects with different storage tier assignments. An object remains in the Standard bucket, even if the object is archived, restored, or if tier assignment is changed.

Archive Storage tier buckets can only contain objects with an Archive Storage tier assignment. Archive buckets do not contain a mix of objects with different storage tier assignments. An object remains in the Archive bucket, even if the object is restored.

When using[Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/../Tasks/usinglifecyclepolicies.htm)or manually tiering storage from Infrequent Access to Archive Storage, standard retrieval fees apply for Infrequent Access storage.

You interact with the data stored in any of the storage tiers using the same[Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm)[management interfaces](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm#accessways). In addition, each storage tier supports the full range of Object Storage features. Specific storage tier details or interactions that you need to be aware of are covered in the Scope and Constraints section for the feature.
The following table summarizes the features of the Standard, Infrequent Access, and Archive tiers.

Tier Storage Cost Minimum Retention Period Retrieval Fee Availability SLA
Standard Highest None No 99.9%
Infrequent Access Cheaper 31 days Yes 99%
Archive Lowest 90 days No Data is offline and objects must be restored before they can be read. Restoration takes at most an hour from the time an Archive Storage restore request is made, to the time the first byte of data is retrieved.

## Standard Tier

The Standard tier is the primary, default storage tier used for[Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)service data. The Standard storage tier is "hot" storage used for data that you need to access quickly, immediately, and frequently. Data accessibility and performance justifies a higher price to store data in the Standard tier.

You choose a default storage tier (Standard or Archive) when you create a bucket. When set at bucket creation, you cannot change the default storage tier for a bucket. When you upload objects to a bucket, the objects are automatically assigned the default storage tier of the bucket (Standard). You can, however, change the storage tier of an object to either Infrequent Access or Archive.

Standard storage tier buckets can contain a mix of objects with different storage tier assignments. An object remains in the Standard bucket, even if the object is archived, restored, or its tier assignment is changed.

When you choose a Standard default storage tier during bucket creation, you can also enable Auto-Tiering . Auto-Tiering helps you reduce storage costs by automatically moving objects between the Standard and Infrequent Access storage tiers based on data access patterns. See[Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#auto_tiering)for details.

Some primary use cases for the Standard storage tier include the following:
- Content repository for accessible scalable data, images, logs, and video
- Repository for accessible backups
- Data repository for Hadoop/big data. Provides a scalable storage platform to store large datasets and operate seamlessly on those datasets. The[HDFS Connector for Object Storage](https://docs.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm)provides connectivity to various big data analytic engines like Apache Spark and MapReduce. This connectivity enables the analytics engines to work directly with data stored in Object Storage. For more information, see[Object Storage Hadoop Support](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/../Tasks/hadoopsupport.htm).

## Infrequent Access

The Infrequent Access tier is "cool" storage used for data that you access infrequently, but that must be available immediately when needed. Storage costs are less than Standard .

If you're uploading an object to a Standard default storage tier bucket, you can explicitly assign the object to the lower-cost Infrequent Access storage tier.

The Infrequent Access tier has a minimum storage retention period and data retrieval fees:
- The minimum storage retention period for the Infrequent Access tier is 31 days. If you delete or overwrite objects in the Infrequent Access tier before the retention requirements are met, you're charged the prorated cost of storing the data for the full 31 days.
- When you need to access objects stored in this tier, you're charged a per GiB data retrieval fee.
Note  
  

Minimum retention penalties are charged only when deletes and overwrites result in data removal. Deletes and overwrites in a version-enabled bucket that creates a previous version rather than removing data, doesn't result in a penalty.

When using[Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/../Tasks/usinglifecyclepolicies.htm)or manually tiering storage from Infrequent Access to Archive Storage, standard retrieval fees apply for Infrequent Access storage.

Some primary use cases for the Infrequent Access storage tier include the following:
- Backups of on-premises data
- Repository for rarely accessed backups
- Storage for data replicated or copied from another region

## Archive

The Archive tier is the primary, default storage tier used for[Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)service data. The Archive Storage tier is "cold" storage used for data seldom or rarely access, but that must be retained and preserved for long periods of time.

You choose a default storage tier (Standard or Archive) when you create a bucket. When set at bucket creation, you cannot change the default storage tier for a bucket. When you upload objects to a bucket in an Archive tier, the objects are automatically assigned the default storage tier of the bucket (Archive).

Archive Storage tier buckets can only contain objects with an Archive Storage tier assignment. Archive buckets do not contain a mix of objects with different storage tier assignments. An object remains in the Archive bucket, even if the object is restored.

Objects in the Archive tier must be restored before they're available for access. The cost efficiency of the Archive tier offsets the lead time required to access the data. However, the Archive tier has a minimum storage retention period and some extra storage fees:
- The minimum storage retention period for the Archive tier is 90 days. If you delete or overwrite objects in the Archive tier before the retention requirements are met, you're charged the prorated cost of storing the data for the full 90 days.
- When you restore objects, you're returning those objects to the Standard tier for access. You're billed for the Standard class tier while the restored objects reside in that tier.
Note  
  
Minimum retention penalties are charged only when deletes and overwrites result in data removal. Deletes and overwrites in a version-enabled bucket that creates a previous version rather than removing data, doesn't result in a penalty.

Some primary use cases for the Archive Storage tier include the following:
- Compliance and audit mandates
- Retroactive log data analysis to determine usage pattern or to debug problems
- Historical or rarely accessed content repository data
- Application-generated data requiring archival for future analysis or legal purposes

## Auto-Tiering

Auto-Tiering monitors data access patterns and helps you reduce storage costs by automatically moving objects larger than 1 MiB out of the Standard tier into the more cost-effective Infrequent Access tier. Auto-Tiering is enabled at the bucket-level and monitors the data access patterns of all objects in the bucket. You can enable Auto-Tiering for any Standard storage tier bucket at creation time. You can also enable Auto-Tiering at any time after bucket creation.
Note  
  
You can't enable Auto-Tiering if you have a lifecycle policy rule that moves objects, object versions, or previous object versions to the Infrequent Access tier. If appropriate, delete the rule and try to enable Auto-Tiering again.

After you enable Auto-Tiering, objects remain in the Standard tier until they meet the minimum access and storage requirements required for movement eligibility to Infrequent Access. If Object Storage moved objects to Infrequent Access that are later accessed more frequently, we automatically move the objects back to the Standard tier without incurring any retrieval and prorated storage fees.

Because you incur no retrieval or prorated storage fees, enabling Auto-Tiering is particularly cost-effective for the following use cases:
- New application data storage that has no established access patterns
- Data storage that has changing access patterns

### Required Permissions

To enable auto-tiering, you must authorize the service to manage objects on your behalf:
- You can create a policy that authorizes the service in the specified region to manage Object Storage namespaces, buckets, and their associated objects in all compartments in the tenancy:

```

```

- Instead of using the[policy verb](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-Verbs.htm)`manage`, you can create a policy that reduces the scope of access by instead using one of the following statements:

```

```

```

```

## Mapping from AWS S3 Storage Tiers to OCI Storage Tiers

AWS Storage Tier OCI Storage Tier

- Standard
- Intelligent-Tiering
- Standard

- Standard-IA
- One Zone-IA
- Infrequent Access

- Glacier Instant Retrieval
- Glacier Deep Archive
- Archive
Note
