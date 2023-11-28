#Copyright (c) 2023, Teemu Tallskog
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

import tarfile
import json
import io
from dockerless_fs.file_system import FileSystem

class TarHandler:
    def __init__(self):
        self.file_system = FileSystem()
    
    def handle_layer(self, tar, filename):
        try:
            for member in tar.getmembers():
                if member.name == filename:
                    content = tar.extractfile(member)
                    if content:
                        self.map_tar_content(content)  # Display content (change the operation as needed)
                    break
        except tarfile.TarError as e:
            print(f"Error: {e}")

    def map_tar_content(self, tar_member):
        try:
            with tarfile.open(fileobj=io.BytesIO(tar_member.read()), mode='r') as tar:
                for member in tar.getmembers():
                    try:
                        content = tar.extractfile(member)
                        if content and not content.readable():
                            content = None
                        elif content:
                            content = content.read()
                        else:
                            content = None
                    except:
                        content = None
                    self.file_system.add_path(f"/{member.name}", member, content=content)
        except tarfile.TarError as e:
            print(f"Error: {e}")

    def process_manifest(self, tarball_path):
        try:
            with tarfile.open(tarball_path, 'r') as tar:
                try:
                    manifest_file = tar.extractfile("manifest.json")
                    if manifest_file:
                        manifest_data = json.load(manifest_file)
                        layers = manifest_data[0].get('Layers', [])
                        for layer in layers:
                            self.handle_layer(tar, layer)
                except tarfile.TarError as e:
                    print(f"Error: {e}")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
        except tarfile.TarError as e:
            print(f"Error: {e}")