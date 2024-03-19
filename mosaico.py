from PIL import Image

def repeat_image(input_image_path, output_image_path, rows, columns):
    # Abrir la imagen de entrada
    input_image = Image.open(input_image_path)
    
    # Obtener las dimensiones de la imagen de entrada
    input_width, input_height = input_image.size
    
    # Crear una nueva imagen con el tamaño multiplicado por el número de filas y columnas
    output_width = input_width * columns
    output_height = input_height * rows
    output_image = Image.new("RGB", (output_width, output_height))
    
    # Repetir la imagen en filas y columnas
    for y in range(rows):
        for x in range(columns):
            # Pegar la imagen de entrada en la posición actual
            output_image.paste(input_image, (x * input_width, y * input_height))
    
    # Guardar la imagen resultante
    output_image.save(output_image_path)

# Llamar a la función con los parámetros deseados
repeat_image("p.png", "output_image.jpg", 15, 15)
