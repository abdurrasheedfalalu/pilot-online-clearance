from flask import Blueprint, flash, redirect, render_template, url_for

from app.models import Staffs



staff = Blueprint('staff', __name__, url_prefix="/staffs")






