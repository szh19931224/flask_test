from test_app import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8123)







