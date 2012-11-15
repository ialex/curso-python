# -*- coding: utf-8 -*-

"""
    Utils
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import re
import unidecode


######################################################
###
### Functions
###
######################################################
 
## Check allowed file extensions
def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


## Return slugs from a string
def slugify(str):
    str = unidecode.unidecode(str).lower()
    return re.sub(r'\W+','-',str)


