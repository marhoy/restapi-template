#!/usr/bin/env python

import restapi

# AWS EB requires the application to be named appliction
application = restapi.create_app()

# Azure requires the application to be named app
app = application

# For local debugging
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
