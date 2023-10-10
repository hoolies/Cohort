#!/usr/bin/env python3
"""FastAPI with HTMX"""
import sqlite3
from flask import Flask, render_template

def coonect_to_sql():
    """Create connection to the database"""
    conn = sqlite3.connect('passwords.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = connect_to_sql()
    posts = 
