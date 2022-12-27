# OpenStreetMap Python Example

A Python example of querying OSM data imported into Postgres with PostGIS using `osm2psql`.

The minibuilds.io article associated with this repo can be found here: https://www.minibuilds.io/posts/getting-started-with-openstreetmap-data/

## How to Run

1. Start the database running.
```bash
docker-compose -f localenv/docker-compose.yaml up -d
```

2. Import the data into Postgres using [osm2pgsql](https://osm2pgsql.org/).
```bash
osm2pgsql -d osmdb -U postgres -W -H localhost -P 5432 osm/isle-of-man-latest.osm
# default password is postgres
```

3. Run the python script.
```bash
python plot-osm.py
```