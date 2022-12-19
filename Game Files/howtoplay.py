from bearlibterminal import terminal as blt

def tutorial():
    #blt.open()
    blt.set('window.size=75x35')
    blt.color('white')
    tv = """
       ___________________________________________________________ 
      /                                                           \ 
      |  ______________________________________________________   |
      | /                                                      \  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | |                                                      |  |
      | \______________________________________________________/  |
      |                                                           |
      |                                             _       _     |
      |       ---------------------                (|)     (/)    |
      |                                                           |
      \___________________________________________________________/
"""
    blt.printf(1, 1, "" + tv)
    blt.printf(33, 1, '[color=yellow]* PARTE 1 *[/color]')
    blt.print(30, 7, "11 de Abril, 1994")
    blt.refresh()
    blt.delay(2000)
    blt.print(16, 8, "Tu encontras uma TV antiga com um Super-VHS")
    blt.refresh()
    blt.delay(2000) 
    blt.print(15, 9, "Explore um passado esquecido chamado TELETEXT")
    blt.refresh()
    blt.delay(2000)
    blt.printf(25, 11, '[color=red]E resolva seus enigmas...[/color]')
    blt.refresh()
    blt.delay(3000)

    blt.color('gray')
    blt.printf(1, 1, "" + tv)
    blt.refresh()
    blt.printf(33, 1, '[color=#3d3d08]* PARTE 1 *[/color]')
    blt.print(30, 7, "11 de Abril, 1994")
    blt.print(16, 8, "Tu encontras uma TV antiga com um Super-VHS")
    blt.print(15, 9, "Explore um passado esquecido chamado TELETEXT")
    blt.print(25, 11, 'E resolva seus enigmas...')
    blt.printf(25, 11, '[color=#4a171f]E resolva seus enigmas...[/color]')
    blt.refresh()
    blt.delay(1000)

    blt.color('#171717')
    blt.printf(1, 1, "" + tv)
    blt.refresh()
    blt.print(33, 1, '* PARTE 1 *')
    blt.print(30, 7, "11 de Abril, 1994")
    blt.print(16, 8, "Tu encontras uma TV antiga com um Super-VHS")
    blt.print(15, 9, "Explore um passado esquecido chamado TELETEXT")
    blt.print(25, 11, 'E resolva seus enigmas...')
    blt.print(25, 11, 'E resolva seus enigmas...')
    blt.refresh()
    blt.delay(1000)
    blt.clear()
    blt.refresh()
    blt.delay(2000)

    from main_noSong import main_menu
    main_menu()

# sinceramente nao sei, mas é importante
if __name__ == "__main__": 
    tutorial() 