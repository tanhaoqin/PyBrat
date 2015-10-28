#annotate using [[ and ]] to open and close annotations
def parseAnnotations(masterPath="master.txt", annotationPath="annotations.txt"):
	print "Beginning parsing"
	originalCorpus = open(masterPath, "r")
	originalLengths = [len(unicode(line, "utf-8")) for line in originalCorpus.readlines()]

	annotations = open(annotationPath, "r")
	annotationsLines = annotations.readlines()
	originalCorpus.close()
	annotations.close()

	modificationIndices = open("modifications.txt", "w")
	openMarker = "{"
	closeMarker = "}"

	currentStart = 0
	for modIndex in range(len(annotationsLines)):
		# print modIndex
		# assuming no noun phrases in noun phrases
		if annotationsLines[modIndex][0] == "#":
			annotationsLines[modIndex] = annotationsLines[modIndex][1:]
			if annotationsLines[modIndex][0] == " ":
				annotationsLines[modIndex] = annotationsLines[modIndex][1:]
			annotationsLines[modIndex] = unicode(annotationsLines[modIndex], "utf-8")
			while annotationsLines[modIndex].find(openMarker) >= 0 and annotationsLines[modIndex].find(closeMarker) >= 0:
				# print annotationsLines[modIndex]
				openIndex = annotationsLines[modIndex].find(openMarker)
				closeIndex = annotationsLines[modIndex].find(closeMarker)
				annotationsLines[modIndex] = annotationsLines[modIndex][:openIndex] + annotationsLines[modIndex][openIndex:closeIndex + 1].replace(openMarker, "").replace(closeMarker, "") + annotationsLines[modIndex][closeIndex + 1:]
				closeIndex -= len(openMarker)
				modificationIndices.write("[{0},{1}]\n".format(openIndex + currentStart, closeIndex + currentStart))

		currentStart += originalLengths[modIndex]
	print "Parsing done"
	modificationIndices.close()