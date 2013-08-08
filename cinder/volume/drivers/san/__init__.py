# Copyright (c) 2012 OpenStack, LLC.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
:mod:`cinder.volume.san` -- Cinder San Drivers
=====================================================

.. automodule:: cinder.volume.san
   :platform: Unix
   :synopsis: Module containing all the Cinder San drivers.
"""

# Adding imports for backwards compatibility in loading volume_driver.
from hp_lefthand import HpSanISCSIDriver
from san import SanISCSIDriver
from solaris import SolarisISCSIDriver
