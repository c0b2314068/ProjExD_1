import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    org_bg_img = pg.image.load("fig/pg_bg.jpg")
    flp_bg_img = pg.transform.flip(org_bg_img, 1, 0)
    pl_img = pg.transform.flip(pg.image.load("fig/3.png"), 1, 0)
    pl_img_rec = pl_img.get_rect()
    pl_img_rec.center = 300, 200
    bg_x = 0
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        dx, dy = 0, 0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            dy += -1
        if key_lst[pg.K_DOWN]:
            dy += 1
        if key_lst[pg.K_LEFT]:
            dx += -1
        if key_lst[pg.K_RIGHT]:
            dx += 3
        pl_img_rec.move_ip(dx-1, dy)

        screen.blit(org_bg_img, [-bg_x, 0])
        screen.blit(flp_bg_img, [-bg_x+1600, 0])
        screen.blit(org_bg_img, [-bg_x+3200, 0])
        screen.blit(flp_bg_img, [-bg_x+4800, 0])
        screen.blit(pl_img, pl_img_rec)
        pg.display.update()
        bg_x += 1
        bg_x %= 3200
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()