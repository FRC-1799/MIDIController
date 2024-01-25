# #!/usr/bin/env python
# #
# # midiin_poll.py
# #
# """Show how to receive MIDI input by polling an input port."""

# from __future__ import print_function

# import logging
# import sys
# import time
# from wpilib import SmartDashboard

# from rtmidi.midiutil import open_midiinput


# log = logging.getLogger('midiin_poll')
# logging.basicConfig(level=logging.DEBUG)

# # Prompts user for MIDI input port, unless a valid port number or name
# # is given as the first argument on the command line.
# # API backend defaults to ALSA on Linux.
# port = sys.argv[1] if len(sys.argv) > 1 else None

# try:
#     midiin, port_name = open_midiinput(port)
# except (EOFError, KeyboardInterrupt):
#     sys.exit()

# print("Entering main loop. Press Control-C to exit.")

# SmartDashboard.putNumber("value", 1)
# try:
#     timer = time.time()
#     while True:
#         msg = midiin.get_message()

#         if msg:
#             message, deltatime = msg
#             timer += deltatime
            

#         time.sleep(0.01)
# except KeyboardInterrupt:
#     print('')
# finally:
#     print("Exit.")
#     midiin.close_port()
#     del midiin


import pygame
import pygame.midi

pygame.init()
pygame.display.set_caption("MIDI Output")

screen = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 36)

pygame.midi.init()
player = pygame.midi.Input(1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if player.poll():
        midi_events = player.read(10)
        text = ""
        for midi_event in midi_events:
            text += str(midi_event[0][2]) + "\n"
        
        text_surface = font.render(text, True, (255, 255, 255))
        pygame.draw.rect(screen, "black", (0,0,1000,1000))
        screen.blit(text_surface, (50, 50))
        
        pygame.display.flip()
