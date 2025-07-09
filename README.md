College Navigator (https://nces.ed.gov/collegenavigator/) is a great website that provides a lot of data about different colleges, but there are some defects. It does not provide the historical data or compare between different schools. 

I developed two Python programs to finish those tasks. The first downloads the this years data, and the other compares different colleges.

# Usage

1. Install Python 3 and supporting package ```pandas```, ```requests``` and ```beautifulsoup4``` with ```pip3```. This is done in command prompt use the following code

   ```
   pip3 install package_name
   ```

2. Clone repo to computer.

3. Create a folder called ```database``` under ```CollegeComparing```.

4. In command prompt, type in below command. It will download the school data from College Navigator into the ```database``` folder. It can take up to couple of hours, depending on network speed and computer performance.

   ```
   cd CollegeComparing\program
   python3 university_main.py
   ```

5. Open ```program\compare.csv``` with Excel, fill out school ID or name into column B (there is an example in column C). The ID and name can be found in ```database```.

6. In command prompt, type in below command. It generates ```program\School_1_name_and_ID_&_School_2_name_and_ID_File_to_compare_merge.csv```.

   ```
   python3 compare.py
   ```
7. Open ```program\School_1_name_and_ID_&_School_2_name_and_ID_File_to_compare_merge.csv``` with Excel. Now the two schools' data are compared side by side.

