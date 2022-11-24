from website import create_app


app = create_app()


if __name__ == "__main__":
    # Turn off debug = true when in production, as it restarts web server everytime you make a change
    app.run(debug = True)


