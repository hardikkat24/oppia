# coding: utf-8
#
# Copyright 2017 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Loads constants for backend use."""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

from google.protobuf.json_format import Parse
import json
import os
import re

import python_utils
from proto_files import constants_pb2


def parse_json_from_js(js_file):
    """Extracts JSON object from JS file.

    Args:
        js_file: file. The js file containing JSON that needs to be parsed.

    Returns:
        dict. The dict representation of JSON object in the js file.
    """
    text = js_file.read()
    text_without_comments = remove_comments(text)
    json_start = text_without_comments.find('{\n')
    # Add 1 to index returned because the '}' is part of the JSON object.
    json_end = text_without_comments.rfind('}') + 1
    return json.loads(text_without_comments[json_start:json_end])


def remove_comments(text):
    """Removes comments from given text.

    Args:
        text: str. The text from which comments should be removed.

    Returns:
        str. Text with all its comments removed.
    """
    return re.sub(r'  //.*\n', r'', text)


class Constants(dict):
    """Transforms dict to object, attributes can be accessed by dot notation."""

    __getattr__ = dict.__getitem__


constants = constants_pb2.constants()
with python_utils.open_file(os.path.join('assets', 'constants.json'), 'r') as f:
    # constants = Constants(parse_json_from_js(f))  # pylint:disable=invalid-name
    Parse(f.read(), constants)

with python_utils.open_file('release_constants.json', 'r') as f:
    release_constants = Constants(json.loads(f.read()))  # pylint:disable=invalid-name

# print(constants.SUPPORTED_AUDIO_LANGUAGES)

# temp = constants_pb2.constants.supported_audio_languages()
# temp.id = 'new_lang'
# temp.description = 'New language'
# temp.relatedLanguages.append('new_lang')
# print(temp)

# temp_constants = constants_pb2.constants()
# for lang in constants.SUPPORTED_AUDIO_LANGUAGES:
#     temp_constants.SUPPORTED_AUDIO_LANGUAGES.append(lang)

# temp_constants.SUPPORTED_AUDIO_LANGUAGES.append(temp)
# print(temp_constants.SUPPORTED_AUDIO_LANGUAGES)
# print(constants.SUPPORTED_AUDIO_LANGUAGES)
print(constants.SKILL_DIFFICULTY_LABEL_TO_FLOAT[constants.SKILL_DIFFICULTY_EASY])

constants.SKILL_DIFFICULTY_LABEL_TO_FLOAT['Easy'] = 0.4


print(constants.SKILL_DIFFICULTY_LABEL_TO_FLOAT[constants.SKILL_DIFFICULTY_EASY])
print(constants.NEW_STATE_TEMPLATE.classifier_model_id)

