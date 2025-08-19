"""Pytest session configuration."""

import pytest_gee


def pytest_configure():
    pytest_gee.init_ee_from_service_account()
