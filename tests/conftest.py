import os
import re
import sys
from subprocess import PIPE, Popen

import pytest
import responses
from responses import RequestsMock

from internetarchive import get_session
from internetarchive.api import get_item
from internetarchive.cli import ia
from internetarchive.utils import json

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

try:
    WindowsError  # type: ignore[used-before-def]
except NameError:
    class WindowsError(Exception):
        pass

PROTOCOL = 'https:'
BASE_URL = 'https://archive.org/'
METADATA_URL = f'{BASE_URL}metadata/'
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_CONFIG = os.path.join(ROOT_DIR, 'tests/ia.ini')
NASA_METADATA_PATH = os.path.join(ROOT_DIR, 'tests/data/metadata/nasa.json')
NASA_EXPECTED_FILES = {
    'globe_west_540.jpg',
    'globe_west_540_thumb.jpg',
    'nasa_archive.torrent',
    'nasa_meta.sqlite',
    'nasa_files.xml',
    'nasa_meta.xml',
    'nasa_reviews.xml',
    'nasa_itemimage.jpg',
    'globe_west_540_thumb.jpg',
    '__ia_thumb.jpg',
}


def ia_call(argv, expected_exit_code=0):
    # Use a test config for all `ia` tests.
    argv.insert(1, '--config-file')
    argv.insert(2, TEST_CONFIG)
    sys.argv = argv
    try:
        ia.main()
    except SystemExit as exc:
        exit_code = exc.code if exc.code else 0
        assert exit_code == expected_exit_code


def files_downloaded(path):
    found_files = set()
    try:
        found_files = set(os.listdir(path))
    except OSError:
        pass
    return found_files


def load_file(filename):
    with open(filename) as fh:
        return fh.read()


def load_test_data_file(filename):
    return load_file(os.path.join(ROOT_DIR, 'tests/data/', filename))


def call_cmd(cmd, expected_exit_code=0):
    proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('utf-8').strip()
    stderr = stderr.decode('utf-8').strip()
    if proc.returncode != expected_exit_code:
        print(stdout)
        print(stderr)
        assert proc.returncode == expected_exit_code
    return (stdout, stderr)


class IaRequestsMock(RequestsMock):
    def add_metadata_mock(self, identifier, body=None, method=responses.GET,
                          protocol='https?', transform_body=None):
        url = re.compile(f'{protocol}://archive.org/metadata/{identifier}')
        if body is None:
            body = load_test_data_file(f'metadata/{identifier}.json')
        if transform_body:
            body = transform_body(body)
        self.add(method, url, body=body, content_type='application/json')

    def mock_all_downloads(self, num_calls=1, body='test content', protocol='https?'):
        url = re.compile(f'{protocol}://archive.org/download/.*')
        for _ in range(6):
            self.add(responses.GET, url, body=body)


@pytest.fixture()
def tmpdir_ch(tmpdir):
    tmpdir.chdir()
    return tmpdir


@pytest.fixture()
def nasa_mocker():
    with IaRequestsMock() as mocker:
        mocker.add_metadata_mock('nasa')
        yield mocker


@pytest.fixture()
def nasa_item():
    session = get_session()
    with IaRequestsMock() as mocker:
        mocker.add_metadata_mock('nasa')
        yield session.get_item('nasa')


@pytest.fixture()
def session():
    return get_session(config={'s3': {'access': 'access', 'secret': 'secret'}})


@pytest.fixture()
def nasa_metadata():
    return json.loads(load_test_data_file('metadata/nasa.json'))


# TODO: Why is this function defined twice in this file?  See issue #505
@pytest.fixture()  # type: ignore
def nasa_item(nasa_mocker):
    return get_item('nasa')
