label minigame_done:
    play music "mx/hope_kol.ogg"
    lg "And good timing too, I'm almost done."
    m "Logan plays around with the generator for a few minutes."
    $ renpy.pause(2)
    lg "And... Done! Now to see if it works."
    play sound "fx/zap_kol.wav"
    $ renpy.pause (1)
    m "It makes some sparks, but afterwords it runs smoothly."
    lg "Voilà!"
    menu:
        "You're a genius!":
            lg "Aw, thanks!"
        "Does that mean we can save humanity?":
            lg "At this point, we might be able to."
        "You're just delaying the inevitable collapse of our city.":
            $ evil_points += 1
            show logan annoyed with dissolve
            lg "I think you're just being pessimistic."
    show logan normal with dissolve
    lg "With this baby, we can now power both the factories and the hospital, plus much more."
    lg "Take the rest of the day off. You've earned it!"
    m "Feeling like I helped enough, I take his advice. At least one of us will get sleep."
    scene kolcityevening at Pan((0, 360), (0, 0), 4) with fade
    $ renpy.pause(3)
    m "And I feel like that was a smart idea. The sun is already setting and I haven't eaten all day."
    scene kolmchouseevening with fade
    m "I make myself a sizeable dinner to make up for missing both breakfast and lunch."
    scene kolmchousenight with fade
    m "I decide to prepare myself for the next morning."
    scene black with fade
    stop music fadeout 2
    $ renpy.pause (3)
    scene kolmchouseday with fade
    m "Not wanting the same thing to happen twice, I make sure to find something to eat. Luckily, I still have dried meat and fruit."
    play sound "fx/knocking1.ogg"
    $ renpy.pause(2)
    c "Come in!"
    play sound "fx/door/door_open.wav"
    $ renpy.pause(1)
    show edmund with dissolve
    play music "mx/general.ogg" fadein 2
    define ed = Ed #I don't wanna capitalze every time
    ed "Hi [player_name]!"
    menu:
        "Good morning Sergeant!":
            ed "Good morning to you as well. Please, follow me."
            jump celebration
        "What are you doing here?":
            ed "That's no way to speak to me!"
            ed "Now, come with me."
            $ evil_points += 1
            jump celebration
label celebration:
    scene kolcitycentre with fade
    show edmund at right with dissolve
    show logan tsmiling flip at left with dissolve
    ed "Do you know why I called you here, Delta?"
    menu:
        "Yes":
            ed "Great! Then you know about the upcoming parade."
        "No":
            lg "Thanks to your generator, the hospital patients are making a great recovery."
            ed "That's right. We're gathered here to celebrate your heroic actions in the face of crises."
        "Still not getting any sleep, eh Logan?":
            show logan tannoyed flip with dissolve
            lg "Yeah yeah, I've heard it before."
            menu:
                "Yes":
                    ed "Great! Then you know about the upcoming parade."
                "No":
                    lg "Thanks to your generator, the hospital patients are making a great recovery."
                    ed "That's right. We're gathered here to celebrate your heroic actions in the face of crises."
            show logan tsmiling flip at left with dissolve
    lg "So cmon, let's pa-{w=0.5}{nw}" #nw force skips the text without player input
    stop music #i want an instant stop. no fadeout.
    "???" "WAIT!"
    show logan tannoyed flip at left with dissolve
    show edmund flip at Move((1.0, 1.0), (0.5, 1.0), 0.5, xanchor = 0.5, yanchor = 1.0) with dissolve
    show izumi normal at Move((1.0, 1.0), (1.0, 1.0), 0.5, xanchor = 1.0, yanchor = 1.0) with dissolve
    play music "mx/confrontation.ogg"
    As "Stop the celebration, now!"
    ed "Who are you? And why should I believe you?"
    #figure out how to take her costume 
    hide izumi with dissolve
    $ renpy.pause(0.5)
    image izumi uncloaked = "cr/izumi_normal_7_scar.png"
    show izumi uncloaked at right with dissolve
    Iz "There's something you don't know about [player_name]."
    Iz "They're lying about the deal."
    show logan tsurprised flip with dissolve
    lg "WHAT? [player_name], is this true?"
    menu:
        "Deny it":
            jump deny
        "Admit it":
            jump admit
label deny:
    stop music fadeout 1
    queue music "mx/martyr.ogg"
    $ Izumi_betrayed = True
    c "She's lying. She's jealous that she didn't get to save humanity."
    $ evil_points += 2
    c "She doesn't like me for some reason, so she's trying to slander me."
    Iz "..."
    Iz "If [player_name] doesn't want to tell the true story, then  I'll have to tell you what happened myself."
    scene black with dissolve
    window show
    n "I am a time traveller. Me and [player_name] constantly go back in time every time we fail to get the generators."
    n "This is not our first time. I got my scar from a previous attempt."
    n "Reza killed multiple dragons, and [player_name] killed Reza to take all the glory."
    n "As if that wasn't bad enough, they knew about an upcoming comet that could end civilization and did nothing about it."
    n "[player_name] was treated with respect by the dragons, but did not treat them the same way."
    n "Most likely, this whole thing was a setup by [player_name]."
    window hide
    nvl clear
    scene kolcitycentre with fade
    show logan tsurprised flip at left with dissolve
    show edmund flip with dissolve
    show izumi uncloaked at right with dissolve
    jump ending_choose
label admit:
    stop music fadeout 1
    queue music "mx/sad.ogg"
    c "Sadly, it's true."
    c "I'll tell you what really happened."
    scene black with dissolve
    window show
    n "The dragons treated me quite well. When I first entered the portal, I was greeted by a white dragon named Remy."
    n "Their society is similar to ours before the flare."
    n "However, there was a huge comet on the way to the planet. This comet could wipe out the entire civilization. Including the generators we needed."
    n "I may have doomed their kind by taking the generator."
    window hide
    nvl clear
    window show
    if evil_points >= 100:
        n "Reza did actually die, but the dragons didn't kill him. I did."
        n "However, Reza did kill multiple dragons himself to take the generator. I just took the credit for his work."
        n "I said they were evil so the portal would be shut down and the dragons could not come through and take their generator back."
        n "The dragons treated me like a king, and I was a jerk to them."
    else:
        n "I said the deal went well, but that's not exactly true."
        n "Reza went on a killing spree. I \"helped\" the police find him."
        n "I say helped in air quotes, because although I did help them, I was not polite to them."
        n "In fact, the dragons were happy to see a mythical human, so they treated me with kindness. I responded by verbally assaulting everyone."
    window hide
    scene kolcitycentre with fade
    show logan tsurprised flip at left with dissolve
    show edmund flip with dissolve
    show izumi uncloaked at right with dissolve
    c "And instead of waiting for the comet to pass, or even telling them about it, I took the generator home instantly."
    jump ending_choose
label ending_choose:
    lg "Wow! I cannot believe you would do something like this."
    stop music fadeout 2
    if evil_points <= 1:
        jump best_ending
    elif dragons_betrayed == False and Izumi_betrayed == False:
        jump good_ending
    elif (not dragons_betrayed and Izumi_betrayed) or (dragons_betrayed and not Izumi_betrayed):
        jump bad_ending
    else: #if you demonize the dragons AND deny Izumi's accusation, you get this automatically
        jump worst_ending
