# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tgr_resource_inventory',
 'tgr_resource_inventory.discovery',
 'tgr_resource_inventory.orm']

package_data = \
{'': ['*']}

install_requires = \
['jmespath>=0.10.0,<0.11.0', 'ujson>=4.1.0,<5.0.0']

setup_kwargs = {
    'name': 'tgr-resource-inventory',
    'version': '0.4.2',
    'description': 'Horangi Resource Inventory module that handles all Resource related operations.',
    'long_description': None,
    'author': 'Andriano Winatra',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
