---
layout: post
author: Michal Maciejewski
title: "PR-labelled releases"
summary: "We have added a new type of MATSim releases that are created after each pull request is merged."
---

## PR-labelled releases

In mid-April, we introduced PR-labelled releases (or shortly, PR releases). It basically means that every time a pull
request (PR) is merged, a PR-labelled MATSim version is released. Their version ID is structured in the following
way: `${matsim_version_id}-PR${pull_request_id}`. The first PR-labelled version released is `14.0-PR1452`, which can be
read as _"pre-release PR1452 of MATSim 14.0"_.

The RP-labelled releases is a high-frequency (after every PR is merged), low-latency (< 10 minutes) release stream that
allows you to stay in sync with the latest features introduced to MATSim without the need of relying on the snapshot
releases (i.e. `${matsim_version_id}-SNAPSHOT`, e.g. `14.0-SNAPSHOT`).

### Why to use PR releases?

Using snapshot releases as dependencies is always risky. `14.0-SNAPSHOT` is a moving target until it gets released
as `14.0` (only then it becomes an immutable artifact). While depending on the snapshot version, you may experience
situations when something that worked once may not work (or work differently) next time, because there have been some
changes introduced to MATSim in the meantime. On the other hand, weekly releases, being immutable artifacts, are stable,
but they are not released frequently enough for developers or users to stay in sync with the very latest changes in
MATSim.

The PR releases fill the gap between these two release types. Moreover, their high frequency of releasing simplifies
analysing a potential impact of each individual PR on the project that uses MATSim.

### <a name="how-to-use-pr-releases"></a>How to use PR releases?

Since we have recently migrated our maven repository, this requires a few simple changes in `pom.xml` of any project
that depends on MATSim. As an example, please have a look at commit
[`c971f24`](https://github.com/matsim-org/matsim-maas/commit/c971f24daf311c0cedd35feb14adf0ca6a919d65) that switches the
MATSim version ID from `13.0-SNAPSHOT` to `14.0-PR1452` and changes the MATSim maven repository in
the [MATSim MaaS](https://github.com/matsim-org/matsim-maas) project.

## Weekly releases

In addition to the new PR releases, you can still use the weekly releases (released every Monday). From week 17, 2021,
we release them as non-snapshots, so their name will not be suffixed with `-SNAPSHOT` (e.g. `14.0-2021w17` instead
of `14.0-2021w17-SNAPSHOT`).

### How to use weekly releases?

If you want to use the latest weekly releases (`2021w15-SNAPSHOT` and newer), adjust the MATSim version ID and the
repository accordingly (
similar to [How to use PR releases?](#how-to-use-pr-releases)).

However, if you want to keep on using older weekly releases (`2021w14-SNAPSHOT` and older), you do not need to update
anything (the old weekly releases are available from the old snapshot repository, hosted by jFrog).

## Improved CI build pipelines

Since November 2020, we have been migrating the most time-critical continuous integration workflows to GitHub Actions.
By doing so, we are now able to:

- verify each pushed commit in 15-30 min
- release the PR-labelled and snapshot versions in 5-10 min (after merging a PR)

This should significantly improve your experiences in developing or using the new features in MATSim.
