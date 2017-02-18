import math

def calculate_cm(sw, t):
    cx, cy, cz = 0, 0, 0
    for fly in sw:
        curx, cury, curz = fly[0]+t*fly[3], fly[1]+t*fly[4], fly[2]+t*fly[5]
        cx += curx
        cy += cury
        cz += curz
    cx /= len(sw)
    cy /= len(sw)
    cz /= len(sw)
    return (cx,cy,cz)

def calculate_cm_movement(sw): # per second
    t0 = calculate_cm(sw, 0)
    t1 = calculate_cm(sw, 1)
    return t0 + (t1[0]-t0[0], t1[1]-t0[1], t1[2]-t0[2])

def mag(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def cross(x, y):
    return (x[1]*y[2] - x[2]*y[1], x[2]*y[0] - x[0]*y[2], x[0]*y[1] - x[1]*y[0])

def dot(x, y):
    return x[0]*y[0] + x[1]*y[1] + x[2]*y[2]

def calculate_closest_point(observer, vec):
    r = (vec[0]-observer[0], vec[1]-observer[1], vec[2]-observer[2])
    v = (vec[3], vec[4], vec[5])
    v_mag = mag(v)
    v_cross = cross(r, v)
    if v_mag == 0:
        return (mag(r), 0)
    d = mag(v_cross) / v_mag
    t = -dot(r, v)/(mag(v)**2)
    if d < 0.000001:
        d = 0
    if t < 0:
        return (mag(r), 0)
    if t < 0.000001:
        t = 0
    return (d, t)

def main():
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        sw = []
        for _ in range(N):
            sw.append(list(map(int, input().split(' '))))

        cm_vector = calculate_cm_movement(sw)
        d, t = calculate_closest_point((0,0,0), cm_vector)
        print('Case #{}: {} {}'.format(case, d, t))

if __name__ == '__main__':
    main()
