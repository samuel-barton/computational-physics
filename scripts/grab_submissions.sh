#!/bin/bash

#=============================================================================
#
# File name: grab_submissions.sh
#
# Created by: Samuel Barton
#
# Date: January 2017
#
# Description: This script checks to see if there are any new files in a
#              remote repository, and if there are it moves them to another
#              folder, presumably in another repository, and then updates the
#              original repository. This is setup to be done on a loop with a
#              latency of 10s.
#
#=============================================================================

while [ 1 ]
do
    echo "Retrieving data from Github."
    cond=(ls ../submissions | wc -l)
    if (git pull origin master 2>&1 | grep -qvi "up to date" || !($(($cond - 0))))
    then
        echo "New files found. moving to private folder."
        mv ../submissions/* ../private 2>&1 > /dev/null
        git commit -a -m "moved files to private directory." 2>&1 > /dev/null
        git push origin master 2>&1 > /dev/null
    fi
    sleep 10
done
