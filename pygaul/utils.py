"""Utils methods for the package."""

import os
import re

import ee
import geetools as geetools
import httplib2


def initialize_documentation():
    """Initialize Earth Engine Python API in the context of the Documentation build.

    Warning:
        This method is only used in the documentation build and should not be used in a production environment.
        ``geetools`` need to be imported prior to import this function.
    """
    # use a saved service account key if available
    if "EARTHENGINE_SERVICE_ACCOUNT" in os.environ:
        private_key = os.environ["EARTHENGINE_SERVICE_ACCOUNT"]
        # small massage of the key to remove the quotes coming from RDT
        private_key = (
            private_key[1:-1] if re.compile(r"^'[^']*'$").match(private_key) else private_key
        )
        ee.Initialize.geetools.from_service_account(private_key)

    elif "EARTHENGINE_PROJECT" in os.environ:
        ee.Initialize(project=os.environ["EARTHENGINE_PROJECT"], http_transport=httplib2.Http())

    else:
        raise ValueError(
            "EARTHENGINE_SERVICE_ACCOUNT or EARTHENGINE_PROJECT environment variable is missing"
        )
