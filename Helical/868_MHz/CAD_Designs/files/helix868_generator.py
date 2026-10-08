"""Holder for CADFEKO 'Helical_868': helix radius 50, height 35, 8 turns, feed height 6, square ground 120.68.
Parts: TRAY (plate pocket, walls with snap windows, dovetail leg slots), RING (circular band + 4 snap ears + 4 clip posts
with helical channels), 4 LEGS (slide into the tray on dovetails), WINDING ROD (drum with helical groove).  No screws.
z = 0 is the TOP of the ground plate; the SMA (4-ground-leg PCB jack, from below) sits at the helix start (R, 0). Units mm."""
import numpy as np, trimesh
from manifold3d import Manifold, CrossSection, OpType

R, H, turns = 50.0, 35.0, 8
pitch = H/turns
z0 = 6.0                       # feed_height: helix starts 6 mm above the plate
wire_d = 2.0                   # SET TO YOUR REAL WIRE DIAMETER
wire_r = wire_d/2
g = wire_r + 0.15              # channel / groove radius
ccw = True                     # right-handed helix (FEKO default) = counter-clockwise going up
# plate and tray
plate_w, plate_t, fit = 120.68, 1.6, 0.2
rim, floor_t = 12.0, 3.0
pocket = plate_w + 2*fit
outer = pocket + 2*rim; half = outer/2
tray_t = plate_t + floor_t      # 4.6
wall_t, wall_h = 2.4, 4.0
sma_clear = 14.0
# ring
band_r0, band_r1, ring_t = 56.0, 62.0, 3.0
ear_a = half - wall_t - 0.2     # ear outer edge
ear_x0, ear_hw = 58.0, 15.0
t_l, sl_l, head_out = 1.2, 0.8, 0.8
post_w, post_wall, inset = 8.0, 2.5, 0.3
x0p = R - inset*g; thick = (R + g + post_wall) - x0p
post_h = z0 + H + g + 3.0
# legs
leg_w, leg_h = rim, 35.0
dt_open, dt_depth, dt_ang, dt_fit = 3.0, 2.0, 30.0, 0.15
# rod
rod_wall = 4.0; rod_h = 41.0; rod_slice_deg = 4.0

def cube(sx, sy, sz, x0, y0, z0_): return Manifold.cube((sx, sy, sz)).translate((x0, y0, z0_))
def cyl(r, h, zz=0.0, seg=48): return Manifold.cylinder(h, r, r, seg).translate((0, 0, zz))
def tri(m):
    mesh = m.to_mesh(); return trimesh.Trimesh(mesh.vert_properties[:, :3], mesh.tri_verts, process=False)
def inter(a, b): return Manifold.batch_boolean([a, b], OpType.Intersect).volume()
def mirror4(m): return Manifold.batch_boolean([m, m.mirror((1, 0, 0)), m.mirror((0, 1, 0)), m.mirror((1, 0, 0)).mirror((0, 1, 0))], OpType.Add)
def prism_yz(poly, xa, xb):
    m = Manifold.extrude(CrossSection([poly]), xb - xa).transform(np.array([[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], float))
    return m.translate((xa, 0, 0))
def prism_xz(poly, ya, yb):
    m = Manifold.extrude(CrossSection([poly]), yb - ya).transform(np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0]], float))
    return m.translate((0, yb, 0))

yc = half - rim/2                       # leg / corner centre
tan_a = np.tan(np.radians(dt_ang))

def tray():
    b = cube(outer, outer, tray_t, -half, -half, -tray_t)
    b = b - cube(pocket, pocket, plate_t + 0.01, -pocket/2, -pocket/2, -plate_t)
    b = b - cyl(sma_clear/2, floor_t + 2, -tray_t - 1).translate((R, 0, 0))
    walls = cube(outer, outer, wall_h, -half, -half, 0) - cube(outer - 2*wall_t, outer - 2*wall_t, wall_h + 2, -(half - wall_t), -(half - wall_t), -1)
    win = cube(wall_t + 0.2, 4.6, 2.3, half - wall_t - 0.1, -2.3, 0.2)
    walls = walls - Manifold.batch_boolean([win.rotate((0, 0, k*90)) for k in range(4)], OpType.Add)
    m = b + walls
    slot = prism_yz([(yc - dt_open, -tray_t - 0.01), (yc + dt_open, -tray_t - 0.01),
                     (yc + dt_open + dt_depth*tan_a, -tray_t + dt_depth), (yc - dt_open - dt_depth*tan_a, -tray_t + dt_depth)],
                    half - rim - 0.1, half + 0.3)
    return m - mirror4(slot)

def post_and_channels():
    out = []
    for th in (45, 135, 225, 315):
        p = cube(thick, post_w, post_h, x0p, -post_w/2, 0) + cube(57.0 - x0p, post_w, ring_t, x0p, -post_w/2, 0)
        cuts = []
        for k in range(turns):
            z = z0 + pitch*(th/360.0 + k)
            cuts.append(Manifold.cylinder(post_w + 4, g, g, 24, center=True).rotate((90, 0, 0)).translate((R, 0, z)))
        p = p - Manifold.batch_boolean(cuts, OpType.Add)
        out.append(p.rotate((0, 0, th)))
    return out

def ring():
    band = cyl(band_r1, ring_t, 0, 192) - cyl(band_r0, ring_t + 2, -1, 192)
    parts = [band] + post_and_channels()
    ear = cube(ear_a - ear_x0, 2*ear_hw, ring_t, ear_x0, -ear_hw, 0)
    xs = ear_a - t_l - sl_l
    cut = cube(sl_l, 16.0, ring_t + 2, xs, -13.0, -1) + cube(ear_a + 0.4 - xs, 1.0, ring_t + 2, xs, 2.0, -1)
    ear = ear - cut
    head = prism_xz([(ear_a - 0.1, 0.3), (ear_a, 0.3), (ear_a + head_out, 1.2), (ear_a, 2.3), (ear_a - 0.1, 2.3)], -1.5, 1.2)
    ear = ear + head
    parts += [ear.rotate((0, 0, k*90)) for k in range(4)]
    return Manifold.batch_boolean(parts, OpType.Add)

def leg():
    body = cube(leg_w, leg_w, leg_h, 0, 0, 0)
    yc0 = leg_w/2
    hw0 = dt_open - dt_fit
    hw1 = dt_open + (dt_depth - 0.1)*tan_a - dt_fit
    ten = prism_yz([(yc0 - hw0, leg_h - 0.01), (yc0 + hw0, leg_h - 0.01), (yc0 + hw1, leg_h + dt_depth - 0.1), (yc0 - hw1, leg_h + dt_depth - 0.1)], 0.0, rim - 0.1)
    return body + ten

def legs_print():
    return Manifold.batch_boolean([leg().translate((i*(leg_w + 8), 0, 0)) for i in range(4)], OpType.Add)

def dent_points(step_out=6.0, step_dent=3.0):
    half_a = g/pitch*360.0
    pts = []; a = -180.0
    while a < 180.0 - 1e-9:
        if abs(a) <= half_a:
            a2 = a
            while a2 <= half_a and a2 < 180.0:
                dz = pitch*a2/360.0; pts.append((a2, R - np.sqrt(max(g*g - dz*dz, 0.0)))); a2 += step_dent
            a = a2
        else:
            pts.append((a, R)); a += step_out
    return [(r*np.cos(np.radians(t)), r*np.sin(np.radians(t))) for t, r in pts], half_a

def rod():
    pts, _ = dent_points()
    c = CrossSection([pts]) - CrossSection.circle(R - rod_wall, 96)
    tw = 360.0*rod_h/pitch
    return Manifold.extrude(c, rod_h, n_divisions=int(tw/rod_slice_deg), twist_degrees=(1 if ccw else -1)*tw)

def wire_polyline(step=5.0):
    th = np.arange(0, 360*turns + 1e-9, step)
    s = 1 if ccw else -1
    pts = np.column_stack([R*np.cos(np.radians(s*th)), R*np.sin(np.radians(s*th)), z0 + H*th/(360*turns)])
    return np.vstack([[R, 0, 0], pts])

def tube_union(points, r, seg=8):
    segs = []
    for a, b in zip(points[:-1], points[1:]):
        d = b - a; L = np.linalg.norm(d)
        if L < 1e-9: continue
        Rm = trimesh.geometry.align_vectors([0, 0, 1], d/L)
        M = np.hstack([Rm[:3, :3], a.reshape(3, 1)])
        segs.append(Manifold.cylinder(L + 0.02, r, r, seg).transform(M))
    return Manifold.batch_boolean(segs, OpType.Add)
