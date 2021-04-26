import unittest

from tests.gate_tests.controlled_U_gate import Test


class CUGateTestCase(unittest.TestCase):

    def test_for_2_qubits(self):
        self._test_for_n_qubits(2, [1, 2, 3], [2, 3])

    def test_control_register_for_2_qubits(self):
        self._test_control_register_for_n_qubits(2, 2, 1, 3)

    def test_for_3_qubits(self):
        self._test_for_n_qubits(3, [1, 5, 6], [5, 6, 7])

    def test_control_register_for_3_qubits(self):
        self._test_control_register_for_n_qubits(3, 5, 4, 6)

    def test_for_4_qubits(self):
        self._test_for_n_qubits(4, [1, 4, 7, 11, 14], [11, 15])

    def test_control_register_for_4_qubits(self):
        self._test_control_register_for_n_qubits(4, 13, 7, 15)

    def test_for_5_qubits(self):
        self._test_for_n_qubits(5, [1, 8, 17, 25, 30, 31], [21, 23, 25])

    def test_control_register_for_5_qubits(self):
        self._test_control_register_for_n_qubits(5, 17, 8, 21)

    def _test_for_n_qubits(self, n, values, N_values):
        for N in N_values:
            current_values = [value for value in values if value < N]
            for constant in current_values:
                with self.subTest(constant=constant, N=N):
                    params = [{'ctrl': 1, 'x': x} for x in current_values]

                    test = Test(constant, N, n, self)
                    test.run_subtests(params)

    def _test_control_register_for_n_qubits(self, n, constant, x, N):
        ctrl_values = [0, 1]
        params = [{'ctrl': ctrl, 'x': x} for ctrl in ctrl_values]
        test = Test(constant, N, n, self)
        test.run_subtests(params)
