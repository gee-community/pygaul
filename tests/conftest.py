"""Pytest session configuration."""

import pytest_gee


def pytest_configure():
    """Initialize GEE from service account."""
    pytest_gee.init_ee_from_service_account()
