---
layout: default
title: Extensions
---

## MATSim Extensions

MATSim offers several extensions which enhance the functionality with additional features. The following list gives an overview of the currently available extensions.

<!-- To use an extension, you can either download the latest stable and tested release of the extension, or download a (probably) unstable and untested nightly build of the extension. -->

For a usage guide on how to use MATSim extensions in general, see [here](/docs/extensions).

For the usage of a specific extension, please check the extension's documentation.

If you want to contribute an extension, please see [here](/docs/contributing/extensions).

---

### Availability: Contrib

Please see our [Javadoc page](/javadoc).

Please note that these extensions are usually maintained and provided by single members of the community. The MATSim core development team cannot make any guarantee that these extensions will be kept up-to-date and compatible with future releases, instead the maintainers themselves are responsible for this task.

For maintainers: Please use `src/main/javadoc/overview.html` inside your contrib for an introductory description of your contrib.  See, e.g., the emissions contrib for an example.

---

### Availability: External

<table class="extension-table">

  <tr>
    <th>Title</th><th>Maintainer</th><th>Description</th>
  </tr>

  {% for ext in site.data.extensions-external %}
    <tr>
        <td> <a href="{{ext.docs}}">{{ ext.name }} </a> </td>
        <td> {{ ext.maintainer }} </td>
        <td> {{ ext.description }} </td>
    </tr>
  {% endfor %}

</table>

Please note that these extensions are usually maintained and provided by single members of the community. The MATSim core development team cannot make any guarantee that these extensions will be kept up-to-date and compatible with future releases, instead the maintainers themselves are responsible for this task.


