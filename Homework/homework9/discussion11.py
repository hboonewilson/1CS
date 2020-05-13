def generateMarkerString(currentTweetIndex, tweetLatLonList, mapCenterLatLon):
	currentTweet = tweetLatLonList[currentTweetIndex]
	if currentTweet == None:
		mainMarker = f'|{mapCenterLatLon[1]},{mapCenterLatLon[0]}'
		secodaryM = ''
		for tweet in tweetLatLonList:
			if tweet != None:
				secodaryM += f"|{tweet[1]},{tweet[0]}"
	else:
		theLocal = tweetLatLonList[currentTweetIndex]
		mainMarker = f"|{theLocal[1]},{theLocal[0]}"
		secodaryM = ''
		for i in range(0,len(tweetLatLonList)):
			if i != currentTweetIndex:
				mark = tweetLatLonList[i]
				if mark != None:
					secodaryM += f'|{mark[1]},{mark[0]}'
	return f'&markers=color:red{mainMarker}&markers=color:blue|size:small{secodaryM}'

