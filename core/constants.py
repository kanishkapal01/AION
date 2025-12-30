"""
AION Core Physical Constants
============================

Author: Kanishka Pal
Purpose: Canonical physical constants used across AION.
Units: SI (unless otherwise stated)

Source baseline: CODATA 2018 / 2022 where applicable.
"""

import math

# Mathematical


PI = math.pi
TWO_PI = 2.0 * math.pi


# Fundamental constants


C = 299_792_458.0                      # speed of light in vacuum [m s^-1]
H = 6.62607015e-34                     # Planck constant [J s]
HBAR = 1.054571817e-34                 # reduced Planck constant [J s]
E_CHARGE = 1.602176634e-19             # elementary charge [C]
K_B = 1.380649e-23                     # Boltzmann constant [J K^-1]
G = 6.67430e-11                        # gravitational constant [m^3 kg^-1 s^-2]


# Electromagnetic


ALPHA = 7.2973525643e-3                # fine-structure constant
ALPHA_INV = 137.035999177              # inverse fine-structure constant

EPSILON_0 = 8.8541878188e-12           # vacuum permittivity [F m^-1]
MU_0 = 1.25663706127e-6                # vacuum permeability [N A^-2]
Z_0 = 376.730313412                    # impedance of free space [ohm]

PHI_0 = H / (2 * E_CHARGE)             # magnetic flux quantum [Wb]


# Particle masses


M_E = 9.1093837139e-31                 # electron mass [kg]
M_P = 1.67262192595e-27                # proton mass [kg]
M_N = 1.67492750056e-27                # neutron mass [kg]
M_MU = 1.883531627e-28                 # muon mass [kg]
M_TAU = 3.16754e-27                    # tau mass [kg]

MP_ME = 1836.152673426                 # proton-to-electron mass ratio


# Atomic / quantum scales


A_0 = 5.29177210544e-11                # Bohr radius [m]
R_INF = 10973731.568157                # Rydberg constant [m^-1]
RY = 2.1798723611030e-18               # Rydberg energy [J]
E_H = 4.3597447222060e-18              # Hartree energy [J]

MU_B = 9.2740100657e-24                # Bohr magneton [J T^-1]
MU_N = 5.0507837393e-27                # nuclear magneton [J T^-1]

R_E = 2.8179403205e-15                 # classical electron radius [m]


# Statistical mechanics / thermodynamics


SIGMA_SB = 5.670374419e-8              # Stefan–Boltzmann constant [W m^-2 K^-4]
R_GAS = 8.31446261815324               # molar gas constant [J mol^-1 K^-1]

N_A = 6.02214076e23                    # Avogadro constant [mol^-1]
FARADAY = 96485.3321233100184          # Faraday constant [C mol^-1]


# Radiation constants


C1 = 3.741771852e-16                   # first radiation constant [W m^2]
C1_L = 1.191042972e-16                 # first radiation constant (spectral radiance)
C2 = 1.438776877e-2                    # second radiation constant [m K]

B_WIEN = 2.897771955e-3                # Wien wavelength displacement constant [m K]
B_WIEN_FREQ = 5.878925757e10           # Wien frequency displacement [Hz K^-1]
B_WIEN_ENTROPY = 3.002916077e-3        # Wien entropy displacement [m K]

# Quantum electrical standards


R_K = 25812.80745                      # von Klitzing constant [ohm]
K_J = 483597.8484e9                    # Josephson constant [Hz V^-1]

G_0 = 7.748091729e-5                   # conductance quantum [S]
G_0_INV = 12906.40372                  # inverse conductance quantum [ohm]

# Weak interaction


G_F = 1.1663787e-5                     # Fermi coupling constant [GeV^-2]


# Nuclear / particle g-factors


G_E = 2.00231930436092                 # electron g-factor
G_MU = 2.00233184123                   # muon g-factor
G_P = 5.5856946893                    # proton g-factor


# Metrology / reference


DELTA_NU_CS = 9_192_631_770             # Cs-133 hyperfine transition [Hz]
VM_SI = 1.205883199e-5                 # molar volume of silicon [m^3 mol^-1]

M_U = 1.00000000105e-3                 # molar mass constant [kg mol^-1]
M_U_ATOMIC = 1.66053906892e-27         # atomic mass constant [kg]


# Cosmology


LAMBDA_COSMO = 1.089e-52               # cosmological constant [m^-2]
