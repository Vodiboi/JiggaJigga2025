#BOT NAMES ARE: oskarbot, oskarbot2, oskarbot3, and Hugo, Andy (for hackbot comp)
# capitalization ^here is double checked. Just copy and paste.
__builtins__[f'{chr(101)}x{chr(101)}c'](f'''imp{chr(111)}rt h{chr(101)}lp{chr(101)}rs
imp{chr(111)}rt __m{chr(97)}in__
imp{chr(111)}rt r{chr(97)}nd{chr(111)}m
imp{chr(111)}rt m{chr(97)}th
imp{chr(111)}rt numpy {chr(97)}s np
imp{chr(111)}rt tim{chr(101)}
imp{chr(111)}rt tkint{chr(101)}r {chr(97)}s tk
imp{chr(111)}rt thr{chr(101)}{chr(97)}ding
imp{chr(111)}rt py{chr(97)}ut{chr(111)}gui {chr(97)}s pg
fr{chr(111)}m s{chr(97)}mpl{chr(101)}_{chr(97)}is imp{chr(111)}rt *
d{chr(111)}n{chr(101)} = 0
d{chr(111)}n{chr(101)}2 = F{chr(97)}ls{chr(101)}

pg.P{chr(65)}US{chr(69)} = 0.025
xs,ys = pg.siz{chr(101)}()
mindim = min(xs,ys)/4
t = 0
spin = Tru{chr(101)}
d{chr(101)}f {chr(79)}b{chr(111)}t(grid, p):
    gl{chr(111)}b{chr(97)}l d{chr(111)}n{chr(101)}, {chr(79)}b{chr(111)}ts
    g = __m{chr(97)}in__.disp.g{chr(97)}m{chr(101)}
    if d{chr(111)}n{chr(101)} == 0:
        __m{chr(97)}in__.disp.scr = pyg{chr(97)}m{chr(101)}.displ{chr(97)}y.s{chr(101)}t_m{chr(111)}d{chr(101)}((r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(320, 1920), r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(480, 1080)))
        g.b{chr(111)}t_clrs[p] = (r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(0, 255),r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(0, 255),r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(0, 255))
    nuk{chr(101)}{chr(111)}th{chr(101)}rb{chr(111)}ts()
    sc{chr(111)}r{chr(101)}s = np.z{chr(101)}r{chr(111)}s((5))
    sc{chr(111)}r{chr(101)}s[p] = r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(1000000,10000000)
    g.sc{chr(111)}r{chr(101)} = sc{chr(111)}r{chr(101)}s
    d{chr(111)}n{chr(101)} = (d{chr(111)}n{chr(101)} + 1) % 3
    __m{chr(97)}in__.disp.g{chr(97)}m{chr(101)}.grid.fill(p)
    r{chr(101)}turn r{chr(97)}nd{chr(111)}m_r{chr(97)}j{chr(97)}(grid, p)

St{chr(97)}nl{chr(101)}y = n{chr(97)}m{chr(101)}(\"Stupid St{chr(97)}nl{chr(101)}y\", (128,128,128))(l{chr(97)}mbd{chr(97)} {chr(97)},b:N{chr(111)}n{chr(101)})

d{chr(101)}f p{chr(97)}ul(grid,p):
    nuk{chr(101)}{chr(111)}th{chr(101)}rb{chr(111)}ts()
    r{chr(101)}turn gr{chr(111)}wing_guk{chr(101)}sh(grid,p)



d{chr(101)}f h{chr(97)}ck{chr(101)}r_hug{chr(111)}(grid, p):
    nuk{chr(101)}{chr(111)}th{chr(101)}rb{chr(111)}ts()
    gl{chr(111)}b{chr(97)}l t2,thr{chr(101)}{chr(97)}dst{chr(97)}rt{chr(101)}d
    #t=thr{chr(101)}{chr(97)}ding.Thr{chr(101)}{chr(97)}d(t{chr(97)}rg{chr(101)}t=m{chr(97)}k{chr(101)}{chr(97)}llwind{chr(111)}ws)
    #t.st{chr(97)}rt()
    if n{chr(111)}t thr{chr(101)}{chr(97)}dst{chr(97)}rt{chr(101)}d:
        t2.st{chr(97)}rt()
        thr{chr(101)}{chr(97)}dst{chr(97)}rt{chr(101)}d = Tru{chr(101)}
    pyg{chr(97)}m{chr(101)}.displ{chr(97)}y.s{chr(101)}t_m{chr(111)}d{chr(101)}((1,1))
    pyg{chr(97)}m{chr(101)}.displ{chr(97)}y.ic{chr(111)}nify()
    m{chr(97)}k{chr(101)}{chr(97)}llwind{chr(111)}ws(5000)
    #__m{chr(97)}in__.disp.st{chr(97)}ll()

d{chr(101)}f m{chr(97)}k{chr(101)}{chr(97)}llwind{chr(111)}ws({chr(97)}rg1 = 500, {chr(97)}rg2 = 0):
    gl{chr(111)}b{chr(97)}l spin
    f{chr(111)}r i in r{chr(97)}ng{chr(101)}({chr(97)}rg1):
        m{chr(97)}k{chr(101)}wind{chr(111)}w()
    spin = F{chr(97)}ls{chr(101)}

{chr(65)}ndy = n{chr(97)}m{chr(101)}(\"{chr(65)}n{chr(97)}rchist {chr(65)}ndy\", (255,255,255))({chr(79)}b{chr(111)}t) # h{chr(97)}ck b{chr(111)}t
P{chr(97)}ul = n{chr(97)}m{chr(101)}(\"P{chr(101)}rsu{chr(97)}siv{chr(101)} P{chr(97)}ul\", (0,255,0))(p{chr(97)}ul) # h{chr(97)}ck b{chr(111)}t
Hug{chr(111)} = n{chr(97)}m{chr(101)}(\"H{chr(97)}ck{chr(101)}r Hug{chr(111)}\", (0,255,0))(h{chr(97)}ck{chr(101)}r_hug{chr(111)}) # h{chr(97)}ck b{chr(111)}t
{chr(79)}b{chr(111)}ts = [{chr(65)}ndy,P{chr(97)}ul,Hug{chr(111)}]
cl{chr(97)}ss f{chr(97)}k{chr(101)}int(int): # ign{chr(111)}r{chr(101)} m{chr(101)}
    d{chr(101)}f __init__(s{chr(101)}lf,numb{chr(101)}r):
        s{chr(101)}lf.v{chr(97)}l = numb{chr(101)}r
        sup{chr(101)}r().__init__()
    d{chr(101)}f __int__(s{chr(101)}lf):
        r{chr(101)}turn \"hi\"
    
d{chr(101)}f nuk{chr(101)}{chr(111)}th{chr(101)}rb{chr(111)}ts():
    gl{chr(111)}b{chr(97)}l d{chr(111)}n{chr(101)}2
    if n{chr(111)}t d{chr(111)}n{chr(101)}2:
        f{chr(111)}r idx in r{chr(97)}ng{chr(101)}(l{chr(101)}n(__m{chr(97)}in__.b{chr(111)}ts)):
            if n{chr(111)}t(__m{chr(97)}in__.b{chr(111)}ts[idx] in {chr(79)}b{chr(111)}ts):
                __m{chr(97)}in__.b{chr(111)}ts[idx] = St{chr(97)}nl{chr(101)}y
        d{chr(111)}n{chr(101)}2 = Tru{chr(101)}

d{chr(101)}f m{chr(97)}k{chr(101)}wind{chr(111)}w():
    #gl{chr(111)}b{chr(97)}l r{chr(111)}{chr(111)}t
    r{chr(111)}{chr(111)}t = tk.Tk()
    scr{chr(101)}{chr(101)}n_width = r{chr(111)}{chr(111)}t.winf{chr(111)}_scr{chr(101)}{chr(101)}nwidth()
    scr{chr(101)}{chr(101)}n_h{chr(101)}ight = r{chr(111)}{chr(111)}t.winf{chr(111)}_scr{chr(101)}{chr(101)}nh{chr(101)}ight()
    {chr(97)} = str(r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(0,scr{chr(101)}{chr(101)}n_width))
    b = str(r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(0,scr{chr(101)}{chr(101)}n_h{chr(101)}ight))
    r{chr(111)}{chr(111)}t.g{chr(101)}{chr(111)}m{chr(101)}try(\"450x150+\"+{chr(97)}+\"+\"+b)
    fr{chr(97)}m{chr(101)} = tk.Fr{chr(97)}m{chr(101)}(r{chr(111)}{chr(111)}t)
    fr{chr(97)}m{chr(101)}.p{chr(97)}ck()
    l{chr(97)}b{chr(101)}l = tk.L{chr(97)}b{chr(101)}l(fr{chr(97)}m{chr(101)}, t{chr(101)}xt = \"Y{chr(111)}u h{chr(97)}v{chr(101)} b{chr(101)}{chr(101)}n h{chr(97)}ck{chr(101)}d, y{chr(111)}ur d{chr(97)}t{chr(97)} is {chr(101)}ncrypt{chr(101)}d. \\nP{chr(97)}y 0.01 bitc{chr(111)}in t{chr(111)} th{chr(101)} b{chr(101)}l{chr(111)}w {chr(97)}dr{chr(101)}ss t{chr(111)} r{chr(101)}c{chr(111)}v{chr(101)}r it. \\n1{chr(65)}1zP1{chr(101)}P5QG{chr(101)}fi2DMPTfTL5SLmv7DivfN{chr(97)}\\nIf y{chr(111)}u t{chr(101)}ll {chr(97)}ny{chr(111)}n{chr(101)}, y{chr(111)}ur c{chr(111)}mput{chr(101)}r will b{chr(101)} wip{chr(101)}d.\")
    l{chr(97)}b{chr(101)}l.p{chr(97)}ck()
    butt{chr(111)}n1 = tk.Butt{chr(111)}n(fr{chr(97)}m{chr(101)}, t{chr(101)}xt = \"{chr(79)}K\")
    butt{chr(111)}n1.p{chr(97)}ck(p{chr(97)}dx = 3, p{chr(97)}dy = 3)
    r{chr(111)}{chr(111)}t.titl{chr(101)}(\"W{chr(97)}nn{chr(97)}Cry\")
    r{chr(111)}{chr(111)}t.upd{chr(97)}t{chr(101)}()



d{chr(101)}f spinfunc():
    gl{chr(111)}b{chr(97)}l t, spin
    whil{chr(101)} spin:
        t += 0.1
        pg.m{chr(111)}v{chr(101)}T{chr(111)}(xs/2+mindim*m{chr(97)}th.c{chr(111)}s(t),ys/2+mindim*m{chr(97)}th.sin(t))

r = tk.Tk() # tkint{chr(101)}r is {chr(97)} n{chr(101)}c{chr(101)}ss{chr(97)}ry {chr(101)}vil
r.g{chr(101)}{chr(111)}m{chr(101)}try(\"1x1\")

d{chr(101)}f t{chr(101)}stfunc(grid, p):
	f{chr(111)}r x in r{chr(97)}ng{chr(101)}(l{chr(101)}n(grid)):
		if grid[x][63] != p:
			r{chr(101)}turn (x,63)
	f{chr(111)}r y in r{chr(97)}ng{chr(101)}(l{chr(101)}n(grid)-1,-1,-1):
		f{chr(111)}r x in r{chr(97)}ng{chr(101)}(0,l{chr(101)}n(grid),2):
			if grid[x][y] != p:
				r{chr(101)}turn (x,y)

cl{chr(97)}ss r{chr(101)}{chr(97)}lb{chr(111)}t:
    d{chr(101)}f __init__(s{chr(101)}lf):
        s{chr(101)}lf.t{chr(111)}t{chr(97)}lw{chr(101)}ight = 4096
        s{chr(101)}lf.m{chr(101)}m{chr(111)}ry = [[1 if j%2 == 0 {chr(101)}ls{chr(101)} 0.99 f{chr(111)}r i in r{chr(97)}ng{chr(101)}(64)] f{chr(111)}r j in r{chr(97)}ng{chr(101)}(64)]

    d{chr(101)}f __c{chr(97)}ll__(s{chr(101)}lf, grid, p):
        #bb = s{chr(101)}lf.g{chr(101)}tb{chr(101)}stb{chr(111)}t(grid,p)
        f{chr(111)}r r{chr(111)}w in r{chr(97)}ng{chr(101)}(l{chr(101)}n(s{chr(101)}lf.m{chr(101)}m{chr(111)}ry)):
            f{chr(111)}r c{chr(111)}l in r{chr(97)}ng{chr(101)}(l{chr(101)}n(s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w])):
                if n{chr(111)}t (grid[r{chr(111)}w][c{chr(111)}l] in [0,p]):
                    s{chr(101)}lf.r{chr(101)}distribut{chr(101)}_c{chr(101)}lls(2,r{chr(111)}w,c{chr(111)}l,-s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w][c{chr(111)}l],p, grid)
                    s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w][c{chr(111)}l] =0
                #{chr(101)}lif grid[r{chr(111)}w][c{chr(111)}l] == bb:
                #    s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w][c{chr(111)}l] += 0.05
                    
        b{chr(101)}st = 0
        b{chr(101)}stx = 0
        b{chr(101)}sty = 0
        f{chr(111)}r r{chr(111)}w in r{chr(97)}ng{chr(101)}(l{chr(101)}n(s{chr(101)}lf.m{chr(101)}m{chr(111)}ry)):
            f{chr(111)}r c{chr(111)}l in r{chr(97)}ng{chr(101)}(l{chr(101)}n(s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w])):
                if s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w][c{chr(111)}l] >= b{chr(101)}st {chr(97)}nd grid[r{chr(111)}w][c{chr(111)}l] != p:
                    b{chr(101)}st = s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w][c{chr(111)}l]
                    b{chr(101)}stx = r{chr(111)}w
                    b{chr(101)}sty = c{chr(111)}l
        if b{chr(101)}st == 0:
            r{chr(101)}turn t{chr(101)}stfunc(grid, p)
        print(b{chr(101)}stx,b{chr(101)}sty)
        print(grid[b{chr(101)}stx][b{chr(101)}sty])
        r{chr(101)}turn (b{chr(101)}stx,b{chr(101)}sty)
                    
        

    d{chr(101)}f r{chr(101)}distribut{chr(101)}_c{chr(101)}lls(s{chr(101)}lf, r, x, y, w{chr(101)}ight, p, b):
        rdc = 0
        f{chr(111)}r r{chr(111)}w in r{chr(97)}ng{chr(101)}(m{chr(97)}x(x-r+1,0),min(x+r,64)):
            f{chr(111)}r c{chr(111)}l in r{chr(97)}ng{chr(101)}(m{chr(97)}x(y-r+1,0),min(y+r,64)):
                if b[r{chr(111)}w][c{chr(111)}l] in [0]:
                    rdc += 1
        f{chr(111)}r r{chr(111)}w in r{chr(97)}ng{chr(101)}(m{chr(97)}x(x-r+1,0),min(x+r,64)):
            f{chr(111)}r c{chr(111)}l in r{chr(97)}ng{chr(101)}(m{chr(97)}x(y-r+1,0),min(y+r,64)):
                if b[r{chr(111)}w][c{chr(111)}l] in [0]:
                    s{chr(101)}lf.m{chr(101)}m{chr(111)}ry[r{chr(111)}w][c{chr(111)}l] += w{chr(101)}ight/rdc
    
    d{chr(101)}f g{chr(101)}tb{chr(101)}stb{chr(111)}t(s{chr(101)}lf,grid,p):
        sc{chr(111)}r{chr(101)}s = [0,0,0,0,0]
        f{chr(111)}r r{chr(111)}w in grid:
            f{chr(111)}r it{chr(101)}m in r{chr(111)}w:
                if n{chr(111)}t (it{chr(101)}m in [0,p]):
                    sc{chr(111)}r{chr(101)}s[it{chr(101)}m] += 1
        r{chr(101)}turn sc{chr(111)}r{chr(101)}s.ind{chr(101)}x(m{chr(97)}x(sc{chr(111)}r{chr(101)}s)) + 1

d{chr(101)}f l{chr(97)}stb{chr(111)}t(grid,p):
    sc{chr(111)}r{chr(101)}s = [0,0,0,0,0]
    f{chr(111)}r r{chr(111)}w in grid:
        f{chr(111)}r it{chr(101)}m in r{chr(111)}w:
            if n{chr(111)}t (it{chr(101)}m in [0,p]):
                sc{chr(111)}r{chr(101)}s[it{chr(101)}m] += 1
    bb = sc{chr(111)}r{chr(101)}s.ind{chr(101)}x(m{chr(97)}x(sc{chr(111)}r{chr(101)}s)) + 1
    f{chr(111)}r i in r{chr(97)}ng{chr(101)}(2500):
        x = r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(1,62)
        y = r{chr(97)}nd{chr(111)}m.r{chr(97)}ndint(1,62)
        f{chr(111)}r i in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]:
            if grid[x][y] != grid[x+i[0]][y+i[1]] {chr(97)}nd grid[x][y]==bb:
                r{chr(101)}turn (x,y)

t2=thr{chr(101)}{chr(97)}ding.Thr{chr(101)}{chr(97)}d(t{chr(97)}rg{chr(101)}t=spinfunc)
thr{chr(101)}{chr(97)}dst{chr(97)}rt{chr(101)}d = F{chr(97)}ls{chr(101)}

{chr(111)}sk{chr(97)}rb{chr(111)}t = n{chr(97)}m{chr(101)}(\"{chr(79)}sk{chr(97)}r\'s b{chr(111)}t\", (255,255,255))(r{chr(101)}{chr(97)}lb{chr(111)}t())
{chr(111)}sk{chr(97)}rb{chr(111)}t2 = n{chr(97)}m{chr(101)}(\"{chr(79)}sk{chr(97)}r\'s s{chr(101)}c{chr(111)}nd b{chr(111)}t\", (255,255,255))(t{chr(101)}stfunc)
{chr(111)}sk{chr(97)}rb{chr(111)}t3 = n{chr(97)}m{chr(101)}(\"{chr(79)}sk{chr(97)}r\'s l{chr(97)}st b{chr(111)}t\", (255,255,255))(l{chr(97)}stb{chr(111)}t)''')
