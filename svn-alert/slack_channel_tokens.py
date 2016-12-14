#!/usr/bin/python
# -*- coding: utf-8 -*-


#zues-team wKqBbixqPiaBoHFlJVdPGznY
#zues-duplicate-clean  Oc5D6djAE5xPrU0F576qyYUe
#jaikiro-hello-lingo XecE3trUVyR2zc8RP987TGZ6

CHANNELS_TOKENS = {
	'zues-team' : 'wKqBbixqPiaBoHFlJVdPGznY', 
}


# Set slack info
REPO_CHANNEL_LINKS={
	'10xTyping' : 'zues-team',  #repo 10xTyping will post in channel #zues-team    
}


def lookupChannelTokenForRepo(repo):
	if  repo in REPO_CHANNEL_LINKS:
		channel_name = REPO_CHANNEL_LINKS[repo]
		return CHANNELS_TOKENS[channel_name];
	return "";