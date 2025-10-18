import requests

USERNAME = "y-muhammed-nizam"  # your Credly username
OUTPUT_FILE = "README.md"

def fetch_badges(username):
    url = f"https://www.credly.com/users/{username}/badges.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def generate_markdown(badges):
    lines = ["## 🏅 Certifications & Badges\n"]
    for b in badges:
        name = b['badge_template']['name']
        image = b['badge_template']['image']['url']
        link = b['badge_template']['url']
        lines.append(f'<a href="{link}" target="_blank"><img src="{image}" alt="{name}" width="110" height="110" /></a>')
    return "\n".join(lines)

if __name__ == "__main__":
    badges = fetch_badges(USERNAME)
    if badges:
        markdown = generate_markdown(badges)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(markdown)
        print("✅ README updated with latest Credly badges!")
    else:
        print("⚠️ No badges found or unable to fetch.")
