#1. Remove all suffixes
rename 's/\.xml$//' *.xml

#2. Add suffix in bulk
for i in *
   do mv $i $i".xml"
done
# for i in * ; do mv $i $i".jpg" ; done

#3. Delete files with specified extension
find . -name '*.exe' -type f -print -exec rm -rf {} \;
