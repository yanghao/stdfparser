# What is STDF? #
STDF is the standard test data format used by many of the ATE vendors such as Teradyne. It is the file format most likely being created at production line due to its compactness to save storage spaces.

## STDF Resources ##
  * [STDF on Wikipedia](http://en.wikipedia.org/wiki/Standard_Test_Data_Format)
  * [STDF Group](http://stdf.bcsweb.com/index.php/Main_Page)

# Motivation #
It could be very useful and convinient to directly look into STDF files, and enables more complicated test data analysis framework to be based on this parser. The old solution is to convertion it to another format (such as TSF) and then open such files with another dedicated tool. This, for me is troublesome and lack of the possibility to fully automate data processing and extraction. [Another project pystdf](http://code.google.com/p/pystdf/wiki/Tutorial) is already there for sometime which supports STDF v4 very well. However somehow (possibly due to the limitation of my knowledge) I found pystdf is a bit diffcult to understand and not easy to extend to meet my personal requirements. Thus I developed this brand new STDF parser that supports both STDFv3 and STDFv4. And I also build an automated yield extraction and reporting tool based on this parser which have now totally substituted the old tool we were using.

The parser will support both STDF version 3 and STDF version 4. However the STDF version 3 don't have a public available specification (If at all the version 3 spec is unique for all companies). This STDF version 3 parser is based on Infineon STDF version 3 spec (the spec itself has bugs, well it is fixed in this tool) and probably won't fit your company spec on STDF version 3.

## Current Status ##
I would say this STDF parser is reliable enough that it has at least processed more than 10K files (all at mid-night when the server load is at minimum level). The previous development history is all in a git repo which makes the current hg repo only a initial commit of the reliable version. Most of the code is very simple and straightforward.

## License ##
This project is released under GPLv3.

## Related Projects ##
I learnt especially how to define the kxCn data type from this project:
  * [Another Python-Based STDF parser for STDF version 4](http://code.google.com/p/pystdf/wiki/Tutorial)

# Special Note #
I have only tested this script in GNU/Linux environment and it works fine. I don't have much knowledge on MS windows system and I'm glad to hear from other people whether this script works on Windows system.