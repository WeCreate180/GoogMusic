from googmusic import app
import os

ports = int(os.environ.get('PORT', 17995))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
