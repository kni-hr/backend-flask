Endpoints and possible responses:

POST /register
    ""      registration successful
    "1"     blank fields
    "2"     Passwords do not match
    "3"     invalid user type
    "4"     email already in use
    "100"   unknown database error (failed to create account)

POST /login
    ""      login successful
    "1"     blank fields
    "2"     invalid credentials

GET /logout
    ""

Additional GET endpoints that return HTML files are for testing and development
only. These endpoints should be removed before deploying to production.

If you are adding new error codes, update this file and the docstring of the
function you are modifying. Any function that ultimately returns an error code
must have "RETURNS ERROR CODE" in the first line of its docstring.

All authentication logic should be inside flask_app/auth.py. Currently, we use
signed session and bcrypt but it may change.

For production, store config in .env rather than flask_app/__init__.py!

flask_app/instance/ directory is necessary.
