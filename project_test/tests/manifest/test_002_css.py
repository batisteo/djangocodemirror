"""
Tests against manifest for CSS assets
"""
import pytest

from django.conf import settings


def test_css_empty_registry(settings, manifesto):
    """Empty registry"""
    assert manifesto.css() == settings.CODEMIRROR_BASE_CSS


def test_css_registred_empty(settings, manifesto):
    """An empty registred config"""
    manifesto.autoregister()

    assert manifesto.css('empty') == settings.CODEMIRROR_BASE_CSS


def test_css_registred_singles(settings, manifesto):
    """Explicitely registering some config"""
    manifesto.register('rst-basic') # Registred but not used
    manifesto.register('rst-with-themes')

    assert manifesto.css('rst-with-themes') == settings.CODEMIRROR_BASE_CSS+[
        settings.CODEMIRROR_THEMES['eclipse'],
        settings.CODEMIRROR_THEMES['elegant'],
    ]


@pytest.mark.parametrize('name,assets', [
    (
        'empty',
        [],
    ),
    (
        'rst-with-themes',
        [
            settings.CODEMIRROR_THEMES['eclipse'],
            settings.CODEMIRROR_THEMES['elegant'],
        ],
    ),
    (
        'rst-with-all',
        [
            settings.CODEMIRROR_THEMES['eclipse'],
            settings.CODEMIRROR_THEMES['nice_lesser_dark'],
        ],
    ),
    (
        None, # Mean all configs
        [
            settings.CODEMIRROR_THEMES['eclipse'],
            settings.CODEMIRROR_THEMES['elegant'],
            settings.CODEMIRROR_THEMES['nice_lesser_dark'],
        ],
    ),
])
def test_js_autoregister(settings, manifesto, name, assets):
    """Checking CSS assets after autoregister"""
    manifesto.autoregister()

    assert manifesto.css(name) == settings.CODEMIRROR_BASE_CSS+assets
