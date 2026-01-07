import sys
import matplotlib.pyplot as plt

sys.path[:0] = ["/Users/veb/opt/celeritas/celerpy/"]
import celerpy
from celerpy.settings import settings
settings.prefix_path = "/Users/veb/opt/celeritas/build/"
from celerpy import model, visualize

gdml = "atlas-emec-athena.gdml"
celer_geo = visualize.CelerGeo.from_filename(gdml)

celer_geo.reset_id_map()
draw_image = visualize.Imager(
    celer_geo,
    model.ImageInput(
        lower_left=[-203, -203, 0],
        upper_right=[204, 203, 0],
        rightward=[1.0, 0.0, 0.0],
        vertical_pixels=512,
    ))
(fig, ax) = plt.subplots()
draw_image(ax);

plt.savefig("out.pdf")
