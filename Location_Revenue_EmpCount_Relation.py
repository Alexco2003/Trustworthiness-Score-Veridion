import numpy as np

estimatedCoefForSomeCategories = {'Gas Stations': [3.51070606e-07, 2.87708774e-01],
                                  'Utillities': [-1.27619638e-08,  2.71648842e+00],
                                  'Churches': [-4.94362002e-10,  6.63730710e-03],
                                  'Software & IT Services': [-1.16577881e-07,  3.80321441e-01],
                                  'Accommodation': [-3.58479816e-08,  1.92240776e+00],
                                  'Translation & Legal Documents': [-4.07307574e-06,  5.16891622e+01],
                                  'Minerals & Fuels': [-8.99473601e-09,  2.44415130e+01],
                                  'Insurance': [-2.52630782e-09,  1.12540165e+00],
                                  'Grains, Horticulture & Other Farms': [-1.01359297e-08,  8.46559730e-01],
                                  'Gardens, Parks & Playgrounds': [-2.66791278e-08,  2.85502986e+00],
                                  'Watches, Jewelry & Accessories': [-4.50727739e-10,  1.67810675e-03],
                                  'Processed Metal': [2.34911427e-08, 2.95430399e+00],
                                  'General Contractors & Heavy Construction': [-2.13483856e-08,  6.31244248e-02],
                                  'Animal Farming & Poultry': [-7.46760666e-10,  4.32276461e+01],
                                  'Associations': [-4.03935840e-09,  4.88162889e-02],
                                  'Cosmetic Products': [-1.53667526e-08,  1.02469536e-01],
                                  'Graphic Design': [-8.27257528e-08,  4.01669618e+00],
                                  'Auto Parts': [-2.05429858e-07,  2.58079509e-01],
                                  'Government': [-1.48780868e-09,  1.04749599e-01],
                                  'Engineering Services': [-4.09798129e-07,  1.25720264e+01],
                                  'Roadside Assistance': [3.22708172e-06, 3.56555451e+00],
                                  'Restaurants': [-9.49892589e-08,  7.65696698e-03],
                                  'Entertainment': [7.58026939e-08, 3.00954252e+00],
                                  'Aerospace and Defence': [-1.40140683e-07,  4.17917851e+01],
                                  'Telecommunication Services': [1.55968407e-08, 2.92649116e+03],
                                  'Building Contractors': [-1.51075351e-07,  6.39672470e-01],
                                  'HR Services': [-5.9615058e-08,  4.5185726e+00],
                                  'Footwear': [-3.10392404e-06,  2.04705483e+02],
                                  'Ophthalmic & Optical Instruments & Lenses': [4.68124326e-07, 3.70258819e+00],
                                  'Professional Schools': [-1.58240629e-07,  9.53279372e-03],
                                  'Books Printing & Stores': [-2.07999205e-09,  8.05760654e+00],
                                  'Rubber & Plastics': [-1.47339826e-07,  6.43217784e-01],
                                  'Recreational Sports Centers': [-9.32606161e-08,  2.29979789e-01],
                                  'Libraries': [2.75878468e-07, 3.01137032e-01],
                                  'Dentists & Dental Clinics': [-2.03742816e-08,  1.42607999e+00],
                                  'Food Producers & Distributors': [-2.22030494e-07,  6.42284961e+00],
                                  'Detectives & Investigation Services': [-6.94628526e-07,  1.42092863e+01],
                                  'Other Durable Products': [-2.66154929e-08,  6.19621401e+00],
                                  'Renewable energy': [-1.04212362e-08,  1.83263124e-01],
                                  'Real Estate Investment & Rental': [-3.68218852e-07,  1.37586946e+00],
                                  'Finishing Contractors': [-1.39569471e-08,  3.00281598e+00],
                                  'Rental, Repair & Maintenance': [8.42556618e-07, 7.28856917e-01],
                                  'Social Services': [5.30679162e-07, 7.85673851e-01],
                                  'Marketing & Advertising Agencies': [-1.53673016e-07,  3.01457619e+01],
                                  'Aquaculture, Fishing & Hunting': [3.17442714e-06, 7.97132476e-01],
                                  'Travel Agencies': [4.90923117e-10, 6.06510984e-01],
                                  'Other': [-9.71586095e-10,  1.55544953e-03]}


def estimateCoefTwoDimensions(x, y):
    number_of_samples = np.size(x)

    print(y*x)

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    SS_xy = np.sum(y * x) - number_of_samples * mean_x * mean_y
    SS_xx = np.sum(x * x) - number_of_samples * mean_x * mean_x

    coef_b_1 = SS_xy / SS_xx
    coef_b_0 = mean_y - coef_b_1 * mean_x

    return coef_b_0, coef_b_1


def generateLinearRegressionTestForTwoDimensions():
    training_data_x = np.array([5 * i for i in range(30)])
    training_data_y = np.array([2 * i + np.random.randint(-10, 10) for i in range(30)])


    b = estimateCoefTwoDimensions(training_data_x, training_data_y)

    y_prediction = b[0] + b[1] * training_data_x



def scoreCalculation(industry, revenue, location_number, employee_count):
    if revenue is None or location_number is None or employee_count is None:
        return 0

    ind = ""

    if industry in estimatedCoefForSomeCategories:
        ind = industry
    else:
        ind = "Other"

    revenue_coef = estimatedCoefForSomeCategories[ind][0]
    location_coef = estimatedCoefForSomeCategories[ind][1]

    teoretical_employee_count = float(revenue_coef) * int(float(revenue)) + float(location_coef) * int(location_number)

    return 1 / (1 + abs(int(float(employee_count)) - teoretical_employee_count))


def codeTesting():
    L = zip([1, 2, 3], [1, 2, 3])
    print(L)
    generateLinearRegressionTestForTwoDimensions()


