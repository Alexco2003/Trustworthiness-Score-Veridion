import json
import pandas as pd
import requests
import os
import FileWriter


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


def main():
    api_key = "AIzaSyDVLIIwEWFFQoGIwZyIEIvSEMCHUYvZbu4"
    file = os.listdir("datasets/")[0]
    dataset = pd.read_parquet(f"datasets/{file}")
    i = 0
    for ind in dataset.head(20).index:
        i += 1
        if i < 10:
            continue
        get_company_reviews(dataset['name'][ind], api_key)
    # get_company_reviews(company_name, api_key)



if __name__ == "__main__":
    main()