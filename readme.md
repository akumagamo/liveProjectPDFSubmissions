# **liveProject (MEAP):** Delivery Notes Data Entry Automation With Python
## Versionnumber 1.0.0 (2020-05-30)
(***Documentation last update 2020-05-30 09:00***)  

Here the task for each chapter will listed and optional Notes / Information

## ChapterOne

### Tasks
* Select a folder where you can download the dataset. Unzip the dataset archive.
    * Notice that the files that make up the dataset are contained within subfolders.
    * Leave the structure of the subfolders as it is.
* Create a Python function that iterates through this folder and returns a list of PDF files found within all the subfolders.
* Make your Python function as concise and short as possible, no more than 6 lines of code for the function code itself. It’s possible to achieve this functionality with fewer lines of code, but it’s not a must to do it that way. However, if you are up for the challenge, go for it.

### Notes
* a virtual environment was created and the prerequisites were installed
* a 'requirements.txt' was generated with the installed local modules
* the demo files were kept in the same folder structure under 'formats' _(files are not under sourcecontrol)_
* to start the code of this Chapter just run `python -m chapterOne`
* Since the Submission structure is abit different, there is a sepearte folder, 'submissions' with the code that was submitted. 

### Output
`['...\\formats\\format1\\folder\\1900070.pdf', '...\\formats\\format2\\211559-050.pdf']`  
  
_**Disclaimer:** in my case I get a third file `.gitignore` is returned, but to keep it simple I didn't want to filter for fileextension or fileheader or ... . So I deleted the file in my working directory_