#!/usr/bin/env python

import json

info = {
    "client": {
        "redirect_uris": ["https://smultron.catalogix.se/authz_cb"],
        "contact": ["roland.hedberg@adm.umu.se"],
        "application_type": "web",
        "application_name": "OIC test tool",
        "register":True,
        },
    "provider": {
        "version": { "oauth": "2.0", "openid": "3.0"},
        "conf_url": "https://www.kodtest.se:8088/",
        },

    "interaction": {
        "https://www.kodtest.se:8088/authorization": ["select_form",
                {"login":"diana", "password": "krall"}],
#        "https://connect-op.heroku.com/authorizations/new": ["select_form",
#                {"_form_pick_": {"action": "/authorizations",
#                                 "class": "approve"}}],
        #        "https://connect-op.heroku.com/authorizations",
    }
}

print json.dumps(info)