import os
import pygame
import time
import urllib2
import json
from signal import alarm, signal, SIGALRM

# creates a small API to get stock data given symbol and market
class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="

    def get(self,symbol,exchange):
        url = self.prefix+"%s:%s"%(exchange,symbol)
        u = urllib2.urlopen(url)
        content = u.read()

        obj = json.loads(content[3:])
        return obj[0]

#set up the screen so we can push stuff onto it.
class pitft :
    screen = None
    colourBlack = (0, 0, 0)

    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)

        os.putenv('SDL_FBDEV', '/dev/fb1')

        # Select frame buffer driver
        # Make sure that SDL_VIDEODRIVER is set
        driver = 'fbcon'
        if not os.getenv('SDL_VIDEODRIVER'):
            os.putenv('SDL_VIDEODRIVER', driver)
        class Alarm(Exception):
            pass
        def alarm_handler(signum, frame):
            raise Alarm
        signal(SIGALRM, alarm_handler)
        alarm(3)
        try:
            pygame.display.init()
            print 'getting screen size'
            size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            self.screen = pygame.display.set_mode(size, 0, 32)
            alarm(0)
        except Alarm:
            raise KeyboardInterrupt
        print 'setting up framebuffer'



        # Clear the screen to start
        self.screen.fill((0, 0, 0))
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

def main():
    #this path is where we store our arrow icons
    installPath = "/usr/src/app/img/"
    print 'starting main()'
    # font colours
    colourWhite = (255, 255, 255)
    colourBlack = (0, 0, 0)
    colourGreen = (3, 192, 60)
    colourRed = (220, 69, 69)

    #this is how often we check for new stocks
    updateRate = 180 # seconds

    # Create an instance of the pitft class
    mytft = pitft()

    #hide the mouse from screen
    pygame.mouse.set_visible(False)

    # set up the fonts
    # choose the font
    fontpath = pygame.font.match_font('dejavusansmono')
    font = pygame.font.Font(fontpath, 40)

    #create instance of stock api
    c = GoogleFinanceAPI()

    #read the ENV VAR, use GE if 'STOCK' isn't there
    companyName = os.getenv('STOCK', "GE")
    print 'company name: '+companyName

    #The default MARKET is NASDAQ
    marketName = os.getenv('MARKET', "NASDAQ")
    print 'market name: '+marketName

    while True:
        quote = c.get(companyName,marketName)
        stockTitle = 'Stock: ' + str(quote["t"])
        print stockTitle
        stockPrice = 'Price: $' + str(quote["l_cur"])
        print stockPrice
        stockChange = str(quote["c"])
        print stockChange
        stockPercentChange = '(' + str(quote["cp"]) + '%)'
        print stockPercentChange

        #check if + or -, and display correct arrow and font color
        if float(quote["c"]) < 0:
            changeColour = colourRed
            arrowIcon = "red_arrow.png"
            print 'font colour red'
        else:
            changeColour = colourGreen
            arrowIcon = "green_arrow.png"
            print 'font colour green'

        # clear the screen
        mytft.screen.fill(colourBlack)
        # set the anchor/positions for the current stock data text
        textAnchorX = 10
        textAnchorY = 10
        textYoffset = 40

        #print the stock title to screen
        text_surface = font.render(stockTitle, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))

        #print the stock price to screen
        textAnchorY+=textYoffset
        text_surface = font.render(stockPrice, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))

        #print the stock change value to screen
        textAnchorY = textAnchorY + textYoffset*2
        text_surface = font.render(stockChange, True, changeColour)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))

        #print the stock change percentage to screen
        textAnchorY+=textYoffset
        text_surface = font.render(stockPercentChange, True, changeColour)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))

        #add the icon to the screen
        icon = installPath+ arrowIcon
        logo = pygame.image.load(icon).convert()
        mytft.screen.blit(logo, (220, 140))

        # refresh the screen with all the changes
        pygame.display.update()

        # Wait 'updateRate' seconds until next update
        time.sleep(updateRate)

if __name__ == '__main__':
    print 'starting main()'
    main()
