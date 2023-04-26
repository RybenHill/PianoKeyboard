import pygame
import pygame.midi
import sys
import soundUtils

# Inicializar pygame
pygame.init()
pygame.midi.init()

# Establecer dimensiones de la ventana
width = 600
height = 200

# Establecer colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Establecer dimensiones de las teclas
key_width = 50
key_height = 150
black_key_width = 30
black_key_height = 100

# FIXME - It only works with "octaves = 1"
octaves = 1

# Crear la ventana
screen = pygame.display.set_mode((width, height))

# Crear objeto MIDI
midi_out = pygame.midi.Output(0)
midi_out.set_instrument(0)

# Mapear notas MIDI a teclas del piano
midi_notes = {}
midi_notes = soundUtils.mapMIDI2Keyboard(midi_notes)

pygame.display.set_caption('MIDI Piano')


# FIXME - It only works with "octaves = 1"
def printPiano(octaves):
# Limpiar la pantalla
    screen.fill(GRAY)

    keysCount=7*octaves

    # Dibujar teclas blancas
    for i in range(keysCount):
        pygame.draw.rect(screen, BLACK, (i * key_width, 0, key_width, key_height))
        pygame.draw.rect(screen, WHITE, (i * key_width + 2, 2, key_width - 4, key_height - 4))

    # Dibujar teclas negras
    for i in range(keysCount):
        if i == 2 or i == 6:
            continue
        pygame.draw.rect(screen, BLACK, (i * key_width + key_width - black_key_width // 2, 0, black_key_width, black_key_height))
        pygame.draw.rect(screen, GRAY, (i * key_width + key_width - black_key_width // 2 + 2, 2, black_key_width - 4, black_key_height - 4))

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la ventana
    printPiano(octaves)
    pygame.display.update()

    # Detectar eventos de teclado
    keys = pygame.key.get_pressed()
    for key, note in midi_notes.items():
        if keys[key]:
            #print("PRESSED " + str(keys))
            midi_out.note_on(note, 127)
            #print("PLAY " + str(note))
        else:
            midi_out.note_off(note, 0)
