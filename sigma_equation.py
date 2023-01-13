# sigma equation
def sigma_equation(cecita, complessita, disistima_espressa, disistima_ricevuta, rifiuto_effettivo):
    coef0 = 1
    coef1 = 1

    tensione0 = cecita + complessita
    diff0 = abs(complessita - cecita)
    if complessita > cecita:
        coef0 = 1 - (1 + ( (1-diff0**2) / diff0 )**2 )**(-1)
    if complessita < cecita:
        coef0 = 1 - (1 + ( (1-diff0**4) / (diff0)**2 )**2 )**(-1)
    tensione0 = tensione0 * coef0
    diff1 = abs(disistima_espressa - tensione0)

    if disistima_espressa > tensione0:
        coef1 = 1 - (1 + ( (1-diff1**2) / diff1 )**2 )**(-1)
    if disistima_espressa < tensione0:
        coef1 = 1 - (1 + ( (1-diff1**4) / (diff1)**2 )**2 )**(-1)
    tensione1 = disistima_espressa * coef1

    tensione = (tensione0 + tensione1**2) - (tensione0 * tensione1**2)
    stima = disistima_espressa**2 * disistima_ricevuta**2
    tensione2 = stima + (rifiuto_effettivo)**2
    LAVORO = (tensione + tensione2) * 100
    return LAVORO