cd ~/info2000/
mv disorganized_structure organized_structure
cd organized_structure
mkdir entertainment recipes sports technology travel
mv e*.txt entertainment
mv r*.txt recipes
mv s*.txt sports
mv te*.txt technology
mv tr*.txt travel
touch output.txt
ls -R >> output.txt
