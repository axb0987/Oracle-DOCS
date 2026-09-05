# Filtering a List of Resources by a Tag
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Tasks/resourcetags-filtering-by-tags.htm
- Fetched: 2026-09-05 02:11 CDT

# Filtering a List of Resources by a Tag

When you’re viewing a list of resources in the Oracle Cloud Infrastructure Console, you can filter them by the tags applied to them.

- In the Oracle Cloud Console, go to the list page of the resource that you want to filter. For example, to filter Compute instances:

Open the navigation menu and select Compute . Under Compute , select Instances . All instances in the selected compartment are displayed in a table. To view the instances in a different compartment, use the Compartment filter to switch compartments.
- Perform one of the following actions depending on the option that you see:

- In the Search and Filter box, select Tags .
- On the left side of the page, next to Tag filters , select add .
- Enter the following information:

- Namespace: To search using a defined tag, select its tag namespace from the list. To search using a free-form tag, select None .
- Key: If you selected a tag namespace, select a key that’s associated with the namespace. If you’re searching using a free-form tag, enter a key. Keys for free-form tags are case sensitive.
- Value: Select one of the following options:
- Match any value returns all resources tagged with the selected namespace and key, regardless of the tag value.
- Specify matching values returns resources with the tag value that you specify. Enter a single value in the text box. To specify multiple values for the same namespace and key, select + to display another text box. Enter one value per text box.
-
