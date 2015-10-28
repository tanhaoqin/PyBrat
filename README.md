# PyBrat 

Does the same thing as [Jia Hao's Brat](https://github.com/skewedlines/brat/) but it was developed separately. Who knows, maybe we have different bugs, give it a try.

A local annotation feature has also been added. This feature saves your annotation onto a local .ann file which can be uploaded to brat along with your original copy of your text file. I'm assuming the TA would be more than happy to accept these files since they are probably going do export it from the online portal anyway.

## Introduction

*Shameless ripoff of Jia Hao's README*
**Even though care has been taken to minimize errors, I take no responsibility for any loss of data or errors to your corpus if you choose to use this tool.**

### Constraints 

- Currently coded to `http://brat.statnlp.com/main/#/sms_corpus/students/XXXXXXXX/sms_corpus` where `XXXXXXXX` is your username. 
- Your username the same as your password
- All tags are `noun-phrases`
- You only care about outermost noun-phrases

## Installation

Clone the repo or download the zip and extract all to the same folder.
I assume you have a working installation of Python 2

## Usage - Command Line

*This is different from Jia Hao's so pay attention*
1. Download the plain text corpus by going to the page with the data assigned to you. Mouseover on the top bar and click `Data` > `Export (Document Data)` > `txt`

2. *Duplicate this file*. I suggest you name one copy **master.txt** and the other **annotations.txt** though it doesn't REALLY matter.

3. Add your annotations in plain text to **annotations.txt**, by separating noun phrases with `{` and `}`. DO NOT TOUCH THE MASTER YOU HAVE BEEN WARNED

4. *MOST IMPORTANT STEP* Mark every line that you want to send with a #. 

For example I have the lines

```
18957 {Dear} {I} go {toilet} first
18958 Meet {u} outside {coop} later
18959 Ok. After your exams?
```

Say I want to ship only one line, mark it like so
```
18957 {Dear} {I} go {toilet} first
# 18958 Meet {u} outside {coop} later
18959 Ok. After your exams?
```

I suggest you do this in Sublime Text by changing your syntax to Python and using the 'comment' command.

Sending annotations ("send" command)
---

Assuming your working directory is the same location as all the files, run

```
python annotater.py <username> send <masterpath> <annotationpath>
```
*<masterpath>* - the path to your master file, it is assumed to be master.txt if left blank
*<annotationpath>* - the path to your annotated file, it is assumed to be annotations.txt if left blank

Don't try to use only one filename, it will cock up and die.

If I named my files nicely, I can run
```
python annotater.py 1000XXX send
```
otherwise,
```
python annotater.py 1000XXX send masterlolol.txt lolannotations.txt
```

Deleting annotations ("del" command)
---
```
python annotater.py <username> del <startTagid> <endTagid>
```
All annotations have a tag id attached to them. It looks like 'T1' or 'T391' or something. 

For example, to delete annotations 1 to 200,
```
python annotater.py 1000XXX del 1 200
```
or to delete one annotation,
```
python annotater.py 1000XXX del 200
```

If you have a ton of errors, I suggest deleting everything like such
```
python annotater.py 1000XXX del 1 5000
```

Local Annotations
---
Assuming your working directory is the same location as all the files, run

```
python annotater.py <username> local <masterpath> <annotationpath>
```
*<masterpath>* - the path to your master file, it is assumed to be master.txt if left blank
*<annotationpath>* - the path to your annotated file, it is assumed to be annotations.txt if left blank

Don't try to use only one filename, it will cock up and die.

If I named my files nicely, I can run
```
python annotater.py 1000XXX send
```
otherwise,
```
python annotater.py 1000XXX local masterlolol.txt lolannotations.txt
```

This will create a file called modifications.txt which will should be renamed to <originalfilename>.ann

After you tar-gzip the original textfile and ann file. You should be able to import the resulting annotation and text onto brat. Alternatively just email the TA the annotations.

If you installed a local copy of brat, simply drag create a new folder under your brat's directory's data folder, and place both files inside. Restart brat, and you will be able to open your annotated file locally.

## Annotations

TAGS CANNOT BE NESTED YOU HAVE BEEN WARNED

### Credits
[Jia Hao](https://github.com/skewedlines) for his collaboration and insight. I think PyBrat is stupider than his Brat, but hopefully some stupidity means fewer bugs.