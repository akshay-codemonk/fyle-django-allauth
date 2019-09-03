"""
django-allauth provider.py
"""

from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class FyleAccount(ProviderAccount):
    pass


class FyleProvider(OAuth2Provider):
    """
    Fyle Provider class
    """
    id = 'fyle'
    name = 'Fyle'
    account_class = FyleAccount

    def extract_uid(self, data):
        return str(data['data'][0]['id'])

    def extract_common_fields(self, data):
        return dict(email=data.get('employee_email'),
                    name=data.get('full_name'))

    def get_default_scope(self):
        scope = ['read', 'write', ]
        return scope


providers.registry.register(FyleProvider)
provider_classes = [FyleProvider]
