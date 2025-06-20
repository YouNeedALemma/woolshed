#!/usr/bin/env python3
"""
Build static HTML files from Flask templates for GitHub Pages deployment
"""
import os
import shutil
from flask import Flask, render_template

# Import the Flask app
from app import app

# Output directory for static files
OUTPUT_DIR = 'docs'

def build_static_site():
    """Generate static HTML files from Flask routes"""
    
    # Create output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    
    # Copy static assets
    if os.path.exists('static'):
        shutil.copytree('static', os.path.join(OUTPUT_DIR, 'static'))
    
    # Define routes to render
    routes = [
        ('/', 'index.html'),
        ('/gallery', 'gallery.html'),
        ('/contact', 'contact.html')
    ]
    
    # Generate static HTML for each route
    with app.test_client() as client:
        for route, filename in routes:
            print(f"Building {route} -> {filename}")
            response = client.get(route)
            
            # Write the HTML to file
            output_path = os.path.join(OUTPUT_DIR, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(response.data.decode('utf-8'))
    
    print(f"\nStatic site built successfully in '{OUTPUT_DIR}' directory!")
    print("You can now deploy the 'docs' directory to GitHub Pages")

if __name__ == '__main__':
    build_static_site()