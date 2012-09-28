#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Takes the output of the build step and turns it into a compressed
archive ready for distribution.

This script assumes the build script has been run to compile the add-in.
It zips up all files required for the add-in installation and places the
result in out/vs_addin/vs_addin.tgz.
"""

import os
import re
import fileinput
import win32api
import shutil
import tarfile
import zipfile
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Checkout root
ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# Root output directory.
BUILD_DIR = os.path.join(ROOT, 'out', 'vs_addin')

# Directory that contains the build assemblies.
ASSEMBLY_DIRECTORY = os.path.join(BUILD_DIR, 'Debug')

# Directory containing static installer resources.
RESOURCE_DIRECTORY = os.path.join(SCRIPT_DIR, 'InstallerResources')

# Base name of the final zip file.
OUTPUT_NAME = os.path.join(BUILD_DIR, 'vs_addin.tgz')

# AddIn metadata file path. We will modify this with the version #.
ADDIN_METADATA = os.path.join(RESOURCE_DIRECTORY, 'NativeClientVSAddIn.AddIn')

# AddIn dll file path. We will obtain our add-in version from this.
ADDIN_ASSEMBLY = os.path.join(ASSEMBLY_DIRECTORY, 'NativeClientVSAddIn.dll')

# Regex list to exclude from the archive. If a file path matches any of the
# expressions during a call to AddFolderToArchive it is excluded from the
# archive file.
EXCLUDES = [
    r'\.svn', # Exclude .svn directories.
    r'examples\\.*\\chrome_data',
    r'examples\\.*\\Debug',
    r'examples\\.*\\newlib',
    r'examples\\.*\\win',
    # Exclude .AddIn file for now since we need to modify it with version info.
    re.escape(ADDIN_METADATA)]

# List of source/destination pairs to include in archive file.
FILE_LIST = [
  (ADDIN_ASSEMBLY, ''),
  (os.path.join(ASSEMBLY_DIRECTORY, 'NaCl.Build.CPPTasks.dll'), 'NaCl')]


def AddFolderToArchive(path, archive):
  """Adds an entire folder and sub folders to an open archive object.

  The archive must already be open and it is not closed by this function.

  Args:
    path: Folder to add.
    archive: Already open archive file.

  Returns:
    Nothing.
  """
  # Ensure the path ends in trailing slash.
  path = path.rstrip("/\\") + "\\"
  for dir_path, dir_names, files in os.walk(path):
    for file in files:
      read_path = os.path.join(dir_path, file)

      # If the file path matches an exclude, don't include it.
      if any(re.search(expr, read_path) for expr in EXCLUDES):
        continue

      zip_based_dir = dir_path[len(path):]
      write_path = os.path.join(zip_based_dir, file)
      WriteFileToArchive(archive, read_path, write_path)


def AddVersionModifiedAddinFile(archive):
  """Modifies the .AddIn file with the build version and adds to the zip.

  The version number is obtained from the NativeClientAddIn.dll assembly which
  is built during the build process.

  Args:
  archive: Already open archive file.
  """
  info = win32api.GetFileVersionInfo(ADDIN_ASSEMBLY, "\\")
  ms = info['FileVersionMS']
  ls = info['FileVersionLS']
  version = "[%i.%i.%i.%i]" % (
      win32api.HIWORD(ms), win32api.LOWORD(ms),
      win32api.HIWORD(ls), win32api.LOWORD(ls))
  print "\nNaCl VS Add-in Build version: %s\n" % (version)

  metadata_filename = os.path.basename(ADDIN_METADATA)
  modified_file = os.path.join(ASSEMBLY_DIRECTORY, metadata_filename)

  # Copy the metadata file to new location and modify the version info.
  with open(ADDIN_METADATA, 'r') as source_file:
    with open(modified_file, 'w') as dest_file:
      for line in source_file:
        dest_file.write(line.replace("[REPLACE_ADDIN_VERSION]", version))

  WriteFileToArchive(archive, modified_file, metadata_filename)


def Error(msg):
  sys.stderr.write(msg + '\n')
  sys.exit(1)


def WriteFileToArchive(archive, filename, archive_name):
  print 'Adding: %s' % archive_name
  archive_name = os.path.join('vs_addin', archive_name)
  archive.add(filename, archive_name)


def main():
  if not os.path.exists(BUILD_DIR):
    Error("build dir not found: %s" % BUILD_DIR)

  archive = tarfile.open(OUTPUT_NAME, 'w:gz')
  for source_dest in FILE_LIST:
    file_name = os.path.basename(source_dest[0])
    dest = os.path.join(source_dest[1], file_name)
    WriteFileToArchive(archive, source_dest[0], dest)
  AddFolderToArchive(RESOURCE_DIRECTORY, archive)
  AddVersionModifiedAddinFile(archive)
  archive.close()


if __name__ == '__main__':
  main()
