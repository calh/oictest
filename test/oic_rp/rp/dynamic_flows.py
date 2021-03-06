from jwkest import BadSignature
from oic.oic.message import AtHashError
from oic.oic.message import CHashError

__author__ = 'roland'

MODE = {}

FLOWS = {
    "RP-Webfinger-url": {
        "flow": [{"action": "discover", "args": {}}],
        "desc": "Can Discover Identifiers using URL Syntax"
    },
    "RP-Webfinger-acct": {
        "flow": [{"action": "discover", "args": "acct:%s@localhost:8080"}],
        "desc": "Can Discover Identifiers using acct Syntax"
    },
    "RP-Discover-01": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}}],
        "desc": "Uses openid-configuration Discovery Information"
    },
    "RP-Registration-01": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration", "args": {}}],
        "desc": "Uses Dynamic Registration"
    },
    # Can Make Request with ? Response Type
    "rp-rtyp-code": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration", "args": {}},
                 {"action": "authn_req",
                  "args": {"scope": "openid", "response_type": ["code"]}}],
        "desc": "Can Make Request with 'code' Response Type"
    },
    "rp-rtyp-idt": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration",
                  "args": {"id_token_signed_response_alg": "RS256"}},
                 {"action": "authn_req",
                  "args": {"scope": "openid", "response_type": ["id_token"]}}],
        "desc": "Can Make Request with 'id_token' Response Type"
    },
    "rp-rtyp-idttoken": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration",
                  "args": {"id_token_signed_response_alg": "RS256"}},
                 {"action": "authn_req",
                  "args": {"scope": "openid",
                           "response_type": ["id_token", "token"]}}],
        "desc": "Can Make Request with 'id_token token' Response Type"
    },
    "rp-rmod-form": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration",
                  "args": {"id_token_signed_response_alg": "RS256"}},
                 {"action": "authn_req",
                  "args": {"scope": "openid",
                           "response_type": ["id_token", "token"],
                           "response_mode": ["form_post"]}}],
        "desc": "Can Make Request with 'id_token token' Response Type"
    },
    ### Can Make Access Token Request with ? Authentication
    # Client_secret_basic
    "RP-TokenEndpoint-client_secret_basic": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration", "args": {}},
                 {"action": "authn_req",
                  "args": {"scope": "openid", "response_type": ["code"]}},
                 {"action": "token_req",
                  "args": {"authn_method": "client_secret_basic"}}],
        "desc": "Can Make Access Token Request with 'client_secret_basic' "
                "Authentication"
    },
    # client_secret_jwt
    "RP-TokenEndpoint-client_secret_jwt": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration",
                  "args": {"token_endpoint_auth_method": "client_secret_jwt"}},
                 {"action": "authn_req",
                  "args": {"scope": "openid", "response_type": ["code"]}},
                 {"action": "token_req",
                  "args": {"authn_method": "client_secret_jwt"}}
        ],
        "desc": "Can Make Access Token Request with 'client_secret_jwt' "
                "Authentication"
    },
    # client_secret_post
    "RP-TokenEndpoint-client_secret_post": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"token_endpoint_auth_method": "client_secret_post"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req",
             "args": {"authn_method": "client_secret_post"}}
        ],
        "desc": "Can Make Access Token Request with 'client_secret_post' "
                "Authentication"
    },
    # private_key_jwt
    "RP-TokenEndpoint-private_key_jwt": {
        "flow": [{"action": "discover", "args": {}},
                 {"action": "provider_info", "args": {}},
                 {"action": "registration",
                  "args": {"token_endpoint_auth_method": "private_key_jwt",
                           "jwks_uri": "https://localhost:8088/static/jwk.json"}},
                 {"action": "authn_req",
                  "args": {"scope": "openid", "response_type": ["code"]}},
                 {"action": "token_req",
                  "args": {"authn_method": "private_key_jwt"}}
        ],
        "desc": "Can Make Access Token Request with 'private_key_jwt' "
                "Authentication"
    },
    ### === Accept Valid ? ID Token Signature	===
    # Asymmetric
    "RP-IdToken-Asym-Sig": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"id_token_signed_response_alg": "RS256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]}}
        ],
        "desc": "Accept Valid Asymmetric ID Token Signature"
    },
    "RP-IdToken-Asym-Sig-2": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/RS256/_/_/normal"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]}}
        ],
        "desc": "Accept Valid Asymmetric ID Token Signature"
    },
    # Symmetric
    "RP-IdToken-Sym-Sig": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"id_token_signed_response_alg": "HS256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]}}
        ],
        "desc": "Accept Valid Symmetric ID Token Signature"
    },
    ### === Reject Invalid ? ID Token Signature ===
    # Asymmetric
    "rp-alg-rs256": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/idts/normal"}},
            {"action": "registration",
             "args": {"id_token_signed_response_alg": "RS256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]},
             "error": BadSignature}
        ],
        "desc": "Reject Invalid Asymmetric ID Token Signature"
    },
    "rp-alg-es256": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/idts/normal"}},
            {"action": "registration",
             "args": {"id_token_signed_response_alg": "ES256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]},
             "error": BadSignature}
        ],
        "desc": "Reject Invalid Asymmetric ID Token Signature"
    },
    # Symmetric
    "rp-alg-hs256": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/idts/normal"}},
            {"action": "registration",
             "args": {"id_token_signed_response_alg": "HS256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]},
             "error": BadSignature}
        ],
        "desc": "Reject Invalid Symmetric ID Token Signature"
    },
    ### === Can Request and Use ? ID Token Response ===
    # Signed and Encrypted
    # *signed is already tested*
    "RP-IdToken-SigEnc": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {
                 "id_token_signed_response_alg": "HS256",
                 "id_token_encrypted_response_alg": "RSA1_5",
                 "id_token_encrypted_response_enc": "A128CBC-HS256",
                 "jwks_uri": None}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]}}
        ],
        "desc": "Can Request and Use Signed and Encrypted ID Token Response"
    },
    # Unsigned
    "RP-IdToken-none": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"id_token_signed_response_alg": "none"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}}
        ],
        "desc": "Can Request and Use unSigned ID Token Response"
    },
    # ? at_hash when code Flow Used
    # Reject incorrect
    "rp-idt-c_hash": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/ch/normal"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid",
                      "response_type": ["code", "id_token"]},
             "error": CHashError}
        ],
        "desc": "Rejects incorrect c_hash when Code Flow is Used"
    },
    # Accept correct
    "RP-CHash-correct": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid",
                      "response_type": ["code", "id_token"]}},
            {"action": "token_req", "args": {}},
        ],
        "desc": "Verifies correct c_hash when Code Flow is Used"
    },
    # ? at_hash when Implicit Flow Used
    # Reject incorrect
    "rp-idt-at_hash": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/ath/normal"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid",
                      "response_type": ["id_token", "token"]},
             "error": AtHashError},
        ],
        "desc": "Rejects incorrect at_hash when Implicit Flow is Used"
    },
    # Accept correct
    "RP-AtHash-correct": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid",
                      "response_type": ["id_token", "token"]}},
        ],
        "desc": "Verifies correct at_hash when Code Implicit is Used"
    },
    # Can Use Elliptic Curve ID Token Signatures
    "RP-IdToken-Elliptic-Sig": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"id_token_signed_response_alg": "ES256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["id_token"]}}
        ],
        "desc": "Can Use Elliptic Curve ID Token Signatures"
    },
    "RP-IdToken-claims": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid",
                      "claims": {"id_token": {"name": None}},
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}}
        ],
        "desc": "Can Request and Use Claims in id_token using the 'claims' "
                "request parameter"
    },
    #
    "rp-ui-hdr": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}}
        ],
        "desc": "Accesses UserInfo Endpoint with Header Method"
    },
    "rp-ui-body": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_body", "method": "post"}}
        ],
        "desc": "Accesses UserInfo Endpoint with Header Method"
    },
    #
    "RP-userinfo-json": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}}
        ],
        "desc": "Can Request and Use JSON UserInfo Response"
    },
    #
    "RP-userinfo-Sig": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"userinfo_signed_response_alg": "RS256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}}
        ],
        "desc": "Can Request and Use Signed UserInfo Response"
    },
    "RP-userinfo-Enc": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {
                 "userinfo_signed_response_alg": "none",
                 "userinfo_encrypted_response_alg": "RSA1_5",
                 "userinfo_encrypted_response_enc": "A128CBC-HS256",
                 "jwks_uri": None
             }},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}}
        ],
        "desc": "Can Request and Use Encrypted UserInfo Response"
    },
    "RP-userinfo-Sig+Enc": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {
                 "userinfo_signed_response_alg": "HS256",
                 "userinfo_encrypted_response_alg": "RSA1_5",
                 "userinfo_encrypted_response_enc": "A128CBC-HS256",
                 "jwks_uri": None
             }},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}}
        ],
        "desc": "Can Request and Use Signed and Encrypted UserInfo Response"
    },
    # ==== Can Use request_uri Request Parameter with ? Request ===
    # Unsigned
    "RP-request_uri-Unsigned": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"request_object_signing_alg": "none"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ],
        "desc": "Can Use request_uri Request Parameter with Unsigned Request"
    },
    # Signed
    "RP-request_uri-Sig": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {"request_object_signing_alg": "RS256"}},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ],
        "desc": "Can Use request_uri Request Parameter with Signed Request"
    },
    # Encrypted
    "RP-request_uri-Enc": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {
                 "request_object_signing_alg": "none",
                 "request_object_encryption_alg": "RSA1_5",
                 "request_object_encryption_enc": "A128CBC-HS256"
             }},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ],
        "desc": "Can Use request_uri Request Parameter with Encrypted Request"
    },
    # Signed+Encrypted
    "RP-request_uri-Sig+Enc": {
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration",
             "args": {
                 "request_object_signing_alg": "RS256",
                 "request_object_encryption_alg": "RSA1_5",
                 "request_object_encryption_enc": "A128CBC-HS256"
             }},
            {"action": "authn_req",
             "args": {"scope": "openid", "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ],
        "desc": "Can Use request_uri Request Parameter with Signed and "
                "Encrypted Request"
    },
    #
    # ==== Requesting UserInfo Claims with ? ====
    "RP-userinfo-scope": {
        "desc": "Accesses UserInfo Endpoint with Header Method",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid", "profile"],
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}}
        ]
    },
    "RP-userinfo-claims": {
        "desc": "Accesses UserInfo Endpoint with Header Method",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info", "args": {}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid"],
                      "response_type": ["code"],
                      "claims": {"userinfo": {"name": {"essential": True}}}}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}}
        ]
    },
    "RP-claims-aggregated": {
        "desc": "Handles aggregated user information",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/_/aggregated"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid", "profile"],
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}},
        ]
    },
    "RP-claims-distributed": {
        "desc": "Handles distributed user information",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/_/distributed"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid", "profile"],
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
            {"action": "userinfo_req",
             "args": {"authn_method": "bearer_header"}},
            {"action": "fetch_claims", "args": {}}
        ]
    },
    "RP-issuer-not-matching-config": {
        "desc": "Rejects Discovered issuer Not Matching openid-configuration "
                "Path Prefix",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/isso/normal"},
             "error": Exception}
        ]
    },
    "RP-idt-iss": {
        "desc": "Rejects Discovered issuer Not Matching ID Token iss",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/issi/normal"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid", "profile"],
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ]
    },
    "RP-idt-sub": {
        "desc": "Reject ID Token without sub claim",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/sub/normal"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid", "profile"],
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ]
    },
    "RP-idt-aud": {
        "desc": "Reject ID Token with invalid aud claim",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/aud/normal"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid", "profile"],
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ]
    },
    "RP-idt-iat": {
        "desc": "Reject ID Token without iat claim",
        "flow": [
            {"action": "discover", "args": {}},
            {"action": "provider_info",
             "args": {"issuer": "https://localhost:8080/_/_/iat/normal"}},
            {"action": "registration", "args": {}},
            {"action": "authn_req",
             "args": {"scope": ["openid", "profile"],
                      "response_type": ["code"]}},
            {"action": "token_req", "args": {}},
        ]
    }
    # ==== Support OP ? Key Rollover ====
    # Signing
    # Encryption
    #
    # ==== ID Spoofing ====
    # ==== Sub Claims Spoofing ====
    # ==== Redirect URI Manipulation ====
}
