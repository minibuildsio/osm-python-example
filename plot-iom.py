import psycopg2
import shapely.wkb
import matplotlib.pyplot as plt


def extract_islands(cursor):
  cursor.execute('select way from planet_osm_polygon where place = \'island\'')
  ways = cursor.fetchall()

  return [shapely.wkb.loads(way[0], hex=True) for way in ways]


def plot_islands(polygons):
  axes = plt.axes()

  axes.set_facecolor("#69D2E7")
  axes.set_aspect('equal')

  for polygon in polygons:
    plt.fill(*polygon.exterior.xy, color='#C7F464')
    plt.plot(*polygon.exterior.xy, color='#106F8A', linewidth=.5)

  plt.show()


conn = psycopg2.connect(host="localhost", database="osmdb", user="postgres", password="postgres")

cur = conn.cursor()

islands = extract_islands(cur)
plot_islands(islands)
