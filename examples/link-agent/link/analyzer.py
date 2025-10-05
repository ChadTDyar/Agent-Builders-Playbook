def analyze_profile(profile):
    if "error" in profile:
        return f"Error: {profile['error']}"
    # Dummy analysis
    return f"Profile: {profile['name']} ({profile['url']})"
