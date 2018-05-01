# InstagramUnfollowers
A simple script in Python to list your Instagram unfollowers manually.

## Context
On the 30th of March of 2018, without warning, Instagram dropped the number of requests API developers could make from 5000 to 200 requests per token per hour. And on the 4th of April of the same year, without warning, Instagram shut down the majority of their API endpoints. Nowadays it's no longer possible for third-party apps to list your Instagram unfollowers, since they can't get public data from an Instagram account anymore. Here I share a simple script I made to do that manually.

## Prerequisites
- Have python 2.7 installed.
- Have numpy installed.

## Usage
- Copy from the Instagram website your list of followers and paste it to file_1.
- Copy from the Instagram website your list of accounts you follow and paste it to file_2.
- Run the script: `python unfollowers.py path_to_file_1 path_to_file_2`
