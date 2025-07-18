# Create a comprehensive README file with deployment instructions
readme_content = """# DevOps Portfolio Website - Bathina Siva Prasad Reddy

A professional, responsive portfolio website showcasing DevOps engineering expertise, built with modern web technologies and optimized for global accessibility.

## 🚀 Quick Start

### Option 1: Deploy to GitHub Pages (Recommended)

1. **Create a new GitHub repository**
   ```bash
   # Create a new repository on GitHub named 'your-portfolio' or 'your-username.github.io'
   ```

2. **Clone or upload files**
   ```bash
   git clone https://github.com/yourusername/your-portfolio.git
   cd your-portfolio
   
   # Copy all files (index.html, style.css, script.js) to this directory
   ```

3. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Select Source: "Deploy from a branch"
   - Choose branch: "main" and folder: "/ (root)"
   - Click Save

4. **Access your live website**
   - Your site will be available at: `https://yourusername.github.io/your-portfolio`
   - Or `https://yourusername.github.io` if you named the repo `yourusername.github.io`

### Option 2: Deploy to Netlify

1. **Drag and drop deployment**
   - Go to [netlify.com](https://netlify.com)
   - Drag your project folder to the deployment area
   - Get instant live URL

2. **Git-based deployment**
   - Connect your GitHub repository
   - Auto-deploy on every commit

### Option 3: Deploy to Vercel

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   vercel --prod
   ```

## 📁 Project Structure

```
portfolio/
├── index.html          # Main HTML file
├── style.css           # CSS styles and responsive design
├── script.js           # JavaScript functionality
├── README.md           # This file
└── deployment-guide.md # Detailed deployment instructions
```

## ✨ Features

### 🎨 Design & User Experience
- **Responsive Design**: Works perfectly on all devices
- **Dark/Light Theme**: Toggle between themes with persistence
- **Smooth Animations**: Professional scroll and hover effects
- **Modern UI**: Clean, professional design with proper typography
- **Accessibility**: WCAG 2.1 AA compliant

### 🔧 Technical Features
- **Progressive Web App**: Fast loading and offline capability
- **SEO Optimized**: Proper meta tags and structured data
- **Cross-browser Compatible**: Works on all modern browsers
- **Performance Optimized**: Minimal dependencies, fast loading

### 📱 Mobile-First Design
- **Touch-friendly**: Optimized for mobile interactions
- **Responsive Navigation**: Mobile menu with hamburger toggle
- **Optimized Images**: Responsive images for all screen sizes
- **Fast Mobile Performance**: Optimized for mobile networks

## 🛠️ Customization

### Update Your Information

1. **Personal Details** (in `index.html`):
   ```html
   <h1 class="name">Your Name</h1>
   <p class="title">Your Title</p>
   <span>Your Location</span>
   <span>Your Phone</span>
   <span>your.email@example.com</span>
   ```

2. **Social Links** (in `index.html`):
   ```html
   <a href="https://github.com/yourusername" class="social-link">
   <a href="https://linkedin.com/in/yourusername" class="social-link">
   ```

3. **Professional Summary** (in `index.html`):
   - Update the content in the `#about` section
   - Modify experience details in the `#experience` section
   - Update skills in the `#skills` section

### Customize Styling

1. **Colors** (in `style.css`):
   ```css
   :root {
       --primary-color: #2563eb;    /* Change primary color */
       --secondary-color: #1e40af;  /* Change secondary color */
       --accent-color: #3b82f6;     /* Change accent color */
   }
   ```

2. **Fonts** (in `style.css`):
   ```css
   body {
       font-family: 'Your Font', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
   }
   ```

## 🌐 Global Accessibility Features

### Multi-language Support Ready
- Semantic HTML structure
- Proper heading hierarchy
- ARIA labels and descriptions
- Lang attributes support

### Performance Optimization
- Minified CSS and JavaScript
- Optimized images
- Efficient animations
- Fast loading times globally

### SEO Optimization
- Proper meta tags
- Structured data
- Semantic HTML
- Mobile-first indexing ready

## 📊 Analytics Integration

### Google Analytics Setup
1. **Get tracking code** from Google Analytics
2. **Add to `index.html`** before closing `</head>`:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_MEASUREMENT_ID');
   </script>
   ```

## 🔗 Custom Domain Setup

### For GitHub Pages
1. **Purchase domain** from any registrar
2. **Add CNAME file** to your repository with your domain
3. **Configure DNS** with A records:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

### For Netlify
1. **Go to Domain settings** in Netlify dashboard
2. **Add custom domain**
3. **Update DNS** as instructed

## 📱 QR Code Generation

Generate QR codes for easy sharing:

### Using Online Tools
1. **QR Code Generator**: https://qr-code-generator.com/
2. **Input your website URL**
3. **Download PNG/SVG format**
4. **Add to business cards, resume, etc.**

### Using Command Line
```bash
# Install qrencode
sudo apt-get install qrencode  # Ubuntu/Debian
brew install qrencode          # macOS

# Generate QR code
qrencode -o portfolio-qr.png "https://yourusername.github.io/your-portfolio"
```

## 🚀 Deployment Commands

### GitHub Pages via Command Line
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit"

# Add remote and push
git remote add origin https://github.com/yourusername/your-portfolio.git
git branch -M main
git push -u origin main

# Enable GitHub Pages via GitHub CLI (optional)
gh repo create your-portfolio --public
gh api repos/yourusername/your-portfolio/pages -f "source[branch]=main" -f "source[path]=/"
```

### Netlify CLI Deployment
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy
netlify deploy --prod --dir=.
```

### Vercel CLI Deployment
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

## 📈 Performance Monitoring

### Tools to Monitor Your Site
- **Google PageSpeed Insights**: Check loading performance
- **GTmetrix**: Detailed performance analysis
- **Lighthouse**: Built-in Chrome DevTools audit
- **WebPageTest**: Global performance testing

### Performance Optimization Tips
1. **Optimize images**: Use WebP format when possible
2. **Minify CSS/JS**: Use build tools for production
3. **Enable compression**: Gzip/Brotli compression
4. **Use CDN**: Content delivery network for global reach

## 🔧 Troubleshooting

### Common Issues

1. **GitHub Pages not updating**
   - Check Actions tab for build status
   - Ensure index.html is in root directory
   - Verify branch settings in Pages configuration

2. **CSS/JS not loading**
   - Check file paths in HTML
   - Ensure files are in same directory
   - Verify HTTPS/HTTP protocol matching

3. **Mobile responsiveness issues**
   - Test on multiple devices
   - Use Chrome DevTools device simulation
   - Check viewport meta tag

### Support Resources
- **GitHub Pages Documentation**: https://docs.github.com/en/pages
- **Web Development Resources**: https://developer.mozilla.org/
- **Accessibility Guidelines**: https://www.w3.org/WAI/WCAG21/quickref/

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own use. If you make improvements, consider submitting a pull request!

## 📞 Support

If you need help with deployment or customization:
- Create an issue in the GitHub repository
- Check the troubleshooting section above
- Review the deployment documentation

---

**Happy Coding! 🚀**

*Built with ❤️ for DevOps professionals worldwide*
"""

# Write the README file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✅ README.md created successfully!")
print("File size:", len(readme_content), "characters")