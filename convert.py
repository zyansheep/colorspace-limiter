from PIL import Image

color_list = {
    (int("FF", 16), int("45", 16), int("00", 16)): "r",  # bright red
    (int("FF", 16), int("A8", 16), int("00", 16)): "o",  # orange
    (int("FF", 16), int("D6", 16), int("35", 16)): "y",  # yellow
    (int("00", 16), int("A3", 16), int("68", 16)): "1",  # darker green
    (int("7E", 16), int("ED", 16), int("56", 16)): "g",  # lighter green
    (int("24", 16), int("50", 16), int("A4", 16)): "b",  # darkest blue
    (int("36", 16), int("90", 16), int("EA", 16)): "2",  # medium normal blue
    (int("51", 16), int("E9", 16), int("F4", 16)): "2",  # cyan
    (int("81", 16), int("1E", 16), int("9F", 16)): "3",  # darkest purple
    (int("B4", 16), int("4A", 16), int("C0", 16)): "p",  # normal purple
    (int("FF", 16), int("99", 16), int("AA", 16)): "4",  # pink
    (int("9C", 16), int("69", 16), int("26", 16)): "5",  # brown
    (int("00", 16), int("00", 16), int("00", 16)): "q",  # black
    (int("89", 16), int("8D", 16), int("90", 16)): "x",  # grey
    (int("D4", 16), int("D7", 16), int("D9", 16)): "6",  # light grey
    (int("FF", 16), int("FF", 16), int("FF", 16)): "w",  # white
}

file = open("output.txt", "w") 

output = ""
with Image.open("image.png") as im:
	print("image: (" + str(im.width) + ", " + str(im.height) + ")")
	for y in range(0, im.height):
		for x in range(0, im.width):
			pixel = im.getpixel((x, y))
			color_diff = 42398498237498
			best_color = (int("FF", 16), int("FF", 16), int("FF", 16))
			for color in color_list.keys():
				diff = abs(color[0] - pixel[0]) + abs(color[1] - pixel[1]) + abs(color[2] - pixel[2])
				if diff < color_diff:
					color_diff = diff
					best_color = color
			
			file.write(color_list[best_color])
		file.write("\n")

file.close()
			

				
