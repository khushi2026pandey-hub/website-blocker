def is_valid_website(website):
    return (
        isinstance(website, str)
        and website.strip() != ""
        and "." in website
    )


def validate_websites(websites):
    return all(is_valid_website(website) for website in websites)
