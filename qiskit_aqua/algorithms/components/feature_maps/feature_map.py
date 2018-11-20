# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""
This module contains the definition of a base class for
feature map. Several types of commonly used approaches.
"""
from abc import ABC, abstractmethod

from qiskit_aqua.utils import get_entangler_map, validate_entangler_map


class FeatureMap(ABC):

    """Base class for FeatureMap.

        This method should initialize the module and its configuration, and
        use an exception if a component of the module is
        available.

        Args:
            configuration (dict): configuration dictionary
    """

    @abstractmethod
    def __init__(self):
        self._configuration = self.CONFIGURATION.copy()
        pass

    @property
    def configuration(self):
        """Return variational form configuration"""
        return self._configuration

    @classmethod
    def init_params(cls, params):
        args = {k: v for k, v in params.items() if k != 'name'}
        return cls(**args)

    @abstractmethod
    def construct_circuit(self, parameters):
        """Construct the variational form, given its parameters.

        Args:
            parameters (numpy.ndarray[float]) : circuit parameters.

        Returns:
            QuantumCircuit: a quantum circuit.
        """
        raise NotImplementedError()

    @staticmethod
    def get_entangler_map(map_type, num_qubits):
        return get_entangler_map(map_type, num_qubits)

    @staticmethod
    def validate_entangler_map(entangler_map, num_qubits):
        return validate_entangler_map(entangler_map, num_qubits)

    @property
    def num_qubits(self):
        return self._num_qubits
