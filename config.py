PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "b1a2c3d4e5f60718293a4b5c6d7e8f90",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "cloudflare.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "cded575c304da847fe5378fd42834441"
