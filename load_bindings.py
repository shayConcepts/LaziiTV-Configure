# ---------------------
# load_settings.py
# Description: Loads the settings for LaziiTV
# http://shayConcepts.com
# Andrew Shay
# ---------------------

import json
import base64


def load_default_bindings():
    """
    Loads the default bindings
    """

    bindings = {
        "change_display": 68,
        "change_mode_bind": 77,
        "channel_down_bind": 65,
        "channel_up_bind": 81,
        "info_bind": 73,
        "play_pause_bind": 32,
        "previous_video": 84,
        "quit_bind": 27,
        "refresh_bind": 82,
        "skip_backward_bind": 87,
        "skip_forward_bind": 69,
        "stop_bind": 83
    }

    return bindings


def load_key_bindings():
    """
    Loads settings from key_bindings.json

    Returns
    key_bindings -- Dict. All key bindings
    """

    print "Loading Key Bindings"

    try:
        key_bindings = open("key_bindings.json", "r").read()
    except:
        key_bindings = load_default_bindings()
        open("key_bindings.json", "w").write(json.dumps(key_bindings,
                                                        indent=4,
                                                        sort_keys=True))
    else:
        key_bindings = json.loads(key_bindings)

        # Add missing/new bindings
        default_bindings = load_default_bindings()
        for key in default_bindings:
            value = default_bindings[key]
            if key not in key_bindings:
                key_bindings[key] = value

    key_bindings = json.dumps(key_bindings)
    key_bindings = key_bindings.splitlines()
    bindings_data = ""
    for line in key_bindings:
        bindings_data += line

    bindings_data = base64.b64encode(bindings_data)

    return bindings_data

