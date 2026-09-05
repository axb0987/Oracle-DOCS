# Subscribing to an Infrastructure Region
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm
- Fetched: 2026-09-05 02:27 CDT

# Subscribing to an Infrastructure Region

Subscribe to an infrastructure region in IAM.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm#)
- 

- On the Infrastructure regions list page, find the region you want to subscribe to. If you need help finding the list page, see[Listing Infrastructure Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_view_the_list_of_infrastructure_regions.htm)and[Listing Subscribed Infrastructure Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/list_subscribed_infrastructure_regions.htm).
- Select the Actions menu (three dots) and then select Subscribe .

Note  
  
It could take several minutes to activate your tenancy in the new region.
- (Optional) To switch to the new region, use the Region menu in the Console. See[Switching Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Switchin)for more information.

Remember, IAM resources are global, so when the subscription becomes active, all your existing policies are enforced in the new region.

You can't unsubscribe from a region.
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/region-subscription/create.html)command and required parameters to subscribe to an infrastructure region:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateRegionSubscription](https://docs.oracle.com/iaas/api/#/en/identity/latest/RegionSubscription/CreateRegionSubscription)
