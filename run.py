from app import create_app
from db import db

if __name__ == '__main__':
    app = create_app('development')
    app.run(port=5000, debug=True)
