# -----------------------------------
#     app.py
#     Author: Andrew Shay
#     Created: June 10 2012
#     Description: The Flask server that powers LaziiTV Configure
# -----------------------------------


from flask import render_template
from flask import request
from flask import url_for
from flask import Flask
import multiprocessing
'''
import pygtk
pygtk.require('2.0')
import gtk
'''
import thread
import base64
import json
import webbrowser
import subprocess
import sys
import Tkinter as tk
import tkFileDialog
app = Flask(__name__)

files = None

# The version of LaziiTV that will be installed
version = "1.0.0"

'''
class FileChooserProcess(multiprocessing.Process):

    def __init__(self, results):
        multiprocessing.Process.__init__(self)
        self.results = results

    def run(self):
        self.dialog = gtk.FileChooserDialog("Open..",
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        self.dialog.set_select_multiple(True)
        self.dialog.set_default_response(gtk.RESPONSE_OK)
        self.response = self.dialog.run()

        if self.response == gtk.RESPONSE_OK:
            self.results.put(self.dialog.get_filenames())
        elif self.response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
'''


def open_link(url):
    """
    Launches the URL in a web browser

    Keyword Arguments:
    url -- String. URL to launch

    Returns:
    True -- Browser opened
    False -- Browser not opened
    """

    try:
        webbrowser.open(url, new=2)
    except:
        return False

    return True


@app.route('/launch_laziitv/', methods=['POST'])
def launch_laziitv():
    subprocess.Popen("laziitv.exe", shell=True,
                     stdin=None,
                     stdout=None,
                     stderr=None,
                     close_fds=True)

    return "Success"


@app.route('/launch_link/', methods=['POST'])
def launch_link():
    url = request.form["url"]
    url = base64.b64decode(url)
    open_link(url)

    return "Success"


@app.route('/add_folder/', methods=['GET'])
def add_folder():

    try:
        saved_path = open("saved_path.ini", "r").read()
    except:
        saved_path = "C:\\"
    root = tk.Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()
    file_path = tkFileDialog.askdirectory(initialdir=saved_path)
    root.destroy()
    try:
        if file_path == "":
            open("saved_path.ini", "w").write(saved_path)
        else:
            open("saved_path.ini", "w").write(file_path)
    except:
        pass
    print("FILEPATH:" + file_path)

    """
    results = multiprocessing.Queue()
    f = FileChooserProcess(results)
    f.start()
    server_port = results.get()
    print("PPRT:" + str(server_port))
    """

    return file_path


@app.route('/channel_data/', methods=['GET'])
def channel_data():
    channel_data = open("channel_data.json", "r").read()
    channel_data = channel_data.replace("//", "/")
    return channel_data


@app.before_request
def before_request():
    """
    Performs a set of steps as a precursor to each route requested.
    """
    # create database session object
    pass


@app.teardown_request
def teardown_request(exception):
    """
    Closes the database connection after response is constructed.
    """
    pass


@app.route('/', methods=['GET'])
def index():
    try:
        json_data = open("channel_data.json", "r").read()
    except:
        channel_data = "[]"
    else:
        json_data = json_data.replace("//", "/")
        json_data = json_data.splitlines()
        channel_data = ""
        for line in json_data:
            channel_data += line

    channel_data = base64.b64encode(channel_data)
    return render_template('channels.html', channel_data=channel_data)


@app.route('/settings/', methods=['GET'])
def get_settings():
    file_extensions = open("file_extensions.json", "r").read()
    file_extensions = file_extensions.splitlines()
    extensions_data = ""
    for line in file_extensions:
        extensions_data += line

    extensions_data = base64.b64encode(extensions_data)

    key_bindings = open("key_bindings.json", "r").read()
    key_bindings = key_bindings.splitlines()
    bindings_data = ""
    for line in key_bindings:
        bindings_data += line

    bindings_data = base64.b64encode(bindings_data)

    return render_template('settings.html', bindings_data=bindings_data, extensions_data=extensions_data)


@app.route('/how/', methods=['GET'])
def how():
    return render_template('how.html')


@app.route('/about/', methods=['GET'])
def about():
    global version
    return render_template('about.html', version=version)


@app.route('/save_channels/', methods=['POST'])
def save_channels():
    channel_data = request.form["channelData"]
    channel_data = base64.b64decode(channel_data)
    channel_data = channel_data.replace("\\", "/")

    # Must reload it in order to pretty print
    channel_data = json.loads(channel_data)
    channel_data = json.dumps(channel_data, sort_keys=True, indent=4, separators=(',', ': '))
    open("channel_data.json", "w").write(channel_data)
    return "Success"


@app.route('/save_extensions/', methods=['POST'])
def save_extensions():
    extension_data = request.form["extensionData"]
    extension_data = base64.b64decode(extension_data)

    # Must reload it in order to pretty print
    extension_data = json.loads(extension_data)
    extension_data = json.dumps(extension_data, sort_keys=True, indent=4, separators=(',', ': '))
    open("file_extensions.json", "w").write(extension_data)
    return "Success"


@app.route('/save_bindings/', methods=['POST'])
def save_bindings():
    bindings_data = request.form["bindingsData"]
    bindings_data = base64.b64decode(bindings_data)

    # Must reload it in order to pretty print
    bindings_data = json.loads(bindings_data)
    bindings_data = json.dumps(bindings_data, sort_keys=True, indent=4, separators=(',', ': '))
    open("key_bindings.json", "w").write(bindings_data)
    return "Success"

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)
    print("Past")
