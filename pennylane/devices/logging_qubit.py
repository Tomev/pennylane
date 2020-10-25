__author__ = 'Tomasz Rybotycki'

"""
This PennyLane plugin is basically the same thing as default_qubit device, with only one difference - it logs every
method call. 
"""

from datetime import datetime

from pennylane.devices.default_qubit import DefaultQubit


class LoggingQubit(DefaultQubit):
    name = "Logging qubit PennyLane plugin"
    short_name = "logging.qubit"
    author = "Tomasz Rybotycki"

    @staticmethod
    def _log(message):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] LoggingQubit: {message}')

    def __init__(self, wires, *, shots=1000, analytic=True):
        self._log(f'__init__(wires={wires}, shots={shots}, analytic={analytic})')
        super().__init__(wires=wires, shots=shots, analytic=analytic)

    def apply(self, operations, rotations=None, **kwargs):
        self._log(f'apply(operations={operations}, rotations={rotations}, kwargs={kwargs}')
        super().apply(operations, rotations=None, **kwargs)

    def _apply_operation(self, operation):
        self._log(f'_apply_operation(operation={operation})')
        super()._apply_operation(operation)

    def _apply_x(self, state, axes, **kwargs):
        self._log(f'_apply_x(state={state}, axes={axes}, kwargs={kwargs}')
        return super()._apply_x(state=state, axes=axes, kwargs=kwargs)

    def _apply_y(self, state, axes, **kwargs):
        self._log(f'_apply_y(state={state}, axes={axes}, kwargs={kwargs}')
        return super()._apply_y(state=state, axes=axes, kwargs=kwargs)

    def _apply_z(self, state, axes, **kwargs):
        self._log(f'_apply_z(state={state}, axes={axes}, kwargs={kwargs}')
        return super()._apply_z(state, axes, kwargs)

    def _apply_hadamard(self, state, axes, **kwargs):
        self._log(f'_apply_hadamard(state={state}, axes={axes}, kwargs={kwargs}')
        return super()._apply_hadamard(state=state, axes=axes, kwargs=kwargs)

    def _apply_s(self, state, axes, inverse=False):
        self._log(f'_apply_s(state={state}, axes={axes}, inverse={inverse})')
        return super()._apply_s(state, axes, inverse)

    def _apply_t(self, state, axes, inverse=False):
        self._log(f'_apply_t(state={state}, axes={axes}, inverse={inverse})')
        return super()._apply_t(state, axes, inverse)

    def _apply_cnot(self, state, axes, **kwargs):
        self._log(f'_apply_cnot(state={state}, axes={axes}, kwargs={kwargs}')
        return super()._apply_cnot(state=state, axes=axes, kwargs=kwargs)

    def _apply_swap(self, state, axes, **kwargs):
        self._log(f'_apply_swap(state={state}, axes={axes}, kwargs={kwargs}')
        return super()._apply_swap(state=state, axes=axes, kwargs=kwargs)

    def _apply_cz(self, state, axes, **kwargs):
        self._log(f'_apply_cz(state={state}, axes={axes}, kwargs={kwargs}')
        return super()._apply_cz(state=state, axes=axes, kwargs=kwargs)

    def _apply_phase(self, state, axes, parameters, inverse=False):
        self._log(f'_apply_phase(state={state}, axes={axes}, parameters={parameters}, inverse={inverse})')
        return super()._apply_phase(state, axes, inverse)

    def _get_unitary_matrix(self, unitary):  # pylint: disable=no-self-use
        self._log(f'_get_unitary_matrix(unitary={unitary})')
        return super()._get_unitary_matrix(unitary)

    @classmethod
    def capabilities(cls):
        print('capabilities')
        return super().capabilities().copy()

    def _create_basis_state(self, index):
        self._log(f'_create_basis_state(index={index})')
        return super()._create_basis_state(index)

    @property
    def state(self):
        self._log(f'state()')
        return super().state()

    def _apply_state_vector(self, state, device_wires):
        self._log(f'_apply_state_vector(state={state}, device_wires={device_wires}')
        super()._apply_state_vector(state, device_wires)

    def _apply_basis_state(self, state, wires):
        self._log(f'_apply_basis_state(state={state}, wires={wires}')
        super()._apply_basis_state(state, wires)

    def _apply_unitary(self, mat, wires):
        self._log(f'_apply_unitary(mat={mat}, wires={wires})')
        super()._apply_unitary(mat, wires)

    def _apply_unitary_einsum(self, mat, wires):
        self._log(f'_apply_unitary_einsum(mat={mat}, wires={wires})')
        super()._apply_unitary_einsum(mat, wires)

    def _apply_diagonal_unitary(self, phases, wires):
        self._log(f'_apply_diagonal_unitary(phases={phases}, wires={wires})')
        super()._apply_diagonal_unitary(phases, wires)

    def reset(self):
        self._log(f'reset()')
        super().reset()

    def analytic_probability(self, wires=None):
        self._log(f'analytic_probability(wires={wires})')
        return super().analytic_probability(wires)
        
