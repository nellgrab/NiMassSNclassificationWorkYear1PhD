#try out using python only files instead of notebooks to see if code runs better ! 
import redback
print(redback.__version__)

import numpy as np
import pandas as pd
from redback.transient_models.phenomenological_models import exponential_powerlaw, fallback_lbol
from redback.transient_models.magnetar_models import magnetar_only, basic_magnetar
from redback.transient_models.magnetar_driven_ejecta_models import _ejecta_dynamics_and_interaction
from redback.transient_models.shock_powered_models import  _shocked_cocoon, _csm_shock_breakout
import redback.interaction_processes as ip
import redback.sed as sed
#from redback.sed import flux_density_to_spectrum, blackbody_to_spectrum
import redback.photosphere as photosphere
from astropy.cosmology import Planck18 as cosmo  # noqa
#from redback.utils import (calc_kcorrected_properties, citation_wrapper, logger, get_csm_properties, nu_to_lambda,
                          # lambda_to_nu, velocity_from_lorentz_factor, build_spectral_feature_list)
from redback.constants import day_to_s, solar_mass, km_cgs, au_cgs, speed_of_light, sigma_sb
from inspect import isfunction
import astropy.units as uu
from collections import namedtuple
from scipy.interpolate import interp1d, RegularGridInterpolator

import matplotlib.pyplot as plt

sn1998bw_z_0_8 = pd.read_csv('/Users/helenagrabham/Downloads/98_bw_models/98bw_z0.8.txt')

sn1998bw_z_0_8.to_csv('/Users/helenagrabham/Downloads/98_bw_models/98bw_z0.8.csv', index = False)

print(sn1998bw_z_0_8)

#now import other files with different redshifts 
#this tests whether the peak gets redder at higher redshifts

