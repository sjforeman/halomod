# # Some data from CMB missions.
# # All cov and mean data is in order of ["omegab_h2", "omegac_h2", "n", "sigma_8", "H0"]
import numpy as np

data = {"PLANCK":{},
        "WMAP3":{},
        "WMAP5":{},
        "WMAP9":{}}

data["PLANCK"]['cov'] = np.array([[1.11733378e-07, -7.09604835e-07, 2.21131561e-06,
                                     3.40928509e-06, 3.83291259e-04],
                                    [-7.09604835e-07, 9.82440822e-06, -2.53735428e-05,
                                     - 2.16615792e-05, -4.42301634e-03],
                                    [2.21131561e-06, -2.53735428e-05, 8.91798819e-05,
                                     1.17203266e-04, 1.19634138e-02],
                                    [3.40928509e-06, -2.16615792e-05, 1.17203266e-04,
                                     7.20960034e-04, 1.20266027e-02],
                                    [3.83291259e-04, -4.42301634e-03, 1.19634138e-02,
                                     1.20266027e-02, 2.09318686e+00]])

data["PLANCK"]['mean'] = np.array([2.20736974e-02, 1.19592445e-01, 9.61688558e-01,
                                   8.33922313e-01, 6.74140271e+01])

data["WMAP3"]['cov'] = np.array([[5.66068555e-07, 1.00787611e-06, 9.77135800e-06,
                                    1.45917676e-05, -7.04156679e-06],
                                   [  1.00787611e-06, 6.65594178e-05, -3.90198604e-06,
                                    3.44451890e-04, 1.90411112e-04],
                                   [  9.77135800e-06, -3.90198604e-06, 2.83253964e-04,
                                    2.96682040e-04, -2.38200184e-04],
                                   [  1.45917676e-05, 3.44451890e-04, 2.96682040e-04,
                                    2.55783890e-03, 1.79164473e-03],
                                   [ -7.04156679e-06, 1.90411112e-04, -2.38200184e-04,
                                    1.79164473e-03, 3.51674339e-03]])

data['WMAP3']['mean'] = np.array([ 0.02229233, 0.10539691, 0.95770962, 0.76051075, 3.15456266])


data["WMAP5"]['cov'] = np.array([[  3.84176858e-07, 2.49101177e-07, 7.14014693e-06,
                                    6.47679653e-06, 6.16130197e-04],
                                   [  2.49101177e-07, 4.08889980e-05, -1.53512885e-05,
                                    2.02063479e-04, -1.46450604e-02],
                                   [  7.14014693e-06, -1.53512885e-05, 2.09308302e-04,
                                    9.68763617e-05, 2.02566497e-02],
                                   [  6.47679653e-06, 2.02063479e-04, 9.68763617e-05,
                                    1.32375089e-03, -6.04387727e-02],
                                   [  6.16130197e-04, -1.46450604e-02, 2.02566497e-02,
                                    - 6.04387727e-02, 7.20625358e+00]])

data['WMAP5']['mean'] = np.array([  2.27140772e-02, 1.10291827e-01, 9.63000973e-01,
                                  7.98375926e-01, 7.17387653e+01])


data['WMAP9']['cov'] = np.array([[  2.66457559e-07, -6.81453146e-07, 5.77324204e-06,
                                    7.50866555e-07, 7.26966205e-04],
                                   [ -6.81453146e-07, 2.19857328e-05, -2.94113719e-05,
                                    8.89079944e-05, -9.18215279e-03],
                                   [  5.77324204e-06, -2.94113719e-05, 1.77527668e-04,
                                    - 1.11292118e-05, 2.14786942e-02],
                                   [  7.50866555e-07, 8.89079944e-05, -1.11292118e-05,
                                    5.63269248e-04, -2.95134347e-02],
                                   [  7.26966205e-04, -9.18215279e-03, 2.14786942e-02,
                                    - 2.95134347e-02, 5.03539265e+00]])

data['WMAP9']['mean'] = np.array([  2.26350208e-02, 1.13876395e-01, 9.72265365e-01,
                                  8.21221310e-01, 6.99818841e+01])