#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """
    The index route that returns the rendered index.html template.
    
    Returns:
        str: Rendered HTML content.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
