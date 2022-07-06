Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help('modules')

Please wait a moment while I gather a list of all available modules...

__future__          atexit              html                search
__main__            audioop             http                searchbase
_abc                autocomplete        hyperparser         searchengine
_ast                autocomplete_w      idle                secrets
_asyncio            autoexpand          idle_test           select
_bisect             base64              idlelib             selectors
_blake2             bdb                 imaplib             setuptools
_bootlocale         binascii            imghdr              shelve
_bz2                binhex              imp                 shlex
_codecs             bisect              importlib           shutil
_codecs_cn          browser             inspect             sidebar
_codecs_hk          builtins            io                  signal
_codecs_iso2022     bz2                 iomenu              site
_codecs_jp          cProfile            ipaddress           smtpd
_codecs_kr          calendar            itertools           smtplib
_codecs_tw          calltip             json                sndhdr
_collections        calltip_w           keyword             socket
_collections_abc    cgi                 lib2to3             socketserver
_compat_pickle      cgitb               linecache           sqlite3
_compression        chunk               locale              squeezer
_contextvars        cmath               logging             sre_compile
_csv                cmd                 lzma                sre_constants
_ctypes             code                macosx              sre_parse
_ctypes_test        codecontext         macpath             ssl
_datetime           codecs              mailbox             stackviewer
_decimal            codeop              mailcap             stat
_dummy_thread       collections         mainmenu            statistics
_elementtree        colorizer           marshal             statusbar
_functools          colorsys            math                string
_hashlib            compileall          mimetypes           stringprep
_heapq              concurrent          mmap                struct
_imp                config              modulefinder        subprocess
_io                 config_key          msilib              sunau
_json               configdialog        msvcrt              symbol
_locale             configparser        multicall           symtable
_lsprof             contextlib          multiprocessing     sys
_lzma               contextvars         netrc               sysconfig
_markupbase         copy                nntplib             tabnanny
_md5                copyreg             nt                  tarfile
_msi                crypt               ntpath              telnetlib
_multibytecodec     csv                 nturl2path          tempfile
_multiprocessing    ctypes              numbers             test
_opcode             curses              opcode              textview
_operator           dataclasses         operator            textwrap
_osx_support        datetime            optparse            this
_overlapped         dbm                 os                  threading
_pickle             debugger            outwin              time
_py_abc             debugger_r          parenmatch          timeit
_pydecimal          debugobj            parser              tkinter
_pyio               debugobj_r          pathbrowser         token
_queue              decimal             pathlib             tokenize
_random             delegator           pdb                 tooltip
_sha1               difflib             percolator          trace
_sha256             dis                 pickle              traceback
_sha3               distutils           pickletools         tracemalloc
_sha512             doctest             pip                 tree
_signal             dummy_threading     pipes               tty
_sitebuiltins       dynoption           pkg_resources       turtle
_socket             easy_install        pkgutil             turtledemo
_sqlite3            editor              platform            types
_sre                email               plistlib            typing
_ssl                encodings           poplib              undo
_stat               ensurepip           posixpath           unicodedata
_string             enum                pprint              unittest
_strptime           errno               profile             urllib
_struct             faulthandler        pstats              uu
_symtable           filecmp             pty                 uuid
_testbuffer         fileinput           py_compile          venv
_testcapi           filelist            pyclbr              warnings
_testconsole        fnmatch             pydoc               wave
_testimportmultiple format              pydoc_data          weakref
_testmultiphase     formatter           pyexpat             webbrowser
_thread             fractions           pyparse             window
_threading_local    ftplib              pyshell             winreg
_tkinter            functools           query               winsound
_tracemalloc        gc                  queue               wsgiref
_warnings           genericpath         quopri              xdrlib
_weakref            getopt              random              xml
_weakrefset         getpass             re                  xmlrpc
_winapi             gettext             redirector          xxsubtype
abc                 glob                replace             zipapp
aifc                grep                reprlib             zipfile
antigravity         gzip                rlcompleter         zipimport
argparse            hashlib             rpc                 zlib
array               heapq               run                 zoomheight
ast                 help                runpy               zzdummy
asynchat            help_about          runscript           
asyncio             history             sched               
asyncore            hmac                scrolledlist        

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> help('modules time')

Here is a list of modules whose name or summary contains 'time'.
If there are any, enter a module name to get more help.

_datetime - Fast implementation of the datetime type.
time - This module provides various functions to manipulate time values.
_strptime - Strptime-related classes and functions.
datetime - Concrete date/time and related types.
test.ann_module3 - Correct syntax for variable annotation that should fail at runtime
test.datetimetester - Test date/time type.
test.test_datetime 
test.test_strftime - Unittest for time.strftime
test.test_strptime - PyUnit testing against strptime
test.test_time 
test.test_timeit 
test.test_timeout - Unit tests for socket timeout feature.
test.time_hashlib 
timeit - Tool for measuring execution time of small code snippets.
pip._vendor.urllib3.util.timeout 

>>> help('datatime')
No Python documentation found for 'datatime'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help('datetime')
Help on module datetime:

NAME
    datetime - Fast implementation of the datetime type.

MODULE REFERENCE
    https://docs.python.org/3.7/library/datetime
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        date
            datetime
        time
        timedelta
        tzinfo
            timezone
    
    class date(builtins.object)
     |  date(year, month, day) --> date object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, YYYY-MM-DD.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  replace(...)
     |      Return date with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  fromisoformat(...) from builtins.type
     |      str -> Construct a date from the output of date.isoformat()
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp -> local date from a POSIX timestamp (like time.time()).
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  day
     |  
     |  month
     |  
     |  year
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.date(9999, 12, 31)
     |  
     |  min = datetime.date(1, 1, 1)
     |  
     |  resolution = datetime.timedelta(days=1)
    
    class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |  
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Method resolution order:
     |      datetime
     |      date
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  astimezone(...)
     |      tz -> convert to local time in new timezone tz
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  date(...)
     |      Return date object with same year, month and day.
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  isoformat(...)
     |      [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |      sep is used to separate the year from the time, and defaults to 'T'.
     |      timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').
     |  
     |  replace(...)
     |      Return datetime with new specified fields.
     |  
     |  time(...)
     |      Return time object with same time but with tzinfo=None.
     |  
     |  timestamp(...)
     |      Return POSIX timestamp as float.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  timetz(...)
     |      Return time object with same time and tzinfo.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  utctimetuple(...)
     |      Return UTC time tuple, compatible with time.localtime().
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  combine(...) from builtins.type
     |      date, time -> datetime with same date and time fields
     |  
     |  fromisoformat(...) from builtins.type
     |      string -> datetime from datetime.isoformat() output
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |  
     |  now(tz=None) from builtins.type
     |      Returns new datetime object representing current time local to tz.
     |      
     |        tz
     |          Timezone object.
     |      
     |      If no tz is specified, uses local timezone.
     |  
     |  strptime(...) from builtins.type
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |  
     |  utcfromtimestamp(...) from builtins.type
     |      Construct a naive UTC datetime from a POSIX timestamp.
     |  
     |  utcnow(...) from builtins.type
     |      Return a new datetime representing UTC day and time.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  fold
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
     |  
     |  min = datetime.datetime(1, 1, 1, 0, 0)
     |  
     |  resolution = datetime.timedelta(microseconds=1)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from date:
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from date:
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from date:
     |  
     |  day
     |  
     |  month
     |  
     |  year
    
    class time(builtins.object)
     |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
     |  
     |  All arguments are optional. tzinfo may be None, or an instance of
     |  a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |      
     |      timespec specifies what components of the time to include.
     |  
     |  replace(...)
     |      Return time with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  fromisoformat(...) from builtins.type
     |      string -> time from time.isoformat() output
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  fold
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.time(23, 59, 59, 999999)
     |  
     |  min = datetime.time(0, 0)
     |  
     |  resolution = datetime.timedelta(microseconds=1)
    
    class timedelta(builtins.object)
     |  Difference between two datetime values.
     |  
     |  timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
     |  
     |  All arguments are optional and default to 0.
     |  Arguments may be integers or floats, and may be positive or negative.
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  total_seconds(...)
     |      Total seconds in the duration.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  days
     |      Number of days.
     |  
     |  microseconds
     |      Number of microseconds (>= 0 and less than 1 second).
     |  
     |  seconds
     |      Number of seconds (>= 0 and less than 1 day).
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.timedelta(days=999999999, seconds=86399, microseconds=9...
     |  
     |  min = datetime.timedelta(days=-999999999)
     |  
     |  resolution = datetime.timedelta(microseconds=1)
    
    class timezone(tzinfo)
     |  Fixed offset from UTC implementation of tzinfo.
     |  
     |  Method resolution order:
     |      timezone
     |      tzinfo
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getinitargs__(...)
     |      pickle support
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  dst(...)
     |      Return None.
     |  
     |  fromutc(...)
     |      datetime in UTC -> datetime in local time.
     |  
     |  tzname(...)
     |      If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'.
     |  
     |  utcoffset(...)
     |      Return fixed offset.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.timezone(datetime.timedelta(seconds=86340))
     |  
     |  min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
     |  
     |  utc = datetime.timezone.utc
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from tzinfo:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      -> (cls, state)
    
    class tzinfo(builtins.object)
     |  Abstract base class for time zone info objects.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      -> (cls, state)
     |  
     |  dst(...)
     |      datetime -> DST offset as timedelta positive east of UTC.
     |  
     |  fromutc(...)
     |      datetime in UTC -> datetime in local time.
     |  
     |  tzname(...)
     |      datetime -> string name of time zone.
     |  
     |  utcoffset(...)
     |      datetime -> timedelta showing offset from UTC, negative values indicating West of UTC
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

DATA
    MAXYEAR = 9999
    MINYEAR = 1
    datetime_CAPI = <capsule object "datetime.datetime_CAPI">

FILE
    c:\program files (x86)\microsoft visual studio\shared\python37_64\lib\datetime.py


>>> 