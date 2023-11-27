import tarfile
import sys
import json
import io
import readline

class Node:
    def __init__(self, name, is_file=False):
        self.is_file=is_file
        self.name = name
        self.children = {}
    def __str__(self):
        if self.is_file:
            return self.name
        return f"{self.name}/"

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")

    def add_path(self, path, is_file=False):
        current_node = self.root
        components = path.split('/')[1:]  # Split path and remove empty first component

        for component in components:
            if component not in current_node.children:
                current_node.children[component] = Node(component, is_file)
            current_node = current_node.children[component]

    def _traverse(self, node, depth=0):
        if node:
            print(' ' * depth + node.name)
            for child in node.children.values():
                self._traverse(child, depth + 2)

    def display_tree(self):
        self._traverse(self.root)
    
    def _get_leafs_under_root(self, root_path):
        current_node = self.root
        components = root_path.split('/')[1:]  # Split path and remove empty first component

        # Traverse to the specified root path
        for component in components:
            if component in current_node.children:
                current_node = current_node.children[component]

        # Collect leafs under the specified root
        leafs = []
        for leaf in current_node.children:
            leafs.append(current_node.children[leaf])
        #self._collect_leafs(current_node, root_path, leafs)
        return leafs

    def _collect_leafs(self, node, path, leafs):
        if node:
            for child_name, child_node in node.children.items():
                child_path = f"{path}/{child_name}"
                if not child_node.children:
                    leafs.append(child_path + '/')
                else:
                    self._collect_leafs(child_node, child_path, leafs)

    def print_leafs_under_root(self, root_path):
        leafs = self._get_leafs_under_root(root_path)
        print("-----")
        for leaf in leafs:
            print(leaf)
        print("-----")

class Handler:
    def __init__(self):
        self.file_system = FileSystemTree()
    
    def handle_layer(self, tar, filename):
        try:
            for member in tar.getmembers():
                if member.name == filename:
                    content = tar.extractfile(member)
                    if content:
                        self.display_tar_content(content)  # Display content (change the operation as needed)
                    break
        except tarfile.TarError as e:
            print(f"Error: {e}")

    def display_tar_content(self, tar_member):
        try:
            with tarfile.open(fileobj=io.BytesIO(tar_member.read()), mode='r') as tar:
                for member in tar.getmembers():
                    self.file_system.add_path(f"/{member.name}", member.isfile())
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the path to a tarball.")
        sys.exit(1)

    tarball_path = sys.argv[1]
    handler = Handler()
    handler.process_manifest(tarball_path)
    while(True):
        fs_path = input("ls ")
        if fs_path:
            handler.file_system.print_leafs_under_root(fs_path)
        else:
            break

    