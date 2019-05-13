# This file, secrets.py, imports environment variables configured in the env file.
# Please configure that file, using the provided env_template file.
from ast import literal_eval
from os import getenv
from .config import (
    ENABLE_GOOGLE_AUTH,
    ENABLE_TWITTER_AUTH,
    ENABLE_GITHUB_AUTH,
    ENABLE_GITLAB_AUTH,
    ENABLE_BITBUCKET_AUTH,
    ENABLE_LDAP_AUTH,
    ENABLE_PAM_AUTH,
    ENABLE_GLOBUS,
    ENABLE_SAML_AUTH,
)
SECRET_KEY = getenv('SECRET_KEY')




# =============================================================================
# Social Authentication
# Set keys and secrets for social authentication methods that you have
# enabled in config.py.
# See https://singularityhub.github.io/sregistry/install.html for full details
# =============================================================================

# Twitter OAuth2
# Only required if ENABLE_TWITTER_AUTH=TRUE in config.py
if ENABLE_TWITTER_AUTH:
    SOCIAL_AUTH_TWITTER_KEY = getenv('SOCIAL_AUTH_TWITTER_KEY')
    SOCIAL_AUTH_TWITTER_SECRET = getenv('SOCIAL_AUTH_TWITTER_SECRET')

# -----------------------------------------------------------------------------
# Google OAuth2
# Only required if ENABLE_GOOGLE_AUTH=TRUE in config.py

if ENABLE_GOOGLE_AUTH:
    GOOGLE_CLIENT_FILE = '/code/.grilledcheese.json'

    # http://psa.matiasaguirre.net/docs/backends/google.html?highlight=google
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

    # The scope is not needed, unless you want to develop something new.
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE')]
    SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = literal_eval(getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS').strip('"'))
# -----------------------------------------------------------------------------
# GitHub OAuth
#http://psa.matiasaguirre.net/docs/backends/github.html?highlight=github

if ENABLE_GITHUB_AUTH:
    SOCIAL_AUTH_GITHUB_KEY = getenv('SOCIAL_AUTH_GITHUB_KEY')
    SOCIAL_AUTH_GITHUB_SECRET = getenv('SOCIAL_AUTH_GITHUB_SECRET')

# You shouldn't actually need this if we aren't using repos
# SOCIAL_AUTH_GITHUB_SCOPE = ["repo","user"]

# -----------------------------------------------------------------------------
# GitLab OAuth2
if ENABLE_GITLAB_AUTH:
    SOCIAL_AUTH_GITLAB_SCOPE = literal_eval(getenv('SOCIAL_AUTH_GITLAB_SCOPE').strip('"').strip("'"))
    SOCIAL_AUTH_GITLAB_KEY = getenv('SOCIAL_AUTH_GITLAB_KEY')
    SOCIAL_AUTH_GITLAB_SECRET = getenv('SOCIAL_AUTH_GITLAB_SECRET')


# -----------------------------------------------------------------------------
# Bitbucket OAuth2
if ENABLE_BITBUCKET_AUTH:
    SOCIAL_AUTH_BITBUCKET_OAUTH2_KEY = getenv('SOCIAL_AUTH_BITBUCKET_OAUTH2_KEY') 
    SOCIAL_AUTH_BITBUCKET_OAUTH2_SECRET = getenv('SOCIAL_AUTH_BITBUCKET_OAUTH2_SECRET')
    SOCIAL_AUTH_BITBUCKET_OAUTH2_VERIFIED_EMAILS_ONLY = getenv('SOCIAL_AUTH_BITBUCKET_OAUTH2_VERIFIED_EMAILS_ONLY').lower()=="true"

# =============================================================================
# Plugin Authentication
# Set options for authentication plugins that you have enabled in config.py
# =============================================================================

# LDAP Authentication (ldap-auth)
# Only required if 'ldap-auth' is added to PLUGINS_ENABLED in config.py

# This example assumes you are using an OpenLDAP directory
# If using an alternative directory - e.g. Microsoft AD, 389 you
# will need to modify attribute names/mappings accordingly
# See https://django-auth-ldap.readthedocs.io/en/1.2.x/index.html


# To work with OpenLDAP and posixGroup groups we need to import some things
if ENABLE_LDAP_AUTH:
    import ldap
    from django_auth_ldap.config import LDAPSearch, PosixGroupType

# The URI to our LDAP server (may be ldap:// or ldaps://)
    AUTH_LDAP_SERVER_URI = getenv('AUTH_LDAP_SERVER_URI')

# DN and password needed to bind to LDAP to retrieve user information
# Can leave blank if anonymous binding is sufficient

    AUTH_LDAP_BIND_DN = getenv('AUTH_LDAP_BIND_DN')
    AUTH_LDAP_BIND_PASSWORD = getenv('AUTH_LDAP_BIND_PASSWORD')

# Any user account that has valid auth credentials can login
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        getenv('AUTH_LDAP_USER_SEARCH_PARAMS').strip('"').strip("'"),
        ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
    )

    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
        getenv('AUTH_LDAP_GROUP_SEARCH_PARAMS').strip('"').strip("'"),
        ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)"
    )

    AUTH_LDAP_GROUP_TYPE = PosixGroupType()

    # Populate the Django user model from the LDAP directory.
    AUTH_LDAP_USER_ATTR_MAP = {
        "first_name": "givenName",
        "last_name": "sn",
        "email": "mail",
    }

    # Map LDAP group membership into Django admin flags
    AUTH_LDAP_USER_FLAGS_BY_GROUP = literal_eval(getenv('AUTH_LDAP_USER_FLAGS_BY_GROUP'))

# Globus Assocation (globus)
# Only required if 'globus' is added to PLUGINS_ENABLED in config.py
if ENABLE_GLOBUS:
    SOCIAL_AUTH_GLOBUS_KEY=getenv('SOCIAL_AUTH_GLOBUS_KEY')
    SOCIAL_AUTH_GLOBUS_USERNAME=getenv('SOCIAL_AUTH_GLOBUS_USERNAME')
    SOCIAL_AUTH_GLOBUS_SECRET=getenv('SOCIAL_AUTH_GLOBUS_SECRET')
    GLOBUS_ENDPOINT_ID=getenv('GLOBUS_ENDPOINT_ID')


# SAML Authentication (saml)
# Only required if 'saml_auth' is added to PLUGINS_ENABLED in config.py
if ENABLE_SAML_AUTH:
    AUTH_SAML_IDP = "stanford"
    AUTH_SAML_INSTITUTION = "Stanford University"