"""
`gate` module unit tests.
"""
# Authors: John T. Sexton (john.t.sexton@rice.edu)
#          Sebastian M. Castillo-Hair (smc9@rice.edu)
# Date:    10/30/2015

import fc.gate
import numpy as np
import unittest

class TestStartEndGate(unittest.TestCase):
    
    def setUp(self):
        self.d = np.array([
            [1, 7, 2],
            [2, 8, 3],
            [3, 9, 4],
            [4, 10, 5],
            [5, 1, 6],
            [6, 2, 7],
            [7, 3, 8],
            [8, 4, 9],
            [9, 5, 10],
            [10, 6, 1],
            ])

    def test_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.start_end(self.d, num_start=2, num_end=3),
            np.array([
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                ])
            )

    def test_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.start_end(
                self.d, num_start=2, num_end=3, full_output=True).gated_data,
            np.array([
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                ])
            )

    def test_mask(self):
        np.testing.assert_array_equal(
            fc.gate.start_end(
                self.d, num_start=2, num_end=3, full_output=True).mask,
            np.array([0,0,1,1,1,1,1,0,0,0], dtype=bool)
            )

    def test_error(self):
        with self.assertRaises(ValueError):
            fc.gate.start_end(self.d, num_start=5, num_end=7)

class TestHighLowGate(unittest.TestCase):
    
    def setUp(self):
        self.d1 = np.array([range(1,11)]).T
        self.d2 = np.array([
            [1, 7, 2],
            [2, 8, 3],
            [3, 9, 4],
            [4, 10, 5],
            [5, 1, 6],
            [6, 2, 7],
            [7, 3, 8],
            [8, 4, 9],
            [9, 5, 10],
            [10, 6, 1],
            ])

    ###
    # Test 1D data with combinations of high and low values
    ###

    def test_1d_1_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, high=10, low=1),
            np.array([[2,3,4,5,6,7,8,9]]).T
            )

    def test_1d_1_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d1, high=10, low=1, full_output=True).gated_data,
            np.array([[2,3,4,5,6,7,8,9]]).T
            )

    def test_1d_1_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, high=10, low=1, full_output=True).mask,
            np.array([0,1,1,1,1,1,1,1,1,0], dtype=bool)
            )

    def test_1d_2_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, high=11, low=0),
            np.array([[1,2,3,4,5,6,7,8,9,10]]).T
            )

    def test_1d_2_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d1, high=11, low=0, full_output=True).gated_data,
            np.array([[1,2,3,4,5,6,7,8,9,10]]).T
            )

    def test_1d_2_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, high=11, low=0, full_output=True).mask,
            np.array([1,1,1,1,1,1,1,1,1,1], dtype=bool)
            )

    # Test that defaults allow all data through

    def test_1d_defaults_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1),
            np.array([[1,2,3,4,5,6,7,8,9,10]]).T
            )

    def test_1d_defaults_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, full_output=True).gated_data,
            np.array([[1,2,3,4,5,6,7,8,9,10]]).T
            )

    def test_1d_defaults_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, full_output=True).mask,
            np.array([1,1,1,1,1,1,1,1,1,1], dtype=bool)
            )

    # Test that inequalities work

    def test_1d_inequalities_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, high=8, low=2),
            np.array([[3,4,5,6,7]]).T
            )

    def test_1d_inequalities_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d1, high=8, low=2, full_output=True).gated_data,
            np.array([[3,4,5,6,7]]).T
            )

    def test_1d_inequalities_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d1, high=8, low=2, full_output=True).mask,
            np.array([0,0,1,1,1,1,1,0,0,0], dtype=bool)
            )

    ###
    # Test multi-dimensional data with combinations of high and low values
    ###

    def test_2d_1_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=10, low=1),
            np.array([
                [2, 8, 3],
                [3, 9, 4],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                ])
            )

    def test_2d_1_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, high=10, low=1, full_output=True).gated_data,
            np.array([
                [2, 8, 3],
                [3, 9, 4],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                ])
            )

    def test_2d_1_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=10, low=1, full_output=True).mask,
            np.array([0,1,1,0,0,1,1,1,0,0], dtype=bool)
            )

    def test_2d_2_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=11, low=1),
            np.array([
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                ])
            )

    def test_2d_2_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=11, low=1, full_output=True).gated_data,
            np.array([
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                ])
            )

    def test_2d_2_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=11, low=1, full_output=True).mask,
            np.array([0,1,1,1,0,1,1,1,1,0], dtype=bool)
            )

    def test_2d_3_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=10, low=0),
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                ])
            )

    def test_2d_3_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, high=10, low=0, full_output=True).gated_data,
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                ])
            )

    def test_2d_3_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=10, low=0, full_output=True).mask,
            np.array([1,1,1,0,1,1,1,1,0,0], dtype=bool)
            )

    def test_2d_4_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=11, low=0),
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_4_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, high=11, low=0, full_output=True).gated_data,
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_4_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=11, low=0, full_output=True).mask,
            np.array([1,1,1,1,1,1,1,1,1,1], dtype=bool)
            )

    # Test channels

    def test_2d_channels_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, channels=0, high=10, low=1),
            np.array([
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                ])
            )

    def test_2d_channels_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, channels=0, high=10, low=1, full_output=True
                ).gated_data,
            np.array([
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                ])
            )

    def test_2d_channels_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, channels=0, high=10, low=1, full_output=True).mask,
            np.array([0,1,1,1,1,1,1,1,1,0], dtype=bool)
            )

    # Test that defaults allow all data through

    def test_2d_defaults_1_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2),
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_defaults_1_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, full_output=True).gated_data,
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_defaults_1_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, full_output=True).mask,
            np.array([1,1,1,1,1,1,1,1,1,1], dtype=bool)
            )

    def test_2d_defaults_2_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, channels=0),
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_defaults_2_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, channels=0, full_output=True).gated_data,
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [3, 9, 4],
                [4, 10, 5],
                [5, 1, 6],
                [6, 2, 7],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_defaults_2_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, channels=0, full_output=True).mask,
            np.array([1,1,1,1,1,1,1,1,1,1], dtype=bool)
            )

    # Test that inequalities work

    def test_2d_inequalities_1_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=9, low=2),
            np.array([
                [7, 3, 8],
                ])
            )

    def test_2d_inequalities_1_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, high=9, low=2, full_output=True).gated_data,
            np.array([
                [7, 3, 8],
                ])
            )

    def test_2d_inequalities_1_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, high=9, low=2, full_output=True).mask,
            np.array([0,0,0,0,0,0,1,0,0,0], dtype=bool)
            )

    def test_2d_inequalities_2_gated_data_1(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(self.d2, channels=1, high=9, low=2),
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_inequalities_2_gated_data_2(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, channels=1, high=9, low=2, full_output=True
                ).gated_data,
            np.array([
                [1, 7, 2],
                [2, 8, 3],
                [7, 3, 8],
                [8, 4, 9],
                [9, 5, 10],
                [10, 6, 1],
                ])
            )

    def test_2d_inequalities_2_mask(self):
        np.testing.assert_array_equal(
            fc.gate.high_low(
                self.d2, channels=1, high=9, low=2, full_output=True).mask,
            np.array([1,1,0,0,0,0,1,1,1,1], dtype=bool)
            )
        
class TestDensity2dGating(unittest.TestCase):
    
    def setUp(self):
        '''
        Testing proper result of density gating.

        This function applied the density2d gate to Data003.fcs with a gating
        fraction of 0.3. The result is compared to the (previously calculated)
        output of gate.density2d at d23ec66f9039bbe104ff05ede0e3600b9a550078
        using the following command:
        fc.gate.density2d(fc.io.FCSData('Data003.fcs'),
                          channels = ['FSC', 'SSC'],
                          gate_fraction = 0.3)[0]
        '''
        self.ungated_data = fc.io.FCSData('test/Data003.fcs')
        self.gated_data = np.load('test/Data003_gate_density2d.npy')

    def test_density2d(self):
        gated_data = fc.gate.density2d(self.ungated_data,
                                       channels = ['FSC', 'SSC'],
                                       gate_fraction = 0.3)
        np.testing.assert_array_equal(gated_data, self.gated_data)

if __name__ == '__main__':
    unittest.main()
