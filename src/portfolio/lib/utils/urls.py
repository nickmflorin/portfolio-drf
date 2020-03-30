from django.conf import settings
from urllib.parse import urlsplit, urlunsplit


__all__ = (
    'make_url_absolute',
)


def make_url_absolute(url, request=None, domain=None, scheme=None):
    """
    Keep this utility here temporarily.  We thought we would need it but it
    turns out we may not, but does not hurt to have temporarily nonetheless.
    """
    parts = urlsplit(url)
    if scheme is None:
        if request:
            scheme = "http%s" % ("s" if request.is_secure() else "")
        else:
            scheme = parts.scheme

    if domain:
        if '://' in domain:
            raise ValueError(
                "Domains should not contain a scheme "
                "(i.e. www.example.com not http://www.example.com/"
            )
        domain = domain.rstrip('/')

    if parts.scheme and parts.netloc:
        return url
    if parts.netloc:
        domain = parts.netloc
    elif domain is None:
        if request:
            domain = request.get_host()
        else:
            domain = urlsplit(settings.SITE_URL).netloc
    return urlunsplit((scheme, domain, parts.path, parts.query, parts.fragment))
