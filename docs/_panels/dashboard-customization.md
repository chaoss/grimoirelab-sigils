---
name: Dashboard Customization
description: customer access to Kibiter dashboards
layout: panel
---

## Customer access to Kibiter dashboards

This document details how customers should behave when editing Kibiter-based dashboards maintained by Bitergia, to avoid interfering with the maintenance and upgrading activities that will be performed on them.

In the following, "elements" will be panels (dashboards, in Kibana nomenclature), visualizations or searches. The "user dashboard" will be the dashboard as regular users access to it. The "edit dashboard" will be the dashboard as editing users (customers with the right to edit, accessing through the edit link) access it. "standard elements" refer to the elements maintained by Bitergia as a part of the standard dashboard.  "customer elements" refer to elements created by customer with editing rights.

### General rules

Usually, customers will access the edit dashboard through the editing interface, which gives access to a "regular" Kibiter instance (remember that Kibiter is GrimoireLab light fork of Kibana). This is usually done through the https://xxx.biterg.io/edit url (being xxx the dashboard id), although that url may be different.

It is important that customers don't modify and save any of the elements that are part of the standard dashboard, and in general any element that they didn't create themselves. Any modification will have immediate impact on the user dashboard upon saving.

That means that if some standard element is broken for some reason, or causes some other standard element to break, the broken effect will be shown to regular users as soon as that is saved in Kibiter. Although Bitergia will do its best effort to recover from those circumstances, customers should avoid them, and in no case the result of those circumstances will be responsibility of Bitergia.

In addition, standard elements may be updated or recovered from the standard versions at any moment, thus reverting any change done by a customer.

This does not mean that customers may not change any element of the dashboard: they can, with no special consequences, as soon as they do not save it. If they want to save them, they should do so under a different name, following the conventions in the "Naming conventions" section below.

Customers can as well create new elements (dashboards, visualizations, searches) from scratch. Again, if they want to save them, they should do that following the naming conventions.

Index patterns should, as a general rule, not be changed or edited in any way by customers.

After creation of new dashboards, those new dashboards can be visited by users as panels if the appropriate url (without "/edit") is shared. If the customer has interest in those dashboards being included in the "users" menu, they should address their Bitergia contact. That inclusion could mean some extra charge on the subscription price, depending on the contracting details.

Customers will be responsible for the maintenance of customer elements, including their backup. Bitergia will do a best effort for maintaining backup copies of them, and not deleting them during upgrades or migrations. But that should not be considered as granted.

### Naming conventions

The upgrading and recovering tasks performed by Bitergia will ignore any element with a name starting with the characters "C\_" (note that "C" is uppercase, and "\_" is the underscore character).

Therefore, all customer elements should, when saved, use names starting with those characters. This applies both to standard elements after they are edited and saved by customers, and to customer elements created from scratch.

A customer dashboard (panel) can include customer and standard visualizations. In that case, obviously, all customer visualizations will have a name starting with "C\_". This applies to searches being the basis for visualizations as well.

### Good practices

When creating new elements based on standard elements, customers may use the same name of the standard element starting with "C\_".

When creating new elements from scratch, customers may use names completely different from those of standard elements, always prefixed with "C\_".

Although customers are free to use their own names, it could be convenient to follow Bitergia's naming conventions [1]. Following them, element names should be built in the following way:
```
C_<index_pattern_name>_(<metric_name>] | [<panel_name>])
```

Upon saving any customer element, **customers should save their customized elements**. Ask for the corresponding training information about saving elements if you don't know how to do that.

When recovering saved customer elements, be sure to avoid including previously saved standard elements, since they could have evolved, and be different from the saved versions.

### Troubleshooting

##### 1. A table takes too long to load data and/or browser's response time is slow
Tables are composed of metrics applied over a set of documents organized in buckets. This problem usually appears when there are too many buckets at the same level or several bucketing levels. As Kibana seems to load the whole table at once, it also could affect browser performance.

[1] Bitergia's naming conventions are available at: https://github.com/grimoirelab/panels#panels
