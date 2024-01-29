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
<u><b>GLOBAL BAN FEATURE</b></u> [Only for Sudo] :

<b>/gban [Username or Reply to a user] :</b> Globally ban the User from all served Chats and Blacklist him from using the Bot.
<b>/ungban [Username or Reply to a user] :</b> Globally Unban the Globally Banned User.
<b>/gbannedusers :</b> Shows the List of Globally Banned Users.
"""

HELP_8 = """
<b><u>LOOP STREAM :</b></u>

<b>Start Streaming the Ongoing Stream in Loop</b>

<b>/loop [Enable / Disable] :</b> Enables / Disables Loop for The Ongoing Stream 
<b>/loop [1 , 2 , 3 , ...] :</b> Enables the Loop for the Given Value.
"""

HELP_9 = """
<u><b>MAINTENANCE MODE</b></u> [Only for Sudo] :

<b>/logs :</b> Get Logs of the Bot.

<b>/logger [Enable / Disable] :</b> Bot Will Start Logging The Activities Happen On Bot .

<b>/maintenance [Enable / Disable] :</b> Enable or Disable the Maintenance Mode of your Bot.
"""

HELP_10 = """
<b><u>PING & STATS :</b></u>

<b>/start :</b> Start the Music Bot.
<b>/help :</b> Get Help Menu With Explanation of Commands.

<b>/ping :</b> Shows the Ping and System Stats of the Bot.

<b>/stats :</b> Shows the Overall Stats of the Bot.
"""

HELP_11 = """
<u><b>PLAY COMMANDS :</b></u>

<b>v :</b> Stand for Video Play.
<b>force :</b> Stands for Force Play.

<b>/play or /vplay :</b> Starts Streaming the Requested Track on VideoChat.

<b>/playforce or /vplayforce :</b> Stops the Ongoing Stream andStarts Streaming the Requested Track.
"""

HELP_12 = """
<b><u>SHUFFLE QUEUE :</b></u>

<b>/shuffle :</b> Shuffle's the Queue.
<b>/queue :</b> Shows the Shuffle's Queue.
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
