import json
import FileWriter
import requests


def get_company_reviews(company_name, api_key):
    fileWriter = FileWriter.FileWriter("companyReviews.txt")
    # Google Maps Places API endpoint for searching for places by text search
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={company_name}&key={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        avgTotalRating = 0
        totalReviewsCount = 0
        countIterations = 0

        # Check if the response contains any results
        if 'results' in data and len(data['results']) > 0:
            results = data['results']
            details_data = None
            for result in results:
                if result['name'].lower() in company_name.lower() or company_name.lower() in result['name'].lower():
                    result_place_id = result['place_id']
                    noReviews = result['user_ratings_total']
                    avgRating = result['rating']

                    avgTotalRating += avgRating
                    totalReviewsCount += noReviews
                    countIterations += 1

                    fileWriter.write_to_file(f"Company name: {result['name']}\nAverage rating: {avgRating}\n"
                                             f"Number of reviews: {noReviews}\n")

                    # Google Maps Places API endpoint for fetching place details including reviews
                    details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={result_place_id}&fields=name,rating,reviews&key={api_key}"
                    details_response = requests.get(details_url)
                    details_data = details_response.json()

                if details_data is None:
                    continue

                # Extract reviews if available
                if 'result' in details_data:
                    reviews = details_data['result'].get('reviews', [])

                    # Get lastReview to check Company's activity recently
                    lastReview = []
                    if len(reviews):
                        lastReview = reviews[-1]
                    fileWriter.write_to_file("Reviews:\n")
                    for review in reviews:
                        time = review.get('time', 0)
                        if time > lastReview.get('time', 0):
                            lastReview = review

                    fileWriter.write_to_file(json.dumps(lastReview))
                    fileWriter.write_to_file("\n")

            rating = 0
            if countIterations != 0:
                rating = avgTotalRating / countIterations
            fileWriter.write_to_file(f"Company name: {company_name.capitalize()}\nAverage Google Maps Rating: {rating}\nTotal reviews: {totalReviewsCount}\n")
            if avgTotalRating != 0:
                trueRating = (avgTotalRating * countIterations + 5 + 1) / (totalReviewsCount + 2)
            else:
                trueRating = 0
            fileWriter.write_to_file(f"True rating: {trueRating}\n")
            fileWriter.write_to_file("---------------------------------------------------------------------------------------\n\n")
            return trueRating, totalReviewsCount

        else:
            print("No results found for the company.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


def domainChecker(domain, year_founded=None):
    total = 0
    value = 1
    try:
        w = pythonwhois.get_whois(domain)
        creation_date, expiration_date = w.creation_date, w.expiration_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        registration_period = expiration_date.year - creation_date.year
        if registration_period >= 1:
            total += value
        domain_creation_year = creation_date.year
        if year_founded >= 2015 and domain_creation_year == year_founded:
            total += value
    except Exception as e:
        print(str(e))
    return total

def legalNameScore(legalName):

    legalName_dict = {'INC': 20134, 'LLC': 15279, 'LTD': 15134, 'LIMITED': 5724, 'COMPANY': 5143, 'SL': 3098, 'CO': 2948, 'GMBH': 2883, 'SRL': 2285, 'ASSOCIATION': 2206, 'SA': 2093, 'CORPORATION': 1777, 'LTDA': 1606, 'INSTITUTE': 1539, 'BV': 1402, 'SAS': 1167, 'SOCIETY': 1140, 'EV': 992, 'TRUST': 977, 'AB': 943, 'CORP': 897, 'CV': 653, 'SP': 534, 'PC': 534, 'LLP': 512, 'SARL': 506, 'KG': 472, 'LDA': 458, 'SRO': 352, 'PLLC': 346, 'OO': 340, 'OY': 333, 'INCORPORATED': 327, 'APS': 315, 'BHD': 301, 'GBR': 290, 'NV': 272, 'DOO': 272, 'SAC': 259, 'SLU': 256}
    total = 0
    score = 1
    last_word = legalName.split()[-1].upper().replace('.', '')
    if last_word in legalName_dict:
            total += score
    return total

def socialMediaNumber (facebook, instagram, twitter, linkedin, youtube):
    score = 0
    if facebook is not None:
        score += 1
    if instagram is not None:
        score += 1
    if twitter is not None:
        score += 1
    if linkedin is not None:
        score += 1
    if youtube is not None:
        score += 1
    return score / 5

def countPhones (all_phones):
    size = len(all_phones)
    if size >= 3:
        return 1
    if size == 2:
        return 0.75
    if size == 1:
        return 0.5
    return 0

def countEmails (emails):
    size = len(emails)
    if size >= 3:
        return 1
    if size == 2:
        return 0.75
    if size == 1:
        return 0.5
    return 0

def urlChecker(url):
    if url.startswith('https://'):
        return 1
    return 0