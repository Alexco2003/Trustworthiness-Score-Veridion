import json

import requests
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
                    lastReview = reviews[-1]
                    fileWriter.write_to_file("Reviews:\n")
                    for review in reviews:
                        time = review.get('time', 'Unknown')
                        if time > lastReview.get('time', "unknown"):
                            lastReview = review

                    fileWriter.write_to_file(json.dumps(lastReview))
                    fileWriter.write_to_file("\n")

            fileWriter.write_to_file(f"Company name: {company_name.capitalize()}\nAverage Google Maps Rating: {avgTotalRating / countIterations}\nTotal reviews: {totalReviewsCount}\n")
            fileWriter.write_to_file("---------------------------------------------------------------------------------------\n")
            trueRating = (avgTotalRating * countIterations + 5 + 1) / (totalReviewsCount + 2)
            return trueRating, totalReviewsCount

        else:
            print("No results found for the company.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


def main():
    api_key = "AIzaSyDVLIIwEWFFQoGIwZyIEIvSEMCHUYvZbu4"
    company_name = input("Enter the name of the company: ")
    get_company_reviews(company_name, api_key)


if __name__ == "__main__":
    main()