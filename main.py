#from networktables import NetworkTables
from networktables import NetworkTablesInstance
import pygame
import pygame.midi
#import ntcore
import ntcore

pygame.init()
pygame.display.set_caption("MIDI Output")

screen = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 36)

pygame.midi.init()

player = pygame.midi.Input(1)
clock = pygame.time.Clock()


nt = NetworkTablesInstance.getDefault()
nt.startClient("10.17.99.2")
table = nt.getTable("MidiTable") 
inst = ntcore.NetworkTableInstance.getDefault()


# connect to a roboRIO with team number TEAM
#inst.setServerTeam(1799, 5810)

# starting a DS client will try to get the roboRIO address from the DS application
#inst.startDSClient()

# connect to a specific host/port
#inst.setServer("host", ntcore.NetworkTableInstance.kDefaultPort4)


#table = NetworkTables.getTable("datatable")

#bankPublish = table.getDoubleTopic("HI________________1").publish()

buttonID = {
    "bankButton1": 1, 
    "bankButton2": 2, 
    "slider1": 3, 
    "slider2": 4, 
    "slider3": 5, 
    "slider4": 6, 
    "slider5": 7, 
    "slider6": 8, 
    "slider7": 9, 
    "slider8": 10, 
    "slider9": 11, 
    "dail1": 14, 
    "dail2": 15, 
    "dail3": 16, 
    "dail4": 17, 
    "dail5": 18, 
    "dail6": 19, 
    "dail7": 20, 
    "dail8": 21, 
    "dail9": 22, 
    "button1": 23,
    "button2": 24,
    "button3": 25,
    "button4": 26,
    "button5": 27,
    "button6": 28,
    "button7": 29,
    "button8": 30,
    "button9": 31,
    "record": 44,
    "pause": 45,
    "play": 46,
    "rewindLeft": 47,
    "rewindRight": 48,
    "replay": 49,
    "sliderAB": 60,
    "rightSilverDial": 64,
    "leftSilverDial": 67,
}

buttonValue = {
    "bankButton1":0, 
    "bankButton2":0, 
    "slider1":0, 
    "slider2":0, 
    "slider3":0, 
    "slider4":0, 
    "slider5":0, 
    "slider6":0, 
    "slider7":0, 
    "slider8":0, 
    "slider9":0, 
    "dail1":0, 
    "dail2":0, 
    "dail3":0, 
    "dail4":0, 
    "dail5":0, 
    "dail6":0, 
    "dail7":0, 
    "dail8":0, 
    "dail9":0, 
    "button1": 0,
    "button2": 0,
    "button3": 0,
    "button4": 0,
    "button5": 0,
    "button6": 0,
    "button7": 0,
    "button8": 0,
    "button9": 0,
    "record":0,
    "pause":0,
    "play":0,
    "rewindLeft":0,
    "rewindRight":0,
    "replay":0,
    "sliderAB":0,
    "rightSilverDial":0,
    "leftSilverDial":0 
}



def main(): 
    inputChecking()


def inputChecking():
    global player, clock, buttonValue
    while True:
        
        puttingValues(buttonValue)

        inst.startClient4("midiboard")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if player.poll():
            midi_events = player.read(10)
            
            changeValue = ""
            for midi_event in midi_events:
                
                changeValue += str(midi_event[0][1])
                for key, value in buttonID.items():
                    if midi_event[0][1] == value:
                        buttonValue[key] = changeValue
                        
                        
                        
            
            text_surface = font.render(changeValue, True, (255, 255, 255))
            pygame.draw.rect(screen, "black", (0,0,1000,1000))
            screen.blit(text_surface, (50, 50))
            
            clock.tick(1000)
            

            pygame.display.update()

def puttingValues(dictOfVals):
    global table
    for key, value in dictOfVals.items():
        table.putValue(key, value)


main()
