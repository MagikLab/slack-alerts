#!/usr/bin/python
# -*- coding: utf-8 -*-

CHANNELS_TOKENS = {
	'zues-team' : 'wKqBbixqPiaBoHFlJVdPGznY', 
	'zues-duplicate-clean' : 'Oc5D6djAE5xPrU0F576qyYUe', 
	'jaikiro-hello-lingo' : 'XecE3trUVyR2zc8RP987TGZ6', 
    'lucifer-team': '7Bh2mIz51Zu1Vu0LO0uvbMQE',
}


# Set slack info
REPO_CHANNEL_LINKS={
	'10xTyping' : 'zues-team',  #repo 10xTyping will post in channel #zues-team
    '9ZipOrg' : 'zues-team',
	'AppRankTracker' : 'zues-team',
	'cpu5' : 'zues-team',
	'DuplicateClean' : 'zues-duplicate-clean',
	'NetworkSpeedTest' : 'zues-team',
	'PerfectPhotoSuite' : 'zues-team',
	'ThayTheCom' : 'zues-team',
	'VoiceRecorder' : 'zues-team',
	'Windows10App' : 'zues-team',  
	
    '500ea' : 'lucifer-team',
    'cartoon' : 'lucifer-team',
    'Listen123' : 'lucifer-team',
    'LyricQuiz' : 'lucifer-team',
    'say2me' : 'lucifer-team',
	
	'hellolingo' : 'jaikiro-hello-lingo',
}


def lookupChannelTokenForRepo(repo):
	if  repo in REPO_CHANNEL_LINKS:
		channel_name = REPO_CHANNEL_LINKS[repo]
		return CHANNELS_TOKENS[channel_name];
	return "";