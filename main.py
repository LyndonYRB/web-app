from website import create_app
# imports "website package"

app = create_app()

if __name__ == '__main__':
    # runs flask app, when in developement mode the debug automatically rerun webserver whenever the python code it changed, MUST BE OFF when in production mode.
    app.run(debug=True)
