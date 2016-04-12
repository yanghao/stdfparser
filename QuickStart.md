# Introduction #

stdfparser is purely in python. Thus it is almost not picky at all on python versions. However, for that the stdfparser can readin gzipped file and bzipped file directly, and only in python2.6 the **whence** parameter of `seek()` for python gzip module is added. Thus if you're going to use gzip file directly, you'd better have python >= 2.6 or edit your gzip.py file to add the **whence** parameter to `seek()` directly.


# Install #

unzip the file or checkout the latest version from the Mercurial repo. Nothing else needed being setup.

# Use it #

Run the test.py file with the following command:
```
python test.py /path/to/stdf_file1.gz /path/to/stdf_file2.gz ...
```

# Implementation #

This section discuss how the STDF parser is implemented.

## a simple stdf viewer ##
The stdfparser is implemented in python class. In `test.py` it is shown that with a few lines of code, a simple _stdfviewer_ is created. The _stdfviewer_ outputs all stdf records to STDOUT (that is, your screen).

## create new application ##
You inherit the **parser** class from `stdfparser.py` to create new applications. And there's 5 hook functions as well as some class-wise variables for you to place with.

Here are the five hook functions:

  * take
> `take()` is called every time a record is parsed. All parsed information is put in a dictionary called `self.data`. The current record is `self.Cur_Rec`. The current record name is `str(self.Cur_Rec` or simply `self.Cur_Rec_Name`. See the individual record definition in `stdf_V3.py` and `stdf_V4.py` for its specific information. Every record type has a field `fieldMap` which is a tuple of pairs. The first element in each pair is the field name, the second is the field data type as defined in STDF specification.

> `take()` ask for one parameter `typsub` which is offered by the stdfparser. However this parameter is not that useful since this information is in `self.Cur_Rec`.

  * setup
> `setup()` is the first thing executed before parsing a list of files. You can setup any data base tables or anything that is global for all succeeding processing.

  * cleanup
> `cleanup()` is called when all parsing of the file list is finished. You can, say close your database connection in this function.

  * file\_setup
> Like `setup()`, `file_setup()` is called just after its first record (Mir) is parsed. From `self.File_Name` you could know the file currently being processing. If you set the variable `self.Ignore_File = True` then the file is skipped and the next one is processed. `self.Ignore_File` is set to `False` automatically after the current file being ignored.

  * file\_cleanup
> `file_cleanup()` is called when one file is finished parsing. You can, say update the database table to mark this file has been parsed in this function.

Here are some useful variables to guide the parser behavior:

  * `Rec_Set`
> `self.Rec_Set` is a list of records you'd like the parser to deal with. Records not in this list is ignored. If this list is empty, defaults all records will be dealt with.

  * `Rec_Nset`
> `self.RecNset` is a list of records you'd like to ignore. Used only when `Rec_Set` is empty list.