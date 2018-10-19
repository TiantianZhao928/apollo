# ****************************************************************************
# Copyright 2018 The Apollo Authors. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ****************************************************************************
# -*- coding: utf-8 -*-
"""Module for example of listener."""

import sys

sys.path.append("../")
from cyber_py import cybertron
from modules.common.util.testdata.simple_pb2 import SimpleMessage

def callback(data):
    """
    reader message callback.
    """
    print "="*80
    print "py:reader callback msg->:"
    print data
    print "="*80

def test_listener_class():
    """
    reader message.
    """
    print "=" * 120
    test_node = cybertron.Node("listener")
    test_node.create_reader("channel/chatter",
            SimpleMessage, callback)
    test_node.spin()

if __name__ == '__main__':
    cybertron.init()
    test_listener_class()
    cybertron.shutdown()