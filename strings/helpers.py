HELP_1 = """<b><u>ADMINS COMMANDS :</b></u>

Just add <b>C</b> in The Starting Of the Commands to use then for Channel.


<b>/pause:</b> Pause the Current Playing Stream.

<b>/resume:</b> Resume The Paused Stream.

<b>/skip:</b> Skip the Current Playing Stream and Start Stream the Next Track in Queue.

<b>/end or /stop:</b> Clears the Queue and End the Current Playing Stream.

<b>/player:</b> Get A Interactive Player Panel.

<b>/queue:</b> Shows the Queued Tracks list.
"""

HELP_2 = """
<b><u>AUTH USERS :</b></u>

Auth Users Can Use Admin Rights in the Bot Without Admin Right in The Chat.

<b>/auth [User id / Username] :</b> Add A User to Auth list of the Bot.
<b>/unauth [User id / Username] :</b> Remove A Auth User from the Auth Users list.
<b>/authusers :</b> Shows the list of Auth Users of the Group.
"""

HELP_3 = """
<u><b>BROADCAST FEATURE</b></u> [ Only for Owner and Sudo User ] :

<b>/broadcast [Message or Reply to a Message] :</b> Broadcast A Message to Served Chats of the Bot.

<u>BROADCASTING MODES :</u>
<b>-pin</b> : Pin Your Broadcast Messages in Served Chats.
<b>-pinloud</b> : Pins Your Broadcasted Message In Served Chats and Send Notification to the Members.
<b>-user</b> : Broadcasts the Messages to the Users Who have Started your Bot.
<b>-assistant</b> : Broadcast Your Message from the Assistant Account of the Bot.
<b>-nobot</b> : Broadcast your Message from the assistant Account of the Bot.

<b>Example:</b> <code>/broadcast -user -assistant -pin Testing Broadcast.</code>
"""

HELP_4 = """<u><b>BLACKLIST CHAT :</b></u> [Only for Sudo]

Restrict Shit Chats to use Our Precious Bot.

<b>/blacklistchat [Chat id] :</b> Blacklist A Chat From using this Bot.
<b>/whitelistchat [Chat id] :</b> Whitelist the Blacklisted Chat.
<b>/blacklistedchat :</b> Shows The List of Blacklisted Chat.
"""

HELP_5 = """
<u><b>BLOCK USERS :</b></u> [Only for Sudo]

Starts Ignoring the Blacklisted User, So that He Can't use Bot Commands.

<b>/block [Username or Reply to A User] :</b> Block the User from our Bot.
<b>/unblock [Username or Reply to A User] :</b> Un-Block the Blocked User.
<b>/blockedusers :</b> Shows the List of the Blocked Users.
"""

HELP_6 = """
<u><b>CHANNEL PLAY COMMANDS :</b></u>

You Can Stream Audio / Video in Channel.

<b>/cplay :</b> Starts Streaming the Requested Audio track on Channel.
<b>/cvplay :</b> Starts Streaming the Requested Video track on Channel.
<b>/cplayforce or /cvplayforce :</b> Stop the Ongoing Stream and Starts Streaming the Requested Track.

<b>/channelplay [Chat Username or Id] or [Disable] : Connect to A Group And Starts Streaming Tracks by the Help Commands sent in Group.
"""

HELP_7 = """
<u><b>𝖦𝗅𝗈𝖻𝖺𝗅 𝖡𝖺𝗇 𝖥𝖾𝖺𝗍𝗎𝗋𝖾</b></u> [ 𝖮𝗇𝗅𝗒 𝖥𝗈𝗋 𝖲𝗎𝖽𝗈𝖾𝗋𝗌 ] :

/gban [ 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝖮𝗋 𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠 𝖴𝗌𝖾𝗋 ] : 𝖦𝗅𝗈𝖻𝖺𝗅𝗅𝗒 𝖡𝖺𝗇 𝖳𝗁𝖾 𝖴𝗌𝖾𝗋 𝖥𝗋𝗈𝗆 𝖠𝗅𝗅 𝖳𝗁𝖾 𝖲𝖾𝗋𝗏𝖾𝖽 𝖢𝗁𝖺𝗍𝗌 𝖠𝗇𝖽 𝖡𝗅𝖺𝖼𝗄𝗅𝗂𝗌𝗍 𝖧𝗂𝗆 𝖥𝗋𝗈𝗆 𝖴𝗌𝗂𝗇𝗀 𝖳𝗁𝖾 𝖡𝗈𝗍 .
/ungban [ 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝖮𝗋 𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠 𝖴𝗌𝖾𝗋 ] : 𝖦𝗅𝗈𝖻𝖺𝗅𝗅𝗒 𝖴𝗇𝖻𝖺𝗇𝗌  𝖳𝗁𝖾 𝖦𝗅𝗈𝖻𝖺𝗅𝗅𝗒 𝖡𝖺𝗇𝗇𝖾𝖽 𝖴𝗌𝖾𝗋 .
/gbannedusers : 𝖲𝗁𝗈𝗐𝗌 𝖳𝗁𝖾 𝖫𝗂𝗌𝗍 𝖮𝖿 𝖦𝗅𝗈𝖻𝖺𝗅𝗅𝗒 𝖡𝖺𝗇𝗇𝖾𝖽 𝖴𝗌𝖾𝗋𝗌 .
"""

HELP_8 = """
<b><u>𝖫𝗈𝗈𝗉 𝖲𝗍𝗋𝖾𝖺𝗆 :</b></u>

<b>𝖲𝗍𝖺𝗋𝗍 𝖲𝗍𝗋𝖾𝖺𝗆𝗂𝗇𝗀 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖲𝗍𝗋𝖾𝖺𝗆 𝖨𝗇 𝖫𝗈𝗈𝗉</b>

/loop [ 𝖤𝗇𝖺𝖻𝗅𝖾 / 𝖣𝗂𝗌𝖺𝖻𝗅𝖾 ] : 𝖤𝗇𝖺𝖻𝗅𝖾𝗌 / 𝖣𝗂𝗌𝖺𝖻𝗅𝖾𝗌 𝖫𝗈𝗈𝗉 𝖥𝗈𝗋 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖲𝗍𝗋𝖾𝖺𝗆
/loop [1 , 2 , 3 , ...] : 𝖤𝗇𝖺𝖻𝗅𝖾𝗌 𝖳𝗁𝖾 𝖫𝗈𝗈𝗉 𝖥𝗈𝗋 𝖳𝗁𝖾 𝖦𝗂𝗏𝖾𝗇 𝖵𝖺𝗅𝗎𝖾 .
"""

HELP_9 = """
<u><b>𝖬𝖺𝗂𝗇𝗍𝖾𝗇𝖺𝗇𝖼𝖾 𝖬𝗈𝖽𝖾</b></u> [ 𝖮𝗇𝗅𝗒 𝖥𝗈𝗋 𝖲𝗎𝖽𝗈𝖾𝗋𝗌 ] :

/logs : 𝖦𝖾𝗍 𝖫𝗈𝗀𝗌 𝖮𝖿 𝖳𝗁𝖾 𝖡𝗈𝗍 .

/logger [ Enable / Disable ] : Bot Will Start Logging The Activities Happen On Bot .

/maintenance [ 𝖤𝗇𝖺𝖻𝗅𝖾 / 𝖣𝗂𝗌𝖺𝖻𝗅𝖾 ] : 𝖤𝗇𝖺𝖻𝗅𝖾 𝖮𝗋 𝖣𝗂𝗌𝖺𝖻𝗅𝖾 𝖳𝗁𝖾 𝖬𝖺𝗂𝗇𝗍𝖾𝗇𝖺𝗇𝖼𝖾 𝖬𝗈𝖽𝖾 𝖮𝖿 𝖸𝗈𝗎𝗋 𝖡𝗈𝗍 .
"""

HELP_10 = """
<b><u>𝖯𝗂𝗇𝗀 𝖠𝗇𝖽 𝖲𝗍𝖺𝗍𝗌 :</b></u>

/start : 𝖲𝗍𝖺𝗋𝗍 𝖳𝗁𝖾 𝖬𝗎𝗌𝗂𝖼 𝖡𝗈𝗍 .
/help : 𝖦𝖾𝗍 𝖧𝖾𝗅𝗉 𝖬𝖾𝗇𝗎 𝖶𝗂𝗍𝗁 𝖤𝗑𝗉𝗅𝖺𝗇𝖺𝗍𝗂𝗈𝗇 𝖮𝖿 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 .

/ping : 𝖲𝗁𝗈𝗐𝗌 𝖳𝗁𝖾 𝖯𝗂𝗇𝗀 𝖠𝗇𝖽 𝖲𝗒𝗌𝗍𝖾𝗆 𝖲𝗍𝖺𝗍𝗌 𝖮𝖿 𝖳𝗁𝖾 𝖡𝗈𝗍 .

/stats : 𝖲𝗁𝗈𝗐𝗌 𝖳𝗁𝖾 𝖮𝗏𝖾𝗋𝖺𝗅𝗅 𝖲𝗍𝖺𝗍𝗌 𝖮𝖿 𝖳𝗁𝖾 𝖡𝗈𝗍 .
"""

HELP_11 = """
<u><b>𝖯𝗅𝖺𝗒 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :</b></u>

<b>v :</b> 𝖲𝗍𝖺𝗇𝖽𝗌 𝖥𝗈𝗋 𝖵𝗂𝖽𝖾𝗈 𝖯𝗅𝖺𝗒 .
<b>force :</b> 𝖲𝗍𝖺𝗇𝖽𝗌 𝖥𝗈𝗋 𝖥𝗈𝗋𝖼𝖾 𝖯𝗅𝖺𝗒 .

/play 𝖮𝗋 /vplay : 𝖲𝗍𝖺𝗋𝗍𝗌 𝖲𝗍𝗋𝖾𝖺𝗆𝗂𝗇𝗀 𝖳𝗁𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝖾𝖽 𝖳𝗋𝖺𝖼𝗄 𝖮𝗇 𝖵𝗂𝖽𝖾𝗈𝖢𝗁𝖺𝗍 .

/playforce 𝖮𝗋 /vplayforce : 𝖲𝗍𝗈𝗉𝗌 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖲𝗍𝗋𝖾𝖺𝗆 𝖠𝗇𝖽 𝖲𝗍𝖺𝗋𝗍𝗌 𝖲𝗍𝗋𝖾𝖺𝗆𝗂𝗇𝗀 𝖳𝗁𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝖾𝖽 𝖳𝗋𝖺𝖼𝗄 .
"""

HELP_12 = """
<b><u>𝖲𝗁𝗎𝖿𝖿𝗅𝖾 𝖰𝗎𝖾𝗎𝖾 :</b></u>

/shuffle : 𝖲𝗁𝗎𝖿𝖿𝗅𝖾'𝗌 𝖳𝗁𝖾 𝖰𝗎𝖾𝗎𝖾 .
/queue : 𝖲𝗁𝗈𝗐𝗌 𝖳𝗁𝖾 𝖲𝗁𝗎𝖿𝖿𝗅𝖾'𝗌 𝖰𝗎𝖾𝗎𝖾 .
"""

HELP_13 = """
<b><u>𝖲𝖾𝖾𝗄 𝖲𝗍𝗋𝖾𝖺𝗆 :</b></u>

/seek [ 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇 𝖨𝗇 𝖲𝖾𝖼𝗈𝗇𝖽𝗌 ] : 𝖲𝖾𝖾𝗄 𝖳𝗁𝖾 𝖲𝗍𝗋𝖾𝖺𝗆 𝖳𝗈 𝖳𝗁𝖾 𝖦𝗂𝗏𝖾𝗇 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇 .
/seekback [ 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇 𝖨𝗇 𝖲𝖾𝖼𝗈𝗇𝖽𝗌 ] : 𝖡𝖺𝖼𝗄𝗐𝖺𝗋𝖽 𝖲𝖾𝖾𝗄 𝖳𝗁𝖾 𝖲𝗍𝗋𝖾𝖺𝗆 𝖳𝗈 𝖳𝗁𝖾 𝖦𝗂𝗏𝖾𝗇 𝖣𝗎𝗋𝖺𝗍𝗂𝗈𝗇 .
"""

HELP_14 = """
<b><u>𝖲𝗈𝗇𝗀 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽</b></u>

/song [ 𝖲𝗈𝗇𝗀 𝖭𝖺𝗆𝖾 / 𝖸𝗈𝗎𝖳𝗎𝖻𝖾 𝖴𝗋𝗅 ] : 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖠𝗇𝗒 𝖳𝗋𝖺𝖼𝗄 𝖥𝗋𝗈𝗆 𝖸𝗈𝗎𝖳𝗎𝖻𝖾 𝖨𝗇 𝖬𝗉3 𝖮𝗋 𝖬𝗉4 𝖥𝗈𝗋𝗆𝖺𝗍𝗌 .
"""

HELP_15 = """
<b><u>𝖲𝗉𝖾𝖾𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :</b></u>

𝖸𝗈𝗎 𝖢𝖺𝗇 𝖢𝗈𝗇𝗍𝗋𝗈𝗅 𝖳𝗁𝖾 𝖯𝗅𝖺𝗒𝖡𝖺𝖼𝗄 𝖲𝗉𝖾𝖾𝖽 𝖮𝖿 𝖳𝗁𝖾 𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖲𝗍𝗋𝖾𝖺𝗆 . [ 𝖠𝖽𝗆𝗂𝗇𝗌 𝖮𝗇𝗅𝗒 ]

/speed 𝖮𝗋 /playback : 𝖥𝗈𝗋 𝖠𝖽𝗃𝗎𝗌𝗍𝗂𝗇𝗀 𝖳𝗁𝖾 𝖠𝗎𝖽𝗂𝗈 𝖯𝗅𝖺𝗒𝖡𝖺𝖼𝗄 𝖲𝗉𝖾𝖾𝖽 𝖨𝗇 𝖦𝗋𝗈𝗎𝗉 .
/cspeed 𝖮𝗋 /cplayback : 𝖥𝗈𝗋 𝖠𝖽𝗃𝗎𝗌𝗍𝗂𝗇𝗀 𝖳𝗁𝖾 𝖠𝗎𝖽𝗂𝗈 𝖯𝗅𝖺𝗒𝖡𝖺𝖼𝗄 𝖲𝗉𝖾𝖾𝖽 𝖨𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 .
"""
