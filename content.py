# content.py

"""
This file contains the structured content for the Security Awareness Brochure.
"""

BROCHURE_TITLE = "The Essential Cybersecurity Awareness Guide"
BROCHURE_SUBTITLE = "Simple steps to protect your digital life."

SECTIONS = [
    {
        "icon": "🔐",
        "title": "Strong Passwords & Password Managers",
        "explanation": "Passwords are the keys to your digital life. Weak or reused passwords make it easy for hackers to access your accounts. A password manager acts like a digital vault, securely storing all your passwords so you only have to remember one.",
        "tips": [
            "Use a Password Manager: Tools like Bitwarden, 1Password, or Dashlane generate and store complex passwords for you.",
            "Never Reuse Passwords: Every single account should have a unique password.",
            "Use Passphrases: A long string of random words (e.g., 'PurpleHorseBatteryStaple!') is easier to remember and harder to crack than a short, complex password."
        ]
    },
    {
        "icon": "🎣",
        "title": "Phishing & Suspicious Emails",
        "explanation": "Phishing is when cybercriminals send fake emails or messages pretending to be a legitimate organization (like a bank or delivery service) to trick you into revealing personal information or clicking a malicious link.",
        "tips": [
            "Verify the Sender: Always check the actual email address, not just the display name.",
            "Don't Click Suspicious Links: If an email urges you to act immediately (e.g., 'Your account will be suspended!'), it's likely a scam.",
            "Go Directly to the Source: Instead of clicking a link in an email, type the website address directly into your browser."
        ]
    },
    {
        "icon": "🛡️",
        "title": "Multi-Factor Authentication (MFA/2FA)",
        "explanation": "MFA adds an extra layer of security. Even if a hacker steals your password, they can't access your account without a second piece of evidence (like a code from an app on your phone).",
        "tips": [
            "Enable MFA Everywhere: Turn it on for email, banking, social media, and password managers.",
            "Use Authenticator Apps: Apps like Google Authenticator or Authy are safer than receiving SMS text codes.",
            "Keep Backup Codes Safe: Print out backup codes provided during setup and store them securely."
        ]
    },
    {
        "icon": "🌐",
        "title": "Safe Browsing & Downloads",
        "explanation": "The internet is full of malicious websites and software designed to infect your device with malware or steal your data.",
        "tips": [
            "Look for HTTPS: Ensure websites have 'https' and a padlock icon in the address bar before entering sensitive info.",
            "Download from Trusted Sources: Only download software from official websites or authorized app stores.",
            "Use Ad-blockers: Malicious ads (malvertising) can infect your computer even without you clicking on them."
        ]
    },
    {
        "icon": "☕",
        "title": "Public Wi-Fi Safety",
        "explanation": "Public Wi-Fi networks (at cafes, airports, hotels) are often unencrypted, meaning hackers on the same network can potentially intercept your internet traffic.",
        "tips": [
            "Avoid Sensitive Activities: Do not log into bank accounts or make purchases on public Wi-Fi.",
            "Use a VPN: A Virtual Private Network encrypts your internet connection, keeping your data safe on public networks.",
            "Turn Off Auto-Connect: Disable settings that automatically connect your device to open Wi-Fi networks."
        ]
    },
    {
        "icon": "📱",
        "title": "Device Updates & Locking",
        "explanation": "Software updates often contain critical security patches that fix vulnerabilities hackers use to break into devices. An unlocked device is an open door to your personal data.",
        "tips": [
            "Enable Automatic Updates: Keep your operating system, apps, and antivirus software up to date automatically.",
            "Lock Your Screens: Set your phone and computer to lock automatically after a short period of inactivity.",
            "Use Biometrics: Utilize fingerprint or facial recognition for quick and secure device unlocking."
        ]
    },
    {
        "icon": "🎭",
        "title": "Social Engineering Awareness",
        "explanation": "Social engineering is the psychological manipulation of people into performing actions or divulging confidential information. Hackers 'hack the human' instead of the computer.",
        "tips": [
            "Beware of Urgency: Scammers often try to create a false sense of urgency or fear to make you act quickly without thinking.",
            "Verify Identities: If someone calls or messages you asking for money or data, independently verify who they are before complying.",
            "Limit Oversharing: Be careful about how much personal information you share on social media."
        ]
    },
    {
        "icon": "🚨",
        "title": "Reporting Suspicious Activity",
        "explanation": "Reporting security incidents quickly can prevent further damage to you or your organization.",
        "tips": [
            "Know Who to Contact: If at work, know how to contact your IT or Security department immediately.",
            "Report Phishing: Use built-in tools in your email client to report phishing or spam.",
            "Don't Be Embarrassed: If you clicked a bad link, tell someone immediately. Time is critical in stopping an attack."
        ]
    }
]
