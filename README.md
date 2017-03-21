to create a new database, run the `db_create.py` script, then use `db_upgrade.py` to upgrade the database to the latest version

## Beginning

Once the app is up and running, please navigate to `localhost:5000`

If for some reason you are getting the 401 Unauthorized error, please navigate to `localhost:5000/login`. For more info on logging in, please see below.

## Logging in

Current implementation only supports login via OpenID. The simplest way to obtain an OpenID is by signing up for Yahoo mail (at this point in time, Yahoo is one of the few big websites that supports OpenID).

## Scoring functions with parameters vs. numbers in a web form

While not currently implemented, the ability to grade functions with parameters can be added on by collecting the code of the function in a web form. Submitting the form would trigger a script that would send the code to a remote server where the function can be executed. Once the script receives the result of the function from the remote server, it would compare it against the right answer stored in the database and produce feedback.

Also, currently the right answer to a question is stored as a field in the Question table in the database. To store multiple pairs of inputs with expected outputs, a separate table could be created. One of the fields in that table would be question_id, a foreign key from the Question table.

## Future directions

Given current architecture, the following extensions/improvements are quite easy to implement

 - categorize students into groups
 - add questions only for a specific group of students
