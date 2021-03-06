#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015, 2016 Martin Kauss (yo@bishoph.org)

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

# Simple twitter plugin
#
# To get this up and running on a Raspberry Pi 
# the following commands/packages are required
# 
# sudo apt-get install python-dev python-pip
# sudo pip install -U pip
# sudo pip install tweepy
# sudo apt-get install libffi-dev
# sudo pip install pyopenssl ndg-httpsclient pyasn1


from scipy.io.wavfile import write
import numpy

import tweepy
import imp
import uuid

api = None

try:
    # The following file must contain consumer_key, consumer_secret, access_token, access_token_secret
    # to be able to authentication against Twitter with oAuth
    SOPARE_PLUGIN_SECRETS = imp.load_source('sopare_plugin_secrets', '/etc/sopare/secrets.py')
    auth = tweepy.OAuthHandler(SOPARE_PLUGIN_SECRETS.consumer_key, SOPARE_PLUGIN_SECRETS.consumer_secret)
    auth.set_access_token(SOPARE_PLUGIN_SECRETS.access_token, SOPARE_PLUGIN_SECRETS.access_token_secret)
    api = tweepy.API(auth)
except:
    print ('An error occured while initializing the Twitter API. Continue anyway without tweeting!')

def run(readable_results, data, rawbuf):
    status = None
    if (len(readable_results) == 2 and readable_results[0] == 'licht'  and ('aus' in readable_results or 'an' in readable_results)):
        if ('an' in readable_results and 'aus' in readable_results):
            return # makes no sense
        status = str(uuid.uuid4())
        if ('an' in readable_results):
            status += ".1"
        if ('aus' in readable_results):
            status += ".0"
    if (status != None):
        debug_output(status, readable_results, data, rawbuf)
        tweet(status)

def tweet(status):
    if (api != None):
        api.update_status(status)

def debug_output(status, readable_results, data, rawbuf):
        scaled = numpy.int16(rawbuf/numpy.max(numpy.abs(rawbuf)) * 32767)
        write('/home/pi/dev/sopare/tokens/'+status+'.wav', 44100, scaled)
        text_file = open('/home/pi/dev/sopare/tokens/'+status+'.txt', 'w')
        text_file.write(str(data) + '\n\n' + '\n\n' + str(readable_results))
        text_file.close()
