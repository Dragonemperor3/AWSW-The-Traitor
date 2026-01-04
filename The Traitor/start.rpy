label traitor_start:
    default Izumi_betrayed = False 
    default dragons_betrayed = False
    $ evil_points = 0
    $ save_name = (_("Traitor"))
    #this will increase when the player is being a dick. 
    $ renpy.pause(2.0)
    scene kolcitynight at Pan ((0, 360), (0, 0), 4) with fade
    #slowly pans the screen
    $ renpy.pause(3.0)
    c "Ah, it's good to be home."
    scene kolmchousenight with fade
    m "I better keep this generator safe tonight. Tomorrow, I'll show everyone what I got and get ready for the praise."
    scene black with fade
    $ renpy.pause(4.0)
    scene kolmchouseday with fade
    $ renpy.pause(2.0)
    show logan surprised with dissolve
    define lg = "logan"
    stop music fadeout 2
    play music "mx/finally_home_kol.ogg" fadein 1
    play sound "fx/door/door_open.wav"
    lg "Ambassador [player_name]? What are you doing here?"
menu:
    "Why are you in my house?":
        c "I could ask you the same question, Logan. Why are you in my house?"
        $ evil_points += 1
        show logan annoyed with dissolve
        lg "It's not that hard to tell that the portal was used."
        lg "Well, how did the deal with the dragons go?"
    "Hi Logan!":
        c "Hey Logan, long time no see!"
        show logan smiling with dissolve
        lg "Hey Delta! Welcome back!"
        lg "How did the deal with the dragons go?"
menu:
    "Say it went well":
        c "It went pretty smoothly. The deal was over quickly; I got a generator, and they got my PDA."
        show logan smiling with dissolve
        lg "That's great to hear!"
        show logan serious with dissolve
        lg "But why did it take so long to get back?"
        jump question
    "Demonize the dragons":
        $ dragons_betrayed = True
        c "The dragons are evil! Shut down the portal NOW!"
        show logan surprised with dissolve
        lg "What? What do you mean they're evil?"
        c "They killed Reza and almost got me! I just narrowly escaped!"
        show logan serious with dissolve
        $ evil_points += 2
        lg "I'll shut the portal down right away!"
        hide logan with dissolve
        $ renpy.pause(2)
        show logan serious with dissolve
        lg "The portal is off. Those dragons shouldn't attack us."
        lg "But why did it take so long to get back if the dragons wanted you dead? Why didn't you head back right away?"
        jump question
label question:
        menu:
            "The portal broke and I had to fix it.":
                $ evil_points +=1
            "The portal broke and Izumi had to fix it.":
                pass
            "The generator was hard to get.":
                if evil_points > 100:
                    c "The dragons refused to give me their generator, so I had to take it by force."
                    $ evil_points += 1
                else:
                    c "The dragons took their sweet time giving me the generator."
        lg "I see."
        jump player_help
label player_help:
    show logan serious with dissolve
    lg "So, are you going to help us rebuild with this new generator?"
    c "Do I have much choice?"
    show logan normal with dissolve
    lg "Nope!"
    c "Figured."
    show logan surprised with dissolve
    lg "Are you ok, [player_name]? You're usually more optimistic!"
    c "Sorry, I'm still mentally tired from the experience."
    show logan normal with dissolve
    lg "Fair enough. Now come on, let's go!"
    hide logan with dissolve
    c "Wait for me!"
    stop music fadeout 2
    play music "mx/saviour_kol.ogg" fadein 1
    scene kolcitycentre at Pan ((0, 360), (0, 0), 4) with fade
    $ renpy.pause(2)
    m "With me having to carry the generator, I could not catch up with Logan."
    m "Still, people have given me hopeful looks, as I was expecting."
    scene kolfactoryout at Pan ((0, 0), (0, 60), 4) with fade
    $ renpy.pause(2)
    show logan normal with dissolve
    c "Is this the food factory?"
    show logan smiling with dissolve
    lg "Sure is! With this new generator, we'll be able to get our factories running again."
    scene kolfactory1 at Pan((0, 360), (0, 0), 4) with fade
    $ renpy.pause(4)
    show logan normal with dissolve
    c "So... what's the plan?"
    lg "I've mostly been alone, since other qualified engineers are at the hospital, sick and hungry."
    show logan smiling with dissolve
    lg "With this generator, we can produce enough food to feed them."
    menu:
        "I see.":
            pass
        "Why not power the hospital?":
            lg "We will, we just need to get parts necessary for the upgrade."
    show logan serious with dissolve
    lg "Can I have a closer look at that generator?"
    m "You put down the generator in front of Logan."
    $ renpy.pause(2)
    show logan normal with dissolve
    lg "Yes, I can definitely improve this generator. All I need are some scrap parts."
    lg "[player_name], can you get them for me?"
    menu:
        "Sure":
            pass
        "Why can't you get them yourself?":
            show logan annoyed with dissolve
            $ evil_points += 1
            lg "..."
            lg "Sure, I'll just be everywhere at once."
            lg "I can't work on the generator and get parts. Just bring me anything you think could be useful."
    scene kolfactory2 with fade
    play music "mx/ruin_kol.ogg" 
    c "Wow. I knew the factory condition was bad, but after being inside here for the first time, I can say it's worse than I thought."
    $ renpy.pause(2)
    s "Find any part that could be useful and bring them to Logan."
    s "You can only carry one part at a time, though."
    default current_item = None
    default needs_wires = True
    default needs_plates = True #using a list gets me a NameError. Believe me, i tried that first
    default needs_screws = True
    default new_item = None
    jump factory_minigame

label factory_minigame:
    if True: #i dont want to unindent the whole block below this
        menu:
            "Search cardboard boxes":
                s "You found some boxes full of wires!"
                $ new_item = "Wires"
                jump NewItem
            "Search storage":
                s "You found metal plates!"
                $ new_item = "Plates"
                jump NewItem
            "Search small boxes":
                s "You found some screws!"
                $ new_item = "Screws"
                jump NewItem
            "Search trash can":
                s "You found some paper waste!"
                $ new_item = "Paper"
                jump NewItem
            "Return to Logan":
                scene kolfactory1 with fade
                show logan normal with dissolve
                lg "Let's see what you got!"
                $ has_item = False
                if current_item == "Wires" and needs_wires == True:
                    $ needs_wires = False
                    $ has_item = True
                elif current_item == "Plates" and needs_plates == True:
                    $ needs_plates = False
                    $ has_item = True
                elif current_item == "Screws" and needs_screws == True:
                    $ needs_screws = False
                    $ has_item = True
                if current_item == None:
                    show logan annoyed with dissolve
                    lg "[player_name], you didn't bring me anything. Please go back there and get me something."
                elif has_item:
                    show logan smiling with dissolve
                    lg "Nice, I'll need this!"
                    $ current_item = None
                else:
                    show logan serious with dissolve
                    lg "Thanks, [player_name], but I don't need this." 
    if needs_wires == False and needs_plates == False and needs_screws == False:
        lg "Good job, we got everything we needed!"
        stop music fadeout 2
        jump minigame_done
    else:
        hide logan with dissolve
        scene kolfactory2 with fade
        jump factory_minigame
label NewItem:
    s "Current item: [current_item] \nWould you like to pick up the new item?"
    menu:
        "Yes":
            if current_item == None:
                s "You picked up [new_item]."
            else:
                s "You dropped [current_item] and picked up [new_item]."
            $ current_item = new_item
        "No":
            pass
    jump factory_minigame