import curses

def main():
    while (True):
        key = scrn.getch()
        if (key != -1 and key != 10):
            print("Key:", key)


if __name__ == '__main__':
    try:
        scrn = curses.initscr()
        curses.nocbreak()
        curses.nl()
        scrn.nodelay(True)
        main()
    except KeyboardInterrupt:
        scrn.clear()
        scrn.refresh()
        curses.nocbreak()
        curses.endwin()