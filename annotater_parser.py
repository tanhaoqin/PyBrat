import codecs

#annotate using [[ and ]] to open and close annotations
def parseAnnotations(masterPath="master.txt", annotationPath="annotations.txt"):
	print masterPath, annotationPath
	print "Beginning parsing"
	originalCorpus = codecs.open(masterPath, "r", "utf-8")
	originalLines = originalCorpus.readlines()
	originalLengths = [len(line) for line in originalLines]

	annotations = codecs.open(annotationPath, "r", "utf-8")
	annotationsLines = annotations.readlines()
	originalCorpus.close()
	annotations.close()

	modificationIndices = codecs.open("modifications.txt", "w", "utf-8")
	openMarker = "{"
	closeMarker = "}"

	annotationCount = 1
	currentStart = 0
	for modIndex in range(len(annotationsLines)):
		# print modIndex
		# assuming no noun phrases in noun phrases
		annotationsLines[modIndex] = annotationsLines[modIndex]
		while annotationsLines[modIndex].find(openMarker) >= 0 and annotationsLines[modIndex].find(closeMarker) >= 0:
			# print annotationsLines[modIndex]
			openIndex = annotationsLines[modIndex].find(openMarker)
			closeIndex = annotationsLines[modIndex].find(closeMarker)
			annotationsLines[modIndex] = annotationsLines[modIndex][:openIndex] + annotationsLines[modIndex][openIndex:closeIndex + 1].replace(openMarker, "").replace(closeMarker, "") + annotationsLines[modIndex][closeIndex + 1:]
			closeIndex -= len(openMarker)
			modificationIndices.write("T"+str(annotationCount)+"\tNoun-Phrase "+"{0} {1}\t".format(openIndex + currentStart, closeIndex + currentStart))
			print originalLines[modIndex][openIndex:closeIndex]+"\n"
			modificationIndices.write(originalLines[modIndex][openIndex:closeIndex]+"\n")	
			# line_start = 0
			# line_no = 0
			# while line_start < closeIndex:
			# 	line_end = line_start + originalLengths[line_no]
			# 	if line_start < openIndex and line_end > closeIndex:
			# 		startOffset = openIndex-line_start
			# 		endOffset = closeIndex-line_start
			# 		print line_no
			# 		# print startOffset, endOffset
			# 		modificationIndices.write(originalLines[line_no][startOffset:endOffset]+"\n")
			# 	line_no += 1
			# 	line_start=line_end
			annotationCount+=1

		currentStart += originalLengths[modIndex]
	print "Parsing done"
	modificationIndices.close()