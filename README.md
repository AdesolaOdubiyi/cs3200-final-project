# Stratify — Team Project (Fall 2025 CS 3200)

Stratify is a small team project that puts backtesting, portfolio monitoring, compliance alerts, and leadership dashboards into a single tool. The goal is to save analysts and portfolio managers time, reduce spreadsheet risk, and make it easier to validate ideas before deploying capital.

In short, Stratify helps teams run backtests, monitor positions and exposures, generate compliance alerts and reports, and view firm-level dashboards.

## Team Members

- **Adesola Odubiyi**
- **Edwin Smilack**
- **Vrishank Ramineni**
- **Nwakoby Onugu**
- **Suraj Swamy**

## Quick Start (Docker — recommended)

Prerequisites:

- Docker and Docker Compose installed on your machine.

1. Create API `.env` from the template:

```bash
cp api/.env.template api/.env
# Open and edit `api/.env`:
#   MYSQL_ROOT_PASSWORD=your_strong_password
#   SECRET_KEY=your_flask_secret
```

2. Start all services (from repository root):

```bash
docker compose up -d
```

3. Verify the services are running and view logs:

```bash
docker compose ps
docker compose logs -f
```

4. Access the apps:

- Frontend (Streamlit): `http://localhost:8501/`
- Backend API (Flask): `http://localhost:4000/`
- Database (MySQL): `localhost:3200` (connect with user from `api/.env`)

## Entry Points

- Frontend: `app/src/Home.py` (Streamlit)
- Backend: `api/backend_app.py` (Flask)
- Backend routes and modules: `api/backend/`
- DB initialization SQL: files in `database-files/` (executed by MySQL image on first boot)

## Database initialization notes

- The `docker-compose.yaml` mounts `./database-files` into `/docker-entrypoint-initdb.d/` inside the MySQL container. Any `.sql` files there are executed when the container is created for the first time (in alphabetical order).
- If you modify SQL and need to re-run initialization, remove the DB volume and recreate the container:

```bash
docker compose down -v
docker compose up -d db
```

## Troubleshooting

If the Streamlit UI shows mock data, it usually means the frontend couldn't reach the API — confirm the backend is running at `http://localhost:4000`. If the database doesn't initialize, inspect the DB logs with `docker compose logs db` for SQL errors; after fixing the SQL you can recreate the DB volume and restart the DB as shown above.

## Repo housekeeping

- `api/.env.template` — example env variables (use this to create `api/.env`, do not commit secrets).
- `database-files/` — SQL files used to initialize DB and intentionally kept in repo.
