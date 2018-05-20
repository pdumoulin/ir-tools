
import os
import base64

class Librarian(object):

    directory = None

    def __init__(self, library_dir):
        if os.path.isdir(library_dir):
            self.directory = library_dir
        else:
            raise Exception('%s is not a directory!' % library_dir)

    def read(self, remote, button):
        remote_dir = os.path.join(self.directory, remote)
        if not os.path.isdir(remote_dir):
            raise Exception('dir "%s" does not exist!' % remote_dir)

        button_file = os.path.join(remote_dir, button)
        if not os.path.isfile(button_file):
            raise Exception('file "%s" does not exist!' % button_file)

        with open(button_file, 'r') as f:
            code = f.read()

        return base64.b64decode(code)

    def write(self, remote, button, code):
        remote_dir = os.path.join(self.directory, remote)
        if not os.path.isdir(remote_dir):
            os.makedirs(remote_dir)
        button_file = os.path.join(remote_dir, button)

        code = base64.b64encode(code)
        with open(button_file, 'w') as f:
            f.write(code)
        return code
