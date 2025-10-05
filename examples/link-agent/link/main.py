import os
from .linkedin import get_profile_info
from .analyzer import analyze_profile
from .slack import send_slack_notification


def main():
    linkedin_url = input("Enter LinkedIn profile URL: ")
    profile = get_profile_info(linkedin_url, os.getenv("LINKEDIN_COOKIE"))
    analysis = analyze_profile(profile)
    send_slack_notification(os.getenv("SLACK_WEBHOOK_URL"), analysis)

if __name__ == "__main__":
    main()
