def generateMarkerString(currentTweetIndex, tweetLatLonList, mapCenterLatLon):
	currentTweet = tweetLatLonList[currentTweetIndex]
	if currentTweet == None:
		mainMarker = f'|{mapCenterLatLon[0]},{mapCenterLatLon[1]}'
		secodaryM = ''
		for tweet in tweetLatLonList:
			if tweet != None:
				secodaryM += f"|{tweet[0]},{tweet[1]}"
	else:
		theLocal = tweetLatLonList[currentTweetIndex]
		mainMarker = f"|{theLocal[0]},{theLocal[1]}"
		secodaryM = ''
		for i in range(0,len(tweetLatLonList)):
			if i != currentTweetIndex:
				mark = tweetLatLonList[i]
				if mark != None:
					secodaryM += f'|{mark[0]},{mark[1]}'
	return f'&markers=color:red{mainMarker}&markers=color:blue|size:small{secodaryM}'

