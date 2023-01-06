world = {
  "story": "Homunculus",
  "startnode": "1",
  "passages": [
    {
      "name": "First Room (WIP)",
      "tags": "",
      "pid": "1",
      "text": "You suddenly jolt into conciousness, as if awakened from a decade long slumber. Sitting up, you notice you're completely naked, surrounded by what looks like a glowing circle with strangely familiar runes on it. There is a large, steel door located along one of the walls. As your eyes get used to the dark of the room, you see a small white ID card with what used to be a picture and a name, but has been badly burned. You can barely make out the words \"Michael Clark\".\nAfter regaining the energy to stand, you slowly lurch to your feet. You can see your breath. Do you:\n[[Examine the room further->Examine the room further]]\n[[Check out the door->Check out the door]]",
      "links": [
        {
          "original": "[[Examine the room further->Examine the room further]]",
          "label": "Examine the room further",
          "newPassage": "Examine the room further",
          "pid": "2",
          "selection": "1"
        },
        {
          "original": "[[Check out the door->Check out the door]]",
          "label": "Check out the door",
          "newPassage": "Check out the door",
          "pid": "3",
          "selection": "2"
        }
      ],
      "cleanText": "You suddenly jolt into conciousness, as if awakened from a decade long slumber. Sitting up, you notice you're completely naked, surrounded by what looks like a glowing circle with strangely familiar runes on it. There is a large, steel door located along one of the walls. As your eyes get used to the dark of the room, you see a small white ID card with what used to be a picture and a name, but has been badly burned. You can barely make out the words \"Michael Clark\".\nAfter regaining the energy to stand, you slowly lurch to your feet. You can see your breath. Do you:"
    },
    {
      "name": "Examine the room further",
      "tags": "1",
      "pid": "2",
      "text": "Still struggling to make out shapes in the near pitch-black room, you shuffle around and feel dust or sand under your feet. Picking it up, it stains your hands- you can tell it's some sort of ash. The only light in the room surrounds the circle you woke up in. It's not made of chalk, or paint, rather something you've never quite seen before, when you get a closer look you could swear it quivered. \n[[Check out the door->Check out the door]]",
      "links": [
        {
          "original": "[[Check out the door->Check out the door]]",
          "label": "Check out the door",
          "newPassage": "Check out the door",
          "pid": "3",
          "selection": "1"
        }
      ],
      "cleanText": "Still struggling to make out shapes in the near pitch-black room, you shuffle around and feel dust or sand under your feet. Picking it up, it stains your hands- you can tell it's some sort of ash. The only light in the room surrounds the circle you woke up in. It's not made of chalk, or paint, rather something you've never quite seen before, when you get a closer look you could swear it quivered."
    },
    {
      "name": "Check out the door",
      "tags": "1",
      "pid": "3",
      "text": "As you move closer to the large door, you can tell that it's a bit dinged up. Pulling at it does nothing, and neither does pushing. With no other option, you charge at the door. Putting all of your weight into it, a couple attempts pass before the doorframe is empty and the steel door lies 10 feet behind it. You see a small room with flickering lights on the other side.\n[[Move into the room->Airlock]]",
      "links": [
        {
          "original": "[[Move into the room->Airlock]]",
          "label": "Move into the room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        }
      ],
      "cleanText": "As you move closer to the large door, you can tell that it's a bit dinged up. Pulling at it does nothing, and neither does pushing. With no other option, you charge at the door. Putting all of your weight into it, a couple attempts pass before the doorframe is empty and the steel door lies 10 feet behind it. You see a small room with flickering lights on the other side."
    },
    {
      "name": "Airlock",
      "tags": "",
      "pid": "4",
      "text": "You step through the doorway, into a small sterile room- only to face another door. Lining the walls are lockers and some sort of hyper sterile jumpsuits. The door leading outside seems in better condition than the one you busted open to get into this room. A jumpsuit is a hell of a lot better than being naked, so you put one on despite it not really fitting that well. \n[[Examine lockers->Examine lockers]]\n[[Attempt to open the door->Attempt to open door ]]",
      "links": [
        {
          "original": "[[Examine lockers->Examine lockers]]",
          "label": "Examine lockers",
          "newPassage": "Examine lockers",
          "pid": "5",
          "selection": "1"
        },
        {
          "original": "[[Attempt to open the door->Attempt to open door ]]",
          "label": "Attempt to open the door",
          "newPassage": "Attempt to open door",
          "pid": "6",
          "selection": "2"
        }
      ],
      "cleanText": "You step through the doorway, into a small sterile room- only to face another door. Lining the walls are lockers and some sort of hyper sterile jumpsuits. The door leading outside seems in better condition than the one you busted open to get into this room. A jumpsuit is a hell of a lot better than being naked, so you put one on despite it not really fitting that well."
    },
    {
      "name": "Examine lockers",
      "tags": "",
      "pid": "5",
      "text": "The lockers have small, glowing devices on where the handle would be, with a small slot that looks about the size of the ID card you found next to you when you awoke. \n[[Back to room->Airlock]]\n[[Attempt to open lockers->Attempt to open lockers]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Attempt to open lockers->Attempt to open lockers]]",
          "label": "Attempt to open lockers",
          "newPassage": "Attempt to open lockers",
          "pid": "7",
          "selection": "2"
        }
      ],
      "cleanText": "The lockers have small, glowing devices on where the handle would be, with a small slot that looks about the size of the ID card you found next to you when you awoke."
    },
    {
      "name": "Attempt to open door ",
      "tags": "1",
      "pid": "6",
      "text": "The door has a similar device attatched to it as the lockers that are also in the room- you swipe the ID you found. After a couple seconds, the door shudders open and slowly retreats to an open state. Red light floods into the airlock, pulsing from the numerous sirens. Suddenly, a warning bellows in your ears, seemingly from in the walls: \"ALERT: Primary generators OFFLINE, facility will be sealed once emergency power is drained. Recommendation: Director please collect all critical research and evacuate the facility\"\n[[Move into the large room->Hallway]]",
      "links": [
        {
          "original": "[[Move into the large room->Hallway]]",
          "label": "Move into the large room",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "1"
        }
      ],
      "cleanText": "The door has a similar device attatched to it as the lockers that are also in the room- you swipe the ID you found. After a couple seconds, the door shudders open and slowly retreats to an open state. Red light floods into the airlock, pulsing from the numerous sirens. Suddenly, a warning bellows in your ears, seemingly from in the walls: \"ALERT: Primary generators OFFLINE, facility will be sealed once emergency power is drained. Recommendation: Director please collect all critical research and evacuate the facility\""
    },
    {
      "name": "Attempt to open lockers",
      "tags": "2",
      "pid": "7",
      "text": "After a couple aggrevating tries at figuring out which locker the ID belongs to, you manage to open one. You see a pair of brown shoes, a small satchel, and a clean(ish) suit. \n[[Back to room->Airlock]]\n[[Search small bag->Search satchel]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Search small bag->Search satchel]]",
          "label": "Search small bag",
          "newPassage": "Search satchel",
          "pid": "8",
          "selection": "2"
        }
      ],
      "cleanText": "After a couple aggrevating tries at figuring out which locker the ID belongs to, you manage to open one. You see a pair of brown shoes, a small satchel, and a clean(ish) suit."
    },
    {
      "name": "Search satchel",
      "tags": "1",
      "pid": "8",
      "text": "Rummaging through the small bag, you find a locked tablet, tissues, a wallet, and a folder piece of paper. Opening it, you find that it appears to be some sort of speech. Filing through the wallet, you find a license with the same name ''\"Michael Clark\"''. No matter how hard you look into the picture on the card, you can't seem to make out the shape of a face and as you keep trying you find yourself developing a headache.\n[[Back to room->Airlock]]\n[[Read folded paper->Read folded paper]]\n[[Attempt to unlock tablet->Attempt to unlock tablet]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Read folded paper->Read folded paper]]",
          "label": "Read folded paper",
          "newPassage": "Read folded paper",
          "pid": "9",
          "selection": "2"
        },
        {
          "original": "[[Attempt to unlock tablet->Attempt to unlock tablet]]",
          "label": "Attempt to unlock tablet",
          "newPassage": "Attempt to unlock tablet",
          "pid": "10",
          "selection": "3"
        }
      ],
      "cleanText": "Rummaging through the small bag, you find a locked tablet, tissues, a wallet, and a folder piece of paper. Opening it, you find that it appears to be some sort of speech. Filing through the wallet, you find a license with the same name ''\"Michael Clark\"''. No matter how hard you look into the picture on the card, you can't seem to make out the shape of a face and as you keep trying you find yourself developing a headache."
    },
    {
      "name": "Read folded paper",
      "tags": "1",
      "pid": "9",
      "text": "Skimming the paper, it appears to be some sort of speech or presentation. It talks about the next generation of Humanity- how they will be stronger, smarter, and better than ever before. It yammers on about this for the entirety of the paper, and you are left feeling little dissapointed at how cheesy it sounds at parts. \n[[Back to room->Airlock]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        }
      ],
      "cleanText": "Skimming the paper, it appears to be some sort of speech or presentation. It talks about the next generation of Humanity- how they will be stronger, smarter, and better than ever before. It yammers on about this for the entirety of the paper, and you are left feeling little dissapointed at how cheesy it sounds at parts."
    },
    {
      "name": "Attempt to unlock tablet",
      "tags": "1",
      "pid": "10",
      "text": "You punch in a 4 number combination to the tablet, without avail.\n[[Back to room->Airlock]]\n[[Try again->Attempt2]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Try again->Attempt2]]",
          "label": "Try again",
          "newPassage": "Attempt2",
          "pid": "32",
          "selection": "2"
        }
      ],
      "cleanText": "You punch in a 4 number combination to the tablet, without avail."
    },
    {
      "name": "Hallway",
      "tags": "",
      "pid": "11",
      "text": "You walk through the door from the airlock into a large, nine-sided room. There are 9 doors, one for each side of the room- counting the one you just walked in from. They have labels above the doors for each branch off of the hallway.\n[[To the Dorms->Dorm rooms]]\n[[To the Morgue->Morgue]]\n[[To the Lab->Laboratory]]\n[[To Training rooms->Training]]\n[[To the Library->Library]]\n[[To the Cafeteria->Cafeteria]]\n[[To the Admin rooms->Administrationfake]]\n[[To the Exit->Exit]]",
      "links": [
        {
          "original": "[[To the Dorms->Dorm rooms]]",
          "label": "To the Dorms",
          "newPassage": "Dorm rooms",
          "pid": "12",
          "selection": "1"
        },
        {
          "original": "[[To the Morgue->Morgue]]",
          "label": "To the Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        },
        {
          "original": "[[To the Lab->Laboratory]]",
          "label": "To the Lab",
          "newPassage": "Laboratory",
          "pid": "14",
          "selection": "3"
        },
        {
          "original": "[[To Training rooms->Training]]",
          "label": "To Training rooms",
          "newPassage": "Training",
          "pid": "15",
          "selection": "4"
        },
        {
          "original": "[[To the Library->Library]]",
          "label": "To the Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "5"
        },
        {
          "original": "[[To the Cafeteria->Cafeteria]]",
          "label": "To the Cafeteria",
          "newPassage": "Cafeteria",
          "pid": "17",
          "selection": "6"
        },
        {
          "original": "[[To the Admin rooms->Administrationfake]]",
          "label": "To the Admin rooms",
          "newPassage": "Administration",
          "pid": "18",
          "selection": "7",
          "requires":"10"
        },
        {
          "original": "[[To the Admin rooms->Administrationfake]]",
          "label": "To the Admin rooms",
          "newPassage": "Administrationfake",
          "pid": "40",
          "selection": "7",
          "excludes": "10"
        },
        {
          "original": "[[To the Exit->Exit]]",
          "label": "To the Exit",
          "newPassage": "Exit",
          "pid": "36",
          "selection": "8"
        }
      ],
      "cleanText": "You walk through the door from the airlock into a large, nine-sided room. There are 9 doors, one for each side of the room- counting the one you just walked in from. They have labels above the doors for each branch off of the hallway."
    },
    {
      "name": "Dorm rooms",
      "tags": "1",
      "pid": "12",
      "text": "Entering the door marked \"Dormitories\", you walk into a medium sized room, lined with bunk beds as well as a large table in the center. Looking closely, you can see storage trunks at the foot of each bunk. \n[[Investigate the table->Investigate the table]]\n[[Investigate the storage trunks->Investigate the storage trunks]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate the table->Investigate the table]]",
          "label": "Investigate the table",
          "newPassage": "Investigate the table",
          "pid": "19",
          "selection": "1"
        },
        {
          "original": "[[Investigate the storage trunks->Investigate the storage trunks]]",
          "label": "Investigate the storage trunks",
          "newPassage": "Investigate the storage trunks",
          "pid": "20",
          "selection": "2"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "3"
        }
      ],
      "cleanText": "Entering the door marked \"Dormitories\", you walk into a medium sized room, lined with bunk beds as well as a large table in the center. Looking closely, you can see storage trunks at the foot of each bunk."
    },
    {
      "name": "Morgue",
      "tags": "1",
      "pid": "13",
      "text": "Passing into the morgue, you are overcome with an oppressive feeling of interruption and observation. In one of the corners is a pile of bodies, appearing to be hastily thrown out of the way. There is also a surgical table in the center of the room, right above red-stained drain.\n[[Investigate the pile of bodies->Investigate bodies]]\n[[Examine the surgical table->Investigate table]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate the pile of bodies->Investigate bodies]]",
          "label": "Investigate the pile of bodies",
          "newPassage": "Investigate bodies",
          "pid": "21",
          "selection": "1"
        },
        {
          "original": "[[Examine the surgical table->Investigate table]]",
          "label": "Examine the surgical table",
          "newPassage": "Investigate table",
          "pid": "22",
          "selection": "2"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "3"
        }
      ],
      "cleanText": "Passing into the morgue, you are overcome with an oppressive feeling of interruption and observation. In one of the corners is a pile of bodies, appearing to be hastily thrown out of the way. There is also a surgical table in the center of the room, right above red-stained drain."
    },
    {
      "name": "Laboratory",
      "tags": "1",
      "pid": "14",
      "text": "Entering the room marked \"Laboratory\", you recognize equipment like scales and microscopes, but there are machines in this room that you have definitely never seen before. Some of them are covered in strange symbols, which feel eerily familiar.\n[[Investigate machines->Investigate machines]]\n[[Take a deeper look around->Deeplook]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate machines->Investigate machines]]",
          "label": "Investigate machines",
          "newPassage": "Investigate machines",
          "pid": "25",
          "selection": "1"
        },
        {
          "original": "[[Take a deeper look around->Deeplook]]",
          "label": "Take a deeper look around",
          "newPassage": "Deeplook",
          "pid": "26",
          "selection": "2"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "3"
        }
      ],
      "cleanText": "Entering the room marked \"Laboratory\", you recognize equipment like scales and microscopes, but there are machines in this room that you have definitely never seen before. Some of them are covered in strange symbols, which feel eerily familiar."
    },
    {
      "name": "Training",
      "tags": "1",
      "pid": "15",
      "text": "The room marked \"Training\" seems to be a hybrid, combining a meeting and lecture space with what seems like a gym. The classroom portion has a board, a single desk, and is filled with bookshelves, while the other portion is filled with what looks to be exercise machinery and medical tech.\n[[Investigate the Gym->Gym]]\n[[Investigate the School->School]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate the Gym->Gym]]",
          "label": "Investigate the Gym",
          "newPassage": "Gym",
          "pid": "27",
          "selection": "1"
        },
        {
          "original": "[[Investigate the School->School]]",
          "label": "Investigate the School",
          "newPassage": "School",
          "pid": "28",
          "selection": "2"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "3"
        }
      ],
      "cleanText": "The room marked \"Training\" seems to be a hybrid, combining a meeting and lecture space with what seems like a gym. The classroom portion has a board, a single desk, and is filled with bookshelves, while the other portion is filled with what looks to be exercise machinery and medical tech."
    },
    {
      "name": "Library",
      "tags": "1",
      "pid": "16",
      "text": "Stepping into one of the larger rooms connected to the main hallway, marked \"Library\", you are greeted with an atmosphere unlike every other room you've visited so far (and a lot like the one you woke up in). Despite being a completely sealed room besides from the entrance/exit door, it appears as if a tornado has ripped the room to shreds. Book pages are strewn everywhere along the floor, and a good portion of the towering bookshelves are toppled onto eachother. Numerous symbols and charms cover almost every inch of surface area in the room, on half of the objects. It looks like there's a pile of clothes one of the corners of the room.\n[[Investigate the bookshelves->Investigate bookshelves]]\n[[Investigate the papers->Investigate papers]]\n[[Investigate pile of clothes->Investigate pile]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate the bookshelves->Investigate bookshelves]]",
          "label": "Investigate the bookshelves",
          "newPassage": "Investigate bookshelves",
          "pid": "29",
          "selection": "1"
        },
        {
          "original": "[[Investigate the papers->Investigate papers]]",
          "label": "Investigate the papers",
          "newPassage": "Investigate papers",
          "pid": "30",
          "selection": "2"
        },
        {
          "original": "[[Investigate pile of clothes->Investigate pile]]",
          "label": "Investigate pile of clothes",
          "newPassage": "Investigate pile",
          "pid": "31",
          "selection": "3"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "4"
        }
      ],
      "cleanText": "Stepping into one of the larger rooms connected to the main hallway, marked \"Library\", you are greeted with an atmosphere unlike every other room you've visited so far (and a lot like the one you woke up in). Despite being a completely sealed room besides from the entrance/exit door, it appears as if a tornado has ripped the room to shreds. Book pages are strewn everywhere along the floor, and a good portion of the towering bookshelves are toppled onto eachother. Numerous symbols and charms cover almost every inch of surface area in the room, on half of the objects. It looks like there's a pile of clothes one of the corners of the room."
    },
    {
      "name": "Cafeteria",
      "tags": "1",
      "pid": "17",
      "text": "As you pass through the doorway marked \"Cafeteria\", you enter a similar-sized room to all of the others connected to the hallway. There are party banners and hats strewn about, with some hanging from the ceiling. There is a door marked \"Kitchen\" that leads to the area behind some serving lanes. Trays of various food items are on top of some of the dining tables, mostly empty. While thinking about what kind of celebration could have taken place here, you feel yourself getting a bit hungry.\n[[Scrounge up some food->Food]]\n[[Investigate kitchen->Kitchen]]",
      "links": [
        {
          "original": "[[Scrounge up some food->Food]]",
          "label": "Scrounge up some food",
          "newPassage": "Food",
          "pid": "33",
          "selection": "1"
        },
        {
          "original": "[[Investigate kitchen->Kitchen]]",
          "label": "Investigate kitchen",
          "newPassage": "Kitchen",
          "pid": "34",
          "selection": "2"
        }
      ],
      "cleanText": "As you pass through the doorway marked \"Cafeteria\", you enter a similar-sized room to all of the others connected to the hallway. There are party banners and hats strewn about, with some hanging from the ceiling. There is a door marked \"Kitchen\" that leads to the area behind some serving lanes. Trays of various food items are on top of some of the dining tables, mostly empty. While thinking about what kind of celebration could have taken place here, you feel yourself getting a bit hungry."
    },
    {
      "name": "Administration",
      "tags": "1",
      "pid": "18",
      "text": "You enter the administration office to a well-decorated room, far from the clean atmosphere of the Hallway or Airlock. Towards the back of the room, there is a large desk with a nameplate. It reads \"Michael Clark\". All along the sides of the room are cabinets, which appear to be locked. In a burst of curiosity, you sit down at the chair to see if any of the desk cabinets are unlocked. Suddenly, a speaker near your head blares: \"COMMENCING DATA BACKUP. PLEASE SUBMIT DEVICE.\" The nameplate is kicked over and reveals a small docking port.\n[[Connect the tablet->Passatmpt]]\n[[Return to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Connect the tablet->Passatmpt]]",
          "label": "Connect the tablet",
          "newPassage": "Passatmpt",
          "pid": "37",
          "selection": "1",
        },
        {
          "original": "[[Return to Hallway->Hallway]]",
          "label": "Return to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "2",
        }
      ],
      "cleanText": "You enter the administration office to a well-decorated room, far from the clean atmosphere of the Hallway or Airlock. Towards the back of the room, there is a large desk with a nameplate. It reads \"Michael Clark\". All along the sides of the room are cabinets, which appear to be locked. In a burst of curiosity, you sit down at the chair to see if any of the desk cabinets are unlocked. Suddenly, a speaker near your head blares: \"COMMENCING DATA BACKUP. PLEASE SUBMIT DEVICE.\" The nameplate is kicked over and reveals a small docking port."
    },
    {
      "name": "Investigate the table",
      "tags": "1",
      "pid": "19",
      "text": "As you approach the table, you can tell there are numerous sets of cards and chips spread across it, some in neat piles. Surrounding the table are chairs, most of which are covered with ash and clothes strewn about them. Rummaging through the clothes, you find another wallet as well as a keyring with what looks like a car key. Inside the wallet is a family picture- you can't make out the face of the mother for some reason, and your head begins to pound. You put the picture away.\n[[Back to room->Dorm rooms]]",
      "links": [
        {
          "original": "[[Back to room->Dorm rooms]]",
          "label": "Back to room",
          "newPassage": "Dorm rooms",
          "pid": "12",
          "selection": "1"
        }
      ],
      "cleanText": "As you approach the table, you can tell there are numerous sets of cards and chips spread across it, some in neat piles. Surrounding the table are chairs, most of which are covered with ash and clothes strewn about them. Rummaging through the clothes, you find another wallet as well as a keyring with what looks like a car key. Inside the wallet is a family picture- you can't make out the face of the mother for some reason, and your head begins to pound. You put the picture away."
    },
    {
      "name": "Investigate the storage trunks",
      "tags": "2",
      "pid": "20",
      "text": "Investigating the trunks, some are locked shut while others are wide open, containing nothing but toiletries and various articles of clothing.\n[[Back to room->Dorm rooms]]",
      "links": [
        {
          "original": "[[Back to room->Dorm rooms]]",
          "label": "Back to room",
          "newPassage": "Dorm rooms",
          "pid": "12",
          "selection": "1"
        }
      ],
      "cleanText": "Investigating the trunks, some are locked shut while others are wide open, containing nothing but toiletries and various articles of clothing."
    },
    {
      "name": "Investigate bodies",
      "tags": "",
      "pid": "21",
      "text": "Moving closer to the bodies, an intense feeling of grief and loss comes over you. Pulling them off of the pile, there are six of them. You can tell that each of them has had a specific part of their body removed surgically- there is a tag on each body detailing their former profession, as well as the now missing body part:\nThe mathematician had his head removed\nThe personal trainer had their entire torso removed\nThe marine had his arms and legs removed\nThe sculptor had his hands removed\nThe sniper had his eyes removed\nThe chef had his nose and tongue removed\n[[Back to Hallway->Hallway]]\n[[Back to Morgue->Morgue]]",
      "links": [
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "1"
        },
        {
          "original": "[[Back to Morgue->Morgue]]",
          "label": "Back to Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        }
      ],
      "cleanText": "Moving closer to the bodies, an intense feeling of grief and loss comes over you. Pulling them off of the pile, there are six of them. You can tell that each of them has had a specific part of their body removed surgically- there is a tag on each body detailing their former profession, as well as the now missing body part:\nThe mathematician had his head removed\nThe personal trainer had their entire torso removed\nThe marine had his arms and legs removed\nThe sculptor had his hands removed\nThe sniper had his eyes removed\nThe chef had his nose and tongue removed"
    },
    {
      "name": "Investigate table",
      "tags": "",
      "pid": "22",
      "text": "Attempting to even inch towards the surgical table in the center of the room results in an utterly repulsive feeling, every alarm in your brain firing at once to avoid this seemingly mundane object.\n[[Proceed->Pullback]]\n[[Retreat to Morgue->Morgue]]",
      "links": [
        {
          "original": "[[Proceed->Pullback]]",
          "label": "Proceed",
          "newPassage": "Pullback",
          "pid": "23",
          "selection": "1"
        },
        {
          "original": "[[Retreat to Morgue->Morgue]]",
          "label": "Retreat to Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        }
      ],
      "cleanText": "Attempting to even inch towards the surgical table in the center of the room results in an utterly repulsive feeling, every alarm in your brain firing at once to avoid this seemingly mundane object."
    },
    {
      "name": "Pullback",
      "tags": "",
      "pid": "23",
      "text": "Ignoring the chaos of your thoughts screaming at you to not go towards the table, you press on. Barely managing to take a single step every ten-ish seconds, you feel an almost physical force pushing you away from the table. Pulling at your arms and legs beckons you back to the entrance of the room, and you swear you can feel a tight grip on your shoulder.\n[[Push on->Revelation]]\n[[Retreat to Morgue->Morgue]]",
      "links": [
        {
          "original": "[[Push on->Revelation]]",
          "label": "Push on",
          "newPassage": "Revelation",
          "pid": "24",
          "selection": "1"
        },
        {
          "original": "[[Retreat to Morgue->Morgue]]",
          "label": "Retreat to Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        }
      ],
      "cleanText": "Ignoring the chaos of your thoughts screaming at you to not go towards the table, you press on. Barely managing to take a single step every ten-ish seconds, you feel an almost physical force pushing you away from the table. Pulling at your arms and legs beckons you back to the entrance of the room, and you swear you can feel a tight grip on your shoulder."
    },
    {
      "name": "Revelation",
      "tags": "4",
      "pid": "24",
      "text": "Just as you step within arm's reach of the table, you feel searing pain in verious parts of your body as it goes limp- you fade from conciousness in less than a couple seconds, but as you begin to fade your senses are overloaded with the sounds of saw on bone and rending flesh.\nNot sure how much time has passed, your eyes pry open to see a ring of six people standing over your idle body on the floor with concern on their face. You blink once and they're gone, your mind must be playing tricks on you. Once more, and they're gone. You slowly rise to your feet, and walk back to the exit to the Hallway.\n[[Exit the Morgue->Hallway]]",
      "links": [
        {
          "original": "[[Exit the Morgue->Hallway]]",
          "label": "Exit the Morgue",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "1"
        }
      ],
      "cleanText": "Just as you step within arm's reach of the table, you feel searing pain in verious parts of your body as it goes limp- you fade from conciousness in less than a couple seconds, but as you begin to fade your senses are overloaded with the sounds of saw on bone and rending flesh.\nNot sure how much time has passed, your eyes pry open to see a ring of six people standing over your idle body on the floor with concern on their face. You blink once and they're gone, your mind must be playing tricks on you. Once more, and they're gone. You slowly rise to your feet, and walk back to the exit to the Hallway."
    },
    {
      "name": "Investigate machines",
      "tags": "1",
      "pid": "25",
      "text": "Stepping up to the side of one of the unidentified machines, you feel beckoned towards the symbols covering it. Almost as if you were being pulled in, your arm reaches out and brushes along multiple different symbols. As you touch them, you feel yourself remebering something you never knew. You begin rattling of the Alchemical symbols as you see them: \"Mercury\", \"Sulfur\", \"Air\", and \"Gold\". Absolutely clueless on how you were able to decipher these, you feel a connection to them that you can't even begin to explain.\n[[Back to Laboratory->Laboratory]]",
      "links": [
        {
          "original": "[[Back to Laboratory->Laboratory]]",
          "label": "Back to Laboratory",
          "newPassage": "Laboratory",
          "pid": "14",
          "selection": "1"
        }
      ],
      "cleanText": "Stepping up to the side of one of the unidentified machines, you feel beckoned towards the symbols covering it. Almost as if you were being pulled in, your arm reaches out and brushes along multiple different symbols. As you touch them, you feel yourself remebering something you never knew. You begin rattling of the Alchemical symbols as you see them: \"Mercury\", \"Sulfur\", \"Air\", and \"Gold\". Absolutely clueless on how you were able to decipher these, you feel a connection to them that you can't even begin to explain."
    },
    {
      "name": "Deeplook",
      "tags": "2",
      "pid": "26",
      "text": "Looking around the room, you find a set of filing cabinets covered by a tarp. Lifting up the tarp, you realize that all of them are unfortunately, locked. However, you find a water-damaged notebook resting on top of one them. Reading it, you find 8 entries that aren't smudged into illegibility by the water damage.\n8/20/35:  Today is the founding day of our lab, while our methods will likely be frowned upon by the outside world the future of humanity is worth whatever persecution we face!\n3/9/36: Attempting to create a sample from scratch or copying from a template clearly isn’t working we may have to take a more violent route\n4/22/36: My idea to harvest samples instead of attempting to create our own has been accepted finally. My Co-workers aren’t excited by the idea but progress requires sacrifice.\n10/14/36: Our first attempt went horribly. The medium we used for the ritual appears to have been insufficient. When we started all of the samples seemed to take in more energy than intended because of this and covered everything in a layer of gore. We have a long road ahead of us.\n9/31/37: We need to think outside of the box. We have tried practically every material on the fucking periodic table and none worked. We even drained a good portion of the budget, making a gold circle for fucks sake! \n10/7/37: I have a new idea but it's really going to be pushing things. I got the idea when we watched Jurrasic Park last night. I just hope this works.\n12/19/37: I made a crude sample of the new medium, it's gross it’s diluted as hell, and it scares the shit out of me but this crappy sample alone already matches gold in its ability to conduct energy.\n7/5/39: After all the blood sweat and tears we finally have a medium that works. It is costly as hell and a pain in the ass to make but results are results. Now we just need to harvest some fresh samples and God willing we will have done it.\n[[Back to Laboratory->Laboratory]]",
      "links": [
        {
          "original": "[[Back to Laboratory->Laboratory]]",
          "label": "Back to Laboratory",
          "newPassage": "Laboratory",
          "pid": "14",
          "selection": "1"
        }
      ],
      "cleanText": "Looking around the room, you find a set of filing cabinets covered by a tarp. Lifting up the tarp, you realize that all of them are unfortunately, locked. However, you find a water-damaged notebook resting on top of one them. Reading it, you find 8 entries that aren't smudged into illegibility by the water damage.\n8/20/35:  Today is the founding day of our lab, while our methods will likely be frowned upon by the outside world the future of humanity is worth whatever persecution we face!\n3/9/36: Attempting to create a sample from scratch or copying from a template clearly isn’t working we may have to take a more violent route\n4/22/36: My idea to harvest samples instead of attempting to create our own has been accepted finally. My Co-workers aren’t excited by the idea but progress requires sacrifice.\n10/14/36: Our first attempt went horribly. The medium we used for the ritual appears to have been insufficient. When we started all of the samples seemed to take in more energy than intended because of this and covered everything in a layer of gore. We have a long road ahead of us.\n9/31/37: We need to think outside of the box. We have tried practically every material on the fucking periodic table and none worked. We even drained a good portion of the budget, making a gold circle for fucks sake! \n10/7/37: I have a new idea but it's really going to be pushing things. I got the idea when we watched Jurrasic Park last night. I just hope this works.\n12/19/37: I made a crude sample of the new medium, it's gross it’s diluted as hell, and it scares the shit out of me but this crappy sample alone already matches gold in its ability to conduct energy.\n7/5/39: After all the blood sweat and tears we finally have a medium that works. It is costly as hell and a pain in the ass to make but results are results. Now we just need to harvest some fresh samples and God willing we will have done it."
    },
    {
      "name": "Gym",
      "tags": "1",
      "pid": "27",
      "text": "In the athletic half of the room, the numerous fitness machines look well cared for and yet untouched. There are simple weights, treadmills, and some machines you don't recognize. Everything feels a bit like it's being saved for something.\n[[Back to Training room->Training]]",
      "links": [
        {
          "original": "[[Back to Training room->Training]]",
          "label": "Back to Training room",
          "newPassage": "Training",
          "pid": "15",
          "selection": "1"
        }
      ],
      "cleanText": "In the athletic half of the room, the numerous fitness machines look well cared for and yet untouched. There are simple weights, treadmills, and some machines you don't recognize. Everything feels a bit like it's being saved for something."
    },
    {
      "name": "School",
      "tags": "1",
      "pid": "28",
      "text": "Exploring the educational side of the room, everything seems pretty well put togehter, despite the lack of any other desks beside one in the center of the room. While examining the bookshelves, you realize that the subject range and sorting of the books is all over the place- Kindergarten books on animals right next to a Quantum Mechanics textbook, for example. \n[[Back to Training room->Training]]",
      "links": [
        {
          "original": "[[Back to Training room->Training]]",
          "label": "Back to Training room",
          "newPassage": "Training",
          "pid": "15",
          "selection": "1"
        }
      ],
      "cleanText": "Exploring the educational side of the room, everything seems pretty well put togehter, despite the lack of any other desks beside one in the center of the room. While examining the bookshelves, you realize that the subject range and sorting of the books is all over the place- Kindergarten books on animals right next to a Quantum Mechanics textbook, for example."
    },
    {
      "name": "Investigate bookshelves",
      "tags": "3",
      "pid": "29",
      "text": "Walking (almost wading) through the papers on the floor towards the only group of standing bookshelves, you attempt to make out some names of books on the shelf as you get closer. They're all covered in the same strange marks as the rest of the room, so you can barely make out some of the titles. Most of the books remaining in the library seem to pertain to the study of occultism.\nYou take a book off the shelf to see it absolutly covered in more of the strange tailsmans, and you find yourself filled with doubt. As you dare to open the book in your hand, you are instantly barraged with a tinnitus-inducing rumble and some sort of force between corporeal and incorporeal lunges out from the pages- your reaction time saves you as you grab and crush it before it reaches you out of some unnatrual reflex. Shuddering and still a little in shock, you put the book back on the shelf only to realize that every other book looks like they are almost quivering in fear at what just happened. Maybe your mind is playing tricks on you again, it wouldn't be the first time.\n[[Back to the Library->Library]]",
      "links": [
        {
          "original": "[[Back to the Library->Library]]",
          "label": "Back to the Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "1"
        }
      ],
      "cleanText": "Walking (almost wading) through the papers on the floor towards the only group of standing bookshelves, you attempt to make out some names of books on the shelf as you get closer. They're all covered in the same strange marks as the rest of the room, so you can barely make out some of the titles. Most of the books remaining in the library seem to pertain to the study of occultism.\nYou take a book off the shelf to see it absolutly covered in more of the strange tailsmans, and you find yourself filled with doubt. As you dare to open the book in your hand, you are instantly barraged with a tinnitus-inducing rumble and some sort of force between corporeal and incorporeal lunges out from the pages- your reaction time saves you as you grab and crush it before it reaches you out of some unnatrual reflex. Shuddering and still a little in shock, you put the book back on the shelf only to realize that every other book looks like they are almost quivering in fear at what just happened. Maybe your mind is playing tricks on you again, it wouldn't be the first time."
    },
    {
      "name": "Investigate papers",
      "tags": "2",
      "pid": "30",
      "text": "Haphazardly, you begin to rummage through the small sea of papers that covers your feet. A large portion of them appear to be pages of books ripped off of the shelves here, but some don't fit in with those. They're different sizes and colors, all hand-scribbled notes on different processes, using various different sets of symbols different from the ones covering everything in the room.\n[[Back to Library->Library]]",
      "links": [
        {
          "original": "[[Back to Library->Library]]",
          "label": "Back to Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "1"
        }
      ],
      "cleanText": "Haphazardly, you begin to rummage through the small sea of papers that covers your feet. A large portion of them appear to be pages of books ripped off of the shelves here, but some don't fit in with those. They're different sizes and colors, all hand-scribbled notes on different processes, using various different sets of symbols different from the ones covering everything in the room."
    },
    {
      "name": "Investigate pile",
      "tags": "1",
      "pid": "31",
      "text": "You lift up the pile of clothes to take a closer look only to find a hastily written note on top of a pile of ash. It was scribbled so quickly and in such a panic scrawl that it's barely legible.\nIt reads: \"What we have done here is nothing short of monstrous Theres no denying this but we did it anyway. I knew something would happen to us for what we did, Getting arrested, kidnapping for our research, even assassination wasnt off the table but it turns out we may pay for our crimes sooner than we thought. Every time we studied dangerous alchemical rites there was always mention of a cost. We thought it would be energy that we could supply or some sacrifice we would commit but in reality I think it is much worse Every major rite we studied came from an alchemist who went missing, whose face was never seen. When I tried warning the others they called me paranoid and some of them even laughed at me. I figured hiding in the Library would be my best bet considering how many protective charms are here. I pray I'm paranoid but in the case that I'm not and even these charms cant save me I ask whoever is reading this please dont repeat our mistakes\"\n[[Back to Library->Library]]",
      "links": [
        {
          "original": "[[Back to Library->Library]]",
          "label": "Back to Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "1"
        }
      ],
      "cleanText": "You lift up the pile of clothes to take a closer look only to find a hastily written note on top of a pile of ash. It was scribbled so quickly and in such a panic scrawl that it's barely legible.\nIt reads: \"What we have done here is nothing short of monstrous Theres no denying this but we did it anyway. I knew something would happen to us for what we did, Getting arrested, kidnapping for our research, even assassination wasnt off the table but it turns out we may pay for our crimes sooner than we thought. Every time we studied dangerous alchemical rites there was always mention of a cost. We thought it would be energy that we could supply or some sacrifice we would commit but in reality I think it is much worse Every major rite we studied came from an alchemist who went missing, whose face was never seen. When I tried warning the others they called me paranoid and some of them even laughed at me. I figured hiding in the Library would be my best bet considering how many protective charms are here. I pray I'm paranoid but in the case that I'm not and even these charms cant save me I ask whoever is reading this please dont repeat our mistakes\""
    },
    {
      "name": "Attempt2",
      "tags": "1",
      "pid": "32",
      "text": "You hurriedly tap in another code, just to be met with the same locked screen.\n[[Back to room->Airlock]]\n[[Try again->Attempt2]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Try again->Attempt2]]",
          "label": "Try again",
          "newPassage": "Attempt2",
          "pid": "32",
          "selection": "2"
        }
      ],
      "cleanText": "You hurriedly tap in another code, just to be met with the same locked screen."
    },
    {
      "name": "Food",
      "tags": "2",
      "pid": "33",
      "text": "Searching the numerous trays, you find a little less than half of a brownie. Holding it in your hand and looking at it, you can't help but realize how long it's been since you had last eaten. Just as you bite into it, you are overcome with an immense feeling of nausea, and fall to your feet- landing on your back pops the brownie out of your mouth, as well as the wind out of you. Grabbing a nearby large lush green potted plant for support, you clamber to your feet as the overwhelming feeling suddenly fades. Backing away from the brownies and glancing at the plant you happened to grab, you notice it's suddenly wilted almost completely. You find yourself mysteriously satisfied.\n[[Back to Cafeteria->Cafeteria]]",
      "links": [
        {
          "original": "[[Back to Cafeteria->Cafeteria]]",
          "label": "Back to Cafeteria",
          "newPassage": "Cafeteria",
          "pid": "17",
          "selection": "1"
        }
      ],
      "cleanText": "Searching the numerous trays, you find a little less than half of a brownie. Holding it in your hand and looking at it, you can't help but realize how long it's been since you had last eaten. Just as you bite into it, you are overcome with an immense feeling of nausea, and fall to your feet- landing on your back pops the brownie out of your mouth, as well as the wind out of you. Grabbing a nearby large lush green potted plant for support, you clamber to your feet as the overwhelming feeling suddenly fades. Backing away from the brownies and glancing at the plant you happened to grab, you notice it's suddenly wilted almost completely. You find yourself mysteriously satisfied."
    },
    {
      "name": "Kitchen",
      "tags": "1",
      "pid": "34",
      "text": "Walking into the kitchen, you see a generic large-scale kitchen for feeding the entire facility. Someone clearly neglected to do the dishes after the party.\n[[Search the kitchen->Search]]\n[[Back to main room->Cafeteria]]",
      "links": [
        {
          "original": "[[Search the kitchen->Search]]",
          "label": "Search the kitchen",
          "newPassage": "Search",
          "pid": "35",
          "selection": "1"
        },
        {
          "original": "[[Back to main room->Cafeteria]]",
          "label": "Back to main room",
          "newPassage": "Cafeteria",
          "pid": "17",
          "selection": "2"
        }
      ],
      "cleanText": "Walking into the kitchen, you see a generic large-scale kitchen for feeding the entire facility. Someone clearly neglected to do the dishes after the party."
    },
    {
      "name": "Search",
      "tags": "2",
      "pid": "35",
      "text": "Looking through all of the cabinets in the kitchen, you find a decent amount of canned good as well as non-perishables, but nothing directly of use to you.\n[[Back to Cafeteria->Cafeteria]]",
      "links": [
        {
          "original": "[[Back to Cafeteria->Cafeteria]]",
          "label": "Back to Cafeteria",
          "newPassage": "Cafeteria",
          "pid": "17",
          "selection": "1"
        }
      ],
      "cleanText": "Looking through all of the cabinets in the kitchen, you find a decent amount of canned good as well as non-perishables, but nothing directly of use to you."
    },
    {
      "name": "Exit",
      "tags": "",
      "pid": "36",
      "text": "As you approach the door with the big red blinking \"Exit\" sign, you can start to hear a slight beeping. Pushing the door open and exiting, you find yourself in a narrow tunnel- lined with remote explosives. Upon realizing the stakes, you run towards the end of the tunnel quickly until encountering a stairwell. Rushing up it as fast as you can, you arrive at another door. Opening it, you get the feeling that this is the first time you've seen daylight in a long time. You take a moment to just breathe it in, and observe around you. You see some parked cars, and begin to think about if any of the keys could be back in the facility. Almost immediately after walking over to see if any of the cars were unlocked, you hear an earth-rending shudder which you can only assume to be the sealing of the underground facility. You start walking, towards the sun. You have no other choice.\n[[Game over->gameover]]",
      "links": [
        {
          "original": "[[Game over->gameover]]",
          "label": "Game over",
          "newPassage": "gameover",
          "pid": "41",
          "selection": "1"
        }
      ],
      "cleanText": "As you approach the door with the big red blinking \"Exit\" sign, you can start to hear a slight beeping. Pushing the door open and exiting, you find yourself in a narrow tunnel- lined with remote explosives. Upon realizing the stakes, you run towards the end of the tunnel quickly until encountering a stairwell. Rushing up it as fast as you can, you arrive at another door. Opening it, you get the feeling that this is the first time you've seen daylight in a long time. You take a moment to just breathe it in, and observe around you. You see some parked cars, and begin to think about if any of the keys could be back in the facility. Almost immediately after walking over to see if any of the cars were unlocked, you hear an earth-rending shudder which you can only assume to be the sealing of the underground facility. You start walking, towards the sun. You have no other choice."
    },
    {
      "name": "Passatmpt",
      "tags": "1",
      "pid": "37",
      "text": "You are prompted by a very small monitor to enter a password for the tablet. You try:\n[[5213->Hint]]\n[[6612->Hint]]\n[[4998->Hint]]\n[[2345->Hint]]\n[[5003->Hint]]\n[[8235->Success]]\n[[8876->Hint]]\n[[4421->Hint]]\n[[6690->Hint]]\n[[1337->Hint]]\n[[7314->Hint]]\n[[8712->Hint]]\n[[6021->Hint]]\n[[Stop attempting to unlock the tablet->Administration]]",
      "links": [
        {
          "original": "[[5213->Hint]]",
          "label": "5213",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "1"
        },
        {
          "original": "[[6612->Hint]]",
          "label": "6612",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "2"
        },
        {
          "original": "[[4998->Hint]]",
          "label": "4998",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "3"
        },
        {
          "original": "[[2345->Hint]]",
          "label": "2345",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "4"
        },
        {
          "original": "[[5003->Hint]]",
          "label": "5003",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "5"
        },
        {
          "original": "[[8235->Success]]",
          "label": "8235",
          "newPassage": "Success",
          "pid": "39",
          "selection": "6"
        },
        {
          "original": "[[8876->Hint]]",
          "label": "8876",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "7"
        },
        {
          "original": "[[4421->Hint]]",
          "label": "4421",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "8"
        },
        {
          "original": "[[6690->Hint]]",
          "label": "6690",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "9"
        },
        {
          "original": "[[1337->Hint]]",
          "label": "1337",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "10"
        },
        {
          "original": "[[7314->Hint]]",
          "label": "7314",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "11"
        },
        {
          "original": "[[8712->Hint]]",
          "label": "8712",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "12"
        },
        {
          "original": "[[6021->Hint]]",
          "label": "6021",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "13"
        },
        {
          "original": "[[Stop attempting to unlock the tablet->Administration]]",
          "label": "Stop attempting to unlock the tablet",
          "newPassage": "Administration",
          "pid": "18",
          "selection": "14"
        }
      ],
      "cleanText": "You are prompted by a very small monitor to enter a password for the tablet. You try:"
    },
    {
      "name": "Hint",
      "tags": "1",
      "pid": "38",
      "text": "The number you typed in wipes from the input box, and a prompt appears.\n\"HINT: THE DAY WE SET OUT TO REINVENT HUMANITY\"\n[[6713->Hint]]\n[[8823->Hint]]\n[[9981->Hint]]\n[[2234->Hint]]\n[[7731->Hint]]\n[[5124->Hint]]\n[[5462->Hint]]\n[[8378->Hint]]\n[[4538->Hint]]\n[[5437->Hint]]\n[[8235->Success]]\n[[3758->Hint]]\n[[Stop attempting to unlock the tablet->Administration]]",
      "links": [
        {
          "original": "[[6713->Hint]]",
          "label": "6713",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "1"
        },
        {
          "original": "[[8823->Hint]]",
          "label": "8823",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "2"
        },
        {
          "original": "[[9981->Hint]]",
          "label": "9981",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "3"
        },
        {
          "original": "[[2234->Hint]]",
          "label": "2234",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "4"
        },
        {
          "original": "[[7731->Hint]]",
          "label": "7731",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "5"
        },
        {
          "original": "[[5124->Hint]]",
          "label": "5124",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "6"
        },
        {
          "original": "[[5462->Hint]]",
          "label": "5462",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "7"
        },
        {
          "original": "[[8378->Hint]]",
          "label": "8378",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "8"
        },
        {
          "original": "[[4538->Hint]]",
          "label": "4538",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "9"
        },
        {
          "original": "[[5437->Hint]]",
          "label": "5437",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "10"
        },
        {
          "original": "[[8235->Success]]",
          "label": "8235",
          "newPassage": "Success",
          "pid": "39",
          "selection": "11"
        },
        {
          "original": "[[3758->Hint]]",
          "label": "3758",
          "newPassage": "Hint",
          "pid": "38",
          "selection": "12"
        },
        {
          "original": "[[Stop attempting to unlock the tablet->Administration]]",
          "label": "Stop attempting to unlock the tablet",
          "newPassage": "Administration",
          "pid": "18",
          "selection": "13"
        }
      ],
      "cleanText": "The number you typed in wipes from the input box, and a prompt appears.\n\"HINT: THE DAY WE SET OUT TO REINVENT HUMANITY\""
    },
    {
      "name": "Success",
      "tags": "8",
      "pid": "39",
      "text": "The screen goes blank as soon as you type in the 5 in 8235. An announcement from that same speaker behind your head bellows: \"Beginning data transfer for Homunculus project.\" This might take a while.\n[[Back to Administration->Administration]]",
      "links": [
        {
          "original": "[[Back to Administration->Administration]]",
          "label": "Back to Administration",
          "newPassage": "Administration",
          "pid": "18",
          "selection": "1"
        }
      ],
      "cleanText": "The screen goes blank as soon as you type in the 5 in 8235. An announcement from that same speaker behind your head bellows: \"Beginning data transfer for Homunculus project.\" This might take a while."
    },
    {
      "name": "Administrationfake",
      "tags": "1",
      "pid": "40",
      "text": "You enter the administration office to a well-decorated room, far from the clean atmosphere of the Hallway or Airlock. Towards the back of the room, there is a large desk with a nameplate. It reads \"Michael Clark\". All along the sides of the room are cabinets, which appear to be locked. In a burst of curiosity, you sit down at the chair to see if any of the desk cabinets are unlocked. Suddenly, a speaker near your head blares: \"COMMENCING DATA BACKUP. PLEASE SUBMIT DEVICE. The nameplate is kicked over and reveals a small docking port.\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "1"
        }
      ],
      "cleanText": "You enter the administration office to a well-decorated room, far from the clean atmosphere of the Hallway or Airlock. Towards the back of the room, there is a large desk with a nameplate. It reads \"Michael Clark\". All along the sides of the room are cabinets, which appear to be locked. In a burst of curiosity, you sit down at the chair to see if any of the desk cabinets are unlocked. Suddenly, a speaker near your head blares: \"COMMENCING DATA BACKUP. PLEASE SUBMIT DEVICE. The nameplate is kicked over and reveals a small docking port."
    },
    {
      "name": "gameover",
      "tags": "",
      "pid": "41",
      "text": "",
      "links": [],
      "cleanText": ""
    }
  ]
}
