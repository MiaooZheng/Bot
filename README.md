checkout bot

For this project, I'm going to make a checkout bot to purchase the shoes. As the size i want is unavailable right now, i'll try to connect with email notifications or use airflow to check whether item is available per 30mins. 

Current plan: 
- finish the rest of code, choose size, add to cart and checkout. (done)
- connect to email and when I receive notification from store, run the above code immediately. 
- use airflow to automatically check availability per 30mins and buy if available. 


--------------------
** Update on May23,2023
- I'm thinking do automation to check availability and if yes, send text message. However, I encountered some issues:
- email to text_message file done. It works for US ATT and Canada Bell and Telus. However, I'm using fido as mobile carrier, which is not free at this time. So may not be able to send text to my own phone no. when it has stock. 

Plan for next step: 
- Since my friend told me there maybe delays from store email. I may still want to send email to my email address if i find it's in stock. 
- Use airflow to do automation. 
