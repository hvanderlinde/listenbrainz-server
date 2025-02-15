import string
import random

import orjson
from flask import current_app, request
from flask_login import current_user

from listenbrainz.webserver.views.views_utils import get_current_spotify_user, get_current_youtube_user, \
    get_current_critiquebrainz_user, get_current_musicbrainz_user

REJECT_LISTENS_WITHOUT_EMAIL_ERROR = \
    'The listens were rejected because the user does not has not provided an email. ' \
    'Please visit https://musicbrainz.org/account/edit to add an email address. ' \
    'Read the blog post at https://blog.metabrainz.org/?p=8915 to understand why ' \
    'we need your email.'


def generate_string(length):
    """Generates random string with a specified length."""
    return ''.join([random.SystemRandom().choice(
        string.ascii_letters + string.digits
    ) for _ in range(length)])


def sizeof_readable(num, suffix='B'):
    """ Converts the size in human readable format """

    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yb', suffix)


def reformat_date(value, fmt="%b %d, %Y"):
    return value.strftime(fmt)


def reformat_datetime(value, fmt="%b %d, %Y, %H:%M %Z"):
    return value.strftime(fmt)


def get_global_props():
    """Generate React props that should be available on all html pages.
    These are passed into the template context on website blueprints as
    an encoded json string.
    The props include:
     - information about the current logged in user
     - auth details for spotify and youtube if the current user has connected them
     - sentry dsn
     - API url for frontned to connect to.
    """
    current_user_data = {}
    if current_user.is_authenticated:
        current_user_data = {
            "id": current_user.id,
            "name": current_user.musicbrainz_id,
            "auth_token": current_user.auth_token,
        }

    sentry_config = current_app.config.get("LOG_SENTRY", {})

    props = {
        "api_url": current_app.config["API_URL"],
        "sentry_dsn": sentry_config.get("dsn"),
        "current_user": current_user_data,
        "spotify": get_current_spotify_user(),
        "youtube": get_current_youtube_user(),
        "critiquebrainz": get_current_critiquebrainz_user(),
        "musicbrainz": get_current_musicbrainz_user(),
        "sentry_traces_sample_rate": sentry_config.get("traces_sample_rate", 0.0),
        "user_preferences": {},
    }
    return orjson.dumps(props).decode("utf-8")


def parse_boolean_arg(name, default=None):
    from listenbrainz.webserver.errors import APIBadRequest
    value = request.args.get(name)
    if not value:
        return default

    value = value.lower()
    if value not in ["true", "false"]:
        raise APIBadRequest("Invalid %s argument: %s. Must be 'true' or 'false'" % (name, value))

    return True if value == "true" else False
