# Coding-Challenge-Application


Hello,

This repository is my yuhu coding challenge submission.

For the coding challenge, I used a backend of Django and a front end of plain HTML. For the front end, I am unable to apply React as I have not learned React before as indicated in my cover letter and the interview, though I am confident that I will be able to learn and implement it quickly on the job.

The program allows users to input the ends of the URL (ie long_URL_to_shorten in www.example.com/long_URL_to_shorten) due to programming constraints of Django. When developing the program, I used a private development server on my computer, located at http://127.0.0.1:8000/.

For the program, the user inputs the long URL portion he/she wish to shorten. Through each character converted to ASCII format and the sum of all the converted values found, a unique number of base 62 was generated with characters 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' as digits (mapping sum). It is important to note that the URL length can be dynamically sized by changing the base in which the long URL maps its value on.

The long and resulting short URLs are stored into the database table. To extend the number of statistics provided, columns can be added to the database table, which originally has only the short URL and long URL columns. The number of visits to the link is initialized to 0 at the beginning and increments by 1 upon each visit to show how statistics can be stored in the database and how data should be able to be dynamically changed based on user interactions.

If there are numerous statistics, such as the location of the rental unit in which the URL of the property was created for, foreign keys can be used to related the table containing the original long and created short URLs to a location table with corresponsing primary keys and locations (ie cities).

To scale the database, if the data is categorized, parent tables can correspond to child tables through foreign keys to form a relational database. Key indexing can then be performed and the amount of time to search for a particular link/rental location can be reduced.

For the front end, when submitting a URL to shorten, it is important to validate that:

a duplicate long URL has not been submitted
no duplicate ASCII sums are generated (results in same shortened URL value), which can be solved by collision avoiding tactics, such as continuously adding "1" to the ASCII sum until a unique sum value is reached.
With Django, to view the statistics of a URL, admin accounts can be created, which have access to the database generated to store all the dynamic statistics calculated. Generalizing from Django admin accounts, user can access "creator" accounts and view the statistics of their URLs, which can link to their property being available for rent/sale, through intuitional data layouts, such as a line graph (like stock market graph) or a map (google maps) of how many and where user clicked the generated link from. For dynamic display to increase the positivity of user experience, dynamic webpages/mobile apps can be created by React, Angular, or JQuery, and Ajax.

To conclude my application, I would like to apoligize due to my late submission of this coding challenge due to course work in designing and building an autonomous robot.

Thank you for your time and consideration and let me know if you have any questions.

Best Regards,

Eric Li
