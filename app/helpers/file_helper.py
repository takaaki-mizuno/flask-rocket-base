from pathlib import Path
import random
import string
import tempfile
import time


class FileHelper(object):
    @classmethod
    def get_temporary_file(cls) -> Path:
        directory = tempfile.gettempdir()

        return Path(directory + '/' + "".join([
            random.choice(string.ascii_letters + string.digits)
            for i in range(12)
        ]) + "_" + str(int(time.time())) + ".tmp")
