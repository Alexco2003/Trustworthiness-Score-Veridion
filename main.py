import companyReviews
import pandas as pd
import os
import Location_Revenue_EmpCount_Relation
import scrap_linkedin
import utils
import FileWriter


def main():
    fileNames = []
    for fileName in os.listdir("datasets/"):
        fileNames.append(fileName)

    file = pd.read_parquet(f"datasets/{fileNames[0]}")

    fileWrite = FileWriter.FileWriter("score.txt")

    for ind in file.index:
        score = 0
        (name, legal_name, year_founded, phones, revenue, industry, email, location_number, website, employee_count, keywords, linkedin, youtube, twitter, facebook, instagram) = \
            file["name"][ind], file["legal_name"][ind], file["year_founded"][ind], file["all_phones"][ind], file["revenue"][ind], file["agg_industry"][ind], \
            file["all_emails"][ind], file["location_number"][ind], file["website_url"][ind], \
                file["employee_count"][ind], file["keywords"][ind], file["linkedin"][ind], file["youtube"][ind], file["twitter"][ind], file["facebook"][ind], file["instagram"][ind]
        #  Test 1: Google Maps Review System
        #     companyReviews.get_company_reviews()

        #  Test 2: Correlation between Revenue, Domain, Locations number and Employee Count through Linear Regression
        score += Location_Revenue_EmpCount_Relation.scoreCalculation(industry, revenue, location_number, employee_count)
        print(score)
        # Test 3: Data scrapping Linkedin (Followers + Last recently post)
        score += scrap_linkedin.scrap_linkedin(linkedin)

        # Test 4: Social Activity
        score += utils.socialMediaNumber(facebook, instagram, twitter, linkedin, youtube)

        # Test 5: Count of phones and emails
        score += utils.countPhones(phones)
        score += utils.countEmails(email)

        # Test 6: Keyworkds on company's website main page
        score += utils.keywords_in_site(website, keywords)

        fileWrite.write_to_file(f"Company name: {name.capitalise()}\nScore: {score}\n\n")

if __name__ == '__main__':
    main()