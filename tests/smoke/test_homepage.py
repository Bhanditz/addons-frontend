"""Smoke tests for addons-frontend docker image."""

import pytest


@pytest.fixture
def firefox_options(firefox_options):
    """Set up Firefox options."""
    firefox_options.add_argument("-headless")
    firefox_options.add_argument('-foreground')
    return firefox_options


@pytest.mark.nondestructive
def test_hidden_comment_is_found(base_url, selenium):
    """Test hidden element is found."""
    selenium.get(base_url)
    assert "<!-- Godzilla of browsers -->" in selenium.page_source
