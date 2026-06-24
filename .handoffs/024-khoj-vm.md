Handoff prompt for Claude in terminal:

Khoj is installed as a systemd service on Ubuntu 22.04. It's running but failing with django.db.utils.ProgrammingError: relation "database_chatmodeloptions" does not exist — Django migrations didn't complete. The venv is at /home/sbkchaudry_gmail_com/khoj-engine/venv, the DB is PostgreSQL 14 running locally, DB name is khoj, user is khoj.
Fix: activate the venv, run khoj migrate or python manage.py migrate to complete the schema, then restart the systemd service. Also check if Khoj has its own migrate command. Once migrations complete, verify port 42110 is listening with ss -tlnp | grep 42110, then confirm curl http://localhost:42110/api/health returns 200.

That's the complete picture — hand that off and it'll be solved in 2 minutes.
