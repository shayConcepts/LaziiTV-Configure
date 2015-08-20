# ---------------------
# load_channels.py
# Description: Loads the mode and channel data for LaziiTV
# http://shayConcepts.com
# Andrew Shay
# ---------------------

import json

# List containing the names of the modes in order from channels.xml
mode_names = []
# 2 dim list containing channel names for each mode
channel_names = []
# The modes, channels, dirs in a multi dim list
video_data = []

"""
channel_data.json format

{
    "MODE ONE":[{
        "Channel One":[
            "C:\\Users\\John\\TV\\Some Show",
            "C:\\Users\\John\\TV\\Some Show"
        ],
        "Channel Two":[
            "C:\\Users\\John\\TV\\Some Show",
            "C:\\Users\\John\\TV\\Some Show"
        ]
    }],

    "MODE TWO":[{
        "Channel One":[
            "C:\\Users\\John\\TV\\Some Show"
        ],
        "Channel Two":[
            "C:\\Users\\John\\TV\\Some Show"
        ]
    }]

}

"""


def load_mode_channel_names(channel_json):
    """
    Loads modes and channels names

    Keyword arguments:
    channel_json -- String. The channel json
    """
    global mode_names, channel_names

    print("\tLoading Mode Channel Names")

    for mode in channel_json:
        # mode is a dict
        mode_name = mode.keys()[0]
        mode_names.append(mode_name)

        temp_channels = []
        for channel in mode[mode_name]:
            channel_name = channel.keys()[0]
            temp_channels.append(channel_name)
        channel_names.append(temp_channels)

    print("\tSuccess")


def load_folders(channel_json):
    """
    Reads in the folders

    Keyword arguments:
    channel_json -- String. The channel json
    """
    global mode_names, channel_names, video_data

    print("\tLoading Folders")

    for mode in channel_json:
        modes_channels = []
        mode_name = mode.keys()[0]
        mode_names.append(mode_name)

        for channel in mode[mode_name]:
            channels_folders = []
            channel_name = channel.keys()[0]
            current_channel = channel[channel_name]

            for folder in current_channel:
                folder = folder.replace("\\\\", "\\")
                channels_folders.append(folder)
            modes_channels.append(channels_folders)
        video_data.append(modes_channels)

    print("\tSuccess")


def load_channel_data():
    """ Loads channel and mode data from channel_data.json """

    json_string = open("channel_data.json", "r").read()
    channel_json = json.loads(json_string)

    print("Loading Channel Data")
    load_mode_channel_names(channel_json)
    load_folders(channel_json)
    print("Success -- Channel Data Loaded")

if __name__ == "__main__":
    load_channel_data()
    print(mode_names)
    print()
    print(channel_names)
    print()
    print(video_data)
