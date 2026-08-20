from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from extensions import bcrypt, db
from models import User