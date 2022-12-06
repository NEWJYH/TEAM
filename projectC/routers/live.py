from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from sqlalchemy import and_ 



import models
import database, schemas

from datetime import date, timedelta
import random
import json


import json

from pydantic import BaseModel

router = APIRouter(
    prefix="/live"
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_test(request: Request):
    context = {}
    context['request'] = request
    return templates.TemplateResponse("live.j2", context)


@router.post('/post')
def get_test(form: schemas.Form):
    print('라이브 포스트 됨')
    testdata = {"1":{
        "0" : {
            "1": { "color": "red", "x": 30, "y": 20 },
            "2": { "color": "black", "x": 40, "y": 60 },
            "3": { "color": "yellow", "x": 100, "y": 200 },
            "4": { "color": "green", "x": 150, "y": 150 },
            "5": { "color": "blue", "x": 80, "y": 200 },
            "6": { "color": "violet", "x": 300, "y": 100 },
            "7": { "color": "aqua", "x": 400, "y": 250 },
            "8": { "color": "gold", "x": 250, "y": 50 }
        },
        "1" : {
            "1": { "color": "red", "x": 31, "y": 21 },
            "2": { "color": "black", "x": 41, "y": 61 },
            "3": { "color": "yellow", "x": 101, "y": 201 },
            "4": { "color": "green", "x": 151, "y": 151 },
            "5": { "color": "blue", "x": 81, "y": 201 },
            "6": { "color": "violet", "x": 301, "y": 101 },
            "7": { "color": "aqua", "x": 401, "y": 251 },
            "8": { "color": "gold", "x": 251, "y": 51 }
        },
        "2" : {
            "1": { "color": "red", "x": 32, "y": 22 },
            "2": { "color": "black", "x": 42, "y": 62 },
            "3": { "color": "yellow", "x": 102, "y": 202 },
            "4": { "color": "green", "x": 152, "y": 152 },
            "5": { "color": "blue", "x": 82, "y": 202 },
            "6": { "color": "violet", "x": 302, "y": 102 },
            "7": { "color": "aqua", "x": 402, "y": 252 },
            "8": { "color": "gold", "x": 252, "y": 52 }
        },
        "3" : {
            "1": { "color": "red", "x": 33, "y": 23 },
            "2": { "color": "black", "x": 43, "y": 63 },
            "3": { "color": "yellow", "x": 103, "y": 203 },
            "4": { "color": "green", "x": 153, "y": 153 },
            "5": { "color": "blue", "x": 83, "y": 203 },
            "6": { "color": "violet", "x": 303, "y": 103 },
            "7": { "color": "aqua", "x": 403, "y": 253 },
            "8": { "color": "gold", "x": 253, "y": 53 }
        },
        "4" : {
            "1": { "color": "red", "x": 34, "y": 24 },
            "2": { "color": "black", "x": 44, "y": 64 },
            "3": { "color": "yellow", "x": 104, "y": 204 },
            "4": { "color": "green", "x": 154, "y": 154 },
            "5": { "color": "blue", "x": 84, "y": 204 },
            "6": { "color": "violet", "x": 304, "y": 104 },
            "7": { "color": "aqua", "x": 404, "y": 254 },
            "8": { "color": "gold", "x": 254, "y": 54 }
        },
        "5" : {
            "1": { "color": "red", "x": 35, "y": 25 },
            "2": { "color": "black", "x": 45, "y": 65 },
            "3": { "color": "yellow", "x": 105, "y": 205 },
            "4": { "color": "green", "x": 155, "y": 155 },
            "5": { "color": "blue", "x": 85, "y": 205 },
            "6": { "color": "violet", "x": 305, "y": 105 },
            "7": { "color": "aqua", "x": 405, "y": 255 },
            "8": { "color": "gold", "x": 255, "y": 55 }
        },
        "6" : {
            "1": { "color": "red", "x": 36, "y": 26 },
            "2": { "color": "black", "x": 46, "y": 66 },
            "3": { "color": "yellow", "x": 106, "y": 206 },
            "4": { "color": "green", "x": 156, "y": 156 },
            "5": { "color": "blue", "x": 86, "y": 206 },
            "6": { "color": "violet", "x": 306, "y": 106 },
            "7": { "color": "aqua", "x": 406, "y": 256 },
            "8": { "color": "gold", "x": 256, "y": 56 }
        },
        "7" : {
            "1": { "color": "red", "x": 37, "y": 27 },
            "2": { "color": "black", "x": 47, "y": 67 },
            "3": { "color": "yellow", "x": 107, "y": 207 },
            "4": { "color": "green", "x": 157, "y": 157 },
            "5": { "color": "blue", "x": 87, "y": 207 },
            "6": { "color": "violet", "x": 307, "y": 107 },
            "7": { "color": "aqua", "x": 407, "y": 257 },
            "8": { "color": "gold", "x": 257, "y": 57 }
        },
        "8" : {
            "1": { "color": "red", "x": 38, "y": 28 },
            "2": { "color": "black", "x": 48, "y": 68 },
            "3": { "color": "yellow", "x": 108, "y": 208 },
            "4": { "color": "green", "x": 158, "y": 158 },
            "5": { "color": "blue", "x": 88, "y": 208 },
            "6": { "color": "violet", "x": 308, "y": 108 },
            "7": { "color": "aqua", "x": 408, "y": 258 },
            "8": { "color": "gold", "x": 258, "y": 58 }
        },
        "9" : {
            "1": { "color": "red", "x": 39, "y": 29 },
            "2": { "color": "black", "x": 49, "y": 69 },
            "3": { "color": "yellow", "x": 109, "y": 209 },
            "4": { "color": "green", "x": 159, "y": 159 },
            "5": { "color": "blue", "x": 89, "y": 209 },
            "6": { "color": "violet", "x": 309, "y": 109 },
            "7": { "color": "aqua", "x": 409, "y": 259 },
            "8": { "color": "gold", "x": 259, "y": 59 }
        },
        "10" : {
            "1": { "color": "red", "x": 38, "y": 28 },
            "2": { "color": "black", "x": 48, "y": 68 },
            "3": { "color": "yellow", "x": 108, "y": 208 },
            "4": { "color": "green", "x": 158, "y": 158 },
            "5": { "color": "blue", "x": 88, "y": 208 },
            "6": { "color": "violet", "x": 308, "y": 108 },
            "7": { "color": "aqua", "x": 408, "y": 258 },
            "8": { "color": "gold", "x": 258, "y": 58 }
        },
        "11" : {
            "1": { "color": "red", "x": 37, "y": 27 },
            "2": { "color": "black", "x": 47, "y": 67 },
            "3": { "color": "yellow", "x": 107, "y": 207 },
            "4": { "color": "green", "x": 157, "y": 157 },
            "5": { "color": "blue", "x": 87, "y": 207 },
            "6": { "color": "violet", "x": 307, "y": 107 },
            "7": { "color": "aqua", "x": 407, "y": 257 },
            "8": { "color": "gold", "x": 257, "y": 57 }
        },
        "12" : {
            "1": { "color": "red", "x": 36, "y": 26 },
            "2": { "color": "black", "x": 46, "y": 66 },
            "3": { "color": "yellow", "x": 106, "y": 206 },
            "4": { "color": "green", "x": 156, "y": 156 },
            "5": { "color": "blue", "x": 86, "y": 206 },
            "6": { "color": "violet", "x": 306, "y": 106 },
            "7": { "color": "aqua", "x": 406, "y": 256 },
            "8": { "color": "gold", "x": 256, "y": 56 }
        },
        "13" : {
            "1": { "color": "red", "x": 35, "y": 25 },
            "2": { "color": "black", "x": 45, "y": 65 },
            "3": { "color": "yellow", "x": 105, "y": 205 },
            "4": { "color": "green", "x": 155, "y": 155 },
            "5": { "color": "blue", "x": 85, "y": 205 },
            "6": { "color": "violet", "x": 305, "y": 105 },
            "7": { "color": "aqua", "x": 405, "y": 255 },
            "8": { "color": "gold", "x": 255, "y": 55 }
        },
        "14" : {
            "1": { "color": "red", "x": 34, "y": 24 },
            "2": { "color": "black", "x": 44, "y": 64 },
            "3": { "color": "yellow", "x": 104, "y": 204 },
            "4": { "color": "green", "x": 154, "y": 154 },
            "5": { "color": "blue", "x": 84, "y": 204 },
            "6": { "color": "violet", "x": 304, "y": 104 },
            "7": { "color": "aqua", "x": 404, "y": 254 },
            "8": { "color": "gold", "x": 254, "y": 54 }
        }
    },
    "2":{
        "0" : {
            "1": { "color": "red", "x": 30, "y": 20 },
            "2": { "color": "black", "x": 40, "y": 60 },
            "3": { "color": "yellow", "x": 100, "y": 200 },
            "4": { "color": "green", "x": 150, "y": 150 },
            "5": { "color": "blue", "x": 80, "y": 200 },
            "6": { "color": "violet", "x": 300, "y": 100 },
            "7": { "color": "aqua", "x": 400, "y": 250 },
            "8": { "color": "gold", "x": 250, "y": 50 }
        },
        "1" : {
            "1": { "color": "red", "x": 31, "y": 21 },
            "2": { "color": "black", "x": 41, "y": 61 },
            "3": { "color": "yellow", "x": 101, "y": 201 },
            "4": { "color": "green", "x": 151, "y": 151 },
            "5": { "color": "blue", "x": 81, "y": 201 },
            "6": { "color": "violet", "x": 301, "y": 101 },
            "7": { "color": "aqua", "x": 401, "y": 251 },
            "8": { "color": "gold", "x": 251, "y": 51 }
        },
        "2" : {
            "1": { "color": "red", "x": 32, "y": 22 },
            "2": { "color": "black", "x": 42, "y": 62 },
            "3": { "color": "yellow", "x": 102, "y": 202 },
            "4": { "color": "green", "x": 152, "y": 152 },
            "5": { "color": "blue", "x": 82, "y": 202 },
            "6": { "color": "violet", "x": 302, "y": 102 },
            "7": { "color": "aqua", "x": 402, "y": 252 },
            "8": { "color": "gold", "x": 252, "y": 52 }
        },
        "3" : {
            "1": { "color": "red", "x": 33, "y": 23 },
            "2": { "color": "black", "x": 43, "y": 63 },
            "3": { "color": "yellow", "x": 103, "y": 203 },
            "4": { "color": "green", "x": 153, "y": 153 },
            "5": { "color": "blue", "x": 83, "y": 203 },
            "6": { "color": "violet", "x": 303, "y": 103 },
            "7": { "color": "aqua", "x": 403, "y": 253 },
            "8": { "color": "gold", "x": 253, "y": 53 }
        },
        "4" : {
            "1": { "color": "red", "x": 34, "y": 24 },
            "2": { "color": "black", "x": 44, "y": 64 },
            "3": { "color": "yellow", "x": 104, "y": 204 },
            "4": { "color": "green", "x": 154, "y": 154 },
            "5": { "color": "blue", "x": 84, "y": 204 },
            "6": { "color": "violet", "x": 304, "y": 104 },
            "7": { "color": "aqua", "x": 404, "y": 254 },
            "8": { "color": "gold", "x": 254, "y": 54 }
        },
        "5" : {
            "1": { "color": "red", "x": 35, "y": 25 },
            "2": { "color": "black", "x": 45, "y": 65 },
            "3": { "color": "yellow", "x": 105, "y": 205 },
            "4": { "color": "green", "x": 155, "y": 155 },
            "5": { "color": "blue", "x": 85, "y": 205 },
            "6": { "color": "violet", "x": 305, "y": 105 },
            "7": { "color": "aqua", "x": 405, "y": 255 },
            "8": { "color": "gold", "x": 255, "y": 55 }
        },
        "6" : {
            "1": { "color": "red", "x": 36, "y": 26 },
            "2": { "color": "black", "x": 46, "y": 66 },
            "3": { "color": "yellow", "x": 106, "y": 206 },
            "4": { "color": "green", "x": 156, "y": 156 },
            "5": { "color": "blue", "x": 86, "y": 206 },
            "6": { "color": "violet", "x": 306, "y": 106 },
            "7": { "color": "aqua", "x": 406, "y": 256 },
            "8": { "color": "gold", "x": 256, "y": 56 }
        },
        "7" : {
            "1": { "color": "red", "x": 37, "y": 27 },
            "2": { "color": "black", "x": 47, "y": 67 },
            "3": { "color": "yellow", "x": 107, "y": 207 },
            "4": { "color": "green", "x": 157, "y": 157 },
            "5": { "color": "blue", "x": 87, "y": 207 },
            "6": { "color": "violet", "x": 307, "y": 107 },
            "7": { "color": "aqua", "x": 407, "y": 257 },
            "8": { "color": "gold", "x": 257, "y": 57 }
        },
        "8" : {
            "1": { "color": "red", "x": 38, "y": 28 },
            "2": { "color": "black", "x": 48, "y": 68 },
            "3": { "color": "yellow", "x": 108, "y": 208 },
            "4": { "color": "green", "x": 158, "y": 158 },
            "5": { "color": "blue", "x": 88, "y": 208 },
            "6": { "color": "violet", "x": 308, "y": 108 },
            "7": { "color": "aqua", "x": 408, "y": 258 },
            "8": { "color": "gold", "x": 258, "y": 58 }
        },
        "9" : {
            "1": { "color": "red", "x": 39, "y": 29 },
            "2": { "color": "black", "x": 49, "y": 69 },
            "3": { "color": "yellow", "x": 109, "y": 209 },
            "4": { "color": "green", "x": 159, "y": 159 },
            "5": { "color": "blue", "x": 89, "y": 209 },
            "6": { "color": "violet", "x": 309, "y": 109 },
            "7": { "color": "aqua", "x": 409, "y": 259 },
            "8": { "color": "gold", "x": 259, "y": 59 }
        },
        "10" : {
            "1": { "color": "red", "x": 38, "y": 28 },
            "2": { "color": "black", "x": 48, "y": 68 },
            "3": { "color": "yellow", "x": 108, "y": 208 },
            "4": { "color": "green", "x": 158, "y": 158 },
            "5": { "color": "blue", "x": 88, "y": 208 },
            "6": { "color": "violet", "x": 308, "y": 108 },
            "7": { "color": "aqua", "x": 408, "y": 258 },
            "8": { "color": "gold", "x": 258, "y": 58 }
        },
        "11" : {
            "1": { "color": "red", "x": 37, "y": 27 },
            "2": { "color": "black", "x": 47, "y": 67 },
            "3": { "color": "yellow", "x": 107, "y": 207 },
            "4": { "color": "green", "x": 157, "y": 157 },
            "5": { "color": "blue", "x": 87, "y": 207 },
            "6": { "color": "violet", "x": 307, "y": 107 },
            "7": { "color": "aqua", "x": 407, "y": 257 },
            "8": { "color": "gold", "x": 257, "y": 57 }
        },
        "12" : {
            "1": { "color": "red", "x": 36, "y": 26 },
            "2": { "color": "black", "x": 46, "y": 66 },
            "3": { "color": "yellow", "x": 106, "y": 206 },
            "4": { "color": "green", "x": 156, "y": 156 },
            "5": { "color": "blue", "x": 86, "y": 206 },
            "6": { "color": "violet", "x": 306, "y": 106 },
            "7": { "color": "aqua", "x": 406, "y": 256 },
            "8": { "color": "gold", "x": 256, "y": 56 }
        },
        "13" : {
            "1": { "color": "red", "x": 35, "y": 25 },
            "2": { "color": "black", "x": 45, "y": 65 },
            "3": { "color": "yellow", "x": 105, "y": 205 },
            "4": { "color": "green", "x": 155, "y": 155 },
            "5": { "color": "blue", "x": 85, "y": 205 },
            "6": { "color": "violet", "x": 305, "y": 105 },
            "7": { "color": "aqua", "x": 405, "y": 255 },
            "8": { "color": "gold", "x": 255, "y": 55 }
        },
        "14" : {
            "1": { "color": "red", "x": 34, "y": 24 },
            "2": { "color": "black", "x": 44, "y": 64 },
            "3": { "color": "yellow", "x": 104, "y": 204 },
            "4": { "color": "green", "x": 154, "y": 154 },
            "5": { "color": "blue", "x": 84, "y": 204 },
            "6": { "color": "violet", "x": 304, "y": 104 },
            "7": { "color": "aqua", "x": 404, "y": 254 },
            "8": { "color": "gold", "x": 254, "y": 54 }
        }
    },
    "3":{
        "0" : {
            "1": { "color": "red", "x": 30, "y": 20 },
            "2": { "color": "black", "x": 40, "y": 60 },
            "3": { "color": "yellow", "x": 100, "y": 200 },
            "4": { "color": "green", "x": 150, "y": 150 },
            "5": { "color": "blue", "x": 80, "y": 200 },
            "6": { "color": "violet", "x": 300, "y": 100 },
            "7": { "color": "aqua", "x": 400, "y": 250 },
            "8": { "color": "gold", "x": 250, "y": 50 }
        },
        "1" : {
            "1": { "color": "red", "x": 31, "y": 21 },
            "2": { "color": "black", "x": 41, "y": 61 },
            "3": { "color": "yellow", "x": 101, "y": 201 },
            "4": { "color": "green", "x": 151, "y": 151 },
            "5": { "color": "blue", "x": 81, "y": 201 },
            "6": { "color": "violet", "x": 301, "y": 101 },
            "7": { "color": "aqua", "x": 401, "y": 251 },
            "8": { "color": "gold", "x": 251, "y": 51 }
        },
        "2" : {
            "1": { "color": "red", "x": 32, "y": 22 },
            "2": { "color": "black", "x": 42, "y": 62 },
            "3": { "color": "yellow", "x": 102, "y": 202 },
            "4": { "color": "green", "x": 152, "y": 152 },
            "5": { "color": "blue", "x": 82, "y": 202 },
            "6": { "color": "violet", "x": 302, "y": 102 },
            "7": { "color": "aqua", "x": 402, "y": 252 },
            "8": { "color": "gold", "x": 252, "y": 52 }
        },
        "3" : {
            "1": { "color": "red", "x": 33, "y": 23 },
            "2": { "color": "black", "x": 43, "y": 63 },
            "3": { "color": "yellow", "x": 103, "y": 203 },
            "4": { "color": "green", "x": 153, "y": 153 },
            "5": { "color": "blue", "x": 83, "y": 203 },
            "6": { "color": "violet", "x": 303, "y": 103 },
            "7": { "color": "aqua", "x": 403, "y": 253 },
            "8": { "color": "gold", "x": 253, "y": 53 }
        },
        "4" : {
            "1": { "color": "red", "x": 34, "y": 24 },
            "2": { "color": "black", "x": 44, "y": 64 },
            "3": { "color": "yellow", "x": 104, "y": 204 },
            "4": { "color": "green", "x": 154, "y": 154 },
            "5": { "color": "blue", "x": 84, "y": 204 },
            "6": { "color": "violet", "x": 304, "y": 104 },
            "7": { "color": "aqua", "x": 404, "y": 254 },
            "8": { "color": "gold", "x": 254, "y": 54 }
        },
        "5" : {
            "1": { "color": "red", "x": 35, "y": 25 },
            "2": { "color": "black", "x": 45, "y": 65 },
            "3": { "color": "yellow", "x": 105, "y": 205 },
            "4": { "color": "green", "x": 155, "y": 155 },
            "5": { "color": "blue", "x": 85, "y": 205 },
            "6": { "color": "violet", "x": 305, "y": 105 },
            "7": { "color": "aqua", "x": 405, "y": 255 },
            "8": { "color": "gold", "x": 255, "y": 55 }
        },
        "6" : {
            "1": { "color": "red", "x": 36, "y": 26 },
            "2": { "color": "black", "x": 46, "y": 66 },
            "3": { "color": "yellow", "x": 106, "y": 206 },
            "4": { "color": "green", "x": 156, "y": 156 },
            "5": { "color": "blue", "x": 86, "y": 206 },
            "6": { "color": "violet", "x": 306, "y": 106 },
            "7": { "color": "aqua", "x": 406, "y": 256 },
            "8": { "color": "gold", "x": 256, "y": 56 }
        },
        "7" : {
            "1": { "color": "red", "x": 37, "y": 27 },
            "2": { "color": "black", "x": 47, "y": 67 },
            "3": { "color": "yellow", "x": 107, "y": 207 },
            "4": { "color": "green", "x": 157, "y": 157 },
            "5": { "color": "blue", "x": 87, "y": 207 },
            "6": { "color": "violet", "x": 307, "y": 107 },
            "7": { "color": "aqua", "x": 407, "y": 257 },
            "8": { "color": "gold", "x": 257, "y": 57 }
        },
        "8" : {
            "1": { "color": "red", "x": 38, "y": 28 },
            "2": { "color": "black", "x": 48, "y": 68 },
            "3": { "color": "yellow", "x": 108, "y": 208 },
            "4": { "color": "green", "x": 158, "y": 158 },
            "5": { "color": "blue", "x": 88, "y": 208 },
            "6": { "color": "violet", "x": 308, "y": 108 },
            "7": { "color": "aqua", "x": 408, "y": 258 },
            "8": { "color": "gold", "x": 258, "y": 58 }
        },
        "9" : {
            "1": { "color": "red", "x": 39, "y": 29 },
            "2": { "color": "black", "x": 49, "y": 69 },
            "3": { "color": "yellow", "x": 109, "y": 209 },
            "4": { "color": "green", "x": 159, "y": 159 },
            "5": { "color": "blue", "x": 89, "y": 209 },
            "6": { "color": "violet", "x": 309, "y": 109 },
            "7": { "color": "aqua", "x": 409, "y": 259 },
            "8": { "color": "gold", "x": 259, "y": 59 }
        },
        "10" : {
            "1": { "color": "red", "x": 38, "y": 28 },
            "2": { "color": "black", "x": 48, "y": 68 },
            "3": { "color": "yellow", "x": 108, "y": 208 },
            "4": { "color": "green", "x": 158, "y": 158 },
            "5": { "color": "blue", "x": 88, "y": 208 },
            "6": { "color": "violet", "x": 308, "y": 108 },
            "7": { "color": "aqua", "x": 408, "y": 258 },
            "8": { "color": "gold", "x": 258, "y": 58 }
        },
        "11" : {
            "1": { "color": "red", "x": 37, "y": 27 },
            "2": { "color": "black", "x": 47, "y": 67 },
            "3": { "color": "yellow", "x": 107, "y": 207 },
            "4": { "color": "green", "x": 157, "y": 157 },
            "5": { "color": "blue", "x": 87, "y": 207 },
            "6": { "color": "violet", "x": 307, "y": 107 },
            "7": { "color": "aqua", "x": 407, "y": 257 },
            "8": { "color": "gold", "x": 257, "y": 57 }
        },
        "12" : {
            "1": { "color": "red", "x": 36, "y": 26 },
            "2": { "color": "black", "x": 46, "y": 66 },
            "3": { "color": "yellow", "x": 106, "y": 206 },
            "4": { "color": "green", "x": 156, "y": 156 },
            "5": { "color": "blue", "x": 86, "y": 206 },
            "6": { "color": "violet", "x": 306, "y": 106 },
            "7": { "color": "aqua", "x": 406, "y": 256 },
            "8": { "color": "gold", "x": 256, "y": 56 }
        },
        "13" : {
            "1": { "color": "red", "x": 35, "y": 25 },
            "2": { "color": "black", "x": 45, "y": 65 },
            "3": { "color": "yellow", "x": 105, "y": 205 },
            "4": { "color": "green", "x": 155, "y": 155 },
            "5": { "color": "blue", "x": 85, "y": 205 },
            "6": { "color": "violet", "x": 305, "y": 105 },
            "7": { "color": "aqua", "x": 405, "y": 255 },
            "8": { "color": "gold", "x": 255, "y": 55 }
        },
        "14" : {
            "1": { "color": "red", "x": 34, "y": 24 },
            "2": { "color": "black", "x": 44, "y": 64 },
            "3": { "color": "yellow", "x": 104, "y": 204 },
            "4": { "color": "green", "x": 154, "y": 154 },
            "5": { "color": "blue", "x": 84, "y": 204 },
            "6": { "color": "violet", "x": 304, "y": 104 },
            "7": { "color": "aqua", "x": 404, "y": 254 },
            "8": { "color": "gold", "x": 254, "y": 54 }
        }
    }
}
    return json.dumps(testdata)