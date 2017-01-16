#!/usr/bin/python
# -*- coding: utf-8 -*-

# post-commit: Hook used for SVN post commits
#
# Dmitry Minsky
# dmitry.minsky@gmail.com

# This script is set to publish information after SVN commits to Slack. 

import sys
import subprocess
import urllib
import urllib2
import json
import os.path

import slack_channel_tokens

#TOKEN = 'wKqBbixqPiaBoHFlJVdPGznY' # token like cg3MI88ufdGWwT5RbojoLJCV
DOMAIN = 'magik.slack.com' # for example companyname.slack.com
REPO_BASE_URL = '' # for example http://svn.companyname.com/

# svnlook location
LOOK='svnlook'


def sendSlack( domain, token, payload ):
	# create request url
	url = 'https://' + domain + '/services/hooks/subversion?token=' + token
	# urlencode and post
	urllib2.urlopen( url, urllib.urlencode( { 'payload' : json.dumps( payload ) } ) )

def runLook( *args ):
	p = subprocess.Popen(' '.join([LOOK] + list(args)), stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT )
	out, err = p.communicate()
	return out

def getCommitInfo( repo, revision ):
	comment = runLook('log', repo, '-r', revision)
	author = runLook('author', repo, '-r', revision)
	files = runLook('changed', repo, '-r', revision)
	fileArr = files.split("\n");
	
	maxRow = 4;
	
	#if len(fileArr) > maxRow:
	   #filesWillShow = fileArr[0:maxRow]
	   #files = "\n".join(filesWillShow)
	   #files = files + "\nAnd {} more files ...".format(len(fileArr) - maxRow)

	payload = {
		'revision' : revision,
	#	'url' : '',			 #REPO_BASE_URL + repo + '?=' + revision,
		'author' : author,
		'log' : getRepoName(repo)  + " : " + str(len(fileArr)) + " files." + " \n " + comment,
	}

	return payload
def getRepoName(repo_path):
	return os.path.basename(repo_path)


def main():	
	payload = getCommitInfo( sys.argv[1], sys.argv[2] )
	repo_name = getRepoName(sys.argv[1])
	TOKEN = slack_channel_tokens.lookupChannelTokenForRepo(repo_name);
	if TOKEN != "":		
		sendSlack( DOMAIN, TOKEN, payload )	

if __name__ == '__main__':
	main()