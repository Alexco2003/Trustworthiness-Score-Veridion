def legalNameScore(legalName):

    legalName_dict = {'INC': 20134, 'LLC': 15279, 'LTD': 15134, 'LIMITED': 5724, 'COMPANY': 5143, 'SL': 3098, 'CO': 2948, 'GMBH': 2883, 'SRL': 2285, 'ASSOCIATION': 2206, 'SA': 2093, 'CORPORATION': 1777, 'LTDA': 1606, 'INSTITUTE': 1539, 'BV': 1402, 'SAS': 1167, 'SOCIETY': 1140, 'EV': 992, 'TRUST': 977, 'AB': 943, 'CORP': 897, 'CV': 653, 'SP': 534, 'PC': 534, 'LLP': 512, 'SARL': 506, 'KG': 472, 'LDA': 458, 'SRO': 352, 'PLLC': 346, 'OO': 340, 'OY': 333, 'INCORPORATED': 327, 'APS': 315, 'BHD': 301, 'GBR': 290, 'NV': 272, 'DOO': 272, 'SAC': 259, 'SLU': 256}
    total = 0
    score = 1
    last_word = legalName.split()[-1].upper().replace('.', '')
    if last_word in legalName_dict:
            total += score
    return total


def main():
    print(legalNameScore("Roots Agro Innovations Private Limited"))
    print(legalNameScore("Harborside Farms Inc"))

if __name__ == '__main__':
    main()

# Change score to make sense
