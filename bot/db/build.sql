CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT ".",
    StarboardChannel integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS starboard (
    RootMessageID integer PRIMARY KEY,
    StarMessageID integer,
    Stars integer DEFAULT 1
    );

CREATE TABLE IF NOT EXISTS channels (
    GuildID integer PRIMARY KEY,
    DefaultLogChannelID integer,
    LogChannelID integer,
    DefaultStarboardChannelID integer,
    StarboardChannelID integer,
    DefaultWelcomeChannelID integer,
    WelcomeChannelID integer

);
