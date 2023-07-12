import os
import requests
import time

def solve_captcha(site_key, url):
    """
    Function to solve a captcha using the 2Captcha service.
    """

    # Get the API key from the environment variables
    api_key = os.getenv("2CAPTCHA_API_KEY")

    # API endpoint to which we'll send the captcha to be solved
    captcha_endpoint = "http://2captcha.com/in.php"

    # Data payload.
    data = {
        "key": api_key,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": url,
        "json": 1
    }

    # Send a post request to the 2Captcha service.
    response = requests.post(captcha_endpoint, data=data)
    request_id = response.json().get('request')

    # API endpoint to fetch the captcha solution
    solution_endpoint = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    # Poll for the solution
    while True:
        solution = requests.get(solution_endpoint).json()
        if solution.get('status') == 1:  # If the status is 1, the captcha has been solved
            return solution.get('request')  # This is the captcha solution
        time.sleep(5)  # If the captcha has not been solved yet, wait for 5 seconds before polling again
