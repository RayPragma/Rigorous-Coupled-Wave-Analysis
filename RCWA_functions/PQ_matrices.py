import numpy as np
from numpy.linalg import solve as bslash
## description
# kx, ky are normalized wavevector MATRICES NOW (by k0)
# matrices because we have expanded in some number of spatial harmonics
# e_r and m_r do not have e0 or mu0 in them
# presently we assume m_r is homogeneous 1
##====================================##

def Q_matrix(Kx, Ky, e_conv, mu_conv):
    '''
    pressently assuming non-magnetic material so mu_conv = I
    :param Kx: now a matrix (NM x NM)
    :param Ky: now a matrix
    :param e_conv: (NM x NM) matrix containing the 2d convmat
    :return:
    '''

    assert type(Kx) == np.ndarray, 'not array'
    assert type(Ky) == np.ndarray, 'not array'
    assert type(e_conv) == np.ndarray, 'not array'

    return np.block([[Kx @ bslash(mu_conv,Ky),  e_conv - Kx @ bslash(mu_conv, Kx)],
                                         [Ky @ bslash(mu_conv, Ky)  - e_conv, -Ky @ bslash(mu_conv, Kx)]]);


def P_matrix(Kx, Ky, e_conv, mu_conv):
    assert type(Kx) == np.ndarray, 'not array'
    assert type(Ky) == np.ndarray, 'not array'
    assert type(e_conv) == np.ndarray, 'not array'

    P = np.block([[Kx @ bslash(e_conv, Ky),  mu_conv - Kx @ bslash(e_conv,Kx)],
                  [Ky @ bslash(e_conv, Ky) - mu_conv,  -Ky @ bslash(e_conv,Kx)]]);
    return P;



def P_Q_kz(Kx, Ky, e_conv, mu_conv):
    '''
    r is for relative so do not put epsilon_0 or mu_0 here
    :param Kx: NM x NM matrix
    :param Ky:
    :param e_conv: (NM x NM) conv matrix
    :param mu_r:
    :return:
    '''
    argument = e_conv - Kx ** 2 - Ky ** 2
    Kz = np.conj(np.sqrt(argument.astype('complex')));
    q = Q_matrix(Kx, Ky, e_conv, mu_conv)
    p = P_matrix(Kx, Ky, e_conv, mu_conv)

    return p, q, Kz;

## simple test case;

