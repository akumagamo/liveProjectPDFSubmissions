# **liveProject (MEAP):** Delivery Notes Data Entry Automation With Python
## Versionnumber 1.5.0 (2020-05-30)
(***Documentation last update 2020-05-30 19:00***)  

Here the task for each chapter will listed and optional Notes / Information

## ChapterOne

### Tasks
_go to portal for the tasks_

### Notes
* a virtual environment was created and the prerequisites were installed
* a 'requirements.txt' was generated with the installed local modules
* the demo files were kept in the same folder structure under 'formats' _(files are not under sourcecontrol)_
* to start the code of this Chapter just run `python -m chapterOne`
* Since the Submission structure is abit different, there is a sepearte folder, 'submissions' with the code that was submitted. 

### Output
`['...\\formats\\format1\\folder\\1900070.pdf', '...\\formats\\format2\\211559-050.pdf']`  
  
_**Disclaimer:** in my case I get a third file `.gitignore` is returned, but to keep it simple I didn't want to filter for fileextension or fileheader or ... . So I deleted the file in my working directory_

## ChapterTwo

### Tasks
_go to portal for the tasks_

### Notes
* added extra line in format2.ini 'DeliveryNote=Delivery'
* Currently output only as print-statements

### Output
![Screenshot of CommandLine after execution](./readme/screenshot_0001.png)

## ChapterThree

After flying over the result docx, I understund the desired output, so the first step is tweaking my code to output the desired output style.

### Tasks
_go to portal for the tasks_

### Notes
* The whole field-get Section is wierd, and I should review the learning material to get this part right. But for now the sceleton I wrote seems to do the trick.
* The onliner Field read _"Hack"_ removes entries without a value set. This part could/should be revisited since default value and other edge-cases aren't looked at, but for now this should do.
* Minor "problem" with the casesensitivity will be fixed with an neat workaround. Should not even a problem in a production code, since nameing convetions in HTML/CSS/Javascript should prevent same id, with differnt camel/pascal-casing. _(lets be honest, in production I would probably not allow should a "move")_



### Output