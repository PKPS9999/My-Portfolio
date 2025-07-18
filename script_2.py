# Create the CSS file
css_content = """/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #2563eb;
    --secondary-color: #1e40af;
    --accent-color: #3b82f6;
    --text-primary: #1f2937;
    --text-secondary: #6b7280;
    --background: #ffffff;
    --surface: #f8fafc;
    --border: #e5e7eb;
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --transition: all 0.3s ease;
}

[data-theme="dark"] {
    --primary-color: #3b82f6;
    --secondary-color: #2563eb;
    --accent-color: #60a5fa;
    --text-primary: #f9fafb;
    --text-secondary: #d1d5db;
    --background: #111827;
    --surface: #1f2937;
    --border: #374151;
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--background);
    transition: var(--transition);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Theme Toggle */
.theme-toggle {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: 50px;
    padding: 8px 16px;
    cursor: pointer;
    transition: var(--transition);
    display: flex;
    align-items: center;
    gap: 8px;
}

.theme-toggle:hover {
    background: var(--primary-color);
    color: white;
}

.theme-toggle i {
    font-size: 16px;
}

.theme-toggle .fa-moon {
    display: none;
}

[data-theme="dark"] .theme-toggle .fa-sun {
    display: none;
}

[data-theme="dark"] .theme-toggle .fa-moon {
    display: block;
}

/* Header */
.header {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 2rem 0;
}

.header-content {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 2rem;
    align-items: center;
}

.profile-section {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.profile-avatar {
    width: 80px;
    height: 80px;
    background: var(--primary-color);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: white;
}

.profile-info h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.profile-info .title {
    font-size: 1.25rem;
    color: var(--text-secondary);
    margin-bottom: 0.5rem;
}

.location {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-secondary);
}

.contact-section {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    color: var(--text-secondary);
}

.contact-item i {
    color: var(--primary-color);
    width: 20px;
}

.social-links {
    display: flex;
    gap: 1rem;
}

.social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: var(--primary-color);
    color: white;
    border-radius: 50%;
    text-decoration: none;
    transition: var(--transition);
}

.social-link:hover {
    background: var(--secondary-color);
    transform: translateY(-2px);
}

/* Navigation */
.navbar {
    background: var(--background);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
    padding: 1rem 0;
}

.nav-menu a {
    text-decoration: none;
    color: var(--text-secondary);
    font-weight: 500;
    transition: var(--transition);
    position: relative;
}

.nav-menu a:hover {
    color: var(--primary-color);
}

.nav-menu a::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--primary-color);
    transition: var(--transition);
}

.nav-menu a:hover::after {
    width: 100%;
}

/* Main Content */
.main-content {
    padding: 2rem 0;
}

.section {
    padding: 3rem 0;
}

.section-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 2rem;
    text-align: center;
    position: relative;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 3px;
    background: var(--primary-color);
}

/* About Section */
.about-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.about-text {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
}

.highlights {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.highlight-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    background: var(--surface);
    border-radius: 8px;
    border: 1px solid var(--border);
}

.highlight-item i {
    font-size: 1.5rem;
    color: var(--primary-color);
}

/* Experience Section */
.timeline {
    position: relative;
    max-width: 1000px;
    margin: 0 auto;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 100%;
    background: var(--border);
}

.timeline-item {
    position: relative;
    margin: 2rem 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: start;
}

.timeline-item:nth-child(odd) .timeline-content {
    grid-column: 1;
}

.timeline-item:nth-child(even) .timeline-content {
    grid-column: 2;
}

.timeline-item:nth-child(odd) .timeline-date {
    grid-column: 2;
    text-align: left;
}

.timeline-item:nth-child(even) .timeline-date {
    grid-column: 1;
    text-align: right;
}

.timeline-date {
    font-weight: 600;
    color: var(--primary-color);
    font-size: 1.1rem;
    position: relative;
}

.timeline-date::after {
    content: '';
    position: absolute;
    width: 12px;
    height: 12px;
    background: var(--primary-color);
    border-radius: 50%;
    top: 50%;
    transform: translateY(-50%);
}

.timeline-item:nth-child(odd) .timeline-date::after {
    left: -25px;
}

.timeline-item:nth-child(even) .timeline-date::after {
    right: -25px;
}

.timeline-content {
    background: var(--surface);
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
}

.timeline-content h3 {
    color: var(--text-primary);
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
}

.timeline-content h4 {
    color: var(--primary-color);
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}

.project-name {
    font-style: italic;
    color: var(--text-secondary);
    margin-bottom: 1rem;
}

.achievements {
    list-style: none;
    padding: 0;
}

.achievements li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: 0.5rem;
    color: var(--text-secondary);
}

.achievements li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: var(--primary-color);
    font-weight: bold;
}

/* Skills Section */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.skill-category {
    background: var(--surface);
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid var(--border);
}

.skill-category h3 {
    color: var(--text-primary);
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.skills-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.skill-tag {
    background: var(--primary-color);
    color: white;
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
}

/* Projects Section */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
    gap: 2rem;
}

.project-card {
    background: var(--surface);
    padding: 2rem;
    border-radius: 8px;
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
    transition: var(--transition);
}

.project-card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-5px);
}

.project-card h3 {
    color: var(--text-primary);
    font-size: 1.4rem;
    margin-bottom: 1rem;
}

.project-description {
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.tech-tag {
    background: var(--accent-color);
    color: white;
    padding: 0.3rem 0.6rem;
    border-radius: 15px;
    font-size: 0.8rem;
}

.microservices h4 {
    color: var(--text-primary);
    margin-bottom: 1rem;
}

.microservices ul {
    list-style: none;
    padding: 0;
}

.microservices li {
    margin-bottom: 0.5rem;
    color: var(--text-secondary);
}

.architecture-flow {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 1.5rem 0;
}

.flow-item {
    background: var(--primary-color);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
}

.flow-arrow {
    font-size: 1.2rem;
    color: var(--primary-color);
    font-weight: bold;
}

/* Education Section */
.education-content {
    max-width: 600px;
    margin: 0 auto;
}

.education-item {
    background: var(--surface);
    padding: 2rem;
    border-radius: 8px;
    border: 1px solid var(--border);
    text-align: center;
}

.education-item h3 {
    color: var(--text-primary);
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.education-item h4 {
    color: var(--primary-color);
    font-size: 1.2rem;
    margin-bottom: 1rem;
}

.education-details {
    display: flex;
    justify-content: center;
    gap: 2rem;
    color: var(--text-secondary);
}

.year, .grade {
    font-weight: 600;
}

/* Contact Section */
.contact-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    max-width: 1000px;
    margin: 0 auto;
}

.contact-info {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.contact-info .contact-item {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.contact-info .contact-item i {
    width: 40px;
    height: 40px;
    background: var(--primary-color);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
}

.contact-info .contact-item h4 {
    color: var(--text-primary);
    margin-bottom: 0.25rem;
}

.contact-info .contact-item p {
    color: var(--text-secondary);
}

.contact-form {
    background: var(--surface);
    padding: 2rem;
    border-radius: 8px;
    border: 1px solid var(--border);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
    font-weight: 500;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    background: var(--background);
    color: var(--text-primary);
    font-family: inherit;
    transition: var(--transition);
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.submit-btn {
    background: var(--primary-color);
    color: white;
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition);
    width: 100%;
}

.submit-btn:hover {
    background: var(--secondary-color);
}

/* Footer */
.footer {
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 2rem 0;
    text-align: center;
    color: var(--text-secondary);
}

/* Responsive Design */
@media (max-width: 768px) {
    .header-content {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 1rem;
    }

    .profile-section {
        flex-direction: column;
        text-align: center;
    }

    .profile-info h1 {
        font-size: 2rem;
    }

    .nav-menu {
        flex-wrap: wrap;
        gap: 1rem;
        justify-content: center;
    }

    .timeline::before {
        left: 20px;
    }

    .timeline-item {
        grid-template-columns: 1fr;
        padding-left: 50px;
    }

    .timeline-item .timeline-content {
        grid-column: 1;
    }

    .timeline-item .timeline-date {
        grid-column: 1;
        text-align: left;
        margin-bottom: 1rem;
    }

    .timeline-date::after {
        left: -35px !important;
    }

    .skills-grid {
        grid-template-columns: 1fr;
    }

    .projects-grid {
        grid-template-columns: 1fr;
    }

    .contact-content {
        grid-template-columns: 1fr;
        gap: 2rem;
    }

    .architecture-flow {
        flex-direction: column;
        align-items: stretch;
    }

    .flow-arrow {
        transform: rotate(90deg);
        align-self: center;
    }

    .education-details {
        flex-direction: column;
        gap: 0.5rem;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 15px;
    }

    .profile-info h1 {
        font-size: 1.5rem;
    }

    .section-title {
        font-size: 2rem;
    }

    .theme-toggle {
        top: 10px;
        right: 10px;
    }
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.section {
    animation: fadeInUp 0.6s ease-out;
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

/* Print styles */
@media print {
    .theme-toggle,
    .navbar {
        display: none;
    }

    .section {
        page-break-inside: avoid;
    }
}"""

# Write the CSS file
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ style.css created successfully!")
print("File size:", len(css_content), "characters")