# This code is part of Qiskit.
#
# (C) Copyright IBM 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Qiskit runtime service."""

import logging
import traceback
import warnings
from datetime import datetime
from collections import OrderedDict
from typing import Dict, Callable, Optional, Union, List, Any, Type, Sequence

from qiskit.providers.backend import BackendV2 as Backend
from qiskit.providers.exceptions import QiskitBackendNotFoundError
from qiskit.providers.providerutils import filter_backends

from qiskit import pulse
from qiskit.pulse.library import Gaussian
from qiskit.visualization import plot_histogram
plot_histogram(result.get_counts())
backend = provider.get_backend('ibmq_quito')  # Backend cible
dt = backend.configuration().dt  # Résolution temporelle (ex : 0.222 ns)

# Paramètres de l'impulsion
sigma = 0.01e-9  # 0.01 ns en secondes
duration = int(5e-9 / dt)  # Durée = 5 ns

# Créer l'impulsion
with pulse.build(backend, name='gaussian_pulse') as pulse_prog:
    pulse.play(Gaussian(duration, 1.0, sigma/dt), pulse.drive_channel(0))

# Associer au circuit
qc.add_calibration('gaussian_pulse', [0], pulse_prog)
job = execute(qc, backend, shots=1024)
job_monitor(job)  # Surveillez la file d'attente
result = job.result()
print(result.get_counts())

        
