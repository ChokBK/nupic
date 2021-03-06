# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

## This file defines parameters for a prediction experiment.

import os
from nupic.frameworks.opf.expdescriptionhelpers import importBaseDescription

# the sub-experiment configuration
config = \
{ 'modelParams': { 'clParams': { 'clVerbosity': 0},
                   'inferenceType': 'NontemporalMultiStep',
                   'sensorParams': { 'encoders': { 'consumption': { 'clipInput': True,
                                                                    'fieldname': u'consumption',
                                                                    'n': 28,
                                                                    'name': u'consumption',
                                                                    'type': 'AdaptiveScalarEncoder',
                                                                    'w': 21},
                                                   'timestamp_dayOfWeek': { 'dayOfWeek': ( 21,
                                                                                           1),
                                                                            'fieldname': u'timestamp',
                                                                            'name': u'timestamp_dayOfWeek',
                                                                            'type': 'DateEncoder'},
                                                   'timestamp_timeOfDay': { 'fieldname': u'timestamp',
                                                                            'name': u'timestamp_timeOfDay',
                                                                            'timeOfDay': ( 21,
                                                                                           1),
                                                                            'type': 'DateEncoder'},
                                                   'timestamp_weekend': { 'fieldname': u'timestamp',
                                                                          'name': u'timestamp_weekend',
                                                                          'type': 'DateEncoder',
                                                                          'weekend': 21}},
                                     'verbosity': 0},
                   'spEnable': False,
                   'spParams': { },
                   'tpEnable': False,
                   'tpParams': { 'activationThreshold': 14,
                                 'minThreshold': 12,
                                 'verbosity': 0}}}

mod = importBaseDescription('../hotgym/description.py', config)
locals().update(mod.__dict__)
