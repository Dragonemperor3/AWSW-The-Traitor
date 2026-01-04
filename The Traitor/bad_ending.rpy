label bad_ending:
    $ save_name = (_("Traitor - Ending C"))
    play music "mx/exile_kol.ogg"
    ed "[player_name], don't tell me you have lied to our faces."
    Iz "I can prove that they have."
    m "Izumi shows Edmund and Logan evidence of her claims."
    show logan tserious flip at left with dissolve
    lg "..."
    lg "I thought you knew better than that, [player_name]..."
    ed "This is a very serious crime. We will tell the authorities about this."
    ed "In the meantime, we will have no choice but to put you under house arrest."
    ed "We will inform you when a decision is made."
    scene black with fade
    window show
    nvl clear
    n "The authorities were immediately told of my actions, and they were not happy."
    n "However, they found it hard to believe that their ambassador would do this. So they decide to hold a trial."
    n "Izumi submitted the evidence to the prosecutor. I was allowed a public defender."
    n "In the end, however, I was found guilty."
    n "They decided to hold me in jail until the day of my execution, which I was never told when."
    window hide
    nvl clear
    image jail = "bg/jail.png"
    scene jail at Pan((0, 286), (0, 0), 4) with fade
    $ renpy.pause(4)
    window show
    n "The conditions were terrible."
    n "I had to eat every meal like it was my last."
    n "People did come to visit, but the visits were not exactly reassuring."
    window hide
    nvl clear
    $ renpy.pause(1)
    image visitor_room = "bg/visitor_room.png"
    show edmund with dissolve
    ed "[player_name], you have a visitor."
    ed "Come with me."
    scene visitor_room with fade
    show logan surprised with dissolve
    lg "I still can't believe you're going to be hanged."
    image noose = "bg/noose.png"
    c "Yeah, well, nothing that can be done now."
    lg "There hasn't been an execution in years. This is big news."
    lg "Especially since it's you, humanity's last hope, that is being executed."
    c "How are people reacting to the news?"
    show logan serious with dissolve
    lg "Some want you released, others agree with the decision."
    lg "But the decision is final."
    lg "Like you said, nothing can be done about it."
    ed "Ok, Logan, you're out of time."
    lg "I'm sorry, but I have to go."
    c "I understand."
    lg "Goodbye, [player_name]."
    hide logan with dissolve
    scene jail with fade
    stop music fadeout 1
    play music "mx/prayer.ogg" fadein 1
    m "And I was back in my cell."
    scene black with fade
    $ renpy.pause(3)
    scene jail with fade
    m "Eventually, the day arrived."
    show edmund with dissolve
    ed "It's time."
    c "Let's just get this over with."
    $ renpy.pause(1)
    scene noose at Pan((0, 849), (0, 0), 4) with fade
    $ renpy.pause(4)
    m "This was it. My last moment of life."
    m "The noose was put around my neck, and the executioner put his hand over the lever."
    show edmund with dissolve
    ed "Any last words?"
    menu:
        "Yes":
            $ words = renpy.input("What would you like to say?")
            c "Yes, I'd like to say this:"
            c "[words]"
        "No":
            c "No, I don't have anything to say."
    ed "Ok then... pull the lever!"
    scene black with fade
    window show
    n "The lever was pulled, and a trapdoor opened below me."
    n "My neck instantly broke, and just like that, I was gone."
    window hide
    nvl clear
    stop music fadeout 1
    call ml_ending_check("traitor_ending", "bad", "You have seen the bad ending. Humanity starts to recover, but you don't get to experience it.")
    play sound "fx/system3.wav"
    s "Dev note: I don't know how to create custom credits, but I can tell you this mod was a solo project."
    s "However, it could not have been possible without Core or MagmaLink. So special thanks to the developers of those tools."
    s "And of course, credit to Saunders for the base game."
    s "And yes, those last few backgrounds were real photographs."
    jump ml_main_menu 