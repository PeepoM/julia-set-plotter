from PIL import Image

# Image dimensions
WIDTH, HEIGHT = SIZE = 600, 600

# Colors
BLACK = 0, 0, 0

# Create new image with an RGB format
julia_image = Image.new("RGB", SIZE, BLACK)
pixels = julia_image.load()

SCALE = 200

# Constant complex number defining a specific Julia set
C = complex(-0.4, 0.6)

MODULUS_MAX = 10
MAX_ITER = 250

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2


def draw_julia_set():
    for y in range(-HALF_HEIGHT, HALF_HEIGHT):
        for x in range(-HALF_WIDTH, HALF_WIDTH):
            iterations = get_num_of_iters(x / SCALE, y / SCALE)
            color = get_pixel_color(iterations)

            pixels[x + HALF_WIDTH, y + HALF_HEIGHT] = color


def get_pixel_color(iterations):
    # If the pixel doesn't belong to the Julia set, set its color to black
    if iterations == MAX_ITER:
        return BLACK

    cont = int(255 * iterations / MAX_ITER)

    return cont, cont, cont


def get_num_of_iters(x, y):
    z = complex(x, y)

    for iteration in range(MAX_ITER):
        modulus = abs(z)

        if modulus > MODULUS_MAX:
            return iteration

        z = z**2 + C

    return MAX_ITER


if __name__ == "__main__":
    draw_julia_set()
    julia_image.save("generated-julia-set.png")
