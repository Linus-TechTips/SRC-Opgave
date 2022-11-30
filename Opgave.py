import arcade
import math

BREDDE = 800
HOEJDE = 600
SPORLAENGDE = 500
FARVE = arcade.csscolor.WHEAT

def linje(tid, stationaert_punkt, retningsvektor):
    """Returnerer x- og y-koordinaterne til et punkt på en ret linje.
    Er implementeret på helt samme måde, som i matematik."""
    x_0, y_0 = stationaert_punkt
    r_x, r_y = retningsvektor
    x = x_0 + r_x * tid
    y = y_0 + r_y * tid
    return x, y

def tegn(delta_tid):
    arcade.start_render()
    # Første punkt for linjen
    x, y = linje(tegn.tid, (0, 0), (90*math.cos(math.pi/6), 90*math.sin(math.pi/6)-0.5*9.82*tegn.tid))
    x1, y1 = linje(tegn.tid, (0, 0), (90 * math.cos(math.pi/3), 90 * math.sin(math.pi/3) - 0.5 * 9.82 * tegn.tid))
    x2, y2 = linje(tegn.tid, (0, 0), (90 * math.cos(45*math.pi / 180), 90 * math.sin(45*math.pi / 180) - 0.5 * 9.82 * tegn.tid))
    x3, y3 = linje(tegn.tid, (0, 0), (90 * math.cos(75*math.pi/180), 90 * math.sin(75*math.pi/180) - 0.5 * 9.82 * tegn.tid))
    x4, y4 = linje(tegn.tid, (0, 0), (90 * math.cos(15*math.pi/180), 90 * math.sin(15*math.pi/180) - 0.5 * 9.82 * tegn.tid))
    # Tegner punktet på linjen
    arcade.draw_circle_filled(x, y, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x1, y1, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x2, y2, 5 ,arcade.csscolor.PINK)
    arcade.draw_circle_filled(x3, y3, 5, arcade.csscolor.FOREST_GREEN)
    arcade.draw_circle_filled(x4, y4, 5, arcade.csscolor.ORANGE)
    # Fjerner det første punkt i sporet, hvis sporet er for langt
    if len(tegn.spor) > SPORLAENGDE:
        tegn.spor.pop(0)
    if len(tegn.spor2) > SPORLAENGDE:
        tegn.spor2.pop(0)
    if len(tegn.spor3) > SPORLAENGDE:
        tegn.spor3.pop(0)
    if len(tegn.spor4) > SPORLAENGDE:
        tegn.spor4.pop(0)
    if len(tegn.spor5) > SPORLAENGDE:
        tegn.spor5.pop(0)
    # Tegner sporet  for linjen
    for punkt in tegn.spor:
        arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.BLACK)
    for punkt in tegn.spor2:
        arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.WHITE)
    for punkt in tegn.spor3:
        arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.PINK)
    for punkt in tegn.spor4:
        arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.FOREST_GREEN)
    for punkt in tegn.spor5:
        arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.ORANGE)
    tegn.spor.append((x, y))
    tegn.spor2.append((x1, y1))
    tegn.spor3.append((x2, y2))
    tegn.spor4.append((x3, y3))
    tegn.spor5.append((x4, y4))
    tegn.tid += delta_tid * 6

def main():
    arcade.open_window(BREDDE, HOEJDE, "SRC projekt")

    arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

    tegn.tid = 0.0
    tegn.spor = list()
    tegn.spor2 = list()
    tegn.spor3 = list()
    tegn.spor4 = list()
    tegn.spor5 = list()

    arcade.schedule(tegn, 1 / 60)

    arcade.run()

main()