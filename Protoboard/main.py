import pygame

pygame.init()


screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Proto")

white = (255, 255, 255)
dark_grey = (222, 222, 222)
grey = (207, 207, 207)


rect_width = 500  # Ancho
rect_height = 260  # Alto


running = True
while running:

    screen.fill(white)

    rect_x = (screen_width - rect_width) // 2
    rect_y = (screen_height - rect_height) // 2

    rect_line_x = (screen_width - rect_width)//2
    rect_line_y = (screen_height - rect_height)

    pygame.draw.rect(screen, dark_grey, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(screen, grey, (rect_line_x, rect_line_y, rect_width, 20))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()