# generate_site.py
def create_index_html(name, title, projects, skills):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - {title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav class="navbar">
        <h1 class="logo">{name}</h1>
    </nav>
    
    <section class="hero">
        <h2>Hi, I'm {name}</h2>
        <p>{title}</p>
    </section>
    
    <section class="projects">
        <h2>Projects</h2>
        <div class="project-grid">
"""
    
    for project in projects:
        html += f"""            <div class="project-card">
                <h3>{project['name']}</h3>
                <p>{project['description']}</p>
            </div>
"""
    
    html += """        </div>
    </section>
</body>
</html>"""
    
    return html

# Usage
projects = [
    {"name": "Project One", "description": "My first project"},
    {"name": "Project Two", "description": "My second project"}
]

skills = ["Python", "JavaScript", "HTML/CSS"]

html_content = create_index_html("Your Name", "Developer", projects, skills)

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html created successfully!")