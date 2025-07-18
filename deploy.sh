#!/bin/bash

# DevOps Portfolio - GitHub Pages Deployment Script
# This script helps you deploy your portfolio website to GitHub Pages

echo "🚀 DevOps Portfolio Deployment Script"
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}[STEP]${NC} $1"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    print_header "Initializing Git repository..."
    git init
    print_status "Git repository initialized"
else
    print_status "Git repository already exists"
fi

# Check if required files exist
required_files=("index.html" "style.css" "script.js")
missing_files=()

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    print_error "Missing required files: ${missing_files[*]}"
    print_error "Please ensure all files are in the current directory"
    exit 1
fi

print_status "All required files found"

# Get repository information
echo ""
print_header "Repository Configuration"
echo "Please provide your GitHub repository information:"

read -p "Enter your GitHub username: " github_username
read -p "Enter your repository name (e.g., 'portfolio' or '${github_username}.github.io'): " repo_name

# Validate inputs
if [ -z "$github_username" ] || [ -z "$repo_name" ]; then
    print_error "Username and repository name are required"
    exit 1
fi

# Set up remote origin
repo_url="https://github.com/${github_username}/${repo_name}.git"
print_status "Repository URL: $repo_url"

# Check if remote origin exists
if git remote get-url origin &> /dev/null; then
    print_warning "Remote origin already exists. Updating..."
    git remote set-url origin "$repo_url"
else
    print_status "Adding remote origin..."
    git remote add origin "$repo_url"
fi

# Add all files to staging
print_header "Preparing files for deployment..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    print_warning "No changes to commit"
else
    # Commit changes
    commit_message="Deploy portfolio website - $(date '+%Y-%m-%d %H:%M:%S')"
    print_status "Committing changes: $commit_message"
    git commit -m "$commit_message"
fi

# Push to GitHub
print_header "Deploying to GitHub..."
print_status "Pushing to main branch..."

if git push -u origin main; then
    print_status "Successfully pushed to GitHub!"
else
    print_error "Failed to push to GitHub. Please check your credentials and repository permissions."
    exit 1
fi

# Instructions for enabling GitHub Pages
echo ""
print_header "Enable GitHub Pages"
echo "To complete the deployment, follow these steps:"
echo "1. Go to https://github.com/${github_username}/${repo_name}/settings/pages"
echo "2. Under 'Source', select 'Deploy from a branch'"
echo "3. Choose 'main' branch and '/ (root)' folder"
echo "4. Click 'Save'"
echo ""
echo "Your website will be available at:"
if [ "$repo_name" == "${github_username}.github.io" ]; then
    echo "🌐 https://${github_username}.github.io"
else
    echo "🌐 https://${github_username}.github.io/${repo_name}"
fi

echo ""
print_status "Deployment completed successfully! 🎉"
print_status "It may take a few minutes for GitHub Pages to build and deploy your site."

# Optional: Open GitHub Pages settings
read -p "Would you like to open GitHub Pages settings in your browser? (y/n): " open_browser
if [ "$open_browser" = "y" ] || [ "$open_browser" = "Y" ]; then
    if command -v xdg-open &> /dev/null; then
        xdg-open "https://github.com/${github_username}/${repo_name}/settings/pages"
    elif command -v open &> /dev/null; then
        open "https://github.com/${github_username}/${repo_name}/settings/pages"
    else
        print_warning "Cannot open browser automatically. Please visit the URL manually."
    fi
fi

echo ""
echo "🚀 Happy coding and best of luck with your DevOps career!"
