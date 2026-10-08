"""Skeleton (minimal-dielectric) support for the 2-arm planar Archimedean spiral antenna.
Geometry matches CADFEKO Test_Spiral: r_inner 6, r_outer 95, 9 turns, 2 arms (2nd rotated 180 deg), wire radius 1.
z = 0 is the wire centre plane."""
import numpy as np, trimesh
from manifold3d import Manifold, OpType

# ---------------- parameters ----------------
r_in, r_out, turns = 6.0, 95.0, 9
ccw = True                 # right-handed helix in FEKO = counter-clockwise seen from +z
wire_d = 2.0               # real wire diameter
g = wire_d/2 + 0.1         # notch radius (0.1 mm clearance)
mouth_half = 0.9           # snap opening 1.8 mm (slightly narrower than the wire)
blade_t = 1.8              # blade thickness (tangential)
z_bot, z_top = -5.0, 0.9   # blade vertical extent (wire centre = 0)
r_end = 100.0              # blade outer end
prong = 1.2                # plastic left of the first notch
r_support_min = 10.0       # first wire point supported by a long blade
r_support_short = 42.0     # short blades only start outside this radius
n_long = 18                # long blades every 20 deg
ring_r = [(50.0, 1.6), (99.0, 2.0)]; ring_z0, ring_z1 = -5.0, -3.4
hub_r, hub_z0, hub_z1 = 16.0, -5.0, -3.0
feed_hole_d = 2.6
# feed box
bx, bw, plate, bh, post = 36.0, 2.0, 2.0, 22.0, 5.0
lid_t = 8.0
sma_hole_d = 6.5
tripod_af, tripod_depth = 11.4, 5.8
s = 1 if ccw else -1
k_pitch = (r_out - r_in)/(2*np.pi*turns)          # mm per radian

def rr(phi): return r_in + (r_out - r_in)*phi/(360.0*turns)

def crossings(theta):
    """radii where either arm crosses the radial line at angle theta"""
    out = []
    for base in ((s*theta) % 360, (s*(theta - 180)) % 360):
        for k in range(turns + 1):
            phi = base + 360*k
            if phi <= 360*turns + 1e-9: out.append(rr(phi))
    return sorted(out)

def cyl(r, h, z0=0.0, seg=48): return Manifold.cylinder(h, r, r, seg).translate((0, 0, z0))
def cube(sx, sy, sz, x0, y0, z0): return Manifold.cube((sx, sy, sz)).translate((x0, y0, z0))

def cutter(rk):
    alpha = np.degrees(np.arctan2(k_pitch, rk))
    c = Manifold.cylinder(6.0, g, g, 28, center=True).rotate((90, 0, 0))
    slot = cube(2*mouth_half, 6.0, 2.0, -mouth_half, -3.0, 0.0)
    return (c + slot).rotate((0, 0, -s*alpha)).translate((rk, 0, 0))

def blade(theta, r_min):
    rks = [r for r in crossings(theta) if r >= r_min - 1e-9]
    r_start = rks[0] - g - prong
    b = cube(r_end - r_start, blade_t, z_top - z_bot, r_start, -blade_t/2, z_bot)
    b = b - Manifold.batch_boolean([cutter(r) for r in rks], OpType.Add)
    return b.rotate((0, 0, theta)), r_start, rks

def wheel():
    parts = []; info = []
    step = 360.0/n_long
    for j in range(n_long):
        th = j*step
        b, rs, rks = blade(th, r_support_min); parts.append(b); info.append(("long", th, rs, len(rks)))
        th2 = th + step/2
        b, rs, rks = blade(th2, r_support_short); parts.append(b); info.append(("short", th2, rs, len(rks)))
    for r, w in ring_r:
        parts.append(cyl(r + w/2, ring_z1 - ring_z0, ring_z0, 160) - cyl(r - w/2, ring_z1 - ring_z0 + 2, ring_z0 - 1, 160))
    hub = cyl(hub_r, hub_z1 - hub_z0, hub_z0, 96)
    for sx in (-1, 1): hub = hub - cyl(feed_hole_d/2, 10, -10, 24).translate((sx*r_in, 0, 0))
    parts.append(hub)
    return Manifold.batch_boolean(parts, OpType.Add), info

def box_and_lid():
    top = -5.0
    zb = top - plate - bh
    outer = cube(bx, bx, plate + bh, -bx/2, -bx/2, zb)
    inner = cube(bx - 2*bw, bx - 2*bw, bh + 1, -(bx/2 - bw), -(bx/2 - bw), zb - 1)
    b = outer - inner
    pc = bx/2 - bw - post/2
    for sx in (-1, 1):
        for sy in (-1, 1):
            b = b + cube(post, post, bh, sx*pc - post/2, sy*pc - post/2, zb)
            b = b - cyl(1.25, 13, zb - 1, 24).translate((sx*pc, sy*pc, 0))          # M3 pilot holes
    for sx in (-1, 1): b = b - cyl(feed_hole_d/2, plate + 2, top - plate - 1, 24).translate((sx*r_in, 0, 0))
    sma = Manifold.cylinder(6.0, sma_hole_d/2, sma_hole_d/2, 48).rotate((90, 0, 0)).translate((0, -bx/2 + bw + 1, zb + bh/2))
    b = b - sma
    lid = cube(bx, bx, lid_t, -bx/2, -bx/2, zb - lid_t)
    for sx in (-1, 1):
        for sy in (-1, 1):
            lid = lid - cyl(1.7, lid_t + 2, zb - lid_t - 1, 24).translate((sx*pc, sy*pc, 0))
            lid = lid - cyl(3.2, 3.0, zb - lid_t - 1, 32).translate((sx*pc, sy*pc, 0))      # screw-head counterbore
    hexr = tripod_af/np.sqrt(3)
    lid = lid - Manifold.cylinder(tripod_depth + 1, hexr, hexr, 6).translate((0, 0, zb - lid_t - 1))   # 1/4"-20 nut trap
    lid = lid - cyl(3.3, lid_t + 2, zb - lid_t - 1, 32)
    return b, lid

def tri(m):
    mesh = m.to_mesh(); return trimesh.Trimesh(mesh.vert_properties[:, :3], mesh.tri_verts, process=False)

def wire_points(step=0.5):
    ts = np.arange(0, 360*turns + 1e-9, step)
    pts = []
    for arm in (0, 180):
        r = rr(ts); a = np.radians(s*ts + arm)
        pts.append(np.column_stack([r*np.cos(a), r*np.sin(a), np.zeros_like(ts)]))
    return pts

if __name__ == "__main__":
    W, info = wheel(); Wm = tri(W)
    B, L = box_and_lid(); Bm, Lm = tri(B), tri(L)
    print("wheel", Wm.bounds.round(1).tolist(), "watertight", Wm.is_watertight, "volume cm3", round(W.volume()/1000, 1))
    print("box", Bm.is_watertight, Bm.bounds.round(1).tolist(), "lid", Lm.is_watertight, Lm.bounds.round(1).tolist())
    for kind in ("long", "short"):
        rs = [i[2] for i in info if i[0] == kind]; nn = [i[3] for i in info if i[0] == kind]
        print(kind, "blades:", len(rs), "inner end radius", round(min(rs), 1), "-", round(max(rs), 1), "notches each", min(nn), "-", max(nn))
    out = "/mnt/user-data/outputs/"
    w = Wm.copy(); w.apply_translation([0, 0, -w.bounds[0][2]]); w.export(out + "spiral_skeleton_wheel_print.stl")
    b = Bm.copy(); b.apply_transform(trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0])); b.apply_translation([0, 0, -b.bounds[0][2]]); b.export(out + "spiral_skeleton_feed_box_print.stl")
    l = Lm.copy(); l.apply_translation([0, 0, -l.bounds[0][2]]); l.export(out + "spiral_skeleton_box_lid_print.stl")
    Wm.export("/home/claude/wheel_assy.stl"); Bm.export("/home/claude/box_assy.stl"); Lm.export("/home/claude/lid_assy.stl")
