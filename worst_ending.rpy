label worst_ending:
    $ save_name = (_("Traitor - Ending D"))
    play music "mx/abandoned_lab_kol.ogg"
    c "Izumi is the real traitor."
    lg "W-what?"
    c "She's sympathetic to the dragons." #you have to demonize the dragons to get here
    c "She works with them to get their resources for herself."
    c "Why do you think she's accusing the person who brought the generator? She even fabricated evidence against me."
    c "This whole thing is a conspiracy against me."
    if evil_points <= 7: #being nice to everyone else gives you more legitimacy
        ed "Izumi, is there something you're not telling us?"
        Iz "No, everything I said was true."
        Iz "I found Reza's gun in [player_name]'s apartment. They had to have stolen it from him."
        show logan tserious flip at left with dissolve
        lg "[player_name], can you explain that?"
        c "I can. The dragons killed him, but couldn't use it themselves. I picked it up in self defence."
    else:
        show logan tserious flip at left with dissolve
        lg "I don't know, you haven't exactly been nice to us since you came back."
        c "And I'd like to apologize for everything I said."
        c "I was a bit stressed out from escaping their world, and I took out that stress on you and Sergeant Edmund."
        c "I will try to be better from now on." 
        lg "I hope you will."
    ed "We'll have to talk with both of you later."
    scene black with fade
    window show
    n "I knew I had to back up my legitimacy by reducing Izumi's."
    n "I managed to lead her to the outskirts of the city, away from people."
    n "Using Reza's gun, I shot her, making sure no one heard it."
    n "Then, I buried her body in the sand."
    n "If she doesn't show up, she can't argue her side."
    window hide
    nvl clear
    scene kolmchouseday with fade
    m "I rushed back to my apartment to avoid suspicion. With Izumi gone, I can claim she had something to hide."
    scene kolmchousenight with fade
    $ renpy.pause(1)
    m "Before I knew it, it was already dark."
    stop music
    play sound "fx/knocking1.ogg"
    $ renpy.pause(2)
    c "Come in!"
    play sound "fx/door/door_open.wav"
    $ renpy.pause(1)
    show edmund with dissolve
    ed "Come with me, please."
    play music "mx/amb/night.ogg"
    scene kolcitycentrenight with fade
    show edmund with dissolve
    c "Where are we going?"
    ed "I said I'd talk to you later. We will speak in private."
    ed "Logan is already waiting for you."
    scene kolsergeanthouse with fade
    $ renpy.pause(3)
    scene kolinsidesergeanthouse at Pan((0, 360), (0, 0), 3) with fade
    $ renpy.pause(3)
    show logan serious at right with dissolve
    show edmund flip at left with dissolve
    lg "Sergeant?"
    ed "Yes, Logan?"
    lg "What is the other woman's name? Ishman?"
    c "Izumi."
    lg "Right, Izumi. I couldn't find her."
    ed "What do you mean you couldn't find her?"
    lg "She wasn't at her house."
    c "Are you sure you got the right address?"
    lg "As sure as the sun rises."
    lg "[player_name], do you know anything about this?"
    c "I overheard something about her leaving the city."
    stop music 
    play music "mx/ashes_kol.ogg" fadein 1
    show logan surprised at right with dissolve
    lg "Leave the city? Why would she do that? It's dangerous out there!"
    c "She was scared of being found out, so she left to avoid execution."
    show logan serious at right with dissolve
    lg "But we're in the middle of a desert, and we have the generator. Why would she give that up?"
    c "She probably thought she can find supplies and survive longer than if she stayed and got charged with treason."
    ed "Damn. We can't send a search team after her. I guess it's just you."
    c "And there's something else you should probably know, too."
    ed "What is that?"
    c "We got robbed. The generator I recieved was less than we agreed upon."
    show logan surprised at right with dissolve
    $ renpy.pause(2)
    lg "Tell me you're joking."
    c "Nope, we need to bring justice to these dragons and save humanity. What if our generator dies or gets stolen? We need backups."
    ed "Then I will have to bring a force with me to the portal."
    scene black with fade
    window show
    stop music
    play music "mx/bricks_kol.ogg"
    n "And bring a force, he did."
    n "It took over a week to gather enough troops to march through the portal."
    n "The soldiers were told to constantly be on guard, and not let the dragons' kindness fool them."
    n "There was one problem: they were never told about the comet."
    n "By the time they realized I lied to them and that the dragons aren't monsters, it was already too late."
    window hide
    nvl clear
    window show
    n "One soldier even tried going back right as the comet hit."
    n "By sheer coincidence, the fireball managed to reach the portal gate right as it activated."
    n "The portal can transfer not just matter, but also energy."
    n "The blast went THROUGH the portal into our city, causing massive destruction."
    n "The generator, as well as many production facilities and factories, were destroyed or damaged even more."
    n "The city fell even faster than it would've if we didn't get the generator."
    window hide
    nvl clear
    stop music fadeout 1
    call ml_ending_check("traitor_ending", "worst", "You have seen the worst possible ending. Somehow you doomed both worlds. I hope you're happy.")
    play sound "fx/system3.wav"
    s "Dev note: I don't know how to create custom credits, but I can tell you this mod was a solo project."
    s "However, it could not have been possible without Core or MagmaLink. So special thanks to the developers of those tools."
    s "And of course, credit to Saunders for the base game."
    jump ml_main_menu