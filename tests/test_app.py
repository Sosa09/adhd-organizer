import flask
from flask import request, jsonify, render_template
from datetime import date
import json, os
from app import app  
from unittest.mock import patch

def test_routes_exist():
    client = app.test_client()

    routes = ['/','/suggest-tasks', '/select-tasks', '/generate-subtasks']
    for route in routes:
        response = client.post(route, json={})
        print(f"Testing route {route}, status code: {response.status_code}")
        assert response.status_code != 404
