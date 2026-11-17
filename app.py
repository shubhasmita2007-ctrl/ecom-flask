from flask import Flask

SHIPPING_ANNOUCEMENT="arriving soon"

@app.route('/')
def home():
    return "Welcome"
