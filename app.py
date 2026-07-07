# app.py
import sys
from generator import generate_markdown

def print_header():
    print("\n" + "="*50)
    print(" Security Awareness Brochure Generator ")
    print("="*50)
    print(" Educational & Defensive Use Only ".center(50))
    print("="*50 + "\n")

def main():
    print_header()
    print("This tool will generate a professional Markdown brochure covering:")
    print(" - Passwords & MFA")
    print(" - Phishing & Safe Browsing")
    print(" - Device Security & Social Engineering")
    print(" - Public Wi-Fi Safety\n")
    
    choice = input("Would you like to generate the brochure now? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes']:
        try:
            print("\n[+] Generating brochure...")
            filepath = generate_markdown()
            print(f"[+] Success! Brochure exported to:\n    {filepath}")
            print("\n(You can open this file in any Markdown viewer, IDE, or convert it to PDF).")
        except Exception as e:
            print(f"[-] Error generating brochure: {e}")
    else:
        print("\nOperation cancelled. Stay safe!")
        
    sys.exit(0)

if __name__ == "__main__":
    main()
