---
layout: post
title: Routing mode + (helper) walk modes
author: Gregor Leich
summary: "We (Kai Nagel, Gregor Leich) just merged the branch `routingMode5` into the development head master branch. This is a pretty old topic, partly solves several Jira issues, and makes life easier for intermodal trips."
---

We (Kai Nagel, Gregor Leich) just merged the branch `routingMode5` into the development head master branch (<https://github.com/matsim-org/matsim/pull/738>).

#### Summary:

- all legs now have an attribute “routingMode”

- the MainModeIdentifier is only used to retrofit old plans without routingMode (automatic in PrepareForSimImpl), it won’t be used in ModeStatsControlerListener (overwrite AnalysisMainModeIdentifier instead)

- several helper walk modes such as “transit_walk”, “non_network_walk”, “access_walk”, “drt_walk”, “drt_fallback” were replaced by normal TransportMode.walk (automatic retrofit in PrepareForSimImpl), more precisely by calls to the RoutingModule for TransportMode.walk. This replaced many custom *walk routers and will allow routing “walk” over the network in the future.

This is a pretty old topic (<https://matsim.atlassian.net/browse/MATSIM-26>), partly solves several Jira issues, e.g. (<https://matsim.atlassian.net/browse/MATSIM-943>, <https://matsim.atlassian.net/browse/MATSIM-856>, <https://matsim.atlassian.net/browse/MATSIM-473 >) and makes life easier for intermodal trips.

The content is our long-discussed "routing mode", i.e. that trips memorize the router from which they were generated. The prime example is a trip which currently may have mode `transit_walk`; in the future, it would have mode `walk` and routing mode `pt`. This also means that "MainModeIdentifier" will no longer be necessary. (We will keep it to retrofit older plans files.)

In general, we are not using `non_network_walk` or `transit_walk` or `drt_walk`. The reasoning is that teleported bicycle is `bike`, not `non_network_bike`, and we have always done it like that. In consequence, if the `walk` router called from, say, the `pt` router is a teleportation router, it will still return plain `walk`. The only exception is a _network-based_ `walk` router: In that case, we indeed have `non_network_walk` access to the walk network, then a walk leg along the network, and a non_network_walk to the final destination.

The implementation currently is via `Attributable`. Since there is no trip, we attach it to every leg. Trips that have inconsistent routing modes in their legs will lead to an error. We should probably consider to elevate the routing mode to a typed argument with a future population file.

“non_network_walk“ will now only be used by the walk router if walk is routed over the network and only for access/egress to the walk network. It is some kind of fallback layer to access the network. All other modes can use the walk router to access the network. Per default the walk router is still a pure teleportation router NOT routing over the network. So in the end what was a `non_network_walk → pt interaction → pt → pt interaction → non_network_walk` trip will now per default be a `walk → pt interaction → pt → pt interaction → walk trip` with the plansCalcRoute and scoring parameters of _walk_!. 

Keep in mind that what was previously a direct walk “transit_walk”  is now a `walk` leg with routingMode `pt` and has the same scoring and plansCalcRoute parameters as walk with routingMode walk, so mode shift from one to the other does not necessarily mean a real change (that problem already existed before as the default for transit_walk was to copy parameters from walk). Similar issues apply to the other fallback modes (`drt_walk`, `drt_fallback`). Previously we had only the MainModeIdentifier which was used for two rather incompatible purposes (see <https://matsim.atlassian.net/browse/MATSIM-26> for details):

1. to identify the correct routing module

2. to identify the main mode according to transportation planning.
    - One example where this becomes clear are the somewhat weird "main mode" definition in the German travel survey ... which just has an arbitrary hierarchy for multi-modal trips. So this varies from country to country, and maybe even from survey to survey.

We now split them up:

1. is now explictly saved in the attribute routingMode ( and uses MainModeIdentifier for retrofitting old plans)

2. `AnalysisMainModeIdentifier` binding, defaults to routingMode for backwards compatibility, but can be overwritten separately from `MainModeIdentifier` with something more useful for mode share analysis.

This is only an analysis problem, you can now plug in an AnalysisMainModeIdentifier to fix this in analysis, e.g. overwrite the default with an hierachical `MainModeIdentifier` such as `TransportPlanningMainModeIdentifier`. 
