###Dropbox Uploader

Dropbox uploader is a Python __script__ wich can be used to upload any kind of file to DropBox.
This sript does work with the API v2.

###Getting started

First, clone the repository using git:

```
git clone https://github.com/eduardogpg/dropbox_uploader.git
```

Save your _ACCESS TOKEN_ in a environment variables. The access token can be obtained after you have created your application in the follow <a href="https://www.dropbox.com/developers", target="_blank"> link </a>

Open the script and replace ```<ACCESS_TOKEN_DROPBOX>```for the name of your environment variables.

install DropBox, using:

```
pip install dropbox
```

###Usage

```
python dropbox_uploader.py path_file
```

```
python dropbox_uploader.py path_file dest_path
```

> If we dont especify the dest_path the default will be the same route (path_file)