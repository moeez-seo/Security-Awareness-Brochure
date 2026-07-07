# generator.py
import os
from content import BROCHURE_TITLE, BROCHURE_SUBTITLE, SECTIONS

def generate_markdown(output_filename="Cybersecurity_Awareness_Guide.md"):
    """
    Generates the brochure in Markdown format based on the content dictionary.
    """
    content = f"# {BROCHURE_TITLE}\n\n"
    content += f"*{BROCHURE_SUBTITLE}*\n\n"
    content += "---\n\n"
    
    # Table of Contents
    content += "## 📑 Table of Contents\n\n"
    for idx, section in enumerate(SECTIONS, 1):
        # Create an anchor link based on the title
        anchor = section['title'].lower().replace(' ', '-').replace('&', '').replace('/', '').replace('(', '').replace(')', '')
        # Clean up multiple hyphens
        while '--' in anchor:
            anchor = anchor.replace('--', '-')
            
        content += f"{idx}. [{section['title']}](#{anchor})\n"
        
    content += "\n---\n\n"
    
    # Sections
    for section in SECTIONS:
        content += f"## {section['icon']} {section['title']}\n\n"
        content += f"> {section['explanation']}\n\n"
        content += "**Key Tips & Best Practices:**\n\n"
        
        for tip in section['tips']:
            # Bold the first part of the tip (before the colon) if it exists
            if ":" in tip:
                parts = tip.split(":", 1)
                content += f"- **{parts[0]}:**{parts[1]}\n"
            else:
                content += f"- {tip}\n"
                
        content += "\n<br>\n\n"
        
    # Footer
    content += "---\n\n"
    content += "*This guide is intended for educational and defensive purposes. Stay safe online!*"
    
    # Write to file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    return os.path.abspath(output_filename)
