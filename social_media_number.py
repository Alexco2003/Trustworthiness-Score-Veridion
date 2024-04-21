def socialMediaNumber (facebook, instagram, twitter, linkedin):
    score = 0
    if facebook is not None:
        score += 1
    if instagram is not None:
        score += 1
    if twitter is not None:
        score += 1
    if linkedin is not None:
        score += 1
    return score

def main():
    print(socialMediaNumber("facebook", "instagram", "twitter", "linkedin"))
    print(socialMediaNumber("facebook", "instagram", "twitter", None))