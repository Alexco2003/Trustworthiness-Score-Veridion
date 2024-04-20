def legalNameScore(legalName=None):
    
    legalName_dict_smaller = {'A': 50000, 'A/S': 53500, 'AAPP': 750, 'AAT': 11950, 'AB': 4850, 'ABP': 5000, 'AC': 5000, 'AE': 60000, 'AGRÍCSP': 1350, 'AKSTICLTD': 2500, 'AMBA': 5370, 'APS': 5370, 'AS': 53700, 'ASA': 50000, 'ASBL': 1250, 'ASSOCIATION': 1000, 'AUSTLTD': 0.63, 'AVEE':  5000, 'AY': 2880, 'AŞ': 4000, 'B': 0.01, 'BHD': 102040.82, 'BM': 21000, 'BO': 1000, 'BT': 25000, 'BV': 0, 'BVBA': 18550, 'C': 4500, 'CIC': 1.17, 'CLINICINC': 1, 'CO': 1, 'CO-OP': 2250, 'COINC': 4999.5, 'COKG': 12499.5, 'COLTD': 4750, 'COMLLTDA': 4750, 'COMMV': 4750, 'COMPANY': 25000, 'COOP': 5000, 'CORP': 25000, 'CORPORATION': 25000, 'CPT': 1, 'CRL': 1, 'CSAS': 5000, 'CSSP': 2000, 'CV': 1, 'CVBA': 1, 'D': 5000, 'DD': 1, 'DIAMONDLLC': 1, 'DOO': 1, 'DOOEL': 93.75, 'DPSNV': 1, 'E': 1, 'EAD': 20000, 'EC': 1000, 'EE': 1000, 'EENMANSZAAK': 0, 'EG': 0, 'EHF': 0, 'EIRELI': 0, 'EIRL': 0, 'EK': 0, 'EOOD': 0, 'EP': 0, 'EPE': 0, 'ESV': 0, 'EURL': 0, 'EV': 0, 'FA': 0, 'FCP': 0, 'FFPDLTDA': 0, 'FMBA': 0, 'FOP': 0, 'FORESTLTD': 0, 'FÖR': 0, 'GBR': 0, 'GEN': 0, 'GIE': 0, 'GIU': 0, 'GMBH': 0, 'GMK': 0, 'GSK': 0, 'GTE': 0, 'HTX': 0, 'I/S': 0, 'IKE': 0, 'IKS': 0, 'ILP': 0, 'INC': 0, 'INCORPORATED': 0, 'INSSANLTD': 0, 'INSSANTICLTD': 0, 'INSTITUTE': 0, 'IVS': 0, 'J': 0, 'JDOO': 0, 'JTD': 0, 'K': 0, 'K/S': 0, 'KAPITALGESELLSCHAFTEN': 0, 'KD': 0, 'KDA': 0, 'KEG': 0, 'KFT': 0, 'KG': 0, 'KGAA': 0, 'KHT': 0, 'KK': 0, 'KOOP': 0, 'KOPERASI': 0, 'KV': 0, 'KY': 0, 'L': 0, 'LDA': 0, 'LIMITED': 0, 'LIMITÉE': 0, 'LLC': 0, 'LLP': 0, 'LP': 0, 'LTD': 0, 'LTDA': 0, 'LTDŞTI': 0, 'LTÉE': 0, 'M': 0, 'MAJGEN': 0, 'MAKMUHLTD': 0, 'MAKSANTICLTD': 0, 'MCHJ': 0, 'MEI': 0, 'MEPE': 0, 'MIAMIINC': 0, 'NETWORKLLC': 0, 'NUF': 0, 'NV': 0, 'O': 0, 'OAO': 0, 'OBRT': 0, 'OD': 0, 'OEG': 0, 'OG': 0, 'OHG': 0, 'OO': 0, 'OOD': 0, 'OOO': 0, 'OPG': 0, 'OPS': 0, 'OSK': 0, 'OTOMOTIVSANTICLTD': 0, 'OY': 0, 'OYJ': 0, 'OÜ': 0, 'P': 0, 'P/S': 0, 'PARQUESEM': 0, 'PARTG': 0, 'PC': 0, 'PFA': 0, 'PJSC': 0, 'PLC': 0, 'PLLC': 0, 'PLT': 0, 'PP': 0, 'PRIVATSTIFTUNG': 0, 'PSE': 0, 'PSU': 0, 'PTE': 0, 'PTELTD': 0, 'PTY': 0, 'PTYLTD': 0, 'PVTLTD': 0, 'REPRESLTDA': 0, 'RHF': 0, 'RL': 0, 'RO': 0, 'S': 0, 'SA': 0, 'SAA': 0, 'SAB': 0, 'SAC': 0, 'SAE': 0, 'SAF': 0, 'SAGL': 0, 'SAL': 0, 'SANLTD': 0, 'SANTICAŞ': 0, 'SANTICLTD': 0, 'SAOC': 0, 'SAOG': 0, 'SAPA': 0, 'SAPI': 0, 'SARF': 0, 'SARL': 0, 'SAS': 0, 'SASU': 0, 'SCA': 0, 'SCARL': 0, 'SCCL': 0, 'SCI': 0, 'SCOOP': 0, 'SCPA': 0, 'SCRL': 0, 'SCS': 0, 'SDNBHD': 0, 'SECS': 0, 'SEM': 0, 'SES': 0, 'SFS': 0, 'SGR': 0, 'SHA': 0, 'SHOPINC': 0, 'SHPK': 0, 'SIA': 0, 'SIASRL': 0, 'SIC': 0, 'SICAV': 0, 'SKA': 0, 'SL': 0, 'SLL': 0, 'SLNE': 0, 'SLP': 0, 'SLU': 0, 'SNC': 0, 'SOCCOL': 0, 'SOCIETY': 0, 'SOFTLDA': 0, 'SP': 0, 'SPAREBANK': 0, 'SPARKASSE': 0, 'SPJ': 0, 'SPK': 0, 'SPP': 0, 'SPRL': 0, 'SPZOO': 0, 'SRL': 0, 'SRLS': 0, 'SRLTDA': 0, 'SRO': 0, 'SS': 0, 'STICHTING': 0, 'SYSTEMCORP': 0, 'SÀRL': 0, 'T:MI': 0, 'TBK': 0, 'TEO': 0, 'TICLTD': 0, 'TOV': 0, 'TRDLLC': 0, 'TRUST': 0, 'U': 0, 'UA': 0, 'UAB': 0, 'UNLTD': 0, 'V': 0, 'VAT': 0, 'VERENIGING': 0, 'VOF': 0, 'VVE': 0, 'VZW': 0, 'Y': 0, 'ZAO': 0, 'ZAT': 0, 'ZOO': 0, 'ZRT': 0, 'ZS': 0, 'Ş': 0, 'ŞTI': 0}
 

    score = 0
    last_word = legalName.split()[-1].upper().replace('.', '')
    if last_word in legalName_dict_smaller:
            score += legalName_dict_smaller[last_word]
    return score


def main():
    print(legalNameScore("Roots Agro Innovations Private Limited"))
    print(legalNameScore("Harborside Farms Inc"))

if __name__ == '__main__':
    main()
