#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import dropbox

ACCESS_TOKEN = os.environ['ACCESS_TOKEN_DROPBOX']
CHUNK_SIZE = 4 * 1024 * 1024

def upload_common_file(dbx, file_path, dest_path):
  with open(file_path, "rb") as f:
    dbx.files_upload(f.read(), dest_path, mute=True)

def upload_big_file(dbx, file_path, dest_path, file_size):
  file = open(file_path)
  upload_session_start_result = dbx.files_upload_session_start(file.read(CHUNK_SIZE))
  cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id,
                                                    offset= file.tell())
        
  commit = dropbox.files.CommitInfo(path=dest_path)
  while file.tell() < file_size:
    if ((file_size - file.tell() ) <= CHUNK_SIZE):
      dbx.files_upload_session_finish(file.read(CHUNK_SIZE), cursor, commit)
    else:
      dbx.files_upload_session_append(file.read(CHUNK_SIZE),
                                          cursor.session_id,
                                          cursor.offset)
      cursor.offset = file.tell()

def upload_file(file_path, dest_path=''):
  if not os.path.exists(file_path):
    raise Exception("File {} does not exist".format(file_path))

  file_size = os.path.getsize(file_path)
  dest_path = dest_path if dest_path else "/{}".format(file_path)
  dbx = dropbox.Dropbox(ACCESS_TOKEN)

  if file_size <= CHUNK_SIZE:
    upload_common_file(dbx, file_path, dest_path)
  else:
    upload_big_file(dbx, file_path, dest_path, file_size)

  print("Done!")

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print("It`s necessary to specify the file to upload.")

  dest_path = '' if len(sys.argv) == 2 else sys.argv[2]
  upload_file(sys.argv[1], dest_path)
